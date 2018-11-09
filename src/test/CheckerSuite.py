import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_undecl_3(self):
        input = """
                var a: real;
                procedure main();
                begin
                    a := 1 * b/2;
                end
                procedure b(i: boolean;j:real);
                begin
                    putIntLn(4);
                    a:=a+1;
                end
                """
        expect = 'Undeclared Identifier: b'
        self.assertTrue(TestChecker.test(input,expect,413))
