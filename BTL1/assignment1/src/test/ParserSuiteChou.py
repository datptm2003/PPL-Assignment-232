import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
    def test_1 (self): 
        self.assertTrue(TestParser.test("","Error on line 1 col 0: <EOF>",201))
    def test_2 (self):
        input="""number a[1] <- ["hihi"]
                bool ahihi[10,23] <- [a[b[2, 3]] + 4]
                string ahihi[2] <- [[1,2,3],[2,1,2]]
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_3 (self):
        input="""a<-10
            """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_4 (self): #check output
        input="""number a <- 10"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5 (self): 
        input="""func main(number b, string b, number a[5]) return 2
            number a
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6 (self):
        input= """var tRue <- true
        func ahihi() return
        """
        expect ="successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7 (self):
        input= """
        var tRue <- true
        func ahihi() return
        if (IF) else fALse <- true
        """
        expect ="Error on line 4 col 8: if"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8 (self):
        input= """
        var tRue <- true
        func ahihi() begin 
        return
        if (IF) else fALse <- true
        end
        """
        expect ="Error on line 5 col 16: else"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9 (self):
        input= """
        var 1a <- 10
        """
        expect ="Error on line 2 col 12: 1"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10 (self):
        input= """
        var true <- 10
        """
        expect ="Error on line 2 col 12: true"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11 (self):
        input= """
        var fAlse <- (10.89e-1*8..."ahihi")%7
        """
        expect ="."
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12 (self):
        input= """
        var fAlse <- (10.89e-1*8.0e1-9...."ahihi")%7.
        """
        expect ="successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13 (self):
        input= """
        var a <- []
        """
        expect ="Error on line 2 col 18: ]"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14 (self):
        input = """func main() return
        return
        """
        expect = 'Error on line 2 col 8: return'
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15 (self):
        input = """func main() return
        var a = []
        """
        expect = 'Error on line 2 col 14: ='
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16 (self):
        input = """boolean isTrue <- true()
        """
        expect = 'Error on line 1 col 0: boolean'
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17 (self):
        input = """bool isTrue <- true()
        """
        expect = 'Error on line 1 col 19: ('
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18 (self):
        input = """bool isValid <- true and false
        """
        expect = 'successful'
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19 (self):
        input = """average <- (score1 + score2) / 2"""
        expect = """Error on line 1 col 0: average"""
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20 (self):
        input = """string stringWith <- "test inside: \"Hello\"\""""
        expect = """Error on line 1 col 36: Hello"""
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21 (self):
        input = """func main() begin
        concatenatedString <- "Hello" ... " " ... "World"
        end
        """
        expect = """Error on line 2 col 46: ..."""
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22 (self):
        input = """func main() begin
        mixedString <- "Numbers: " + (1 + 2) + " Text"
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23 (self):
        input = """func main() begin
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24 (self):
        input = """func main() begin
        number a
        a <- 10
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25 (self):
        input = """func main() begin
        number a <- 10
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26 (self):
        input = """func main() begin
        string a <- "ahihi"
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27 (self):
        input = """func main() begin
        bool a <- true
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28 (self):
        input = """func main() begin
        bool a <- true+false
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29 (self):
        input = """func main() begin
        foo() <- 1
        end
        """
        expect = """Error on line 2 col 14: <-"""
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30 (self):
        input = """func main() begin
        foo()[1] <- 1
        end
        """
        expect = """Error on line 2 col 13: ["""
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31 (self):
        input = """func main(number a) begin
        a <- a + 1 / 2
        foo()[1][2] <- 1
        end
        """
        expect = """Error on line 3 col 13: ["""
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32 (self):
        input = """func main(number a) begin
        a <- a + 1 / 2
        "a"[1] <- 1
        end
        """
        expect = """Error on line 3 col 8: a"""
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        input = """func main(number a) begin
        a <- a + 1 / 2
        a[1][2] <- 1
        end
        """
        expect = """Error on line 3 col 12: ["""
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        input = """func main(dynamic a) begin
        a <- a + 1 / 2
        a[1][2] <- 1
        end
        """
        expect = """Error on line 1 col 10: dynamic"""
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35(self):
        input = """func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        input = """func main(number a[1+1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        end
        """
        expect = """Error on line 1 col 20: +"""
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        input = """
        func test() return
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        test() return
        end
        """
        expect = """Error on line 6 col 15: return"""
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        test() 
        return 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        if (1) number b
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        if (1) number b
        else return
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        c <- 0
        """
        expect = """Error on line 10 col 8: c"""
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm()
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin
        a <- a + 1 / 2
        a[1] <- 1
        ##this is a comment
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm() return
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin##this is a comment
        a <- a + 1 / 2
        a[1] <- 1
        
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm() return 1
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin##this is a comment
        a <- a + 1 / 2
        a[1] <- 1
        string str <- "ahihi\na"
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm() return 1
        """
        expect = """ahihi"""
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin##this is a comment
        a <- a + 1 / 2
        a[1] <- 1
        string str <- "ahihi\\na"
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm() return 1
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        input = """
        func test() return "success"
        func main(number a[1]) begin##this is a comment
        begin
        begin
        end
        end
        a <- a + 1 / 2
        a[1] <- 1
        string str <- "ahihi\\na"
        if (1) number b
        else return "fail"
        end
        var b <- [1,2,3]
        func hmmm() return 1
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49(self):
        input = """
        func foo1()
        func foo2()
        begin
        func foo3()
        end
        """
        expect = """Error on line 5 col 8: func"""
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        input = """
        func foo1()
        func foo2()
        begin
        foo1()
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        input = """
        func foo1()
        func foo2()
        begin
        a[foo2()] <- a[foo1()]%6
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        input = """
        func foo1()
        func foo2()
        begin
        a[foo2()+1-0*6....0.e-4] <- a[foo1()]%6
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        input = """
        func foo1()
        func foo2() return 1
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main() 
        begin
        exp <- "str1"..."str2"
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56 (self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main() return
        begin
        exp <- "str1"..."str2"
        end
        """
        expect = """Error on line 6 col 8: begin"""
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57 (self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main()
        begin
        exp <- "str1"..."str2"
        print(exp)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58 (self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main()
        begin
        exp <- "str1"..."str2"
        print(exp)
        input <- readBool()
        writeBool(i)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59 (self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main()
        begin
        exp <- "str1"..."str2"
        print(exp)
        input <- readBool()
        writeBool("string"...a)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        """Simple program: int main() {} """
        input = """
func areDivisors(number num1, number num2)
    return (num1 % num2 = 0 or num2 % num1 = 0)
func main()
    begin
        var num1 <- readNumber()
        var num2 <- readNumber()
        if areDivisors(num1, num2) printString("Yes")
        else printString("No")
    end
"""
        expect = """Error on line 3 col 43: ="""
        self.assertTrue(TestParser.test(input, expect, 260))
    def test_61(self):
        input = """
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main()
        begin
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        input = """
        var foo <- 0
        func foo1() return 1
        func foo2() return 2*1+0
        string exp
        func main() return
        begin
        end
        """
        expect = """Error on line 7 col 8: begin"""
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        input = """
        var foo <- 0
        number a <- foo
        dynamic a
        
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        input = """
        begin
        end
        """
        expect = """Error on line 2 col 8: begin"""
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        input = """
        func a[]()
        begin
        begin
        end
        end
        """
        expect = """Error on line 2 col 14: ["""
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        input = """
        func a(number )
        begin
        begin
        end
        end
        """
        expect = """Error on line 2 col 22: )"""
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        input = """
        func a()
        begin
        begin
        return 
        end
        break
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        input = """
        func a()
        begin
        begin
        return 
        end
        break
        continue
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        input = """
        func a()
        begin
        for i until i<=10 by 1+1
        
        
        
        number a[1]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        input = """
        func a()
        begin
        for a until i<=10 by 1+1
        
        
        
        number a[1]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71(self):
        input = """
        func a()
        begin
        for foo()[i] until i<=10 by 1+1
        
        
        
        number a[1]
        end
        """
        expect = """Error on line 4 col 15: ("""
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        input = """
        func a()
        begin
        for a until i<=10 by 1+1
        
        
        
        number a[1]
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73 (self):
        input = """
        func a()
        begin
        for a until i<=10 by 1+1 func()
        end
        """
        expect = """Error on line 4 col 33: func"""
        self.assertTrue(TestParser.test(input,expect,273))
    def test_74 (self):
        input = """
        func aahihihihi() return 
        begin
        for a[i*2] until i<=10 by 1+1 func()
        end
        """
        expect = """Error on line 3 col 8: begin"""
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75(self):
        """Simple program: int main() {} """
        input = """
        func main()
        begin
        number x <- readNumber()
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_76(self):
        input = """
        func main()
        begin
        number x <- readNumber(i)
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_77(self):
        input = """
        func main()
        begin
        number x <- writeNumber(i)
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_78(self):
        input = """
        func main()
        begin
        number x <- writeNumber(i[foo()])
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_79(self):
        input = """
        func main()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_80(self):
        input = """
        func main()
        begin
        number x <- writeNumber(i[foo()])
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        """
        expect = "Error on line 7 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_81(self):
        input = """
        func main()
        begin
        number x <- writeNumber(i[foo()])
        if (isPrime(x)) writeString("Yes")
        else writeString("No")
        return
        end
        end
        """
        expect = "Error on line 9 col 8: end"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_82(self):
        input = """
        func main()
        begin
        foo()
        foo()+1-0.8..."0"
        end
        """
        expect = "Error on line 5 col 13: +"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_83(self):
        input = """
        func main()
        begin
        foo()
        a <- foo()+1-0.8..."0"
        return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_84(self):
        input = """
        func main()
        begin
        foo()<-foo()*foo
        a <- foo()+1-0.8..."0"
        return
        end
        """
        expect = "Error on line 4 col 13: <-"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_85(self):
        input = """
        func main()
        begin
        foo<-foo()*foo
        a <- foo()+1-0.8..."0"
        return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_86(self):
        input = """
        func main()
        begin
        begin
        foo<-foo()*foo
        a <- foo()+1-0.8..."0"
        return
        end
        """
        expect = "Error on line 9 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_87 (self):
        input = """
        1
        func main()
        begin
        begin
        foo<-foo()*foo
        a <- foo()+1-0.8..."0"
        return
        end
        end
        """
        expect = "Error on line 2 col 8: 1"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_88(self):
        input = """
        func main() break
        """
        expect = "Error on line 2 col 20: break"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_89(self):
        input = """
        func main() begin
        continue <- 0
        end
        """
        expect = "Error on line 3 col 17: <-"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_90(self):
        input = """
        func main() begin
        a <- 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_91(self):
        input = """
        func main() begin
        number a <- 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_92(self):
        input = """
        func main() begin
        foo -1  <- a*a+1
        end
        """
        expect = "Error on line 3 col 12: -"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_93(self):
        input = """
        func main(number a[1*1%6.0e-4]) begin
        number a <- 0
        end
        """
        expect = "Error on line 2 col 28: *"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94(self):
        input = """
        func main()
        begin
        begin
        begin
        end
        end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95(self):
        input = """
        func main()
        func main()
        func main()
        return func
        """
        expect = "Error on line 5 col 15: func"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96(self):
        input = """
        func main() return [1,2,3]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_97(self):
        input = """
        func main() return [1,2,3]*[1,[2]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_98(self):
        input = """
        func main() return #
        """
        expect = "#"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_99(self):
        input = """##ahihihihihihihihihihihihihihihihih"""
        expect = "Error on line 1 col 36: <EOF>"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_100(self):
        input = """func main()
        begin
        string c <- "\mmmp"
        end
        """
        expect = '\m'
        self.assertTrue(TestParser.test(input,expect,300))
        
