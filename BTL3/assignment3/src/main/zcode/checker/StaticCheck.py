from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

# o = {
#         name1: [type,scope],
#         name2: [type,scope],
#         name3: [type,scope]
#     }

class Symbol:
    def __init__(self,name,typ,scope):
        self.name = name
        self.typ = typ
        self.scope = scope

class VarSym(Symbol):
    def __init__(self, name, value, typ, scope):
        super().__init__(name, value, typ, scope)
        self.value = value

class FuncSym(Symbol):
    def __init__(self, name, ret_typ, scope, param_typ):
        super().__init__(name, ret_typ, scope)
        self.param_typ = param_typ

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        o = {}
        o['var'] = None
        o['for'] = False
        o['func'] = []
        o['dynamic'] = []
        o['return'] = None
        self.visit(self.ast, o)

    def enterScope(self,o):
        new_o = {}
        for name in o:
            if name in ['var','for','dynamic','func','return']:
                new_o[name] = o[name]
                continue
            new_o[name] = []
            for elmt in o[name]:
                new_o[name].append(elmt)
            new_o[name][1] += 1
        return new_o

    def copyType(self,name,base_typ,o):
        if base_typ is None:
            return None
        for typ_obj in [NumberType(),BoolType(),StringType()]:
            if base_typ == type(typ_obj):
                o[name][0] = typ_obj
                return type(typ_obj)
        return None
    
    def copyTypeNoId(self,base_typ):
        if base_typ is None:
            return None
        for typ_obj in [NumberType(),BoolType(),StringType()]:
            if base_typ == type(typ_obj):
                return typ_obj
        return None

    def filterScope(self,func,scope,o):
        def scope_func(pair):
            _, value = pair
            if func(value[1], scope):
                return True
            else:
                return False
        return dict(filter(scope_func, o.items()))

    def visitProgram(self, ast, o):
        for dclr in ast.decl:
            self.visit(dclr,o)
        if len(o['func']) > 0:
            raise NoDefinition(o['func'][0])
        for name in o:
            if name == 'main' and type(o['main'][0]) == list:
                return
        raise NoEntryPoint()

    def visitVarDecl(self, ast, o):
        o['dynamic'] = []
        name = ast.name.name
        if name in o and o[name][1] == 0:
            raise Redeclared(Variable(),name)
        else:
            if ast.varInit is not None:
                self.visit(ast.varInit,o)
                if ast.varType is not None:
                    if o['var'] is None:
                        raise TypeCannotBeInferred(ast)
                    if type(o['var']) != type(ast.varType):
                        ############
                        #   TODO   #
                        ############
                        raise TypeMismatchInExpression(ast.varInit)
                    else:
                        o[name] = [ast.varType,0]
                else:
                    o[name] = [o['var'],0]
            else:
                if ast.varType is not None:
                    o[name] = [ast.varType,0]
                else:
                    o[name] = [None,0]
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)
        # print(name,"==",o)


    def visitFuncDecl(self, ast, o):
        # Gia su khai bao bien cung ten tham so trong than ham la hop le
        o['return'] = None
        func_name = ast.name.name
        if func_name in o:
            raise Redeclared(Function(),func_name)
        
        if ast.body is None:
            o['func'].append(func_name)
        else:
            if func_name in o['func']:
                o['func'].remove(func_name)
        
        o[func_name] = [[],0]
        # print("---",o)
        new_o = self.enterScope(o)
        for dclr in ast.param:
            name = dclr.name.name
            if name in new_o and new_o[name][1] == 0:
                raise Redeclared(Parameter(),name)
            else:
                new_o[name] = [dclr.varType,0]
                o[func_name][0].append(dclr.varType)
        
        if ast.body is not None:
            self.visit(ast.body,new_o)
            # print("@@@",func_name,new_o['return'])
            o['return'] = self.copyTypeNoId(type(new_o['return']))
            o[func_name][0].append(new_o['return'])
        else:
            o[func_name][0].append(None)
        
        

    def visitNumberType(self, ast, o):
        pass

    def visitBoolType(self, ast, o):
        pass

    def visitStringType(self, ast, o):
        pass

    def visitArrayType(self, ast, o):
        
        pass

    def visitBinaryOp(self, ast, o):
        self.visit(ast.left,o)
        ltype = type(o['var']) if o['var'] is not None else None
        self.visit(ast.right,o)
        rtype = type(o['var']) if o['var'] is not None else None

        if ast.op in ['+','-','*','/','%']:
            # print("$$",ltype,rtype)
            if ltype is None:
                if type(ast.left) == Id:
                    ltype = self.copyType(ast.left.name,NumberType,o)
                    if ast.left.name in o['dynamic']:
                        o['dynamic'].remove(ast.left.name)
            if rtype is None:
                if type(ast.right) == Id:
                    rtype = self.copyType(ast.right.name,NumberType,o)
                    if ast.right.name in o['dynamic']:
                        o['dynamic'].remove(ast.right.name)
            is_valid = (ltype == NumberType and rtype == NumberType)
            ret_type = NumberType()
        elif ast.op in ['and','or']:
            if ltype is None:
                if type(ast.left) == Id:
                    ltype = self.copyType(ast.left.name,BoolType,o)
                    if ast.left.name in o['dynamic']:
                        o['dynamic'].remove(ast.left.name)
            if rtype is None:
                if type(ast.right) == Id:
                    rtype = self.copyType(ast.right.name,BoolType,o)
                    if ast.right.name in o['dynamic']:
                        o['dynamic'].remove(ast.right.name)

            is_valid = (ltype == BoolType and rtype == BoolType)
            ret_type = BoolType()
        elif ast.op in ['...']:
            if ltype is None:
                if type(ast.left) == Id:
                    ltype = self.copyType(ast.left.name,StringType,o)
                    if ast.left.name in o['dynamic']:
                        o['dynamic'].remove(ast.left.name)
            if rtype is None:
                if type(ast.right) == Id:
                    rtype = self.copyType(ast.right.name,StringType,o)
                    if ast.right.name in o['dynamic']:
                        o['dynamic'].remove(ast.right.name)

            is_valid = (ltype == StringType and rtype == StringType)
            ret_type = StringType()
        elif ast.op in ['=','!=','>','<','>=','<=']:
            if ltype is None:
                if type(ast.left) == Id:
                    ltype = self.copyType(ast.left.name,NumberType,o)
                    if ast.left.name in o['dynamic']:
                        o['dynamic'].remove(ast.left.name)
            if rtype is None:
                if type(ast.right) == Id:
                    rtype = self.copyType(ast.right.name,NumberType,o)
                    if ast.right.name in o['dynamic']:
                        o['dynamic'].remove(ast.right.name)

            is_valid = (ltype == NumberType and rtype == NumberType)
            ret_type = BoolType()
        elif ast.op in ['==']:
            if ltype is None:
                if type(ast.left) == Id:
                    ltype = self.copyType(ast.left.name,StringType,o)
                    if ast.left.name in o['dynamic']:
                        o['dynamic'].remove(ast.left.name)
            if rtype is None:
                if type(ast.right) == Id:
                    rtype = self.copyType(ast.right.name,StringType,o)
                    if ast.right.name in o['dynamic']:
                        o['dynamic'].remove(ast.right.name)

            is_valid = (ltype == StringType and rtype == StringType)
            ret_type = BoolType()

        if is_valid:
            o['var'] = ret_type
        else:
            # print("YYYYY")
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        self.visit(ast.operand,o)
        opr_type = type(o['var']) if o['var'] is not None else None

        if ast.op in ['-']:
            if opr_type is None:
                if type(ast.operand) == Id:
                    opr_type = self.copyType(ast.operand.name,NumberType,o)
                if ast.operand.name in o['dynamic']:
                    o['dynamic'].remove(ast.operand.name)
            is_valid = (opr_type == NumberType)
            ret_type = NumberType()
        elif ast.op in ['not']:
            if opr_type is None:
                if type(ast.operand) == Id:
                    opr_type = self.copyType(ast.operand.name,BoolType,o)
                    if ast.operand.name in o['dynamic']:
                        o['dynamic'].remove(ast.operand.name)
            is_valid = (opr_type == BoolType)
            ret_type = BoolType()
        
        if is_valid:
            o['var'] = ret_type
        else:
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, o):
        name = ast.name.name
        if name not in o:
            raise Undeclared(Function(),name)
        else:
            if len(ast.args) != len(o[name][0]) - 1 or o[name][0][-1] is None or type(o[name][0][-1]) == VoidType:
                raise TypeMismatchInExpression(ast)
            else:
                idx = 0
                for arg in ast.args:
                    self.visit(arg,o)
                    if o['var'] is None:
                        if type(arg) == Id:
                            # print("XXXXXX")
                            o['dynamic'].append(arg.name)
                            # print("*******",o)
                        continue
                    if type(o['var']) != type(o[name][0][idx]):
                        raise TypeMismatchInExpression(ast)
                    idx += 1
                o['var'] = self.copyTypeNoId(type(o[name][0][-1]))


    def visitId(self, ast, o):
        if ast.name not in o:
            raise Undeclared(Identifier(),ast.name)
        else:
            o['var'] = o[ast.name][0]

    def visitArrayCell(self, ast, o):
        self.visit(ast.arr,o)
        arr_type_obj = o['var']
        if arr_type_obj is None or type(arr_type_obj) != ArrayType:
            raise TypeMismatchInExpression(ast)
        else:
            if len(arr_type_obj.size) != len(ast.idx):
                raise TypeMismatchInExpression(ast)
            for idx in ast.idx:
                if type(idx) != NumberType:
                    raise TypeMismatchInExpression(ast)

    def visitBlock(self, ast, o):
        new_o = self.enterScope(o)
        # print(o,"\n",new_o,"\n\n")
        for stmt in ast.stmt:
            self.visit(stmt,new_o)
        # for typ_obj in [NumberType(),BoolType(),StringType()]:
        #     if type(new_o['return']) == type(typ_obj):
        #         o['return'] = typ_obj
        #         break
        o['return'] = self.copyTypeNoId(type(new_o['return']))
        print(new_o)

    def visitIf(self, ast, o):
        o['dynamic'] = []
        self.visit(ast.expr)
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast) 
        self.visit(ast.thenStmt)
        if ast.elifStmt is not None:
            self.visit(ast.elifStmt)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt)
        

    def visitFor(self, ast, o):
        self.visit(ast.name,o)
        self.visit(ast.condExpr,o)
        self.visit(ast.updExpr,o)
        outer_for = o['for']
        o['for'] = True
        self.visit(ast.body,o)
        o['for'] = outer_for

    def visitContinue(self, ast, o):
        if not o['for']:
            raise MustInLoop(ast)
        

    def visitBreak(self, ast, o):
        if not o['for']:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o):
        if ast.expr is not None:
            self.visit(ast.expr,o)
            # for typ_obj in [NumberType(),BoolType(),StringType()]:
            #     if type(o['var']) == type(typ_obj):
            #         o['return'] = typ_obj
            #         break
            if o['var'] is None:
                raise TypeCannotBeInferred(ast)
            o['return'] = self.copyTypeNoId(type(o['var']))
        else:
            o['return'] = VoidType()

    def visitAssign(self, ast, o):
        o['dynamic'] = []
        self.visit(ast.rhs,o)
        rtype = type(o['var']) if o['var'] is not None else None
        self.visit(ast.lhs,o)
        ltype = type(o['var']) if o['var'] is not None else None
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)
        if ltype is None:
            ltype = self.copyType(ast.lhs.name,rtype,o)
        else:
            if ltype != rtype:
                raise TypeMismatchInStatement(ast)


    def visitCallStmt(self, ast, o):
        o['dynamic'] = []
        name = ast.name.name
        if name not in o:
            raise Undeclared(Function(),name)
        else:
            if len(ast.args) != len(o[name][0]) - 1 or o[name][0][-1] is None or o[name][0][-1] != VoidType():
                raise TypeMismatchInStatement(ast)
            else:
                idx = 0
                for arg in ast.args:
                    self.visit(arg,o)
                    if o['var'] is None:
                        raise TypeCannotBeInferred(ast)
                    if type(o['var']) != type(o[name][0][idx]):
                        raise TypeMismatchInStatement(ast)
                    idx += 1
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)

    def visitNumberLiteral(self, ast, o):
        o['var'] = NumberType()

    def visitBooleanLiteral(self, ast, o):
        o['var'] = BooleanType()

    def visitStringLiteral(self, ast, o):
        o['var'] = StringType()

    def visitArrayLiteral(self, ast, o):
        common_typ = None
        for e in ast.value:
            self.visit(e,o)
            if o['var'] is not None and type(o['var']) != VoidType:
                if common_typ is None:
                    common_typ = o['var']
                else:
                    if common_typ != o['var']:
                        raise TypeMismatchInExpression(ast)
            elif o['var'] is not None and type(o['var']) == VoidType:
                raise TypeMismatchInExpression(ast)
        if common_typ is None:
            o['var'] = ArrayType([len(ast.value)],None)
        else:
            for e in ast.value:
                self.visit(e,o)
                if o['var'] is None:
                    o[e.name] = common_typ

            # TODO: Fix bugs when got access to multidimensional array

            o['var'] = ArrayType([len(ast.value)],common_typ)

                    
