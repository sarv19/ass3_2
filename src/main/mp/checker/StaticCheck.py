"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return 'MType([' + ','.join(str(i) for i in self.partype) + ']' + ',' + str(self.rettype) + ')'

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self):
        return 'Symbol(' + self.name + ',' + str(self.mtype) + ')'

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType())),
                   Symbol("putInt",MType([IntType()],VoidType())),
                   Symbol("getFloat",MType([],FloatType())),
                   Symbol("putFloat",MType([FloatType()],VoidType())),
                   Symbol("putFloatLn",MType([FloatType()],VoidType())),
                   Symbol("putBool",MType([BoolType()],VoidType())),
                   Symbol("putBoolLn",MType([BoolType()],VoidType())),
                   Symbol("putString",MType([StringType()],VoidType())),
                   Symbol("putStringLn",MType([StringType()],VoidType())),
                   Symbol("putLn",MType([],VoidType()))]

    def __init__(self,ast):
        self.ast = ast

    def checkRedeclared(self,sym, kind, env):
        if self.lookup(sym.name.lower(), env, lambda x: x.name.lower()):
            raise Redeclared(kind, sym.name)
        else:
            return sym

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast, c):
        #return [self.visit(x,c) for x in ast.decl]
        var_list = [x for x in ast.decl if type(x) is VarDecl]
        res = [x for x in ast.decl if type(x) is not VarDecl]
        poten = []
        for x in res:
            if (type(x.returnType) is VoidType) and (not x.param):
                poten.append(x)
        #lst = var_list+res
        checkmain = self.lookup('main',poten, lambda x: x.name.name.lower())
        if checkmain is None:
            raise NoEntryPoint()
        nomain =[]
        yesmain=[]
        for x in res:
            if x.name.name == 'main':
                yesmain.append(x)
            elif x.name.name is not 'main':
                nomain.append(x)
        lst =  var_list+ nomain + yesmain
        return reduce(lambda x,y: [self.visit(y,x+c)]+x,lst,[])

    def visitVarDecl(self, ast, c):
        return self.checkRedeclared(Symbol(ast.variable.name, ast.varType), Variable(),c)

    def visitFuncDecl(self,ast, c):
        # return list(map(lambda x: self.visit(x,(c,True)),ast.body))
        try:
            param = reduce(lambda x,y: [self.visit(y,x)] + x, ast.param,[])
        except Redeclared as e:
            raise Redeclared(Parameter(),e.n)
        localenv = reduce(lambda x,y: [self.visit(y,x)] + x, ast.local,param) #reverse, local 1st then param
        abc = Symbol(ast.name.name, MType([i.varType for i in ast.param],ast.returnType))
        tmp = list(map(lambda x: self.visit(x,localenv+[abc]+ c),ast.body))
        kind = Procedure() if type(ast.returnType) is VoidType else Function()

        if type(ast.returnType) is VoidType:
            if ast.body is not None:
                for x in ast.body:
                    checkReturn = self.checkReturnProce(x)

        if type(ast.returnType) is not VoidType:
            if self.checkReturn(ast.body) is False:
                raise FunctionNotReturn(ast.name.name)
            for x in ast.body:
                if type(x) is Return:
                    checkExpr = self.checkInReturn(x, ast.returnType, localenv)

        if self.checkBrCont(ast.body) is True:
            raise BreakNotInLoop()

        return self.checkRedeclared(Symbol(ast.name.name, MType([i.varType for i in ast.param],ast.returnType)),kind,c)

    def checkReturnProce(self, state):
        if type(state) is Return:
            if state.expr is not None:
                raise TypeMismatchInStatement(state)

    def checkReturnStatement(self, state): ##check if enough return in one stmt
        if type(state) is Return:
            return True
        elif type(state) is If:
            return (self.checkReturn(state.thenStmt) and self.checkReturn(state.elseStmt)) ##what is else is empty
        else:
             return False

    def checkReturn(self, body):  ##check enough return in [stmt]
        for x in body:
            if (self.checkReturnStatement(x) is True):
                return True
        return False

    def checkBreakCont(self, stmt):
        if type(stmt) is Break:
            raise BreakNotInLoop()
            return True
        elif type(stmt) is Continue:
            raise ContinueNotInLoop()
            return True
        elif type(stmt) is If:
            return (self.checkBrCont(stmt.thenStmt) or self.checkBrCont(stmt.elseStmt))
        elif type(stmt) is While: ### no error
            return False
        elif type(stmt) is For:  ### no error
                return False
        elif type(stmt) is With:
            return self.checkBrCont(stmt.stmt)
        else:
            return False

    def checkBrCont(self, lst):
        for x in lst:
            if (self.checkBreakCont(x) is True):
                return True
        return False

    def checkInReturn(self, state, kind, env): ##check if the return type is right
        if state.expr is None:
            raise TypeMismatchInStatement(state)
        else:
            gettype = self.visit(state.expr,env)
            if type(gettype) is type(kind) and type(gettype) is not ArrayType:
                return gettype
            elif type(gettype) is type(kind) and type(gettype) is ArrayType:
                if gettype.lower is kind.lower and gettype.upper is kind.upper and type(gettype.eleType) is type(kind.eleType):
                    return gettype
                else:
                    raise TypeMismatchInStatement(state)
            elif type(gettype) is IntType and type(kind) is FloatType:
                return FloatType()
            else:
                raise TypeMismatchInStatement(state)


    def visitCallStmt(self, ast, c):
        at = [self.visit(x,c) for x in ast.param] #get the type of param
        res = self.lookup(ast.method.name.lower(),c,lambda x: x.name.lower()) #find if CallStmt name is already had
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
        #      Undeclared
            raise Undeclared(Procedure(),ast.method.name)

        elif len(res.mtype.partype) != len(at) or True in [((type(a) != type(b)) and not (type(b) is FloatType and type(a) in [FloatType,IntType]) ) for a,b in zip(at,res.mtype.partype)]:
            raise TypeMismatchInStatement(ast)
        else:
            for a,b in zip(at,res.mtype.partype):
                if type(b) is ArrayType:
                    if (b.lower is not a.lower) or (b.upper is not a.upper):
                        raise TypeMismatchInStatement(ast)
                    elif ((type(a.eleType)  != type(b.eleType)) and not (type(b.eleType) is FloatType and type(a.eleType) in [FloatType,IntType])):
                        raise TypeMismatchInStatement(ast)
            return res.mtype.rettype

    def visitCallExpr(self, ast, c):
        return self.checkTypeMisMatch(Function(), TypeMismatchInExpression(ast),ast,c)

    def checkTypeMisMatch(self, kind, err, tree, env):
        at = [self.visit(x,env) for x in tree.param] #get the type of param

        res = self.lookup(tree.method.name.lower(),env,lambda x: x.name.lower()) #find if CallStmt name is already had

        if res is None or not type(res.mtype) is MType or type(res.mtype.rettype) is VoidType:
        #      Undeclared
            raise Undeclared(kind,tree.method.name)

        elif len(res.mtype.partype) != len(at) or True in [((type(a) != type(b)) and not (type(b) is FloatType and type(a) in [FloatType,IntType]) ) for a,b in zip(at,res.mtype.partype)]:
            raise err
        # elif len(res.mtype.partype) != len(at) or False in [self.checkArray(res.mtype.partype, at)]:
        #     raise err
        else:
            for a,b in zip(at,res.mtype.partype):
                if type(b) is ArrayType:
                    if (b.lower is not a.lower) or (b.upper is not a.upper):
                        raise err
                    elif ((type(a.eleType)  != type(b.eleType)) and not (type(b.eleType) is FloatType and type(a.eleType) in [FloatType,IntType])):
                        raise err
            return res.mtype.rettype
        # elif type(res.mtype.partype) is ArrayType and (res.lower is not at.lower or res.upper is not at.upper):
        # elif not self.checkArray(res.mtype.partype, at):
        #     raise err
        # else:
        #     return res.mtype.rettype

    def checkArray(self, lst, tmp):  ##problem??
        for a, b in zip(tmp, lst):
            if type(a) is ArrayType and type(b) is ArrayType:
                if (a.lower is b.lower) and (a.upper is b.upper) and (a.eleType is b.eleType):
                    return True
                else:
                    return False
            elif type(a) is FloatType and type(b) is IntType:
                return True
            else:
                return False


    def visitId(self,ast,c):
        res = self.lookup(ast.name.lower(),c,lambda x: x.name.lower())

        if res:
            return res.mtype
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitIntLiteral(self,ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitVoidType(self, ast, c):
        return VoidType()

    def visitArrayType(self, ast, c):
        lower = ast.lower
        upper = ast.upper
        eleType = ast.eleType
        return ArrayType(lower, upper, eleType)

    def visitBinaryOp(self, ast, c):
        lefttype = self.visit(ast.left, c)
        righttype = self.visit(ast.right, c)
        if type(lefttype) is StringType or type(righttype) is StringType:
            raise TypeMismatchInExpression(ast)
        elif type(lefttype) is BoolType and type(righttype) is BoolType:
            if ast.op in ['and','or','andthen','orelse']:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        elif type(lefttype) is BoolType or type(righttype) is BoolType:
            raise TypeMismatchInExpression(ast)
        elif ast.op in ['>','<','<>','=','<=','>=']:
            return BoolType()
        elif ast.op in ['*','-','+']:
            if type(lefttype) is IntType and type(righttype) is IntType:
                return IntType()
            else:
                return FloatType()
        elif ast.op in ['mod','div']:
            if type(lefttype) is IntType and type(righttype) is IntType:
                return IntType()
            else:
                raise TypeMismatchInExpression(ast)
        elif ast.op is '/':
            return FloatType()
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        exp = self.visit(ast.body,c)
        if ast.op is '-' and (type(exp) is IntType or FloatType):
            return exp
        elif ast.op is 'not' and type(exp) is BoolType:
            return exp
        else:
            raise TypeMismatchInExpression(ast)

    def visitFor(self, ast, c):
        res = self.lookup(ast.id.name.lower(),c,lambda x:x.name.lower())
        if res is None:
            raise Undeclared(Identifier(),ast.id.name)
        # res = self.visit(ast.id,c)
        a = self.visit(ast.expr1,c)
        b = self.visit(ast.expr2,c)
        if type(res.mtype) is not IntType or type(a) is not IntType or type(b) is not IntType:
            raise TypeMismatchInStatement(ast)
        loop = [self.visit(x,c) for x in ast.loop]

    def visitIf(self, ast, c):
        exp = self.visit(ast.expr, c)
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        thenstmt = [self.visit(x, c) for x in ast.thenStmt]
        elsestmt = [self.visit(x, c) for x in ast.elseStmt]

    def visitWhile(self, ast, c):
        exp = self.visit(ast.exp, c)
        if type(exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        sl = [self.visit(x,c) for x in ast.sl]

    def visitAssign(self, ast, c):
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.exp, c)
        if type(lhs) is StringType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)

        if (type(lhs) is not type(rhs)):
            if (type(lhs) is not FloatType) or (type(rhs) is not IntType):
                raise TypeMismatchInStatement(ast)
        else:
            return Assign(lhs, rhs)


    def visitReturn(self, ast, c):
        if ast.expr is not None:
            exp = self.visit(ast.expr,c)
            return exp

    def visitWith(self, ast, c):
        try:
            decl = reduce(lambda x, y: [self.visit(y,x)] + x, ast.decl,[])
        except Redeclared as e:
            raise Redeclared(Variable(),e.n) ## WRONG
        body = list(map(lambda x: self.visit(x, decl + c),ast.stmt))

    def visitArrayCell(self, ast, c):
        arr = self.visit(ast.arr, c)
        idx = self.visit(ast.idx, c)
        if type(arr) is not ArrayType or type(idx) is not IntType:
            raise TypeMismatchInExpression(ast)
        else:
            return arr.eleType
