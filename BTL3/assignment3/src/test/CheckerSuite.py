import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    checkTest = 399
    def test_check_00(self):
        input = \
"""number a
"""
        expect = "No Entry Point"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_01(self):
        input = \
"""var a <- bcd + 456
func foo(number x, string s)
begin
    y <- x + 4
    s <- concat(s,"s")
end

func main() begin

end
"""
        expect = "Undeclared Identifier: bcd"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_02(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func foo(number x, string s)
begin
    y <- x + 4
    s <- concat(s,"s")
end

func main() begin

end
"""
        expect = "Undeclared Identifier: y"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_03(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end

func main() begin

end
"""
        expect = "Undeclared Function: concat"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_04(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end
"""
        expect = "No Entry Point"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_05(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(y,"s")
end

func main() begin

end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(concat), [Id(y), StringLit(s)])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_06(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end
"""
        expect = "No Function Definition: concat"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_07(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end

func concat(string s1, string s2, bool b) begin
    if (b) return s1...s2
    else return s2...s1
end
"""
        expect = "Redeclared Function: concat"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_08(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end

func concat(string s1, string s2) begin
    bool b <- s1 == s2
    if (b) return (s1...s2)..."a"
    else return (s2...s1)..."b"
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_09(self):
        input = \
"""number bcd <- 78910
var a <- bcd + 456
func concat(string s1, string s2)

func concat(string s1, string s2) begin
    bool b <- s1 == s2
    if (b) return (s1...s2)..."a"
    else return (s2...s1)..."b"
end

func foo(number x, string s)
begin
    number y <- x + 4
    s <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_10(self):
        input = \
"""func concat(string s1, string s2)

func concat(string s1, string s2) begin
    bool b <- s1 == s2
    if (b) return (s1...s2)..."a"
    else return (s2...s1)..."b"
end

func foo(number x, string s)
begin
    number y <- x + 4
    number a <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, CallExpr(Id(concat), [Id(s), StringLit(s)]))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_11(self):
        input = \
"""func concat(string s1, string s2) begin
    bool b <- s1 == s2
    if (b) return (s1...s2)..."a"
    else return (s2...s1)..."b"
end

func concat(string s1, string s2)

func foo(number x, string s)
begin
    number y <- x + 4
    number a <- concat(s,"s")
end

func main() begin
    foo(5,"5")
    
end
"""
        expect = "Redeclared Function: concat"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_12(self):
        input = \
"""dynamic a
string x[1] <- [a]

func main() return
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_13(self):
        input = \
"""dynamic a
string x <- ["a",a,[a]]

func main() return
"""
        expect = "Type Mismatch In Expression: ArrayLit(StringLit(a), Id(a), ArrayLit(Id(a)))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_14(self):
        input = \
"""## dynamic a
number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    x[0] <- [6,7,8]
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_15(self):
        input = \
"""dynamic a
number x[2] <- [a,1]

number y <- a - 2

func main() return
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_16(self):
        input = \
"""func main() begin
    number x[2,3] <- [[1,2,3],[4,5,6]]
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_17(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    x[0,1] <- [6,7,8]
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(x), [NumLit(0.0), NumLit(1.0)]), ArrayLit(NumLit(6.0), NumLit(7.0), NumLit(8.0)))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_18(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    x[0,1] <- 9
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_19(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    string x[3] <- ["1","2","3"]
    x[0] <- 4
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(x), [NumLit(0.0)]), NumLit(4.0))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_20(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    string x[3] <- ["1","2","3"]
    x[0,1] <- 4
end
"""
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(x), [NumLit(0.0), NumLit(1.0)]), NumLit(4.0))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_21(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    string x[3] <- ["1","2","3"]
    number x <- 4
    ## x[0,1] <- 4
end
"""
        expect = "Redeclared Variable: x"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_22(self):
        input = \
"""number x[2,3] <- [[0,1,2],[3,4,5]]

func main() begin
    string x[3] <- ["1","2","3"]
    begin 
        number x <- 2
        begin
            bool x <- false
        end
    end

end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_23(self):
        input = \
"""func foo(number a, bool b) begin
    if (b) return a + 1
    else begin
        var b <- "b"
    end
    begin
        bool a <- true
    end
end

func main() begin
    number x <- foo(16,false)

end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_24(self):
        input = \
"""func foo(number a, bool b) begin
    if (b) return a + 1
    else begin
        var b <- "b"
    end
    begin
        bool a <- true
    end
end

func main() begin
    number x <- foo(16,"abc")

end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(16.0), StringLit(abc)])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_25(self):
        input = \
"""func foo(number a, bool b) begin
    if (b) return a + 1
    else begin
        var b <- "b"
    end
    begin
        bool a <- true
    end
end

func main() begin
    number x <- foo(16,true,"16")

end
"""
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(16.0), BooleanLit(True), StringLit(16)])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_26(self):
        input = \
"""func foo(number a, bool b) begin
    if (b) return a + 1
    else begin
        var b <- "b"
    end
    begin
        bool a <- true
    end
end

func main() begin
    foo(16,true,"16")

end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(16.0), BooleanLit(True), StringLit(16)])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_27(self):
        input = \
"""func foo(number a, bool b) begin
    if (b) return a + 1
    else begin
        var b <- "b"
    end
    begin
        bool a <- true
    end
end

func main() begin
    number x <- foo(b,true)

end
"""
        expect = "Undeclared Identifier: b"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_28(self):
        input = \
"""
func main() begin
    begin
        var x <- 789
    end
    number x <- true and not false
    begin
        var x <- "789"
    end

end
"""
        expect = "Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, BinaryOp(and, BooleanLit(True), UnaryOp(not, BooleanLit(False))))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_29(self):
        input = \
"""
func main() begin
    begin
        var x <- 789
    end
    bool x <- true and not false
    begin
        var x <- "789"
    end

end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_30(self):
        input = \
"""func foo(number x) begin
    number a <- x + 9
    a <- a + 1
    string x <- "foo"
    return x
end
func main() begin
    string x <- foo(2e5)

end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_31(self):
        input = \
"""func foo(number x) begin
    number a <- x + 9
    a <- a + 1
    return x * 2 - a
    string x <- "foo"
    return x
end
func main() begin
    string x <- foo(2e5)

end
"""
        expect = "Type Mismatch In Statement: Return(Id(x))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_32(self):
        input = \
"""func foo(number x) begin
    writeNumber(x)
    string y <- readString()
end
func main() begin
    foo(16)

end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_33(self):
        input = \
"""func foo(number x) begin
    readNumber(x)
    writeString()
end
func main() begin
    foo(16)

end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(readNumber), [Id(x)])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_34(self):
        input = \
"""func foo(number x) begin
    ## readNumber(x)
    writeString()
end
func main() begin
    foo(16)

end
"""
        expect = "Type Mismatch In Statement: CallStmt(Id(writeString), [])"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_35(self):
        input = \
"""func foo(number x, string s, bool b) begin
    number x <- readNumber() / 8
    writeNumber(x)
    string s <- readString()..."abc"
    writeString(s)
    bool b <- readBool() or b
    writeBool(b)
end
func main() begin
    foo(16,"Dat",false)
    string s <- "123"
    writeString(s)
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_36(self):
        input = \
"""func isEven(number n) return n % 2 = 0
func main() begin
    number arr[5] <- [156,6546,795,29,1]
    number i <- 0
    for i until i < 4 by 1
        if (isEven(arr[i])) writeString("Even number\\n")
        else writeString("Odd number\\n")
    
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_37(self):
        input = \
"""func foo() begin
    dynamic a
    return a
end

func main() begin
    foo()
end
"""
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_38(self):
        input = \
"""func compare(number a[5]) begin
    number arr[5] <- [156,6546,795,29,1]
    number i <- 0
    for i until i < 5 by 1
        if (a[i] != arr[i]) break
    writeString("End.")
end
func main() begin
    compare([1,2,4,5,6])
    
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_check_39(self):
        input = \
"""func compare(number a[5]) begin
    number arr[5] <- [156,6546,795,29,1]
    number i <- 0
    for i until i < 5 by 1
        if (a[i] != arr[i]) break
    writeString("End.")
end
func main() begin
    compare([1,2,4,5,6,7])
    
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))

    def test_0(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 500))
    def test_1(self):
        input = """
        func main() begin
        var f <- g
        end
        """
        expect = "Undeclared Identifier: g"
        self.assertTrue(TestChecker.test(input, expect, 501))
    def test_2(self):
        input = """  
        func b()
        func main() return 
        number a <- b()
        number c<- 8
        func b() begin
        return 1+1
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))
    def test_3(self):
        input = """  
        func b()
        func main() return 
        bool bo <- true
        number a <- b()
        number c<- 8
        func b() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 503))
    def test_4(self):
        input = """  
        func d() begin
        return 10
        return 
        return "Aaaaa"
        end
        func main() begin
        end
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 504))
    def test_5(self):   
        input = """
            func fun() begin
                dynamic b
                dynamic c
                number a[2] <- [b,c]
                b <- "ahhh"
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), StringLit(ahhh))"
        self.assertTrue(TestChecker.test(input, expect, 505)) 
    def test_6(self):   
        input = """
            func fun() begin
                dynamic b
                dynamic c
                string a <- c
                b <- "a"
            end
            func main() begin 
               
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 506))    
    def test_7(self):
        input = """
            func fun() begin
                number a[3,2]
                return
                return a
            end
            func main() begin 
               
            end
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 507))  
    def test_8(self):
        input = """
            func main() begin
                var x <- [vari]
            end
        """
        expect = "Undeclared Identifier: vari"
        self.assertTrue(TestChecker.test(input, expect, 508)) 
    def test_9(self):
        input = """##
            func main() begin
                dynamic b
                var x <- [1,b]
                var y <- [1,b]
                b <- 10
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 509)) 
    def test_10(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                number a[2,2] <- [[x,2],[1,2]]
                x <- 10
            end
        """
        expect = ""
        
        self.assertTrue(TestChecker.test(input, expect, 510))
    def test_11(self):
        input = """
            func foo(number a[2,2]) return
            func main() begin
                dynamic x
                x <- [1]
            end
        """
        expect = ""
        
        self.assertTrue(TestChecker.test(input, expect, 511))
    def test_12(self):
        input = """##
            func foo(number a) return
            func main() begin
                dynamic x
                foo(x)
                x <- 1
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 512)) 
    def test_13(self):
        input = """##
            func f()
func main() begin
number a <- f() 
end
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 513))
    def test_14(self):
       input = """
func f()begin
end
func main() begin
f()
end
       """
       expect = ""
       self.assertTrue(TestChecker.test(input, expect, 514))
    def test_15(self):
        input = """
            dynamic x
            number a <- x
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 515))
    def test_16(self):
        input = """func main () return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 516))
    def test_17(self):
        input = """func main ()
        begin
        number a <- arr[i]
        end
        """
        expect = "Undeclared Identifier: arr"
        self.assertTrue(TestChecker.test(input, expect, 517))
    def test_18(self):
        input = """func main ()
        begin
        number i
        number arr[10,10]
        number a <- arr[i,2]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 518))
    def test_19(self):
        input = """
        func inc(number a) return a + 1
        func mai() begin
            begin
            begin
            return 1
            end
            end
            return "str"
        end
        func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(str))"
        self.assertTrue(TestChecker.test(input, expect, 519))
    def test_20(self):
        input = """
        func inc(number a) return a + 1
        func mai() begin
            begin
            begin
            return 1
            end
            end
            return 2
        end
        func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 520))
    def test_21(self):
        input = """
        func main() begin
            number i
            begin
            string i
            begin
            i <- "str"
            end
            end
            i <- 10
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 521))
    def test_22(self):
        input = """
        func main() begin
            number i
            number a
            dynamic c
            for i until c by 1 a<- 10
            c <- true
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 522))
    def test_23(self):
        input = """
        func inc(number a)
        func main() begin
        end
        """
        expect = "No Function Definition: inc"
        self.assertTrue(TestChecker.test(input, expect, 523))
    def test_24(self):
        input = """
        func inc(number a) return a + 1
        func main() begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 524))
    def test_25(self):
        input = """
        func inc(number a) begin
        number a <- b
        dynamic c <- b
        c <- 10
        end
        func main() begin
        end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 525))
    def test_26(self):
        input = """
        func inc(number a) return
        func main() begin
            var a <- 1
            inc(a)
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 526))
    def test_27(self):
        input = """
        func main() begin
            var a <- 1
            inc(a)
        end
        """
        expect = "Undeclared Function: inc"
        self.assertTrue(TestChecker.test(input, expect, 527))
    def test_28(self):
        input = """func inc(number a) return "a"
        func main() begin
            var a <- 1
            a <- inc(a)
        end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(inc), [Id(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 528))
    def test_29(self):
        input = """
        func inc(number a) return 1
        func main() begin
            var a <- 1
            a <- inc(a)
            if (a > 5) return a
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 529))
    
    def test_30(self):
        input = """
        func inc(number a) return 1
        func main() begin
            return 1
        end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 530))

    def test_100(self):
        input = """
            func swapNumbers(number a, number b)
            begin
                var temp <- a
                a <- b
                b <- temp
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 800))
    def test_101(self):
        input = """
            func swapNumbers(number a, number b)
            begin
                var temp <- a
                a <- b
                b <- temp
            end
            func foo()
            func main() return
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 801))
    def test_102(self):
        input = """
            func foo()
            func swapNumbers(number a, number b)
            begin
                var temp <- a
                a <- b
                b <- temp
                foo()
            end
            func foo() return 10
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(NumLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 802))
    def test_103(self):
        input = """
            func foo()
            func swapNumbers(number a, number b)
            begin
                var temp <- a
                a <- b
                b <- temp
                foo()
            end
            func foo() return
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 803))
    def test_104(self):
        input = """
            func swapNumbers(number a, number b)
            begin
                var temp <- a
                a <- b
                b <- temp
            end
            ## Main program
            func main()
            begin
                var x <- 5
                var y <- 10

                writeString("Before swapping: ")
                writeString("x = ")
                writeNumber(x)
                writeString(", y = ")
                writeNumber(y)
                writeString("\\n")

                ## Call the swapNumbers function to swap x and y
                swapNumbers(x, y)

                writeString("After swapping: ")
                writeString("x = ")
                writeNumber(x)
                writeString(", y = ")
                writeNumber(y)
                writeString("\\n")
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 804))
    def test_105(self):
        input = """func findChar(string inputString, string targetChar)
begin
    var found <- false
    var i <- 0

    ##Iterate through the string to find the target character
    for i until size(inputString) by 1
    begin
        if (inputString[i] == targetChar)
        begin
            found <- true
            break
        end
        i <- i + 1
    end

    ##Check if the target character was found
    if (found) begin
        writeString("Character ' ")
        writeChar(targetChar)
        writeString("' found in the string.")
        end
    else begin
        writeString("Character ' ")
        writeChar(targetChar)
        writeString("' not found in the string.")
    end
end

## Main program
func main()
begin
    var input <- readString()
    var target <- readString()  ##Character to find in the string

    ##Call the findChar function to search for the target character
    findChar(input, target)
end

        """
        expect = "Undeclared Function: size"
        self.assertTrue(TestChecker.test(input, expect, 805))
    def test_106(self):
        input = """
        func size(string s) return 10
        func findChar(string inputString, string targetChar)
begin
    var found <- false
    var i <- 0

    ##Iterate through the string to find the target character
    for i until size(inputString) by 1
    begin
        if (inputString[i] == targetChar)
        begin
            found <- true
            break
        end
        i <- i + 1
    end

    ##Check if the target character was found
    if (found) begin
        writeString("Character ' ")
        writeChar(targetChar)
        writeString("' found in the string.")
        end
    else begin
        writeString("Character ' ")
        writeChar(targetChar)
        writeString("' not found in the string.")
    end
end

## Main program
func main()
begin
    var input <- readString()
    var target <- readString()  ##Character to find in the string

    ##Call the findChar function to search for the target character
    findChar(input, target)
end

        """
        expect = "Type Mismatch In Statement: For(Id(i), CallExpr(Id(size), [Id(inputString)]), NumLit(1.0), Block([If((BinaryOp(==, ArrayCell(Id(inputString), [Id(i)]), Id(targetChar)), Block([AssignStmt(Id(found), BooleanLit(True)), Break])), [], None), AssignStmt(Id(i), BinaryOp(+, Id(i), NumLit(1.0)))]))"
        self.assertTrue(TestChecker.test(input, expect, 806))
    def test_107(self):
        input = """
        func size(string s[10]) return 10
        func findChar(string inputString[10], string targetChar)
begin
    var found <- false
    var i <- 0

    ##Iterate through the string to find the target character
    for i until i <= size(inputString) by 1
    begin
        if (inputString[i] == targetChar)
        begin
            found <- true
            break
        end
        i <- i + 1
    end

    ##Check if the target character was found
    if (found) begin
        writeString("Character ' ")
        writeString(targetChar)
        writeString("' found in the string.")
        end
    else begin
        writeString("Character ' ")
        writeString(targetChar)
        writeString("' not found in the string.")
    end
end

## Main program
func main()
begin
    var input <- readString()
    var target <- readString()  ##Character to find in the string

    ##Call the findChar function to search for the target character
    findChar(input, target)
end

        """
        expect = "Type Mismatch In Statement: CallStmt(Id(findChar), [Id(input), Id(target)])"
        self.assertTrue(TestChecker.test(input, expect, 807))
    def test_108(self):
        input = """func calculateSum(number numbers[100])
begin
    var sum <- 0

    ## Iterate through the array and add each element to the sum
    for i until i < size(numbers) by 1
    begin
        sum <- sum + numbers[i]
    end

    ## Return the sum
    return sum
end

## Main program
func main()
begin
    number myArray[5] <- [1, 2, 3, 4, 5]

    ## Call the calculateSum function to calculate the sum of elements in myArray
    var result <- calculateSum(myArray)

    ## Print the result
    writeString("The sum of all elements in the array is: ")
    writeNumber(result)
end

        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 808)) 
    def test_109(self):
        input = """
        func size(number numbers[100]) return 100
        func calculateSum(number numbers[100])
begin
    var sum <- 0
    number i <- 0
    ## Iterate through the array and add each element to the sum
    for i until i < size(numbers) by 1
    begin
        sum <- sum + numbers[i]
    end
    ## Return the sum
    return sum
end

## Main program
func main()
begin
    number myArray[5] <- [1, 2, 3, 4, 5]

    ## Call the calculateSum function to calculate the sum of elements in myArray
    var result <- calculateSum(myArray)

    ## Print the result
    writeString("The sum of all elements in the array is: ")
    writeNumber(result)
end

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 809)) 