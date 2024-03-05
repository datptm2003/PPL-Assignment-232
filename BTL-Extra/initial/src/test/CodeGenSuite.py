import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """void main() {putInt(100);}"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))

    

    def test_int_ast(self):
        input = \
            Program([
                FuncDecl("main",[],Block([
                    CallStmt("putInt",[BinaryOp("+",NumberLiteral(3),NumberLiteral(4))])
                ]))
            ])
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,501))
