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
    def __init__(self, name, typ, scope, value):
        super().__init__(name, typ, scope)
        self.value = value

    def copy(self,enterScope):
        return VarSym(self.name, self.typ, self.scope + 1 if enterScope else self.scope, self.value)

class ArraySym(Symbol):
    def __init__(self, name, typ, scope, size, value):
        super().__init__(name,typ, scope)
        self.size = size
        self.value = value

    def copy(self,enterScope):
        return ArraySym(self.name, self.typ, self.scope + 1 if enterScope else self.scope, self.size, [val for val in self.value] if self.value is not None else None)

class FuncSym(Symbol):
    def __init__(self, name, typ, scope, param_typ, param_arr_typ, has_body, ret_array):
        super().__init__(name, typ, scope)
        self.param_typ = param_typ
        self.param_arr_typ = param_arr_typ
        self.has_body = has_body
        self.ret_array = ret_array

    def copy(self,enterScope):
        return FuncSym(self.name, self.typ, self.scope + 1 if enterScope else self.scope, [param for param in self.param_typ], [param for param in self.param_arr_typ], self.has_body, self.ret_array)

class StaticChecker(BaseVisitor, Utils):

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        o = {}
        env = [
            FuncSym("writeString",VoidType,0,[StringType],[[StringType,[]]],True,None),
            FuncSym("writeNumber",VoidType,0,[NumberType],[[NumberType,[]]],True,None),
            FuncSym("writeBool",VoidType,0,[BoolType],[[BoolType,[]]],True,None),
            FuncSym("readString",StringType,0,[],[],True,None),
            FuncSym("readNumber",NumberType,0,[],[],True,None),
            FuncSym("readBool",BoolType,0,[],[],True,None),
        ]
        o['symbols'] = env
        o['for'] = False
        o['return'] = None
        o['var'] = None
        o['array'] = [None,[]]
        o['return_array'] = [None,[]]
        # o['return_dynamic'] = False
        o['dynamic'] = []
        o['array_typ'] = None
        self.visit(self.ast, o)

    def enterScope(self,o):
        new_o = {}
        new_o['symbols'] = []
        for sym in o['symbols']:
            new_o['symbols'].append(sym.copy(True))
        new_o['for'] = o['for']
        new_o['return'] = o['return']
        new_o['var'] = o['var']
        new_o['array'] = o['array']
        new_o['return_array'] = o['return_array']
        # new_o['return_dynamic'] = o['return_dynamic']
        new_o['dynamic'] = o['dynamic']
        return new_o

    def lookup(self,name,symtyp,o):
        lst = []
        for sym in o['symbols']:
            if name is None:
                match_name = True
            else:
                match_name = (sym.name == name)
            if len(symtyp) == 0:
                match_typ = True
            else:
                match_typ = (type(sym) in symtyp)
            if match_name and match_typ:
                lst.append(sym)
        return lst

    def hasDeclared(self,name,symtyp,o):
        for sym in o['symbols']:
            if name is None:
                match_name = True
            else:
                match_name = (sym.name == name)
            if len(symtyp) == 0:
                match_typ = True
            else:
                match_typ = (type(sym) in symtyp)
            if match_name and match_typ:
                return sym
        return None

    def infer(self,name,symtyp,typ,o):
        if name is None:
            return True
        if type(name) == Id:
            name = name.name
        sym = self.hasDeclared(name,[symtyp],o)
        if sym.typ == typ:
            return True
        if symtyp == VarSym or symtyp == FuncSym or symtyp == ArraySym:
            if sym.typ is None:
                sym.typ = typ
                return True
            elif sym.typ is not None and sym.typ != typ:
                return False
        else:
            return False


    # def copyType(self,name,base_typ,o):
    #     if base_typ is None:
    #         return None
    #     for typ_obj in [NumberType(),BoolType(),StringType()]:
    #         if base_typ == type(typ_obj):
    #             o[name][0] = typ_obj
    #             return type(typ_obj)
    #     return None
    
    # def copyTypeNoId(self,base_typ):
    #     if base_typ is None:
    #         return None
    #     for typ_obj in [NumberType(),BoolType(),StringType()]:
    #         if base_typ == type(typ_obj):
    #             return typ_obj
    #     return None

    # def filterScope(self,func,scope,o):
    #     def scope_func(pair):
    #         _, value = pair
    #         if func(value[1], scope):
    #             return True
    #         else:
    #             return False
    #     return dict(filter(scope_func, o.items()))

    def visitProgram(self, ast, o):
        for dclr in ast.decl:
            self.visit(dclr,o)
        lst = self.lookup('main',[FuncSym],o)
        if len(lst) == 0:
            raise NoEntryPoint()
        lst = self.lookup(None,[FuncSym],o)
        for func in lst:
            if not func.has_body:
                raise NoDefinition(func.name)
        # if len(o['func']) > 0:
        #     raise NoDefinition(o['func'][0])
        # for name in o:
        #     if name == 'main' and type(o['main'][0]) == list:
        #         return
        # raise NoEntryPoint()

    def visitVarDecl(self, ast, o):
        o['dynamic'] = []
        name = ast.name.name
        sym = self.hasDeclared(name,[VarSym,ArraySym],o)
        if sym is not None and sym.scope == 0:
            raise Redeclared(Variable(),name)
        else:
            if ast.varInit is not None:
                self.visit(ast.varInit,o)
                if ast.varType is not None:
                    if o['var'] is None:
                        raise TypeCannotBeInferred(ast)
                    if o['var'] != type(ast.varType):
                        # print("==",o['var'],type(ast.varType))
                        if len(o['dynamic']) > 0:
                            raise TypeCannotBeInferred(ast)
                        raise TypeMismatchInStatement(ast)
                    else:
                        # o[name] = [ast.varType,0]
                        print("###",name,o)
                        if o['var'] == ArrayType:
                            arr_info = o['array']
                            if arr_info[0] is None:
                                ## TODO: Infer all types
                                for name in o['dynamic']:
                                    unknown_syms = self.lookup(name,[VarSym,FuncSym],o)
                                    for unk_sym in unknown_syms:
                                        unk_sym.typ = type(ast.varType.eleType)
                                        o['dynamic'].remove(name)
                                
                            else:
                                if len(o['dynamic']) > 0:
                                    raise TypeCannotBeInferred(ast)
                                # if arr_info[0] == type(ast.varType):
                                #     pass
                            if arr_info[0] is not None and (arr_info[0] != type(ast.varType.eleType) or arr_info[1] != ast.varType.size):
                                raise TypeMismatchInStatement(ast)
                            else:
                                o['symbols'].append(ArraySym(name,type(ast.varType.eleType),0,ast.varType.size,None))
                        else:
                            o['symbols'].append(VarSym(name,type(ast.varType),0,None))
                else:
                    o['symbols'].append(VarSym(name,o['var'],0,None))
                    # o[name] = [o['var'],0]
            else:
                if ast.varType is not None:
                    o['symbols'].append(VarSym(name,type(ast.varType),0,None))
                    # o[name] = [ast.varType,0]
                else:
                    o['symbols'].append(VarSym(name,None,0,None))
                    # o[name] = [None,0]
            if sym is not None and sym.scope > 0:
                o['symbols'].remove(sym)
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)
        # print(name,"==",o)


    def visitFuncDecl(self, ast, o):
        # Gia su khai bao bien cung ten tham so trong than ham la hop le
        o['return'] = None
        func_name = ast.name.name
        func_sym = self.hasDeclared(func_name,[FuncSym],o)
        if func_sym is not None and func_sym.has_body:
            raise Redeclared(Function(),func_name)
        new_o = self.enterScope(o)
        param_typ = []
        param_arr_typ = []
        param_obj = []
        for dclr in ast.param:
            name = dclr.name.name
            sym = self.hasDeclared(name,[VarSym,ArraySym],new_o)
            if sym is not None and sym.scope == 0:
                raise Redeclared(Parameter(),name)
            else:
                ## TODO
                if type(dclr.varType) == ArrayType:
                    new_o['symbols'].append(ArraySym(name,type(dclr.varType.eleType),0,dclr.varType.size,None))
                    param_arr_typ.append([type(dclr.varType.eleType),dclr.varType.size])
                else:
                    new_o['symbols'].append(VarSym(name,type(dclr.varType),0,None))
                    param_arr_typ.append([type(dclr.varType),[]])
                param_typ.append(type(dclr.varType))
                param_obj.append(dclr.varType)
        if func_sym is not None and not func_sym.has_body:
            if len(param_typ) != len(func_sym.param_typ):
                raise Redeclared(Function(),func_name)
            for i,param in enumerate(param_typ):
                self.visit(ast.param[i],o)
                if o['var'] == ArrayType:
                    arr_info = o['array']
                    if param_obj[i].eleType != param or param_obj[i].size != arr_info[1]:
                        raise Redeclared(Function(),func_name)
                else:
                    if param != func_sym.param_typ[i]:
                        raise Redeclared(Function(),func_name)

        new_o['return'] = None
        if ast.body is not None:
            self.visit(ast.body,new_o)

        if ast.body is None:
            ret_typ = None
        elif new_o['return'] is None:
            ret_typ = VoidType
        else:
            ret_typ = new_o['return']

        if func_sym is not None:
            func_sym.has_body = True
            func_sym.typ = ret_typ
        else:
            if new_o['return'] == ArrayType:
                arr_info = new_o['return_array']
                o['symbols'].append(FuncSym(func_name,ret_typ,0,param_typ,param_arr_typ,ast.body is not None,ArraySym("",arr_info[0],0,arr_info[1],None)))
            else:
                o['symbols'].append(FuncSym(func_name,ret_typ,0,param_typ,param_arr_typ,ast.body is not None,None))

        # o['return'] = None
        # func_name = ast.name.name
        # if func_name in o:
        #     raise Redeclared(Function(),func_name)
        
        # if ast.body is None:
        #     o['func'].append(func_name)
        # else:
        #     if func_name in o['func']:
        #         o['func'].remove(func_name)
        
        # o[func_name] = [[],0]
        # # print("---",o)
        # new_o = self.enterScope(o)
        # for dclr in ast.param:
        #     name = dclr.name.name
        #     if name in new_o and new_o[name][1] == 0:
        #         raise Redeclared(Parameter(),name)
        #     else:
        #         new_o[name] = [dclr.varType,0]
        #         o[func_name][0].append(dclr.varType)
        
        # if ast.body is not None:
        #     self.visit(ast.body,new_o)
        #     # print("@@@",func_name,new_o['return'])
        #     o['return'] = self.copyTypeNoId(type(new_o['return']))
        #     o[func_name][0].append(new_o['return'])
        # else:
        #     o[func_name][0].append(None)
        
        

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
        ltype = o['var']
        if type(ast.left) == ArrayCell:
            if type(ast.left.arr) == Id:
                lname = ast.left.arr.name
            else:
                lname = ast.left.arr.name.name
        elif type(ast.left) in [NumberLiteral,StringLiteral,BooleanLiteral,ArrayLiteral]:
            lname = None
        else:
            if type(ast.left) == Id:
                lfindtyp = VarSym
                lname = ast.left.name
            elif type(ast.left) == CallExpr:
                lfindtyp = FuncSym
                lname = ast.left.name
            # lname = ast.left.name

        self.visit(ast.right,o)
        rtype = o['var']
        if type(ast.right) == ArrayCell:
            if type(ast.right.arr) == Id:
                rname = ast.right.arr.name
            else:
                rname = ast.right.arr.name.name
        elif type(ast.right) in [NumberLiteral,StringLiteral,BooleanLiteral,ArrayLiteral]:
            rname = None
        else:
            if type(ast.right) == Id:
                rfindtyp = VarSym
                rname = ast.right.name
            elif type(ast.right) == CallExpr:
                rfindtyp = FuncSym
                rname = ast.right.name
            # rname = ast.right.name

        if ast.op in ['+','-','*','/','%']:
            if ltype is None:
                self.infer(lname,lfindtyp,NumberType,o)
                ltype = NumberType
                # ltype = self.copyType(lname,NumberType,o)
                if lname in o['dynamic']:
                    o['dynamic'].remove(lname)
            if rtype is None:
                self.infer(rname,rfindtyp,NumberType,o)
                rtype = NumberType
                # rtype = self.copyType(rname,NumberType,o)
                if rname in o['dynamic']:
                    o['dynamic'].remove(rname)
            is_valid = (ltype == NumberType and rtype == NumberType)
            ret_type = NumberType
            # print("+++",o)
        elif ast.op in ['and','or']:
            if ltype is None:
                self.infer(lname,lfindtyp,BoolType,o)
                ltype = BoolType
                # ltype = self.copyType(lname,BoolType,o)
                if lname in o['dynamic']:
                    o['dynamic'].remove(lname)
            if rtype is None:
                self.infer(rname,rfindtyp,BoolType,o)
                rtype = BoolType
                # rtype = self.copyType(rname,BoolType,o)
                if rname in o['dynamic']:
                    o['dynamic'].remove(rname)

            is_valid = (ltype == BoolType and rtype == BoolType)
            ret_type = BoolType
        elif ast.op in ['...']:
            if ltype is None:
                self.infer(lname,lfindtyp,StringType,o)
                ltype = StringType
                # ltype = self.copyType(lname,StringType,o)
                if lname in o['dynamic']:
                    o['dynamic'].remove(lname)
            if rtype is None:
                self.infer(rname,rfindtyp,StringType,o)
                rtype = StringType
                # rtype = self.copyType(rname,StringType,o)
                if rname in o['dynamic']:
                    o['dynamic'].remove(rname)

            is_valid = (ltype == StringType and rtype == StringType)
            ret_type = StringType
        elif ast.op in ['=','!=','>','<','>=','<=']:
            if ltype is None:
                self.infer(lname,lfindtyp,NumberType,o)
                ltype = NumberType
                # ltype = self.copyType(lname,NumberType,o)
                if lname in o['dynamic']:
                    o['dynamic'].remove(lname)
            if rtype is None:
                self.infer(rname,rfindtyp,NumberType,o)
                rtype = NumberType
                # rtype = self.copyType(rname,NumberType,o)
                if rname in o['dynamic']:
                    o['dynamic'].remove(rname)

            is_valid = (ltype == NumberType and rtype == NumberType)
            ret_type = BoolType
        elif ast.op in ['==']:
            if ltype is None:
                self.infer(lname,lfindtyp,StringType,o)
                ltype = StringType
                # ltype = self.copyType(lname,StringType,o)
                if lname in o['dynamic']:
                    o['dynamic'].remove(lname)
            if rtype is None:
                self.infer(lname,rfindtyp,StringType,o)
                rtype = StringType
                # rtype = self.copyType(rname,StringType,o)
                if rname in o['dynamic']:
                    o['dynamic'].remove(rname)

            is_valid = (ltype == StringType and rtype == StringType)
            ret_type = BoolType

        if is_valid:
            o['var'] = ret_type
        else:

            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, o):
        self.visit(ast.operand,o)
        opr_type = o['var']
        if type(ast.operand) == ArrayCell:
            name = ast.operand.arr.name.name
        elif type(ast.operand) in [NumberLiteral,StringLiteral,BooleanLiteral,ArrayLiteral]:
            name = None
        else:
            if type(ast.operand) == Id:
                findtyp = VarSym
                name = ast.operand.name
            elif type(ast.right) == CallExpr:
                findtyp = FuncSym
                name = ast.operand.name
            

        if ast.op in ['-']:
            if opr_type is None:
                self.infer(name,findtyp,NumberType,o)
                opr_type = NumberType
                # opr_type = self.copyType(ast.operand.name,NumberType,o)
                if name in o['dynamic']:
                    o['dynamic'].remove(name)
            is_valid = (opr_type == NumberType)
            ret_type = NumberType
        elif ast.op in ['not']:
            if opr_type is None:
                self.infer(name,findtyp,BoolType,o)
                opr_type = BoolType
                # opr_type = self.copyType(ast.operand.name,BoolType,o)
                if name in o['dynamic']:
                    o['dynamic'].remove(name)
            is_valid = (opr_type == BoolType)
            ret_type = BoolType
        
        if is_valid:
            o['var'] = ret_type
        else:
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, o):
        # print("===",o)
        name = ast.name.name
        sym = self.hasDeclared(name,[FuncSym],o)
        if sym is None:
            raise Undeclared(Function(),name)
        else:
            # print("[[[]]]",sym.typ,sym.name)
            if len(ast.args) != len(sym.param_typ) or sym.typ == VoidType:
                raise TypeMismatchInExpression(ast)
            else:
                # idx = 0
                for idx,arg in enumerate(ast.args):
                    self.visit(arg,o)
                    # print(type(arg),":", o['var'])
                    # print("++++",o['var'])
                    if o['var'] is None:
                        o['dynamic'].append(arg.name)
                        continue
                    if o['var'] == ArrayType:
                        arr_info = o['array']
                        if arr_info[0] != sym.param_arr_typ[idx][0] or arr_info[1] != sym.param_arr_typ[idx][1]:
                            raise TypeMismatchInExpression(ast)
                    elif o['var'] != sym.param_typ[idx]:
                        raise TypeMismatchInExpression(ast)

                o['var'] = sym.typ
        # print("===",o)


    def visitId(self, ast, o):
        sym = self.hasDeclared(ast.name,[VarSym,ArraySym],o)
        if sym is None:
            raise Undeclared(Identifier(),ast.name)
        else:
            if type(sym) == VarSym:
                o['var'] = sym.typ
            else:
                o['var'] = ArrayType
                o['array'] = [sym.typ,sym.size]

    def visitArrayCell(self, ast, o):
        self.visit(ast.arr,o)
        arr_type = o['var']
        if arr_type is None or arr_type != ArrayType:
            # print("X")
            raise TypeMismatchInExpression(ast)
        else:
            arr_info = o['array']
            if type(ast.arr) == Id:
                sym = self.hasDeclared(ast.arr.name,[ArraySym],o)
                # print("///",sym.typ)
                ret_typ = sym.typ
            else:
                sym = self.hasDeclared(ast.arr.name.name,[FuncSym],o)
                ret_typ = sym.ret_array.typ

            for idx in ast.idx:
                self.visit(idx,o)
                if o['var'] != NumberType:
                    # print("ABC")
                    raise TypeMismatchInExpression(ast)
            if len(arr_info[1]) > len(ast.idx):
                o['var'] = ArrayType
                o['array'] = [o['array'][0],o['array'][1][len(ast.idx)-len(arr_info[1]):]]
            else:
                o['var'] = ret_typ
                o['array'] = [None,[]]
            print("---",sym.name,o['var'],ret_typ)
            

    def visitBlock(self, ast, o):
        new_o = self.enterScope(o)
        for stmt in ast.stmt:
            self.visit(stmt,new_o)
        # for typ_obj in [NumberType(),BoolType(),StringType()]:
        #     if type(new_o['return']) == type(typ_obj):
        #         o['return'] = typ_obj
        #         break
        o['return'] = new_o['return']
        o['array'] = new_o['array']
        o['return_array'] = new_o['return_array']
        # o['return_dynamic'] = new_o['return_dynamic']
        # print("!!!",self.hasDeclared("x",[ArraySym],new_o).size)

    def visitIf(self, ast, o):
        o['dynamic'] = []
        self.visit(ast.expr,o)
        if o['var'] is None:
            if type(ast.expr) == Id or type(ast.expr) == CallExpr:
                self.infer(ast.expr.name,VarSym,BoolType,o)

        if o['var'] != BoolType:
            raise TypeMismatchInStatement(ast)
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast) 
        self.visit(ast.thenStmt,o)
        for stmt in ast.elifStmt:
            self.visit(stmt,o)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt,o)
        

    def visitFor(self, ast, o):
        o['dynamic'] = []
        self.visit(ast.name,o)
        if not self.infer(ast.name,VarSym,NumberType,o):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.condExpr,o)
        if type(ast.condExpr) == Id:
            if not self.infer(ast.condExpr.name,VarSym,BoolType,o):
                raise TypeMismatchInStatement(ast)
        elif type(ast.condExpr) == CallExpr:
            if not self.infer(ast.condExpr.name.name,FuncSym,BoolType,o):
                raise TypeMismatchInStatement(ast)
        self.visit(ast.updExpr,o)
        if type(ast.condExpr) == Id:
            if not self.infer(ast.updExpr.name,VarSym,NumberType,o):
                raise TypeMismatchInStatement(ast)
        elif type(ast.condExpr) == CallExpr:
            if not self.infer(ast.updExpr.name,FuncSym,NumberType,o):
                raise TypeMismatchInStatement(ast)
        outer_for = o['for']
        o['for'] = True
        self.visit(ast.body,o)
        o['for'] = outer_for
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)

    def visitContinue(self, ast, o):
        if not o['for']:
            raise MustInLoop(ast)
        

    def visitBreak(self, ast, o):
        if not o['for']:
            raise MustInLoop(ast)

    def visitReturn(self, ast, o):
        o['dynamic'] = []
        # o['return_dynamic'] = False
        if ast.expr is not None:
            self.visit(ast.expr,o)
            # print("return",o['var'],o['return'],o['return_dynamic'])
            if o['var'] is None:
                raise TypeCannotBeInferred(ast)
            else:
                if o['return'] is not None and o['var'] != o['return']:
                    raise TypeMismatchInStatement(ast)
                o['return'] = o['var']
                if o['var'] == ArrayType:
                    o['return_array'] = o['array']
                # if o['var'] == ArrayType:
                #     print("////",o['array'])
                # print("::::",o['var'],o['return'])
        else:
            o['return'] = VoidType
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)

    def visitAssign(self, ast, o):
        o['dynamic'] = []
        self.visit(ast.rhs,o)
        rtype = o['var']
        # if type(ast.rhs) == ArrayLiteral:
        #     rarr_info = o['array']
        if rtype == ArrayType:
            rarr_info = o['array']
        self.visit(ast.lhs,o)
        ltype = o['var']
        # if type(ast.lhs) == ArrayCell:
        #     larr_info = o['array']
        if type(ast.lhs) == ArrayCell:
            # print("BBBB")
            larr_info = o['array']
            ltype = ArrayType if larr_info[0] is not None else ltype
        if type(ast.lhs) == Id and ltype is None:
            # ltype = self.copyType(ast.lhs.name,rtype,o)
            self.infer(ast.lhs.name,VarSym,rtype,o)
        else:
            if rtype is None:
                if type(ast.rhs) == Id:
                    self.infer(ast.rhs.name,VarSym,ltype,o)
                    rtype = ltype
                elif type(ast.rhs) == CallExpr:
                    # print(",,,,",type(ast.rhs.name))
                    self.infer(ast.rhs.name,FuncSym,ltype,o)
                    rtype = ltype
            # print("===",ltype,rtype,larr_info,rarr_info)
            if ltype == ArrayType and rtype == ArrayType and larr_info[1] != rarr_info[1] or ltype != rtype:
                raise TypeMismatchInStatement(ast)
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)


    def visitCallStmt(self, ast, o):
        o['dynamic'] = []
        name = ast.name.name
        sym = self.hasDeclared(name,[FuncSym],o)
        if sym is None:
            raise Undeclared(Function(),name)
        else:
            if sym.typ is None:
                sym.typ = VoidType
            if len(ast.args) != len(sym.param_typ) or sym.typ is not None and sym.typ != VoidType:
                raise TypeMismatchInStatement(ast)
            else:
                # idx = 0
                for idx,arg in enumerate(ast.args):
                    self.visit(arg,o)
                    if o['var'] is None:
                        o['dynamic'].append(arg.name)
                        continue
                    if o['var'] != sym.param_typ[idx]:
                        raise TypeMismatchInStatement(ast)

                o['var'] = sym.typ
        if len(o['dynamic']) > 0:
            raise TypeCannotBeInferred(ast)
        
        # o['dynamic'] = []
        # name = ast.name.name
        # if name not in o:
        #     raise Undeclared(Function(),name)
        # else:
        #     if len(ast.args) != len(o[name][0]) - 1 or o[name][0][-1] is None or o[name][0][-1] != VoidType():
        #         raise TypeMismatchInStatement(ast)
        #     else:
        #         idx = 0
        #         for arg in ast.args:
        #             self.visit(arg,o)
        #             if o['var'] is None:
        #                 raise TypeCannotBeInferred(ast)
        #             if type(o['var']) != type(o[name][0][idx]):
        #                 raise TypeMismatchInStatement(ast)
        #             idx += 1
        # if len(o['dynamic']) > 0:
        #     raise TypeCannotBeInferred(ast)

    def visitNumberLiteral(self, ast, o):
        o['var'] = NumberType

    def visitBooleanLiteral(self, ast, o):
        o['var'] = BoolType

    def visitStringLiteral(self, ast, o):
        o['var'] = StringType

    def visitArrayLiteral(self, ast, o):
        common_typ = None
        arr_size = [float(len(ast.value))]
        for e in ast.value:
            tail = self.visit(e,o)
            if o['var'] is not None and o['var'] != VoidType:
                if common_typ is None:
                    common_typ = o['var']
                else:
                    # print("///",common_typ,o['var'])
                    if common_typ != o['var']:
                        raise TypeMismatchInExpression(ast)
            elif o['var'] is not None and o['var'] == VoidType:
                raise TypeMismatchInExpression(ast)
        if common_typ is not None:
            for e in ast.value:
                self.visit(e,o)
                if o['var'] is None:
                    sym = self.hasDeclared(e.name,[VarSym if type(e) == Id else FuncSym],o)
                    sym.typ = common_typ
        o['var'] = ArrayType
        if tail is not None:
            o['array'] = [(common_typ if common_typ != ArrayType else o['array'][0]),arr_size + tail]
            # print(o['array'])
            return arr_size + tail
        else:
            o['array'] = [common_typ,arr_size]
            # print(o['array'])
            return arr_size
        # common_typ = None
        # for e in ast.value:
        #     self.visit(e,o)
        #     if o['var'] is not None and type(o['var']) != VoidType:
        #         if common_typ is None:
        #             common_typ = o['var']
        #         else:
        #             if common_typ != o['var']:
        #                 raise TypeMismatchInExpression(ast)
        #     elif o['var'] is not None and type(o['var']) == VoidType:
        #         raise TypeMismatchInExpression(ast)
        # if common_typ is None:
        #     o['var'] = ArrayType([len(ast.value)],None)
        # else:
        #     for e in ast.value:
        #         self.visit(e,o)
        #         if o['var'] is None:
        #             o[e.name] = common_typ


        #     o['var'] = ArrayType([len(ast.value)],common_typ)

                    
