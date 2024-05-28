from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC

from Utils import *
from Visitor import *
from AST import *


class MType(Type):
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, scope=0):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.scope = scope

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
    
# class ClassType(Type):
#     def __init__(self,cname):
#         self.cname = cname
#     def __str__(self):
#         return "Class({0})".format(str(self.cname))
#     def accept(self, v, param):
#         return None


def retrieveType(origin):
    return ArrayPointerType(origin.eleType) if type(origin) is ArrayType else origin

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readNumber", MType(list(), NumberType()), CName(self.libName),0),
                Symbol("writeNumber", MType([NumberType()],VoidType()), CName(self.libName),0),
                Symbol("readBool", MType(list(), BoolType()), CName(self.libName),0),
                Symbol("writeBool", MType([BoolType()],VoidType()), CName(self.libName),0),
                Symbol("readString", MType(list(), StringType()), CName(self.libName),0),
                Symbol("writeString", MType([StringType()],VoidType()), CName(self.libName),0)
                
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, [])


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = path
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def lookup(self, name, lst, func):
        for x in lst[::-1]:
            if name == func(x):
                return x
        return None

    def visitProgram(self, ast, ctxt):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        self.emit.printout("""
.method public static $concat2string(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V

    aload_0
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    aload_1
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
    areturn
                           
    .limit stack 3
    .limit locals 3
.end method
""")
        
        self.emit.printout("""
.method public static $compare2string(Ljava/lang/String;Ljava/lang/String;)Z
    aload_0
    aload_1

    invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
    ; Return the result
    ireturn
             
    .limit stack 2
    .limit locals 2
.end method
""")
        
        self.emit.printout("""
.method public static $modulo2float(FF)F
    fload_0
    fload_1

    fload_0
    fload_1
    fdiv         
    f2d          
    invokestatic java/lang/Math/floor(D)D
    d2f

    fload_1
    fmul

    fload_0
    fsub
    fneg

    freturn
    
    .limit stack 4
    .limit locals 3
.end method
""")
        e = SubBody(None, self.env)
        var_lst = []
        func_buf = ""
        for dclr in ast.decl:
            code, tmp = self.visit(dclr, e)
            # code, e = self.visit(x, e)
            # print("++++",type(ast.decl))
            if type(dclr) is VarDecl:
                # self.emit.printout(code)
                self.env.append(tmp)
                var_lst.append(dclr)
            else:
                # print('AAAA')
                if tmp is not None:
                    func_buf += code
                    e = tmp
                
        # generate default constructor
        buf, _ = self.genGLOBAL(FuncDecl(Id("<clinit>"), [], Block([var for var in var_lst])), ctxt, Frame("<clinit>",None))

        for dclr in var_lst:
            # sym = self.lookup(dclr.name.name, self.env, lambda x: x.name)
            # print("---",sym.mtype)
            code, tmp_typ = self.visit(dclr,e)
            self.emit.printout(code)

        self.emit.printout(buf)
        self.emit.printout(func_buf)

        init_buf, _ = self.genMETHOD(FuncDecl(Id("<init>"), [], Block([])), ctxt, Frame("<init>",None))
        self.emit.printout(init_buf)
        # print("+++++",self.emit.buff)
        self.emit.emitEPILOG()
        # return ctxt

    def genGLOBAL(self, dclr, o, frame):
        methodName = "<clinit>"
        intype = [retrieveType(x.varType) for x in dclr.param]
        mtype = MType(intype, VoidType())

        frame.enterScope(True)
        buf = ""
        buf += self.emit.emitMETHOD(methodName, mtype, False, frame) + self.emit.emitLABEL(frame.getStartLabel(), frame)
        # self.emit.printout(self.emit.emitMETHOD(methodName, mtype, False, frame))
        # self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        for var_dclr in dclr.body.stmt:
            # print("::::",dclr.body.stmt)
            exprCode, typ = self.visit(var_dclr.varInit,Access(frame,self.env,False,True))
            sym = self.lookup(var_dclr.name.name, self.env, lambda x: x.name)
            buf += exprCode + self.emit.emitPUTSTATIC(self.className + '/' + var_dclr.name.name, var_dclr.varType if var_dclr.varType is not None else typ, frame)
            # self.emit.printout(exprCode)
            # self.emit.printout(self.emit.emitPUTSTATIC(self.className + '/' + var_dclr.name.name, var_dclr.varType if var_dclr.varType is not None else typ, frame))
            sym.mtype = typ
            # sym.

        buf += self.emit.emitRETURN(None, frame) + self.emit.emitLABEL(frame.getEndLabel(), frame) + self.emit.emitENDMETHOD(frame)
        # self.emit.printout(self.emit.emitRETURN(None, frame))

        # self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        # self.emit.printout(self.emit.emitENDMETHOD(frame))

        frame.exitScope()

        return buf, VoidType()

    def genMETHOD(self, dclr, o, frame):
        isInit = (dclr.name.name == "<init>")
        isMain = (dclr.name.name == "main" and len(dclr.param) == 0)
        methodName = "<init>" if isInit else dclr.name.name
        intype = [ArrayType([0],StringType())] if isMain else [retrieveType(x.varType) for x in dclr.param]

        body = dclr.body
        # glenv = o
        # sym = o.sym

        frame.enterScope(True)

        local = SubBody(frame, [])
        param_code = ""

        for param in dclr.param:
            param, newsym = self.visit(param,local)
            local.sym += [newsym]
            param_code += param
        
        glenv = local.sym + o

        # frame.exitScope()

        # frame.enterScope(True)
        _, rettype = self.visit(body, SubBody(frame,glenv))
        sym = self.lookup(dclr.name.name, o, lambda x: x.name)
        if sym is not None:
            sym.mtype = MType(intype,rettype)
        # print("DDDD",rettype)
        # frame.exitScope()
        

        mtype = MType(intype, VoidType() if rettype is None else rettype)

        buf = ""
        buf += self.emit.emitMETHOD(methodName, mtype, not isInit, frame)
        # self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame)) 

        # frame.enterScope(True)
        buf += param_code
        # self.emit.printout(param_code)

        # Generate code for parameter declarations
        if isInit:
            buf += self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame)
            # self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            buf += self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame)
            # self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            
        buf += self.emit.emitLABEL(frame.getStartLabel(), frame)
        # self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            buf += self.emit.emitREADVAR("this", ClassType(self.className), 0, frame) + self.emit.emitINVOKESPECIAL(frame)
            # self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            # self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))
        blockcode, _ = self.visit(body, SubBody(frame,glenv))
        buf += blockcode
        # self.emit.printout(blockcode)

        if rettype is None or type(rettype) is VoidType:
            buf += self.emit.emitRETURN(None, frame)
            # self.emit.printout(self.emit.emitRETURN(None, frame))

        buf += self.emit.emitLABEL(frame.getEndLabel(), frame) + self.emit.emitENDMETHOD(frame)
        # self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        return buf, VoidType() if rettype is None else rettype

    def visitFuncDecl(self, ast, o):
        subctxt = o
        frame = Frame(ast.name,None)
        # print(subctxt.sym)
        if ast.body is not None:
            # print("====",ast.name.name,subctxt)
            buf, rettype = self.genMETHOD(ast, subctxt.sym, frame)
            sym = self.lookup(ast.name.name, self.env, lambda x: x.name)
            if sym is not None:
                sym.mtype = rettype
                return "",None
            else:
                return buf,SubBody(None, [Symbol(ast.name.name, MType([retrieveType(x.varType) for x in ast.param],rettype), CName(self.className),0)] + subctxt.sym)
        else:
            return "",SubBody(None, [Symbol(ast.name.name, MType([retrieveType(x.varType) for x in ast.param],None), CName(self.className),0)] + subctxt.sym)

    def visitVarDecl(self, ast, o):
        frame = o.frame
        env = o.sym
        if frame is None:
            sym = self.lookup(ast.name.name, self.env, lambda x: x.name)
            if sym is not None:
                code = self.emit.emitATTRIBUTE(ast.name.name,sym.mtype,False,None)
            else:
                code = self.emit.emitATTRIBUTE(ast.name.name,ast.varType,False,None)
            return code, Symbol(ast.name.name, ast.varType if ast.varType is not None else None, None,0)
            # if ast.varInit is not None:
            #     exprCode, typ = self.visit(ast.varInit,o)
            #     exprCode += self.emit.emitWRITEVAR(ast.name.name,typ,idx,frame)
        else:
            idx = frame.getNewIndex()
            # self.emit.printout(self.emit.emitVAR(idx, ast.name.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
            if type(ast.varType) is ArrayType:
                arr = self.visit(ast.varInit,o)
                typ = ""
                for i in ast.varType.size:
                    typ += "["
                typ += self.emit.getJVMType(ast.varType.eleType)
                code = self.emit.emitVAR(idx, ast.name.name, typ, frame.getStartLabel(), frame.getEndLabel(), frame)
                code += self.emit.emitARRAY(idx,ast.varType.size,ast.varType.eleType,arr,frame)
                exprCode = ""

            else:
                if ast.varInit is not None:
                    exprCode, typ = self.visit(ast.varInit,o)
                    exprCode += self.emit.emitWRITEVAR(ast.name.name,typ,idx,frame)
                else:
                    exprCode, typ = "", None
                code = self.emit.emitVAR(idx, ast.name.name, ast.varType if ast.varType is not None else typ, frame.getStartLabel(), frame.getEndLabel(), frame)

            return code + exprCode, Symbol(ast.name.name, ast.varType if ast.varType is not None else typ, Index(idx),0)

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # print("```````",ast.name)
        sym = self.lookup(ast.name.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        # print(ctype.rettype)

        in_ = ""
        for i,arg in enumerate(ast.args):
            _, parTyp = self.visit(arg, Access(frame, nenv, False, True))
            # in_ = (in_[0] + parCode, in_[1].append(parType))
            # print('####',in_, parType)
            # print("::::",parTyp,type(arg))
            if parTyp is None:
                if type(arg) is Id:
                    argsym = self.lookup(arg.name, nenv, lambda x: x.name)
                    argsym.mtype = ctype.partype[i]
                else:
                    argsym = self.lookup(arg.name.name, nenv, lambda x: x.name)
                    # print("0000",argsym.mtype.rettype)
                    argsym.mtype.rettype = ctype.partype[i]

        for arg in ast.args:
            parCode, _ = self.visit(arg, Access(frame, nenv, False, True))
            # in_ = (in_[0] + parCode, in_[1].append(parType))
            # print('####',in_, parType)
            # print(parCode)

            in_ = in_ + parCode

        # self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame))
        return in_ + self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame), VoidType()

    def visitArrayCell(self,ast,o):
        frame = o.frame
        nenv = o.sym
        sym = self.lookup(ast.arr.name, nenv, lambda x: x.name)
        res = ""
        res += self.emit.emitREADVAR(ast.arr.name,sym.mtype,sym.value.value,o.frame)
        exprCode, _ = self.visit(ast.idx[0], Access(frame,nenv,False,True))
        res += exprCode + self.emit.emitF2I(frame)
        res += self.emit.emitALOAD(sym.mtype.eleType,frame)

        return res, sym.mtype.eleType

    def visitId(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)

        if sym is not None:
            if type(sym.value) is Index:
                if ctxt.isLeft == True:
                    if ctxt.isFirst == True:
                        return (self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                    else:
                        return ast.name, sym.mtype
                else:
                    if ctxt.isFirst == True:
                        if type(sym.value) is Index:
                            # print("BBBBB",sym.name)
                            # print(self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame))
                            return (self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, frame), sym.mtype)
                    else:
                        return ast.name, sym.mtype
            else:
                return (self.emit.emitGETSTATIC(self.className + "/" + ast.name,sym.mtype,frame), sym.mtype)
                # return ast.name, sym.mtype
        # sym = self.lookup(ast.name, self.env, lambda x: x.cname)

    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        # print("****",sym)

        in_ = ""
        for i,arg in enumerate(ast.args):
            _, parTyp = self.visit(arg, Access(frame, nenv, False, True))
            # in_ = (in_[0] + parCode, in_[1].append(parType))
            # print('####',in_, parType)
            if parTyp is None:
                if type(arg) is Id:
                    argsym = self.lookup(arg.name, nenv, lambda x: x.name)
                    argsym.mtype = ctype.partype[i]
                else:
                    # print("0000",argsym)
                    argsym = self.lookup(arg.name.name, nenv, lambda x: x.name)
                    argsym.mtype.rettype = ctype.partype[i]
            # in_ = in_ + parCode

        for i,arg in enumerate(ast.args):
            # print('////',in_[1])
            parCode, _ = self.visit(arg, Access(frame, nenv, False, True))
            # in_ = (in_[0] + parCode, in_[1].append(parType))
            # print('####',in_, parType)
            in_ = in_ + parCode

        # self.emit.printout(in_[0])
        # self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame))
        # print("[[[[]]]]",frame.currOpStackSize)
        frame.push()
        return in_ + self.emit.emitINVOKESTATIC(cname + "/" + ast.name.name, ctype, frame), ctype.rettype

    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.value), BoolType(), o.frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str("\"" + ast.value + "\""), StringType(), o.frame), StringType()

    def visitArrayLiteral(self,ast,o):
        expr_list = []
        for expr in ast.value:
            if type(expr) is ArrayLiteral:
                expr_list.append(self.visit(expr,o))
            else:
                code, _ = self.visit(expr,Access(o.frame,o.sym,False,True))
                expr_list.append(code)
        return expr_list


    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = o.sym
        op = ast.op

        if op == '+' or op == '-':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitADDOP(op, NumberType(), frame)
            rettype = NumberType()

        elif op == '*' or op == '/':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitMULOP(op, NumberType(), frame)
            rettype = NumberType()

        elif op == '%':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitINVOKESTATIC(self.className + "/$modulo2float", MType([NumberType(),NumberType()],NumberType()), frame)
            rettype = NumberType()

        elif op == 'and':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitANDOP(frame)
            rettype = BoolType()

        elif op == 'or':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitOROP(frame)
            rettype = BoolType()

        elif op == '...':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitINVOKESTATIC(self.className + "/$concat2string", MType([StringType(),StringType()],StringType()), frame)
            rettype = StringType()

        elif op in ['=','>','<','>=','<=','!=']:
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitFREOP(op, BoolType(), frame)
            rettype = BoolType()

        elif op == '==':
            lcode, _ = self.visit(ast.left, Access(frame,sym,False,True))
            rcode, _ = self.visit(ast.right, Access(frame,sym,False,True))
            rescode = self.emit.emitINVOKESTATIC(self.className + "/$compare2string", MType([StringType(),StringType()],BoolType()), frame)
            rettype = BoolType()

        return lcode + rcode + rescode, rettype
    

    def visitUnaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = o.sym
        op = ast.op

        if op == '-':
            code, _ = self.visit(ast.operand, Access(frame,sym,False,True))
            rescode = self.emit.emitNEGOP(NumberType(), frame)
            rettype = NumberType()

        elif op == 'not':
            code, _ = self.visit(ast.operand, Access(frame,sym,False,True))
            rescode = self.emit.emitNEGOP(BoolType(), frame)
            rettype = BoolType()

        return code + rescode, rettype

    def visitBlock(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        syms = ctxt.sym
        blockcode = ""
        rettype = None

        local = []
        local = local + syms

        for sym in local:
            sym.scope += 1

        for stmt in ast.stmt:
            if type(stmt) is not VarDecl:
                code, rettype = self.visit(stmt,SubBody(frame,local))
                blockcode += code
            else:
                code, newsym = self.visit(stmt,SubBody(frame,local))
                local += [newsym]
                if stmt.modifier != "dynamic":
                    blockcode += code

        return blockcode, rettype

    def visitReturn(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        sym = ctxt.sym

        if ast.expr is None:
            # self.emit.printout(self.emit.emitRETURN(rettype,frame))
            rettype = VoidType()
            code = self.emit.emitRETURN(rettype,frame)
            
        else:
            code, rettype = self.visit(ast.expr, Access(frame,sym,False,True))
            # self.emit.printout(code)
            # self.emit.printout(self.emit.emitRETURN(rettype,frame))
            # print("///",code)
            code += self.emit.emitRETURN(rettype,frame)
        return code, rettype

    def visitIf(self,ctx,o):
        frame = o.frame
        sym = o.sym
        new_label = frame.getNewLabel()
        end_label = frame.getNewLabel()
        
        cond, _ = self.visit(ctx.expr,Access(frame,sym,False))
        # print(cond)
        jfalse = self.emit.emitIFFALSE(new_label,frame)
        
        # self.emit.printout(cond + jfalse)
        
        thenStmt, then_ret = self.visit(ctx.thenStmt,o)
        j = self.emit.emitGOTO(end_label,frame)
        flabel = self.emit.emitLABEL(new_label,frame)
        
        # self.emit.printout(j + flabel)

        elifstmts = ""

        for (expr, stmt) in ctx.elifStmt:
            elif_label = frame.getNewLabel()
            elif_cond, _ = self.visit(expr,Access(frame,sym,False))
            elifstmts += elif_cond + self.emit.emitIFFALSE(elif_label,frame)

            elifStmt, elif_ret = self.visit(stmt,o)
            elifstmts += elifStmt
            elifstmts += self.emit.emitGOTO(end_label,frame)
            elifstmts += self.emit.emitLABEL(elif_label,frame)

        if ctx.elseStmt is None:
            elseStmt, then_ret = "", None
        else:
            elseStmt, then_ret = self.visit(ctx.elseStmt,o)
        end = self.emit.emitLABEL(end_label,frame)
        
        # self.emit.printout(end)
        return cond + jfalse + thenStmt + j + flabel + elifstmts + elseStmt + end, then_ret
    
    def visitFor(self,ctx,o):
        frame = o.frame
        sym = o.sym
        
        frame.enterLoop()
        
        new_label = frame.getContinueLabel()
        start_label = frame.getNewLabel()
        end_label = frame.getBreakLabel()
        
        # ini, _ = self.visit(ctx.ini,Access(frame,sym,False))
        # count_sym = self.lookup(ctx.name.name, self.env, lambda x: x.name)
        ridx, _ = self.visit(ctx.name,Access(frame,sym,False,True))
        
        # self.emit.emitREADVAR(sym.value.value,sym.mtype,)
        # self.emit.printout(ini + lidx)
        
        slabel = self.emit.emitLABEL(start_label,frame)
        
        # ridx, _ = self.visit(ctx.idx,Access(frame,sym,False))
        cond, _ = self.visit(ctx.condExpr,Access(frame,sym,False,True))
        
        
        jfalse = self.emit.emitIFFALSE(end_label,frame)
        
        # self.emit.printout(ridx + slabel + cond + jfalse)
        
        stmt, rettype = self.visit(ctx.body,o)
        
        c_label = self.emit.emitLABEL(new_label, frame)

        # ridx, _ = self.visit(ctx.idx,Access(frame,sym,False))
        upd, typ = self.visit(ctx.updExpr,Access(frame,sym,False,True))
        
        lidx, _ = self.visit(ctx.name,Access(frame,sym,False,True))
        add_upd = self.emit.emitADDOP("+",typ,frame)
        lidx_upd, _ = self.visit(ctx.name,Access(frame,sym,True,True))

        # self.emit.printout(c_label + upd + add_upd + lidx)

        j = self.emit.emitGOTO(start_label,frame)
        end = self.emit.emitLABEL(end_label,frame)
        
        # self.emit.printout(j + end)
        
        frame.exitLoop()

        return ridx + slabel + cond + jfalse + stmt + c_label + upd + lidx + add_upd + lidx_upd + j + end, rettype
    
    def visitAssign(self,ast,o):
        frame = o.frame
        syms = o.sym
        
        right, rtype = self.visit(ast.rhs, Access(frame,syms,False,True))

        lsym = self.lookup(ast.lhs.name, syms, lambda x: x.name)
        if lsym.mtype is None:
            lsym.mtype = rtype
            lcode, _ = self.visit(VarDecl(ast.lhs,rtype,None,None),o)
        else:
            lcode = ""

        left, ltype = self.visit(ast.lhs, Access(frame,syms,True,True))     
        
        return right + lcode + left, None

        # self.emit.printout(right + left)

    