'''
*   @author Dr.Nguyen Hua Phung
*   @version 1.0
*   28/6/2006
*   This class provides facilities for method generation
*
'''
class MIPSCode:
    zero_reg = ["$0","$zero"]
    at_reg = ["$at"]
    val_reg = ["$v0","$v1"]
    arg_reg = [f"$a{a}" for a in range(4)]
    tmp_reg = [f"$t{t}" for t in range(10)]
    sav_reg = [f"$s{s}" for s in range(8)]
    ker_reg = ["$k0","$k1"]
    glb_reg = ["$gp"]
    stk_reg = ["$sp"]
    frm_reg = ["$fp"]
    ra_reg = ["$ra"]

    def emitSIMPLEPROGRAM(self):
        return """"""

    def emitADD(self, dest, src1, src2):
        return "add " + dest + ", " + src1 + ", " + src2
        
    def emitSUB(self, dest, src1, src2):
        return "sub " + dest + ", " + src1 + ", " + src2

    def emitADDI(self, dest, src, in_const):
        return "addi " + dest + ", " + src + ", " + str(in_const)

    def emitADDU(self, dest, src1, src2):
        return "addu " + dest + ", " + src1 + ", " + src2

    def emitSUBU(self, dest, src1, src2):
        return "subu " + dest + ", " + src1 + ", " + src2

    def emitADDIU(self, dest, src, in_const):
        return "addiu " + dest + ", " + src + ", " + str(in_const)
    
    def emitMUL(self, dest, src1, src2):
        return "mul " + dest + ", " + src1 + ", " + src2
    
    def emitMULT(self, src1, src2):
        return "mult " + src1 + ", " + src2
    
    def emitDIV(self, src1, src2):
        return "div " + src1 + ", " + src2

    def emitAND(self, dest, src1, src2):
        return "and " + dest + ", " + src1 + ", " + src2

    def emitOR(self, dest, src1, src2):
        return "or " + dest + ", " + src1 + ", " + src2

    def emitNOR(self, dest, src1, src2):
        return "nor " + dest + ", " + src1 + ", " + src2

    def emitANDI(self, dest, src, in_const):
        return "andi " + dest + ", " + src + ", " + str(in_const)

    def emitORI(self, dest, src, in_const):
        return "ori " + dest + ", " + src + ", " + str(in_const)

    def emitSLL(self, dest, src, in_const):
        return "sll " + dest + ", " + src + ", " + str(in_const)

    def emitSRL(self, dest, src, in_const):
        return "srl " + dest + ", " + src + ", " + str(in_const)

    def emitLW(self, dest, src, offset):
        return "lw " + dest + ", " + src + ", " + str(offset)

    def emitLH(self, dest, src, offset):
        return "lh " + dest + ", " + src + ", " + str(offset)

    def emitLB(self, dest, src, offset):
        return "lb " + dest + ", " + src + ", " + str(offset)

    def emitLUI(self, dest, in_const):
        return "lui " + dest + ", " + str(in_const)
    
    def emitLA(self, dest, label):
        return "la " + dest + ", " + label
    
    def emitLI(self, dest, in_const):
        return "la " + dest + ", " + str(in_const)

    def emitLHU(self, dest, src, offset):
        return "lhu " + dest + ", " + src + ", " + str(offset)

    def emitLBU(self, dest, src, offset):
        return "lbu " + dest + ", " + src + ", " + str(offset)

    def emitSW(self, dest, src, offset):
        return "sw " + dest + ", " + src + ", " + str(offset)

    def emitSH(self, dest, src, offset):
        return "sh " + dest + ", " + src + ", " + str(offset)

    def emitSB(self, dest, src, offset):
        return "sb " + dest + ", " + src + ", " + str(offset)

    def emitMFHI(self, dest):
        return "mfhi " + dest
    
    def emitMFLO(self, dest):
        return "mflo " + dest

    def emitGOTO(self, label):
        return "goto " + label

    def emitJ(self, label):
        return "j " + label

    def emitJR(self, reg):
        return "jr " + reg

    def emitJAL(self, reg):
        return "jal " + reg

    def emitBEQ(self, src1, src2, offset):
        return "beq " + src1 + ", " + src2 + ", " + str(offset)

    def emitBNE(self, src1, src2, offset):
        return "bne " + src1 + ", " + src2 + ", " + str(offset)

    def emitBGT(self, src1, src2, offset):
        return "bgt " + src1 + ", " + src2 + ", " + str(offset)
    
    def emitBGE(self, src1, src2, offset):
        return "bge " + src1 + ", " + src2 + ", " + str(offset)
    
    def emitBLT(self, src1, src2, offset):
        return "blt " + src1 + ", " + src2 + ", " + str(offset)
    
    def emitBLE(self, src1, src2, offset):
        return "ble " + src1 + ", " + src2 + ", " + str(offset)

    def emitSLT(self, dest, src1, src2):
        return "slt " + dest + ", " + src1 + ", " + src2

    def emitSLTU(self, dest, src1, src2):
        return "sltu " + dest + ", " + src1 + ", " + src2

    def emitSLTI(self, dest, src, in_const):
        return "slt " + dest + ", " + src + ", " + str(in_const)

    def emitSLTIU(self, dest, src, in_const):
        return "sltiu " + dest + ", " + src + ", " + str(in_const)

    def emitWORD(self, var, val_lst):
        text = val_lst[0]
        for val in val_lst[1:]:
            text += ", " + val
        return var + ": " + ".word " + text
    
    def emitHALF(self, var, val_lst):
        text = val_lst[0]
        for val in val_lst[1:]:
            text += ", " + val
        return var + ": " + ".half " + text
    
    def emitBYTE(self, var, val_lst):
        text = val_lst[0]
        for val in val_lst[1:]:
            text += ", " + val
        return var + ": " + ".byte " + text
    
    def emitASCII(self, var, val):
        return var + ": " + ".ascii " + "\"" + val + "\""
    
    def emitASCIIZ(self, var, val):
        return var + ": " + ".asciiz " + "\"" + val + "\""
    
    def emitSPACE(self, var, n_byte):
        return var + ": " + ".space " + str(n_byte)

    def emitALIGN(self, var, n):
        return var + ": " + ".align " + str(n)

