# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#manydeclares.
    def visitManydeclares(self, ctx:MPParser.ManydeclaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#boollit.
    def visitBoollit(self, ctx:MPParser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#typee.
    def visitTypee(self, ctx:MPParser.TypeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primtype.
    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrtype.
    def visitArrtype(self, ctx:MPParser.ArrtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#intt.
    def visitIntt(self, ctx:MPParser.InttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp6.
    def visitExp6(self, ctx:MPParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#factor.
    def visitFactor(self, ctx:MPParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varde.
    def visitVarde(self, ctx:MPParser.VardeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_list.
    def visitVar_list(self, ctx:MPParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vartype.
    def visitVartype(self, ctx:MPParser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idlist.
    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcde.
    def visitFuncde(self, ctx:MPParser.FuncdeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcde1.
    def visitFuncde1(self, ctx:MPParser.Funcde1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parade.
    def visitParade(self, ctx:MPParser.ParadeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parade1.
    def visitParade1(self, ctx:MPParser.Parade1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compostate.
    def visitCompostate(self, ctx:MPParser.CompostateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procede.
    def visitProcede(self, ctx:MPParser.ProcedeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procede1.
    def visitProcede1(self, ctx:MPParser.Procede1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#semistatement.
    def visitSemistatement(self, ctx:MPParser.SemistatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#nomistatement.
    def visitNomistatement(self, ctx:MPParser.NomistatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstate.
    def visitAssignstate(self, ctx:MPParser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstate.
    def visitIfstate(self, ctx:MPParser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestate.
    def visitWhilestate(self, ctx:MPParser.WhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstate.
    def visitForstate(self, ctx:MPParser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstate.
    def visitBreakstate(self, ctx:MPParser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#contstate.
    def visitContstate(self, ctx:MPParser.ContstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#stopstate.
    def visitStopstate(self, ctx:MPParser.StopstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnsate.
    def visitReturnsate(self, ctx:MPParser.ReturnsateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnexp.
    def visitReturnexp(self, ctx:MPParser.ReturnexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnnoexp.
    def visitReturnnoexp(self, ctx:MPParser.ReturnnoexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parade2.
    def visitParade2(self, ctx:MPParser.Parade2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstate.
    def visitWithstate(self, ctx:MPParser.WithstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstate.
    def visitCallstate(self, ctx:MPParser.CallstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expression.
    def visitExpression(self, ctx:MPParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexpre.
    def visitIndexexpre(self, ctx:MPParser.IndexexpreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invoexpre.
    def visitInvoexpre(self, ctx:MPParser.InvoexpreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exprlist.
    def visitExprlist(self, ctx:MPParser.ExprlistContext):
        return self.visitChildren(ctx)



del MPParser