import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    # def test_undecl_3(self):
    #     input = """
    #             var a: real;
    #             procedure main();
    #             begin
    #                 a := 1 * b/2;
    #             end
    #             procedure b(i: boolean;j:real);
    #             begin
    #                 putIntLn(4);
    #                 a:=a+1;
    #             end
    #             """
    #     expect = 'Undeclared Identifier: b'
        # self.assertTrue(TestChecker.test(input,expect,413))
    def test_6(self):
        input = """
        var a:integer;
        function foo(a, b:integer):integer;
        begin
	       if (a > b) then a := 1 + b;
	       else a := b + 2;
	       return a;
        end
        function foo1(a:integer):integer;
        var b, c, d:integer;
        begin
	           b := 2;
	           c := 3;
	           if (a > b) then d := a + c;
	           else d := b + foo2(1);
	           return d;
       end
       var b:integer;
       function foo2(a:integer):integer;
       begin
	      while (a > 5) do a := a + 1;

	         return a;
      end
      procedure main(); begin
	     a := foo(foo1(1),foo2(2));
	     funy(4);
	     return ;
      end

"""
        expect = "Undeclared Procedure: funy"
        self.assertTrue(TestChecker.test(input, expect, 443))
#
#     def test_13(self):
#         input = """
#         var a:integer;
# var b:real;
# var m:array[1 .. 10] of integer;
# procedure main(); begin
# 	b := m[1] + -1;
# 	b := b * (1.0 + 1);
# 	b := not (m[1] = 1);
# 	return ;
# end
#
#
# """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(b),UnaryOp(not,BinaryOp(=,ArrayCell(Id(m),IntLiteral(1)),IntLiteral(1))))"
#         self.assertTrue(TestChecker.test(input, expect, 413))
#
#     def test_5(self):
#         input = """
#         var a:integer;
# procedure funcA();
# var b:integer;
# begin
#
# 	a := 7;
# 	b := a;
# end
# function sum(b:integer):integer;
# var d:integer;
# begin
#
# 	d := 7;
# 	return a + b + d;
# end
# procedure main();
# var m:array[1 .. 10] of integer;
# begin
#
# 	m[1] := sum(3);
# 	funcA();
# 	a := 1 + n[1];
# 	return ;
# end
#
#
# """
#         expect = "Undeclared Identifier: n"
#         self.assertTrue(TestChecker.test(input, expect, 405))
#
#     def test_10(self):
#         input = """
# var a, b, c:integer;
# var d:boolean;
# var e:real;
# var m: array [1 .. 100] of integer;
# function foo():integer; begin  return 0; end
# procedure main(); begin
# 	b := foo();
# 	d := true;
# 	a := m[0] + 1;
# 	c := m[d] + 1;
# 	return ;
# end
#
# """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(m),Id(d))"
#         self.assertTrue(TestChecker.test(input, expect, 410))
#
#     def test_12(self):
#         input = """
# var a:integer;
# var m:array[1 .. 100] of real;
# procedure foo(); begin
# 	a := - -(a - -1);
# end
# procedure main(); begin
#         foo();
# 	a := -(m[1] + -1 > 1.2);
# 	return ;
# end
#
#
# """
#         expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(>,BinaryOp(+,ArrayCell(Id(m),IntLiteral(1)),UnaryOp(-,IntLiteral(1))),FloatLiteral(1.2)))"
#         self.assertTrue(TestChecker.test(input, expect, 412))
#
#     def test_14(self):
#         input = """
# var a, b, c:integer;
# procedure foo(); begin
# 	while (a < 100) do begin
# 		a := a + 1;
# 		break;
# 	end
# 	return ;
# end
# procedure main(); begin
# 	while (a < 100) do begin
# 		a := a + 1;
# 		break;
# 	end
#         foo();
# 	if(a = 100) then break;
# 	return ;
# end
#
#
#
# """
#         expect = "Break Not In Loop"
#         self.assertTrue(TestChecker.test(input, expect, 414))
#
#     def test_15(self):
#         input = """
# function foo():integer;
# var a:integer;
# begin
# 	a := 4;
# 	if (a = 10) then begin
# 		return 1;
# 	end
# 	return 10;
# end
#
# procedure main();
# var a:integer;
# begin
# 	a := 0;
#
# 	if (foo() > 1) then begin
# 		if(foo2() <= 100) then
#
# 			return ;
# 		else
# 			return ;
# 	end
# 	else begin
# 		a := 2;
# 		return ;
# 	end
# end
#
# """
#         expect = "Undeclared Function: foo2"
#         self.assertTrue(TestChecker.test(input, expect, 415))
