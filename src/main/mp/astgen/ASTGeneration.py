from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce
#flatten_mix
def flatten(l):
    return list(reduce(lambda x, y: x + y if(isinstance(y, list)) else x + [y], l, []))
class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.manydeclares()]))
    def visitManydeclares(self, ctx:MPParser.ManydeclaresContext):
        if ctx.varde():
            return self.visit(ctx.varde())
        if ctx.funcde():
            return self.visit(ctx.funcde())
        if ctx.procede():
            return self.visit(ctx.procede())

    def visitCompostate(self,ctx:MPParser.CompostateContext):
        return flatten([self.visit(x) for x in ctx.statement()])

    def visitVarde(self, ctx:MPParser.VardeContext):
        return flatten([self.visit(x) for x in ctx.var_list()])

    def visitVar_list(self, ctx:MPParser.Var_listContext):
        _type = self.visit(ctx.vartype())
        _id = self.visit(ctx.idlist())
        return list(map(lambda x: VarDecl(x,_type),_id))

    def visitProcede(self, ctx:MPParser.ProcedeContext):
        if ctx.varde():
            local = flatten([self.visit(ctx.varde())])
        else:
            local = []
        cpstmt = self.visit(ctx.compostate())
        id = Id(ctx.procede1().ID().getText())
        param = self.visit(ctx.procede1())
        return FuncDecl(id,
                        param,
                        local,
                        cpstmt)
    def visitProcede1(self, ctx:MPParser.Procede1Context):
        if (ctx.parade()):
            return flatten([self.visit(ctx.parade())])
        return []

    def visitParade(self, ctx:MPParser.ParadeContext):
        return flatten([self.visit(x) for x in ctx.parade1()])

    def visitParade1(self, ctx:MPParser.Parade1Context):
        _type = self.visit(ctx.vartype())
        _id = self.visit(ctx.idlist())
        return list(map(lambda x: VarDecl(x,_type),_id))

    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitVartype(self, ctx:MPParser.VartypeContext):
        if (ctx.primtype()):
            return self.visit(ctx.primtype())
        else:
            return self.visit(ctx.arrtype())

    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.INTEGER():
            return IntType()
        if ctx.REAL():
            return FloatType()
        if ctx.STRING():
            return StringType()

    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        eleType = self.visit(ctx.primtype())
        lower = int(ctx.intt(0).INTLIT().getText())
        upper = int(ctx.intt(1).INTLIT().getText())
        if ctx.intt(0).SUBNE() is not None:
            lower = lower*(-1)
        if ctx.intt(1).SUBNE() is not None:
            upper = upper*(-1)
        return ArrayType(lower, upper, eleType)

    def visitIntt(self, ctx:MPParser.InttContext):
        return

    def visitFuncde(self, ctx:MPParser.FuncdeContext):
        cpstmt = self.visit(ctx.compostate())
        id = Id(ctx.funcde1().ID().getText())
        param = self.visit(ctx.funcde1())
        varType = self.visit(ctx.vartype())
        if ctx.varde():
            local = flatten([self.visit(ctx.varde())])
        else:
            local = []
        return FuncDecl(id,
                        param,
                        local,
                        cpstmt,
                        varType)

    def visitFuncde1(self, ctx:MPParser.Funcde1Context):
        if (ctx.parade()):
            return flatten([self.visit(ctx.parade())])
        return []

    def visitStatement(self, ctx:MPParser.StatementContext):
        if (ctx.semistatement()):
            return self.visit(ctx.semistatement())
        else:
            return self.visit(ctx.nomistatement())

    def visitSemistatement(self, ctx:MPParser.SemistatementContext):
        if (ctx.assignstate()):
            return self.visit(ctx.assignstate())
        elif (ctx.breakstate()):
            return self.visit(ctx.breakstate())
        elif (ctx.contstate()):
            return self.visit(ctx.contstate())
        elif (ctx.returnsate()):
            return self.visit(ctx.returnsate())
        else:
            return self.visit(ctx.callstate())

    def visitNomistatement(self, ctx:MPParser.NomistatementContext):
        if (ctx.ifstate()):
            return self.visit(ctx.ifstate())
        elif (ctx.forstate()):
            return self.visit(ctx.forstate())
        elif (ctx.whilestate()):
            return self.visit(ctx.whilestate())
        elif (ctx.compostate()):
            return self.visit(ctx.compostate())
        else:
            return self.visit(ctx.withstate())

    def visitAssignstate(self, ctx:MPParser.AssignstateContext):
        lhs = flatten([self.visit(x) for x in ctx.lhs()])
        exp = self.visit(ctx.expression())
        lhs.append(exp)
        a=[]
        for i in range(0,len(lhs)-1,1):
            a.append(Assign(lhs[i],lhs[i+1]))
        a.reverse()
        return a

    # def visitAssignstate1(self, ctx:MPParser.Assignstate1Context):
    #     if ctx.assignstate1():
    #         a= [self.visit (ctx.assignstate1())]
    #     if ctx.expression():
    #         a=[self.visit(ctx.expression())]
    #     a.append(self.visit(ctx.lhs()))
    #     b=reduce (lambda x,y: Assign(y,x), list(a))
    #     return b

    def visitLhs(self, ctx:MPParser.LhsContext):
        if (ctx.ID()):
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.indexexpre())

    def visitIndexexpre(self, ctx:MPParser.IndexexpreContext):
        b = [self.visit(i) for i in ctx.expression()]
        a = self.visit(ctx.factor())
        c=ArrayCell(a,b[0])
        for i in range(1,len(b),1):
            c=ArrayCell(c,b[i])
        return c

        # explist= [self.visit(x) for x in ctx.expression()]
        # Inexxep = ArrayCell(self.visit(ctx.factor()), explist[0])
        # for i in explist[1:]:
        #     Inexxep = ArrayCell(Inexxep, explist[i])
        # return Inexxep

    def visitFactor(self, ctx:MPParser.FactorContext):
        if (ctx.LB() and ctx.RB()):
            return self.visit(ctx.exp1())
        elif (ctx.ID()):
            return Id(ctx.ID().getText())
        elif (ctx.INTLIT()):
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif (ctx.boollit()):
            return self.visit(ctx.boollit())
        elif (ctx.REALLIT()):
            return FloatLiteral(float(ctx.REALLIT().getText()))
        elif (ctx.STRINGLIT()):
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return self.visit(ctx.invoexpre())

    def visitBoollit(self, ctx:MPParser.BoollitContext):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if (ctx.AND() and ctx.THEN()):
            return BinaryOp("andthen",self.visit(ctx.exp1()),self.visit(ctx.exp2()))
        elif (ctx.OR() and ctx.ELSE()):
                return BinaryOp("orelse",self.visit(ctx.exp1()),self.visit(ctx.exp2()))
        else:
            return self.visit(ctx.exp2())

    def visitExp2(self, ctx:MPParser.Exp2Context):
        if (ctx.EQ()):
            return BinaryOp("=",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        elif (ctx.NOTEQ()):
            return BinaryOp("<>",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        elif (ctx.LESSTN()):
            return BinaryOp("<",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        elif (ctx.GRETN()):
            return BinaryOp(">",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        elif (ctx.GREEQ()):
            return BinaryOp(">=",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        elif (ctx.LESSEQ()):
            return BinaryOp("<=",self.visit(ctx.exp3(0)),self.visit(ctx.exp3(1)))
        else:
            return self.visit(ctx.exp3(0))

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if (ctx.ADD()):
            return BinaryOp("+",self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif (ctx.SUBNE()):
            return BinaryOp("-",self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        elif (ctx.OR()):
            return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if (ctx.DIVSI()):
            return BinaryOp("/",self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif (ctx.MUL()):
            return BinaryOp("*",self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif (ctx.MOD()):
            mod = ctx.MOD().getText()
            return BinaryOp(mod,self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif (ctx.AND()):
            return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        elif (ctx.DIV()):
            return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp5())

    def visitExp5(self, ctx:MPParser.Exp5Context):
        if (ctx.NOT()):
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp5()))
        elif (ctx.SUBNE()):
            return UnaryOp("-",self.visit(ctx.exp5()))
        else:
            return self.visit(ctx.exp6())

    def visitExp6(self, ctx:MPParser.Exp6Context):
        if (ctx.factor()):
            return self.visit(ctx.factor())
        else:
            return self.visit(ctx.indexexpre())

    def visitInvoexpre(self, ctx:MPParser.InvoexpreContext):
        method = Id(ctx.ID().getText())
        param = []
        if ctx.exprlist():
            param = flatten([self.visit(ctx.exprlist())])
        return CallExpr(method, param)

    def visitExprlist(self, ctx:MPParser.ExprlistContext):
        return [self.visit(x) for x in ctx.expression()]

    def visitExpression(self, ctx:MPParser.ExpressionContext):
        if (ctx.indexexpre()):
            return self.visit(ctx.indexexpre())
        elif (ctx.invoexpre()):
            return self.visit(ctx.invoexpre())
        else:
            return self.visit(ctx.exp1())

    def visitBreakstate(self, ctx:MPParser.BreakstateContext ):
        return Break()

    def visitContstate(self, ctx:MPParser.ContstateContext):
        return Continue()

    def visitReturnsate(self, ctx:MPParser.ReturnsateContext):
        if (ctx.returnexp()):
            return self.visit(ctx.returnexp())
        else:
            return self.visit(ctx.returnnoexp())

    def visitReturnexp(self, ctx:MPParser.ReturnexpContext):
        return Return(self.visit(ctx.expression()))

    def visitReturnnoexp(self, ctx:MPParser.ReturnnoexpContext):
        return Return()

    def visitCallstate(self, ctx:MPParser.CallstateContext):
        method = Id(ctx.ID().getText())
        if ctx.expression(0) is not None:
            param = [self.visit(x) for x in ctx.expression()]
        else:
            param = []
        return CallStmt(method, param)

    def visitIfstate(self, ctx:MPParser.IfstateContext):
        expr = self.visit(ctx.exp1())
        thenStmt = flatten([self.visit(ctx.statement(0))])
        if (ctx.statement(1)) is not None:
            elseStmt = flatten([self.visit(ctx.statement(1))])
            return If(expr, thenStmt, elseStmt)
        else:
            return If(expr, thenStmt)

    def visitForstate(self, ctx:MPParser.ForstateContext):
        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expression(0))
        expr2 = self.visit(ctx.expression(1))
        loop = flatten([self.visit(ctx.statement())])
        if (ctx.TO()):
            up = "True"
        else:
            up = "False"
        return For(id, expr1, expr2, up, loop)

    def visitWhilestate(self, ctx:MPParser.WhilestateContext):
        sl = flatten([self.visit(ctx.statement())])
        exp = self.visit(ctx.expression())
        return While(exp, sl)

    def visitWithstate(self, ctx:MPParser.WithstateContext):
        decl = flatten([self.visit(ctx.parade2())])
        stmt = flatten([self.visit(ctx.statement())])
        return With(decl, stmt)

    def visitParade2(self, ctx:MPParser.Parade2Context):
        return self.visit(ctx.parade())
