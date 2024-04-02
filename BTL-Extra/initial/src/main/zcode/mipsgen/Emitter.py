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

    def clearBuff(self):
        self.buff.clear()

    def pushWORD(self,src,o):
        o["$sp"] -= 4
        return self.mips.emitADDI("$sp","$sp",-4) + self.mips.emitSW(src,"$sp",0)

    def popWORD(self,dst,o):
        o["$sp"] += 4
        return self.mips.emitLW(dst,"$sp",0) + self.mips.emitADDI("$sp","$sp",4)

    def emitADDOP(self,dest,src1,src2,o):
        if type(src1) == int:
            pass
        return self.mips.emitADD(dest,src1,src2)

    def emitNUMBERLITERAL(self,number,o):
        hasEmptyReg = False
        for tmp in MIPSCode.tmp_reg[1:]:
            if o[tmp] is None:
                o[tmp] = number
                return self.mips.emitADDI(tmp,tmp,number),tmp
                hasEmptyReg = True
                break
        if not hasEmptyReg:
            return self.mips.emitADDI("$t0","$t0",number) + self.pushWORD("$t0",o),"$sp"
        
        # Tru stack
        # Load so vao a0
        # Move a0 0($sp)
        

        
