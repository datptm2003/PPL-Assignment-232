from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import MIPSCode



class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.mips = MIPSCode()

    
    def printout(self, in_):
        #in_: String

        self.buff.append(in_)

    def printoutData(self, in_):
        self.buff.insert(0, in_)

    def clearBuff(self):
        self.buff.clear()

    def pushWORD(self,src,o):
        o["$sp"] -= 4
        return self.mips.emitADDI("$sp","$sp",-4) + self.mips.emitSW(src,"$sp",0)

    def popWORD(self,dst,o):
        o["$sp"] += 4
        return self.mips.emitLW(dst,"$sp",0) + self.mips.emitADDI("$sp","$sp",4)

    def emitVAR(self, name, val):
        return name +":" + self.mips.emitWORD(val) 

    def emitFUNC(self, name):
        return self.mips.emitLABEL(name)

    def emitSYS(self):
        return self.mips.emitSYSCALL()

    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()

    def emitTEXT(self):
        return self.mips.emitTEXT()  
    
    def emitDATA(self):
        return self.mips.emitDATA()

    def emitGLOBAL(self, name):
        return self.mips.emitGLOBAL(name)

    def emitLI(self, in_, reg):
        return self.mips.emitLI(reg, in_)


    def emitADDOP(self,typ,dest,src1,src2,o):
        if dest not in o:
            o[dest] = None
        if o[dest] is None:
            o[dest] = src1 + src2
            return self.mips.emitADD(dest,src1,src2),dest
        hasEmptyReg = False
        for res in MIPSCode.sav_reg[1:]:
            if res not in o:
                o[res] = None
            if o[res] is None:
                o[res] = src1 + src2
                if src1 == dest:
                    src1 = res
                if src2 == dest:
                    src2 = res
                return self.mips.emitADD(res,src1,src2),res
        return self.mips.emitADD("$s0",src1,src2) + self.pushWORD("$s0",o),"$sp"

    def emitNUMBERLITERAL(self,number,o):
        hasEmptyReg = False
        for tmp in MIPSCode.tmp_reg[1:]:
            if tmp not in o:
                o[tmp] = None
            if o[tmp] is None:
                o[tmp] = number
                return self.mips.emitADDI(tmp,tmp,number),tmp
        return self.mips.emitADDI("$t0","$t0",number) + self.pushWORD("$t0",o),"$sp"
        
        # Tru stack
        # Load so vao a0
        # Move a0 0($sp)
        

        
