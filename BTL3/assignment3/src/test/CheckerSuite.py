import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    checkTest = 399
    def test_check_00(self):
        input = \
"""number a
var x <- "Test"
func foo(number x) begin
    number b <- 0
    ## dynamic k
    return b
end
func main(bool a, number x) begin
    string a <- "abc"
    number b <- foo(x) - 6
    dynamic c
    dynamic d
    dynamic y
    number num <- d + c + b + x * y
    num <- "abc"
    ## bool e <- d
end
"""
        expect = ""
        CheckerSuite.checkTest += 1
        self.assertTrue(TestChecker.test(input, expect, CheckerSuite.checkTest))
