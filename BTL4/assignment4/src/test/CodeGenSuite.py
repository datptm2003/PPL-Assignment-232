import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    codegenTest = 499
    def test_codegen_00(self):
        input = \
"""
func main ()
begin
    number x
    x <- 5
    writeNumber(x)
end

"""
        expect = "5.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))
    
    def test_codegen_01(self):
        input = \
"""
func main ()
begin
    number x <- 7.5 % 3.5
    writeNumber(x)
end

"""
        expect = "0.5"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_02(self):
        input = \
"""
func main ()
begin
    string x <- "abc"..."abc"
    writeString(x)
end

"""
        expect = "abcabc"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_03(self):
        input = \
"""
func main ()
begin
    string x <- "abc"..."def"
    writeString(x)
end

"""
        expect = "abcdef"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_04(self):
        input = \
"""
func main ()
begin
    bool x <- "abc" == "def"
    writeBool(x)
end

"""
        expect = "false"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_05(self):
        input = \
"""
func main ()
begin
    bool x <- "abc" == "abc"
    writeBool(x)
end

"""
        expect = "true"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_06(self):
        input = \
"""
func helper(bool x, bool y) return x and y
func main ()
begin
    bool x <- "abc" == "abc"
    writeBool(helper(x,false))
end

"""
        expect = "false"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_07(self):
        input = \
"""
func help(number x, number y) return x + y
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "16.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_08(self):
        input = \
"""
func help(number x, number y) return x * y
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "55.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_09(self):
        input = \
"""
func help(number x, number y) return y / x
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "2.2"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_09(self):
        input = \
"""
func help(number x, number y) return y - x
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "6.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_10(self):
        input = \
"""
func help(number x, number y) return y - x * 2
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "1.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_11(self):
        input = \
"""
func help(number x, number y) return y - x * 2 + 10
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "11.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_12(self):
        input = \
"""
func help(number x, number y) return y - x * 2 + 10
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "11.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_13(self):
        input = \
"""
func help(number x, number y) return x *y - x * 2 + 8
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "53.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_14(self):
        input = \
"""
func help(number x, number y) return x + y + y + y
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "38.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_15(self):
        input = \
"""
func help(number x, number y) return x - y - y - y
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "-28.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_16(self):
        input = \
"""
func help(number x, number y) return x / y - 5
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "-4.5454545"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_17(self):
        input = \
"""
func help(number x, number y) return 6 / 5 + x
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "6.2"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_18(self):
        input = \
"""
func help(number x, number y) return 6 / 5 - x
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "3.8"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_codegen_19(self):
        input = \
"""
func help(number x, number y) return x
func main ()
begin
    number a <- 5
    number b <- 11
    writeNumber(help(a,b))
end

"""
        expect = "5.0"
        CheckCodeGenSuite.codegenTest += 1
        self.assertTrue(TestCodeGen.test(input, expect, CheckCodeGenSuite.codegenTest))

    def test_20(self):
        input = """func main ()
        begin
            number a <- 0
            writeNumber(a)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))
    def test_21(self):
        input = """func main ()
        begin
            string a <- "0.0"
            writeString(a)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 521))
    def test_22(self):
        input = """func main ()
        begin
            bool a <- true
            writeBool(a)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
    def test_23(self):
        input = """func main ()
        begin
            bool a <- true
            writeBool(a and true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
    def test_24(self):
        input = """func main ()
        begin
            var a <- true
            writeBool(a)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    def test_25(self):
        input = """func main ()
        begin
            var a <- 1
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    def test_26(self):
        input = """func main ()
        begin
            var a <- "1.0"
            writeString(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    def test_27(self):
        input = """func main ()
        begin
            if (true) writeNumber(1)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
    def test_28(self):
        input = """func main ()
        begin
            if (false) writeNumber(1)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 528))
    def test_29(self):
        input = """func main ()
        begin
            if (true) writeNumber(1)
            else writeString("hi")
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 529))
    def test_30(self):
        input = """func main ()
        begin
            if (false) writeNumber(1)
            else writeString("hi")
        end
        """
        expect = "hi"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
    def test_31(self):
        input = """func main ()
        begin
            bool a <- false
            if (a) writeNumber(1)
            else writeString("hi")
        end
        """
        expect = "hi"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
    def test_32(self):
        input = """func main ()
        begin
            bool a <- true
            if (a) writeNumber(1)
            else writeString("hi")
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
    def test_33(self):
        input = """func main ()
        begin
            var a <- 1
            a <- a + 1
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    def test_34(self):
        input = """func main ()
        begin
            var a <- 1
            for a until a <= 5 by 1
                begin
                writeNumber(a)
                writeString("-")
                end
        end
        """
        expect = "1.0-2.0-3.0-4.0-5.0-"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
    def test_35(self):
        input = """
        func a() 
        begin
        end
        func main ()
        begin
            number a <- 10
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 535))
    def test_36(self):
        input = """
        func a(number a, bool b, string s) 
        begin
        end
        func main ()
        begin
            number a <- 10
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 536))
    def test_37(self):
        input = """
        func a(number a, bool b, string s) 
        begin
            writeNumber(1)
        end
        func main ()
        begin
            number a <- 10
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 537))
    def test_38(self):
        input = """
        func main ()
        begin
            number a <- 10
            number b <- 10
            writeNumber(a+b)
        end
        """
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    def test_39(self):
        input = """
        func main ()
        begin
            var a <- 10
            number b <- 10
            writeNumber(a+b)
        end
        """
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))
    def test_40(self):
        input = """
        func main ()
        begin
            var a <- 10
            number b <- 10
            writeBool(a=b)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 540))
    def test_41(self):
        input = """
        func main ()
        begin
            var a <- "10"
            string b <- "10"
            writeBool(a==b)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 541))
    def test_42(self):
        input = """
        func main ()
        begin
            var a <- "10"
            bool b <- false
            writeBool(b)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    def test_43(self):
        input = """
        func main ()
        begin
            var b <- true
            b <- not b
            if (b) writeString("b is true")
            else writeString("b is false")
        end
        """
        expect = "b is false"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    def test_44(self):
        input = """
        func main ()
        begin
            var b <- true
            if (b) writeString("b is true")
            else writeString("b is false")
        end
        """
        expect = "b is true"
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    def test_45(self):
        input = """
        func main ()
        begin
            var b <- true
            if (b) writeString("b is true")
        end
        """
        expect = "b is true"
        self.assertTrue(TestCodeGen.test(input, expect, 545))
    def test_46(self):
        input = """
        func main ()
        begin
            var b <- true
            if (b and false) writeString("b is true")
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))
    def test_47(self):
        input = """
        func main ()
        begin
            var b <- true
            if (b or false) writeString("b is true")
        end
        """
        expect = "b is true"
        self.assertTrue(TestCodeGen.test(input, expect, 547))
    def test_48(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            if (b or false) writeNumber(c)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 548))
    def test_49(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            if (b and false) writeNumber(c)
            else writeNumber(c-11)
        end
        """
        expect = "-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    def test_50(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            if (b and false) writeNumber(c)
            else writeString("Toi da co gang het suc")
        end
        """
        expect = "Toi da co gang het suc"
        self.assertTrue(TestCodeGen.test(input, expect, 550))
    def test_51(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            for c until c < 0 by 1
                writeNumber(c)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 551))
    def test_52(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            for c until c < 12 by 1
                writeNumber(c)
                writeString("-")
        end
        """
        expect = "10.011.0-"
        self.assertTrue(TestCodeGen.test(input, expect, 552))
    def test_53(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 10
            for c until c < 12 by 1
                writeNumber(c)
        end
        """
        expect = "10.011.0"
        self.assertTrue(TestCodeGen.test(input, expect, 553))
    def test_54(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 0
            for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = "0.02.04.06.08.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
    def test_55(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 0
            if (b) for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = "0.02.04.06.08.010.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))
    def test_56(self):
        input = """
        func main ()
        begin
            var b <- true
            number c <- 0
            if (not b) for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 556))
    def test_57(self):
        input = """
        func a() 
        func main ()
        begin
            var b <- true
            number c <- 0
            if (not b) for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    def test_58(self):
        input = """
        func a() 
        func main ()
        begin
            var b <- 1 < 0
            number c <- 0
            if (b) for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    def test_59(self):
        input = """
        func a() 
        func main ()
        begin
            var b <- 1 >= 0
            number c <- 12
            if (b) for c until c < 12 by 2
                writeNumber(c)
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 559))
    def test_60(self):
        input = """
        func main ()
        begin
            var b <- 1 >= 0
            number c <- 10
            for c until c < 12 by 2
                writeNumber(c)

        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    def test_61(self):
        input = """
        func main ()
        begin
            number c <- 11
            for c until c < 12 by 2
                writeNumber(c)

        end
        """
        expect = "11.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    def test_62(self):
        input = """
        func main ()
        begin
            number c <- 14
            for c until c > 12 by -2
                writeNumber(c)

        end
        """
        expect = "14.0"
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    def test_63(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c - -1
            writeNumber(c)

        end
        """
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
    def test_64(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c - 1
            writeNumber(c)

        end
        """
        expect = "13.0"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    def test_65(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c + 1
            writeNumber(c)

        end
        """
        expect = "15.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    def test_66(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c * 1
            writeNumber(c)

        end
        """
        expect = "14.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    def test_67(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c / 1
            writeNumber(c)

        end
        """
        expect = "14.0"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
    def test_68(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c * 1 +2
            writeNumber(c)

        end
        """
        expect = "16.0"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
    def test_69(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c / 2 +2
            writeNumber(c)

        end
        """
        expect = "9.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    def test_70(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c * 2 +2
            writeNumber(c)

        end
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
    def test_71(self):
        input = """
        func main ()
        begin
            number c <- 14
            c <- c / 2 + 3
            writeNumber(c)

        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 571))
    def test_72(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            writeString(s)

        end
        """
        expect = "toi "
        self.assertTrue(TestCodeGen.test(input, expect, 572))
    def test_73(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            writeString(s..."di")

        end
        """
        expect = "toi di"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
    def test_74(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            writeString(s..."di hoc")

        end
        """
        expect = "toi di hoc"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
    def test_75(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            writeString(s..."di hoc lop")
            writeNumber(10)

        end
        """
        expect = "toi di hoc lop10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
    def test_76(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            writeString(s..."di hoc lop")
            writeNumber(1)

        end
        """
        expect = "toi di hoc lop1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    def test_77(self):
        input = """
        func main ()
        begin
            string s <- "toi "
            

        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 577))
    def test_78(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            writeString(s)

        end
        """
        expect = "toi tram kem"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
    def test_79(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            string a <- "toi tram kem"
            writeBool(s == a)

        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 579))
    def test_80(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            string a <- "toi tramem"
            writeBool(s == a)

        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    def test_81(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            string a <- "toi tram kem"

        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    def test_82(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            string a <- "toi tram kem"
            writeString(s...a)

        end
        """
        expect = "toi tram kemtoi tram kem"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    def test_83(self):
        input = """
        func main ()
        begin
            string s <- "toi tram kem"
            string b <- "toi tram kem"
            writeString(s...b)

        end
        """
        expect = "toi tram kemtoi tram kem"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    def test_84(self):
        input = """
        func main ()
        begin
            
            writeBool(true)

        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
    def test_85(self):
        input = """
        func main ()
        begin
            var t<- true
            writeBool(t)

        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
    def test_86(self):
        input = """
        func main ()
        begin
            var t<- false
            writeBool(t)

        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    def test_87(self):
        input = """
        func main ()
        begin
            var t<- false or true
            writeBool(t)

        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 587))
    def test_88(self):
        input = """
        func main ()
        begin
            var t<- false and true
            writeBool(t)

        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 588))
    def test_89(self):
        input = """
        func main ()
        begin
            var t<- not true
            writeBool(t)

        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 589))
    def test_90(self):
        input = """
        func main ()
        begin
            var t<- not false
            writeBool(t)

        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
    def test_91(self):
        input = """
        func main ()
        begin
            var t<- 1
            writeNumber(t)

        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 591))
    def test_92(self):
        input = """
        func main ()
        begin
            var t<- 1.0
            writeNumber(t+1)

        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    def test_93(self):
        input = """
        func main ()
        begin
            var t<- 1.0
            writeNumber(t-1)

        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    def test_94(self):
        input = """
        func main ()
        begin
            var t<- 10.0
            writeNumber(t*1)

        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 594))
    def test_95(self):
        input = """
        func main ()
        begin
            var t<- 10.0
            writeNumber(t/5)

        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 595))
    def test_96(self):
        input = """
        func main ()
        begin
            var t<- 10.0
            writeNumber(t/2)

        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 596))
    def test_97(self):
        input = """
        func main ()
        begin
            var t<- 100.0
            writeNumber(t/100)

        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    def test_98(self):
        input = """
        func main ()
        begin
            var t<- 100.0
            writeNumber(t/10)

        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 598))
    def test_99(self):
        input = """
        func main ()
        begin
            var t<- 100.0
            writeNumber(t/1)

        end
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 599))