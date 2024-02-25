# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dclr.
    def visitDclr(self, ctx:ZCodeParser.DclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_prime.
    def visitNewline_prime(self, ctx:ZCodeParser.Newline_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_dclr.
    def visitVar_dclr(self, ctx:ZCodeParser.Var_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_list.
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_prime.
    def visitPara_prime(self, ctx:ZCodeParser.Para_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#para_dclr.
    def visitPara_dclr(self, ctx:ZCodeParser.Para_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_type.
    def visitVar_type(self, ctx:ZCodeParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_imp.
    def visitFunc_imp(self, ctx:ZCodeParser.Func_impContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_dclr.
    def visitFunc_dclr(self, ctx:ZCodeParser.Func_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_dclr.
    def visitArr_dclr(self, ctx:ZCodeParser.Arr_dclrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_acs.
    def visitArr_acs(self, ctx:ZCodeParser.Arr_acsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_elmt.
    def visitArr_elmt(self, ctx:ZCodeParser.Arr_elmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#num_prime.
    def visitNum_prime(self, ctx:ZCodeParser.Num_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_prime.
    def visitExpr_prime(self, ctx:ZCodeParser.Expr_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cmpr_type.
    def visitCmpr_type(self, ctx:ZCodeParser.Cmpr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assgn_expr.
    def visitAssgn_expr(self, ctx:ZCodeParser.Assgn_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_stmt.
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_prime.
    def visitElif_prime(self, ctx:ZCodeParser.Elif_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_stmt.
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_stmt.
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_prime.
    def visitStmt_prime(self, ctx:ZCodeParser.Stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)



del ZCodeParser