import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin foo();end"""
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))
    #
    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """procedure main (); begin
    #         putIntLn();
    #     end"""
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))

    # def test_only_varde(self):
    #     input = Program([VarDecl(Id('a'), IntType()),
    #                     VarDecl(Id('a'), FloatType())])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,1202))
    #
    # def test_only_varde2(self):
    #     input = Program([VarDecl(Id('a'), IntType()),
    #                     VarDecl(Id('b'), FloatType()),
    #                     VarDecl(Id('a'), FloatType())])
    #     expect = "Redeclared Variable: a"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    #
    # def test_only_varde3(self):
    #     input = Program([VarDecl(Id('a'), IntType()),
    #                     VarDecl(Id('b'), FloatType()),
    #                     VarDecl(Id('putInt'), FloatType())])
    #     expect = "Redeclared Variable: putInt"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    #
    # def test_para_func1(self):
    #     input = Program([FuncDecl(Id("main"),[VarDecl(Id('a'), IntType()),
    #                     VarDecl(Id('a'), FloatType())],[],[])])
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input,expect,405))

    # def test_para_func2(self):
    #     input = Program([FuncDecl(Id("main"),[VarDecl(Id('a'), IntType()),
    #                     VarDecl(Id('a'), FloatType())],[
    #                     VarDecl(Id('c'), IntType()),
    #                     VarDecl(Id('d'), FloatType()),
    #                     VarDecl(Id('c'), FloatType())
    #                     ],[])])
    #     expect = "Redeclared Parameter: a"
    #     self.assertTrue(TestChecker.test(input,expect,406))
    #
    # def test_para_func3(self):
    #     input = Program([FuncDecl(Id("main"),
    #                         [VarDecl(Id('a'), IntType())],
    #                         [VarDecl(Id('b'), IntType())],
    #                         [For(Id('a'),IntLiteral(1),IntLiteral(2),True,[]),
    #                         For(Id('b'),FloatLiteral(1),IntLiteral(2),True,[])])
    #                     ])
    #     expect = "Type Mismatch In Statement: "+str(For(Id('b'),FloatLiteral(1),IntLiteral(2),True,[]))
    #     self.assertTrue(TestChecker.test(input,expect,407))
    #
    # def test_para_func4(self):
    #     input = Program([FuncDecl(Id("main"),
    #                         [VarDecl(Id('a'), StringType())],
    #                         [VarDecl(Id('b'), IntType())],
    #                         [For(Id('a'),IntLiteral(1),IntLiteral(2),True,[])])
    #                     ])
    #     expect = "Type Mismatch In Statement: "+str(For(Id('a'),IntLiteral(1),IntLiteral(2),True,[]))
    #     self.assertTrue(TestChecker.test(input,expect,408))
    #
    # def test_body_func1(self):
    #     input = Program([FuncDecl(Id("main"),
    #                         [VarDecl(Id('a'), IntType())],
    #                         [VarDecl(Id('b'), FloatType())],
    #                         [For(Id('a'),IntLiteral(1),IntLiteral(2),True,[CallStmt(Id("putIntLn"),[Id("b")])])])
    #                     ])
    #     expect = "Type Mismatch In Statement: "+str(CallStmt(Id("putIntLn"),[Id("b")]))
    #     self.assertTrue(TestChecker.test(input,expect,409))






    def test_decl_fun(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())],
                            [])
                        ,
                        FuncDecl(Id("find"),
                                [],
                                [],
                                [For(Id('b'),IntLiteral(1),IntLiteral(2),True,[])]
                                )
                        ])
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_if1(self):
        input = Program([VarDecl(Id('c'), BoolType()),
                        FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())
                            ],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                               [CallStmt(Id("putIntLn"),[Id("a")])],
                               [CallStmt(Id("putFloat"),[Id("b")])]),
                             If(BinaryOp('+',Id('c'),Id('c')),
                                [CallStmt(Id("putIntLn"),[Id("a")])],
                                [CallStmt(Id("putIntLn"),[Id("b")])])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('+',Id('c'),Id('c')))
        self.assertTrue(TestChecker.test(input,expect,601))

    def test_if2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('>=',Id('b'),Id('a')),
                               [CallStmt(Id("putIntLn"),[Id("a")])],
                               [CallStmt(Id("putFloat"),[Id("b")])]),
                             If(BinaryOp('/',Id('a'),Id('a')),
                                [CallStmt(Id("putIntLn"),[Id("a")])],
                                [CallStmt(Id("putIntLn"),[Id("b")])])]
                        )])
        expect = "Type Mismatch In Statement: "+str(If(BinaryOp('/',Id('a'),Id('a')),
           [CallStmt(Id("putIntLn"),[Id("a")])],
           [CallStmt(Id("putIntLn"),[Id("b")])]))
        self.assertTrue(TestChecker.test(input,expect,602))

    def test_for1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [For(Id('a'),BinaryOp('*',Id('a'),Id('a')),Id('a'),True,[]),
                             For(Id('b'),BinaryOp('*',Id('a'),Id('a')),Id('a'),True,[])]
                        )])
        expect = "Type Mismatch In Statement: "+str(For(Id('b'),BinaryOp('*',Id('a'),Id('a')),Id('a'),True,[]))
        self.assertTrue(TestChecker.test(input,expect,701))

    def test_for2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [For(Id('a'),BinaryOp('*',Id('a'),Id('a')),Id('a'),True,[]),
                             For(Id('a'),BinaryOp('*',Id('b'),Id('a')),Id('a'),True,[])]
                        )])
        expect = "Type Mismatch In Statement: "+str(For(Id('a'),BinaryOp('*',Id('b'),Id('a')),Id('a'),True,[]))
        self.assertTrue(TestChecker.test(input,expect,702))

    def test_while1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[]),
                             While(BinaryOp('*',Id('a'),Id('b')),[])
                            ]
                        )])
        expect = "Type Mismatch In Statement: "+str(While(BinaryOp('*',Id('a'),Id('b')),[]))
        self.assertTrue(TestChecker.test(input,expect,801))

    def test_while2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[]),
                             While(BinaryOp('orelse',Id('c'),Id('c')),[CallStmt(Id('putIntLn'),[Id('c')])])
                            ]
                        )])
        expect = "Type Mismatch In Statement: "+str(CallStmt(Id('putIntLn'),[Id('c')]))
        self.assertTrue(TestChecker.test(input,expect,802))

    def test_assign1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [Assign(Id('c'),BooleanLiteral(True)),
                             Assign(Id('a'),Id('b'))
                            ]
                        )])
        expect = "Type Mismatch In Statement: "+str(Assign(Id('a'),Id('b')))
        self.assertTrue(TestChecker.test(input,expect,1101))

    def test_assign2(self):
        input = Program([FuncDecl(Id("main"),[],[],
                             [Assign(Id("d"),IntLiteral(5)),
                             Assign(Id("c"),Id("d")),Assign(Id("b"),Id("c")),
                             Assign(Id("a"),Id("b"))],VoidType())])
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,1102))


    def test_BinaryOp1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())],
                            [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('b'))]),
                            CallStmt(Id('putInt'),[BinaryOp('+',BooleanLiteral('true'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('+',BooleanLiteral('true'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,502))

    def test_BinaryOp2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())],
                            [CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral('true'),BooleanLiteral('false'))]),
                            CallStmt(Id('putBool'),[BinaryOp('and',BooleanLiteral('true'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('and',BooleanLiteral('true'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,503))

    def test_BinaryOp3(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())],
                            [CallStmt(Id('putBool'),[BinaryOp('or',BooleanLiteral('true'),BooleanLiteral('false'))]),
                            CallStmt(Id('putBool'),[BinaryOp('or',BooleanLiteral('true'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('or',BooleanLiteral('true'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,504))

    def test_BinaryOp4(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType())],
                            [CallStmt(Id('putBool'),[BinaryOp('andthen',BooleanLiteral('true'),BooleanLiteral('false'))]),
                            CallStmt(Id('putBool'),[BinaryOp('orelse',BooleanLiteral('true'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('orelse',BooleanLiteral('true'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,505))

    def test_BinaryOp5(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                            VarDecl(Id('c'), StringType()),
                            VarDecl(Id('d'), BoolType())],
                            [CallStmt(Id('putIntLn'),[BinaryOp('div',Id('a'),Id('a'))]),
                            CallStmt(Id('putInt'),[BinaryOp('div',BooleanLiteral('true'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('div',BooleanLiteral('true'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,506))

    def test_BinaryOp6(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                            VarDecl(Id('c'), StringType()),
                            VarDecl(Id('d'), BoolType())],
                            [CallStmt(Id('putIntLn'),[BinaryOp('div',Id('a'),Id('a'))]),
                            CallStmt(Id('putInt'),[BinaryOp('div',Id('c'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('div',Id('c'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,507))

    def test_BinaryOp7(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                            VarDecl(Id('c'), StringType()),
                            VarDecl(Id('d'), BoolType())],
                            [CallStmt(Id('putIntLn'),[BinaryOp('*',Id('a'),Id('a'))]),
                            CallStmt(Id('putFloat'),[BinaryOp('*',Id('c'),Id('a'))]),
                            CallStmt(Id('putIntLn'),[BinaryOp('*',Id('a'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('*',Id('c'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,508))

    def test_BinaryOp8(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                            VarDecl(Id('c'), StringType()),
                            VarDecl(Id('d'), BoolType())],
                            [CallStmt(Id('putBool'),[BinaryOp('<>',Id('a'),Id('b'))]),
                            CallStmt(Id('putInt'),[BinaryOp('<>',Id('d'),Id('a'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('<>',Id('d'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,509))

    def test_BinaryOp9(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                            VarDecl(Id('c'), StringType()),
                            VarDecl(Id('d'), BoolType())],
                            [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))]),
                            CallStmt(Id('putFloat'),[BinaryOp('/',Id('d'),Id('b'))])]
                        )])
        expect = "Type Mismatch In Expression: "+str(BinaryOp('/',Id('d'),Id('b')))
        self.assertTrue(TestChecker.test(input,expect,510))


    def test_with1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [With([VarDecl(Id('d'),IntType()),VarDecl(Id('e'), FloatType())],
                                  [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])]),
                             With([VarDecl(Id('b'),IntType()),VarDecl(Id('e'), FloatType())],
                                   [CallStmt(Id('putFloat'),[BinaryOp('/',Id('c'),Id('a'))])])
                            ]
                        )])
        expect = "Type Mismatch In Expression: "+ str(BinaryOp('/',Id('c'),Id('a')))
        self.assertTrue(TestChecker.test(input,expect,901))

    def test_with2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [With([VarDecl(Id('a'),IntType()),VarDecl(Id('e'), FloatType())],
                                  [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])]),
                             With([VarDecl(Id('b'),IntType()),VarDecl(Id('e'), FloatType())],
                                   [CallStmt(Id('putFloat'),[BinaryOp('/',Id('k'),Id('a'))])])
                            ]
                        )])
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,902))

    def test_with3(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [With([VarDecl(Id('c'),IntType()),VarDecl(Id('e'), FloatType())],
                                  [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])]),
                             With([VarDecl(Id('b'),IntType()),VarDecl(Id('e'), FloatType())],
                                   [CallStmt(Id('putFloat'),[BinaryOp('/',Id('k'),Id('a'))])])
                            ]
                        )])
        expect = "Undeclared Identifier: k"
        self.assertTrue(TestChecker.test(input,expect,903))


    def test_with4(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [With([VarDecl(Id('c'),IntType()),VarDecl(Id('e'), FloatType())],
                                  [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])]),
                             With([VarDecl(Id('b'),IntType()),VarDecl(Id('b'), FloatType())],
                                   [CallStmt(Id('putFloat'),[BinaryOp('/',Id('k'),Id('a'))])])
                            ]
                        )])
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,904))





    def test_return1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [Assign(IntLiteral(5), Id('a')),
                            Return(Id('a'))
                            ],
                            IntType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [Assign(IntLiteral(5), Id('a'))
                                             ],IntType()
                                                  )
                        ])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,1001))

    def test_return2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [With([VarDecl(Id('c'),IntType()),VarDecl(Id('e'), FloatType())],
                                                          [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])]),
                            Return(Id('a'))
                            ],
                            IntType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [With([VarDecl(Id('c'),IntType()),VarDecl(Id('e'), FloatType())],
                                                                           [CallStmt(Id('putFloat'),[BinaryOp('/',Id('a'),Id('a'))])])
                                             ],IntType()
                                                  )
                        ])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,1002))

    def test_return3(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return(Id('a'))
                            ],
                            IntType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])])
                                             ],IntType()
                                                  )
                        ])
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,1003))

    def test_return4(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return()
                            ]
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                              Return(Id('a'))
                                             ]
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+str(Return(Id('a')))
        self.assertTrue(TestChecker.test(input,expect,1004))

    def test_return5(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return(Id('a'))
                            ],
                            IntType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                             Return()
                                             ],IntType()
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+ str(Return())
        self.assertTrue(TestChecker.test(input,expect,1005))

    def test_return6(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return(Id('a'))
                            ],
                            IntType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                             Return(Id('b'))
                                             ],IntType()
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+ str(Return(Id('b')))
        self.assertTrue(TestChecker.test(input,expect,1006))

    def test_return7(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return(ArrayType(2,7,IntType()))
                            ],
                            ArrayType(2,7,IntType())
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                             Return(ArrayType(1,6,IntType()))
                                             ],ArrayType(1,5,IntType())
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+ str(Return(ArrayType(1,6,IntType())))
        self.assertTrue(TestChecker.test(input,expect,1007))

    def test_return8(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")])],
                                                       [CallStmt(Id("putFloat"),[Id("b")])]),
                            Return(Id('a'))
                            ],
                            FloatType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                             Return(Id('b'))
                                             ],IntType()
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+ str(Return(Id('b')))
        self.assertTrue(TestChecker.test(input,expect,1008))

    def test_return9(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [If(BinaryOp('and',Id('c'),Id('c')),
                                                       [CallStmt(Id("putIntLn"),[Id("a")]),Return(Id('a'))],
                                                       [CallStmt(Id("putFloat"),[Id("b")]),Return(Id('a'))])

                            ],
                            FloatType()
                                 ),
                         FuncDecl(Id("foo"),
                                             [VarDecl(Id('a'), IntType())],
                                             [VarDecl(Id('b'), FloatType()),
                                              VarDecl(Id('c'), BoolType())],
                                             [If(BinaryOp('and',Id('c'),Id('c')),
                                                                        [CallStmt(Id("putIntLn"),[Id("a")]), Return(Id('a'))],
                                                                        [CallStmt(Id("putFloat"),[Id("b")])]),
                                             Return(Id('b'))
                                             ],IntType()
                                                  )
                        ])
        expect = "Type Mismatch In Statement: "+ str(Return(Id('b')))
        self.assertTrue(TestChecker.test(input,expect,1009))

    def test_break_cont1(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[Break()]),
                             While(BinaryOp('<=',Id('a'),Id('b')),[]),Break()
                            ]
                        )])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,3001))

    def test_break_cont2(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[Break()]),
                             While(BinaryOp('<=',Id('a'),Id('b')),[]),Continue()
                            ]
                        )])
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,3002))

    def test_break_cont3(self):
        input = Program([FuncDecl(Id("main"),
                            [VarDecl(Id('a'), IntType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],

                             [If(BinaryOp('and',Id('c'),Id('c')),
                                [CallStmt(Id("putIntLn"),[Id("a")]), Break()],
                                [CallStmt(Id("putFloat"),[Id("b")])])
                                ]

                        )])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,3003))

    def test_break_cont4(self):
        input = Program([FuncDecl(Id("main"),
                            [],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[Break()]),
                             While(BinaryOp('<=',Id('a'),Id('b')),[]),Break()
                            ]
                        ),VarDecl(Id('a'), IntType())])
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,3004))

    def test_break_cont5(self):
        input = Program([FuncDecl(Id("foo"),
                            [VarDecl(Id('f'), FloatType()),VarDecl(Id('d'), IntType()),VarDecl(Id('e'), BoolType())],
                            [VarDecl(Id('b'), FloatType()),
                             VarDecl(Id('c'), BoolType())],
                            [While(BinaryOp('>',Id('a'),Id('b')),[Break()]),
                             While(BinaryOp('<=',Id('a'),Id('b')),[])
                            ]
                        ),VarDecl(Id('a'), IntType()),
                         FuncDecl(Id("main"),
                                             [],
                                             [],
                                             [CallStmt(Id('foo'),[FloatLiteral(1.25),IntLiteral(10),BooleanLiteral(True)])
                                             ]
                                         )
                        ]
                       )
        expect = "Type Mismatch In Statement: "+str(CallStmt(Id('foo'),[FloatLiteral(1.25),IntLiteral(10),StringLiteral('fdsf')]))
        self.assertTrue(TestChecker.test(input,expect,3005))




    # def test_body_func2(self):
    #     input = Program([FuncDecl(Id("main"),
    #                         [VarDecl(Id('a'), IntType())],
    #                         [VarDecl(Id('b'), FloatType())],
    #                         [For(Id('a'),IntLiteral(1),IntLiteral(2),True,[CallExpr(Id("putIntLn"),[Id("b")])])])
    #                     ])
    #     expect = "Type Mismatch In Statement: "+str(CallStmt(Id("putIntLn"),[Id("b")]))
    #     self.assertTrue(TestChecker.test(input,expect,410))

    # def test_body_func1(self):
    #     input = Program([FuncDecl(Id("main"),
    #                     [],
    #                     [VarDecl(Id('a'), FloatType())],
    #                     [CallStmt(Id("putInt"),[Id('a')])])])
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,408))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],[],[
    #         CallStmt(Id("foo"),[])])])
    #     expect = "Undeclared Procedure: foo"
    #     self.assertTrue(TestChecker.test(input,expect,402))
    #
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],[VarDecl(Id('a'),FloatType())],[
    #                 CallStmt(Id("putIntLn"),[Id('a')])])])
    #
    #     expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    # def test_q2_7(self):
    #     input = Program([
    #             FuncDecl(Id("foo"),[VarDecl(Id("c"),FloatType())],
    #                                 [VarDecl(Id("f"),IntType()),VarDecl(Id("d"),FloatType())],[
    #                                 CallStmt(Id("putIntLn"),[Id("c")])
    #                                 ],IntType()),
    #             FuncDecl(Id("main"),[],[],[])])
    #
    #     expect = "Redeclared Function: main"
    #     self.assertTrue(TestChecker.test(input,expect,407))



#cho CallExpr & CallExpr xài chung 1 hàm
