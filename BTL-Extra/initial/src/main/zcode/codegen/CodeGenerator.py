'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

def retrieveType(origin):
    return ArrayPointerType(origin.eleType) if type(origin) is ArrayType else origin

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return  [
            Symbol("getInt", MType([],NumberType()), CName(self.libName)),
            Symbol("putInt", MType([NumberType()],None), CName(self.libName)),
            Symbol("putIntLn", MType([NumberType()],None), CName(self.libName))            
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
    
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".asm")
        

    def visitProgram(self, ast: Program, o):
        #ast: Program
        #c: Any
        # print("########")
        # self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # e = SubBody(None, self.env)
        # for x in ast.decl:
        #     e = self.visit(x, e)
        # # generate default constructor
        # # self.genMETHOD(FuncDecl("<init>", [], Block([])), ctxt, Frame("<init>"))
        # self.emit.emitEPILOG()
        # return ctxt

        self.emit.printout(self.emit.emitTEXT())
        o = {}
        for dclr in ast.decl:
            self.visit(dclr, o)
        self.emit.emitEPILOG()

    # def genMETHOD(self, dclr: FuncDecl, o: List[Symbol], frame):
    #     #consdecl: FuncDecl
    #     #o: Any
    #     #frame: Frame

    #     isInit = (dclr.name == "<init>")
    #     isMain = (dclr.name == "main" and len(dclr.param) == 0)
    #     methodName = "<init>" if isInit else dclr.name
    #     intype = [ArrayPointerType(StringType())] if isMain else [retrieveType(x.varType) for x in dclr.param]
    #     mtype = MType(intype, None)

    #     self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame)) # Need handle mtype

    #     frame.enterScope(True)

    #     glenv = o

    #     # Generate code for parameter declarations
    #     if isInit:
    #         self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
    #     if isMain:
    #         self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

    #     body = dclr.body
    #     self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

    #     # Generate code for statements
    #     if isInit:
    #         self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
    #         self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
    #     list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

    #     self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

    #     # if type(returnType) is VoidType:
    #     self.emit.printout(self.emit.emitRETURN(None, frame))

    #     self.emit.printout(self.emit.emitENDMETHOD(frame))
    #     frame.exitScope()

    def visitVarDecl(self, ctx, o):
        val = "" 
        self.emit.printoutData(self.emit.emitVAR(ctx.name, val))
        self.emit.printoutData(self.emit.emitDATA())

    def visitBlock(self, ast, o):
        for s in ast.stmt:
            self.visit(s, o)

    def visitFuncDecl(self, ast: FuncDecl, o):
        #ast: FuncDecl
        #o: Any

        # subctxt = o
        # frame = Frame(ast.name)
        # self.genMETHOD(ast, subctxt.sym, frame)
        # return SubBody(None, [Symbol(ast.name, [], CName(self.className))] + subctxt.sym)
        if ast.name == "main":
            # Set the global function in MIPS
            self.emit.printout(self.emit.emitGLOBAL("main"))
        self.emit.printout(self.emit.emitFUNC(ast.name))
        # print("************",ast.body)
        self.visit(ast.body, o)

        if ast.name == "main":
            self.emit.printout(self.emit.emitLI(10,"$v0"))
            self.emit.printout(self.emit.emitSYS())

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        # print("::::::::",ast.name)
        if (ast.name == "writeNumber"):
            # print("::::::::",ast.args)
            for arg in ast.args:
                text, reg = self.visit(arg, o)
                self.emit.printout("\n")
                add_text, add_reg = self.emit.emitADDOP(NumberType(), '$a0', reg, '$zero',o)
                self.emit.printout(add_text)
                self.emit.printout(self.emit.emitLI(1,"$v0"))
                self.emit.printout(self.emit.emitSYS())
                self.emit.printout("\n")

    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        text = ""

        if op == '+':
            lcode, lreg = self.visit(ast.left, o)

            # if lreg == "$sp":
            #     lcode = self.emit.popWORD("$t0",o) + lcode
            #     lreg = "$t0"

            add_ltext, add_lreg = self.emit.emitADDOP(NumberType(),"$s1","$s1",lreg,o)

            if add_lreg == "$sp":
                add_ltext = self.emit.popWORD("$s0",o) + add_ltext
                add_lreg = "$s0"

            text += add_ltext

            

            rcode, rreg = self.visit(ast.right, o)
            # if rreg == "$sp":
            #     rcode = self.emit.popWORD("$t0",o) + rcode
            #     rreg = "$t0"

            add_rtext, add_rreg = self.emit.emitADDOP(NumberType(),"$s1","$s1",rreg,o)

            if add_rreg == "$sp":
                add_rtext = self.emit.popWORD("$s0",o) + add_rtext
                add_rreg = "$s0"

            text += add_rtext
            add_text, add_reg = self.emit.emitADDOP(NumberType(),"$s0",add_lreg,add_rreg,o)
            text += add_text
            self.emit.printout(text)
            return text,add_reg


    def visitNumberLiteral(self, ast: NumberLiteral, o):
        #o: Any
        text,reg = self.emit.emitNUMBERLITERAL(ast.value, o)
        if reg == "$sp":
            text = self.emit.popWORD("$t0",o) + text
            reg = "$t0"
        self.emit.printout(text)
        return text, reg

    
