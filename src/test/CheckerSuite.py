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
    #     self.assertTrue(TestChecker.test(input,expect,413))
#     def test_5(self):
#         input = """
#         var a:integer;
#         function foo(a, b:integer):integer;
#         begin
# 	       if (a > b) then a := 1 + b;
# 	       else a := b + 2;
# 	       return a;
#         end
#         function foo1(a:integer):integer;
#         var b, c, d:integer;
#         begin
# 	           b := 2;
# 	           c := 3;
# 	           if (a > b) then d := a + c;
# 	           else d := b + foo2(1);
# 	           return d;
#        end
#        var b:integer;
#        function foo2(a:integer):integer;
#        begin
# 	      while (a > 5) do a := a + 1;
#
# 	         return a;
#       end
#       procedure main(); begin
# 	     a := foo(foo1(1),foo2(2));
# 	     funy(4);
# 	     return ;
#       end
#
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 443))

    def test_5(self):
        input = """
        var a:integer;
var b:real;
var m:array[1 .. 10] of integer;
procedure main(); begin
	b := m[1] + -1;
	b := b * (1.0 + 1);
	b := not (m[1] = 1);
	return ;
end


"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))
