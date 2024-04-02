import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

    def test_codegen_00(self):
        input = \
            Program([
                FuncDecl("main",[],Block([
                    CallStmt("writeNumber",[BinaryOp("+",NumberLiteral(4),NumberLiteral(3))])
                ]))
            ])
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_codegen_01(self):
        input = \
            Program([
                FuncDecl("main",[],Block([
                    CallStmt("writeNumber",[NumberLiteral(16)])
                ]))
            ])
        expect = "16"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_codegen_02(self):
        input = \
            Program([
                FuncDecl("main",[],Block([
                    CallStmt("writeNumber",[BinaryOp("+",BinaryOp("+",NumberLiteral(1),NumberLiteral(2)),NumberLiteral(3))])
                ]))
            ])
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,502))