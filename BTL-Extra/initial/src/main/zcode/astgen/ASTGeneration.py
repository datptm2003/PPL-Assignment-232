from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declaration()))
        # return Program([VarDecl(Id(ctx.IDENTIFIER().getText()),NumberType())])

    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.dclr())] + self.visit(ctx.declaration())
        else:
            return [self.visit(ctx.dclr())]
        
    def visitDclr(self, ctx:ZCodeParser.DclrContext):
        if ctx.NEWLINE():
            if ctx.var_dclr():
                return self.visit(ctx.var_dclr())
            else:
                return self.visit(ctx.func_dclr())
        else:
            return self.visit(ctx.func_imp())
        
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        if ctx.newline_prime():
            return self.visit(ctx.newline_prime())
        else:
            return []
        
    def visitNewline_prime(self, ctx:ZCodeParser.Newline_primeContext):
        if ctx.newline_prime():
            return [ctx.NEWLINE()] + self.visit(ctx.newline_prime())
        else:
            return [ctx.NEWLINE()]
        
    def visitVar_dclr(self, ctx:ZCodeParser.Var_dclrContext):
        if ctx.VAR():
            return VarDecl(Id(ctx.ID().getText()),None,ctx.VAR().getText(),self.visit(ctx.expr()))
        elif ctx.DYNAMIC():
            if ctx.expr():
                return VarDecl(Id(ctx.ID().getText()),None,ctx.DYNAMIC().getText(),self.visit(ctx.expr()))
            else:
                return VarDecl(Id(ctx.ID().getText()),None,ctx.DYNAMIC().getText(),None)
        elif ctx.var_type():
            if ctx.expr():
                return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.var_type()),None,self.visit(ctx.expr()))
            else:
                return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.var_type()),None,None)
        else:
            return self.visit(ctx.arr_dclr())
        
    def visitPara_list(self, ctx:ZCodeParser.Para_listContext):
        if ctx.para_prime():
            return self.visit(ctx.para_prime())
        else: 
            return []
        
    def visitPara_prime(self, ctx:ZCodeParser.Para_primeContext):
        if ctx.SEP():
            return [self.visit(ctx.para_dclr())] + self.visit(ctx.para_prime())
        else:
            return [self.visit(ctx.para_dclr())]
        
    def visitPara_dclr(self, ctx:ZCodeParser.Para_dclrContext):
        if ctx.ID():
            return VarDecl(Id(ctx.ID().getText()),self.visit(ctx.var_type()),None,None)
        else:
            return VarDecl(Id(ctx.ID().getText()),ArrayType(self.visit(ctx.array)[1],self.visit(ctx.var_type())),None,None)
        
    def visitVar_type(self, ctx:ZCodeParser.Var_typeContext):
        if ctx.BOOL_TYPE():
            return BoolType()
        elif ctx.NUM_TYPE():
            return NumberType()
        else:
            return StringType()
        
    def visitFunc_imp(self, ctx:ZCodeParser.Func_impContext):
        if ctx.block():
            return FuncDecl(self.visit(ctx.func_dclr()).name,self.visit(ctx.func_dclr()).param,self.visit(ctx.block()))
        else:
            return FuncDecl(self.visit(ctx.func_dclr()).name,self.visit(ctx.func_dclr()).param,self.visit(ctx.return_stmt()))

    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        return Block(self.visit(ctx.stmt_list()))
    
    def visitFunc_dclr(self, ctx:ZCodeParser.Func_dclrContext):
        return FuncDecl(Id(ctx.ID().getText()),self.visit(ctx.para_list()),None)
    
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return (Id(ctx.ID().getText()),self.visit(ctx.expr_list()))
    
    def visitArr_dclr(self, ctx:ZCodeParser.Arr_dclrContext):
        if ctx.expr():
            return VarDecl(self.visit(ctx.array()),ArrayType(self.visit(ctx.array)[1],self.visit(ctx.var_type())),None,self.visit(ctx.expr()))
        else:
            return VarDecl(self.visit(ctx.array()),ArrayType(self.visit(ctx.array)[1],self.visit(ctx.var_type())),None,None)
    
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return (Id(ctx.ID().getText()),self.visit(ctx.num_prime()))

    def visitArr_acs(self, ctx:ZCodeParser.Arr_acsContext):
        if ctx.ID():
            return (Id(ctx.ID().getText()),self.visit(ctx.expr_prime()))
        else:
            return (CallExpr(self.visit(ctx.func_call())[0],self.visit(ctx.func_call())[1]),self.visit(ctx.expr_prime()))
    
    # def visitElmt_prime(self, ctx:ZCodeParser.Elmt_primeContext):
    #     if ctx.SEP():
    #         return [self.visit(ctx.elmt())] + self.visit(ctx.elmt_prime())
    #     else:
    #         return [self.visit(ctx.elmt())]
        
    # def visitElmt(self, ctx:ZCodeParser.ElmtContext):
    #     if ctx.arr_elmt():
    #         return self.visit(ctx.arr_elmt())
    #     else:
    #         return self.visit(ctx.expr())

    # def visitArr_list(self, ctx:ZCodeParser.Arr_listContext):
    #     if ctx.arr_prime():
    #         return self.visit(ctx.arr_prime())
    #     else:
    #         return []
        
    # def visitArr_prime(self, ctx:ZCodeParser.Arr_primeContext):
    #     if ctx.SEP():
    #         return [self.visit(ctx.arr_elmt())] + self.visit(ctx.arr_prime())
    #     else:
    #         return [self.visit(ctx.arr_elmt())]
        
    def visitArr_elmt(self, ctx:ZCodeParser.Arr_elmtContext):
        return ArrayLiteral(self.visit(ctx.expr_prime()))
    
    def visitNum_prime(self, ctx:ZCodeParser.Num_primeContext):
        if ctx.SEP():
            return [float(ctx.NUMBER().getText())] + self.visit(ctx.arr_prime())
        else:
            return [float(ctx.NUMBER().getText())]

    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.expr_prime():
            return self.visit(ctx.expr_prime())
        else:
            return []
    
    def visitExpr_prime(self, ctx:ZCodeParser.Expr_primeContext):
        if ctx.SEP():
            return [self.visit(ctx.expr())] + self.visit(ctx.expr_prime())
        else:
            return [self.visit(ctx.expr())]
        
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.STR_CONCAT().getText(),self.visit(ctx.expr1(0)),self.visit(ctx.expr1(1)))
        else:
            return self.visit(ctx.expr1(0))
        
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(self.visit(ctx.cmpr_type()),self.visit(ctx.expr2(0)),self.visit(ctx.expr2(1)))
        else:
            return self.visit(ctx.expr2(0))
        
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 3:
            if ctx.AND():
                return BinaryOp(ctx.AND().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
            else:
                return BinaryOp(ctx.OR().getText(),self.visit(ctx.expr2()),self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())
        
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 3:
            if ctx.ADD():
                return BinaryOp(ctx.ADD().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
            else:
                return BinaryOp(ctx.SUB().getText(),self.visit(ctx.expr3()),self.visit(ctx.expr4()))
        else:
            return self.visit(ctx.expr4())
        
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 3:
            if ctx.MUL():
                return BinaryOp(ctx.MUL().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
            elif ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
            else:
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.expr4()),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr5())
        
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.NOT().getText(),self.visit(ctx.expr5()))
        else:
            return self.visit(ctx.expr6())
        
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.SUB().getText(),self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr7())
        
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.arr_elmt():
            return self.visit(ctx.arr_elmt())
        elif ctx.arr_acs():
            return None # Incomplete #
        elif ctx.func_call():
            return CallExpr(self.visit(ctx.func_call())[0],self.visit(ctx.func_call())[1])
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.BOOL():
            return BooleanLiteral(bool(ctx.BOOL().getText()))
        elif ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        else:
            return StringLiteral(ctx.STRING().getText())
        
    def visitCmpr_type(self, ctx:ZCodeParser.Cmpr_typeContext):
        # EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL | STR_EQUAL;
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        if ctx.LESS():
            return ctx.LESS().getText()
        if ctx.LESS_EQUAL():
            return ctx.LESS_EQUAL().getText()
        if ctx.GREATER():
            return ctx.GREATER().getText()
        if ctx.GREATER_EQUAL():
            return ctx.GREATER_EQUAL().getText()
        else:
            return ctx.STR_EQUAL().getText() 
        
    def visitAssgn_expr(self, ctx:ZCodeParser.Assgn_exprContext):
        if ctx.expr_prime():
            return Assign(ArrayCell(Id(ctx.ID().getText()),self.visit(ctx.expr_prime())),self.visit(ctx.expr()))
        else:
            return Assign(Id(ctx.ID().getText()),self.visit(ctx.expr()))
        
    def visitIf_stmt(self, ctx:ZCodeParser.If_stmtContext):
        return If(self.visit(ctx.expr()),self.visit(ctx.stmt()),self.visit(ctx.elif_list()),self.visit(ctx.else_stmt))
    
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        if ctx.elif_prime():
            return self.visit(ctx.elif_prime())
        else:
            return []
    
    def visitElif_prime(self, ctx:ZCodeParser.Elif_primeContext):
        if ctx.elif_prime():
            return [self.visit(ctx.elif_stmt())] + self.visit(ctx.elif_prime())
        else:
            return [self.visit(ctx.elif_stmt())]
        
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.expr()),self.visit(ctx.stmt()))
    
    def visitElse_stmt(self, ctx:ZCodeParser.Else_stmtContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        else:
            return None
        
    def visitFor_stmt(self, ctx:ZCodeParser.For_stmtContext):
        return For(Id(ctx.ID().getText()),self.visit(ctx.expr(0)),self.visit(ctx.expr(1)),self.visit(ctx.stmt()))
    
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return(None)
        
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        if ctx.stmt_prime():
            return self.visit(ctx.stmt_prime())
        else:
            return []
        
    def visitStmt_prime(self, ctx:ZCodeParser.Stmt_primeContext):
        if ctx.stmt_prime():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_prime())
        else:
            return [self.visit(ctx.stmt())]

    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        elif ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        elif ctx.BREAK():
            return Break()
        elif ctx.CONTINUE():
            return Continue()
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.var_dclr():
            return self.visit(ctx.var_dclr())
        elif ctx.arr_dclr():
            return self.visit(ctx.arr_dclr())
        elif ctx.assgn_expr():
            return self.visit(ctx.assgn_expr())
        elif ctx.func_call():
            return CallStmt(self.visit(ctx.func_call())[0],self.visit(ctx.func_call())[1])
        else:
            return self.visit(ctx.return_stmt())
