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

    def emitADDOP(self):
        pass

    

        
