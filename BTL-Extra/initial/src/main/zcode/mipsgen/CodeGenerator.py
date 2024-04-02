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
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast: Program, ctxt):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl("<init>", [], Block([])), ctxt, Frame("<init>"))
        self.emit.emitEPILOG()
        return ctxt

    def genMETHOD(self, dclr: FuncDecl, o: List[Symbol], frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = (dclr.name == "<init>")
        isMain = (dclr.name == "main" and len(dclr.param) == 0)
        methodName = "<init>" if isInit else dclr.name
        intype = [ArrayPointerType(StringType())] if isMain else [retrieveType(x.varType) for x in dclr.param]
        mtype = MType(intype, None)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame)) # Need handle mtype

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

        body = dclr.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))

        # if type(returnType) is VoidType:
        self.emit.printout(self.emit.emitRETURN(None, frame))

        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

        

    def visitFuncDecl(self, ast: FuncDecl, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, [], CName(self.className))] + subctxt.sym)

    def visitCallStmt(self, ast: CallStmt, o: SubBody):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name, nenv, lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype
        # print(ctype)

        in_ = ("", list())
        for x in ast.args:
            parCode, parType = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + parCode, in_[1].append(parType))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame))

    def visitBinaryOp(self, ast: BinaryOp, o):
        op = ast.op
        text = ""

        if op == '+':
            lcode, lreg = self.visit(ast.left, o)
            if lreg == "$sp":
                lcode = self.emit.popWORD("$t0",o) + lcode
                lreg = "$t0"

            text += lcode + self.emit.emitADDOP("$s0",lreg,0)

            rcode, rreg = self.visit(ast.right, o)
            if rreg == "$sp":
                rcode = self.emit.popWORD("$t0",o) + rcode
                rreg = "$t0"

            text += rcode + self.emit.emitADDOP("$s0",rreg,0)

            return text,"$s0"


    def visitNumberLiteral(self, ast: NumberLiteral, o):
        #o: Any

        return self.emit.emitNUMBERLITERAL(ast.value, o)

    
