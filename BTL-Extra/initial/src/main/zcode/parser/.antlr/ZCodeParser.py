# Generated from f://STUDY MATERIAL//HK232//NGUYEN LY NNLT//ASSIGNMENT//BTL-Extra//initial//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,49,373,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,92,8,1,1,2,1,2,
        3,2,96,8,2,1,2,1,2,1,2,1,2,3,2,102,8,2,1,3,1,3,3,3,106,8,3,1,4,1,
        4,1,4,3,4,111,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,119,8,5,1,5,1,5,1,
        5,3,5,124,8,5,1,5,3,5,127,8,5,1,6,1,6,3,6,131,8,6,1,7,1,7,1,7,1,
        7,1,7,3,7,138,8,7,1,8,1,8,1,8,3,8,143,8,8,1,9,1,9,1,10,1,10,1,10,
        1,10,3,10,151,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,186,
        8,15,1,16,1,16,1,16,1,16,1,16,1,17,1,17,3,17,195,8,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,209,8,19,
        1,20,1,20,3,20,213,8,20,1,21,1,21,1,21,1,21,1,21,3,21,220,8,21,1,
        22,1,22,1,22,1,22,1,22,3,22,227,8,22,1,23,1,23,1,23,1,23,1,23,3,
        23,234,8,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,242,8,24,10,24,12,
        24,245,9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,253,8,25,10,25,12,
        25,256,9,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,264,8,26,10,26,12,
        26,267,9,26,1,27,1,27,1,27,3,27,272,8,27,1,28,1,28,1,28,3,28,277,
        8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,
        290,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,3,31,299,8,31,1,31,1,
        31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,
        33,1,33,3,33,317,8,33,1,34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,
        35,1,35,1,35,1,35,3,35,331,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,1,36,1,37,1,37,1,37,3,37,345,8,37,1,38,1,38,3,38,349,8,38,
        1,39,1,39,1,39,1,39,3,39,355,8,39,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,3,40,367,8,40,1,40,1,40,3,40,371,8,40,1,40,0,
        3,48,50,52,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
        38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,
        0,5,1,0,10,12,1,0,23,24,1,0,32,33,1,0,34,36,1,0,25,31,378,0,82,1,
        0,0,0,2,91,1,0,0,0,4,101,1,0,0,0,6,105,1,0,0,0,8,110,1,0,0,0,10,
        126,1,0,0,0,12,130,1,0,0,0,14,137,1,0,0,0,16,139,1,0,0,0,18,144,
        1,0,0,0,20,146,1,0,0,0,22,155,1,0,0,0,24,161,1,0,0,0,26,167,1,0,
        0,0,28,172,1,0,0,0,30,185,1,0,0,0,32,187,1,0,0,0,34,194,1,0,0,0,
        36,200,1,0,0,0,38,208,1,0,0,0,40,212,1,0,0,0,42,219,1,0,0,0,44,226,
        1,0,0,0,46,233,1,0,0,0,48,235,1,0,0,0,50,246,1,0,0,0,52,257,1,0,
        0,0,54,271,1,0,0,0,56,276,1,0,0,0,58,289,1,0,0,0,60,291,1,0,0,0,
        62,293,1,0,0,0,64,303,1,0,0,0,66,316,1,0,0,0,68,318,1,0,0,0,70,330,
        1,0,0,0,72,332,1,0,0,0,74,344,1,0,0,0,76,348,1,0,0,0,78,354,1,0,
        0,0,80,370,1,0,0,0,82,83,3,6,3,0,83,84,3,2,1,0,84,85,5,0,0,1,85,
        1,1,0,0,0,86,87,3,4,2,0,87,88,3,6,3,0,88,89,3,2,1,0,89,92,1,0,0,
        0,90,92,3,4,2,0,91,86,1,0,0,0,91,90,1,0,0,0,92,3,1,0,0,0,93,96,3,
        10,5,0,94,96,3,24,12,0,95,93,1,0,0,0,95,94,1,0,0,0,96,97,1,0,0,0,
        97,98,5,45,0,0,98,99,3,6,3,0,99,102,1,0,0,0,100,102,3,20,10,0,101,
        95,1,0,0,0,101,100,1,0,0,0,102,5,1,0,0,0,103,106,3,8,4,0,104,106,
        1,0,0,0,105,103,1,0,0,0,105,104,1,0,0,0,106,7,1,0,0,0,107,108,5,
        45,0,0,108,111,3,8,4,0,109,111,5,45,0,0,110,107,1,0,0,0,110,109,
        1,0,0,0,111,9,1,0,0,0,112,113,5,8,0,0,113,114,5,43,0,0,114,115,5,
        21,0,0,115,127,3,44,22,0,116,119,3,18,9,0,117,119,5,9,0,0,118,116,
        1,0,0,0,118,117,1,0,0,0,119,120,1,0,0,0,120,123,5,43,0,0,121,122,
        5,21,0,0,122,124,3,44,22,0,123,121,1,0,0,0,123,124,1,0,0,0,124,127,
        1,0,0,0,125,127,3,30,15,0,126,112,1,0,0,0,126,118,1,0,0,0,126,125,
        1,0,0,0,127,11,1,0,0,0,128,131,3,14,7,0,129,131,1,0,0,0,130,128,
        1,0,0,0,130,129,1,0,0,0,131,13,1,0,0,0,132,133,3,16,8,0,133,134,
        5,42,0,0,134,135,3,14,7,0,135,138,1,0,0,0,136,138,3,16,8,0,137,132,
        1,0,0,0,137,136,1,0,0,0,138,15,1,0,0,0,139,142,3,18,9,0,140,143,
        5,43,0,0,141,143,3,32,16,0,142,140,1,0,0,0,142,141,1,0,0,0,143,17,
        1,0,0,0,144,145,7,0,0,0,145,19,1,0,0,0,146,147,3,24,12,0,147,150,
        3,6,3,0,148,151,3,22,11,0,149,151,3,74,37,0,150,148,1,0,0,0,150,
        149,1,0,0,0,151,152,1,0,0,0,152,153,5,45,0,0,153,154,3,6,3,0,154,
        21,1,0,0,0,155,156,5,16,0,0,156,157,5,45,0,0,157,158,3,6,3,0,158,
        159,3,76,38,0,159,160,5,17,0,0,160,23,1,0,0,0,161,162,5,2,0,0,162,
        163,5,43,0,0,163,164,5,40,0,0,164,165,3,12,6,0,165,166,5,41,0,0,
        166,25,1,0,0,0,167,168,5,43,0,0,168,169,5,40,0,0,169,170,3,40,20,
        0,170,171,5,41,0,0,171,27,1,0,0,0,172,173,5,43,0,0,173,174,5,40,
        0,0,174,175,3,40,20,0,175,176,5,41,0,0,176,29,1,0,0,0,177,178,3,
        18,9,0,178,179,3,32,16,0,179,180,5,21,0,0,180,181,3,44,22,0,181,
        186,1,0,0,0,182,183,3,18,9,0,183,184,3,32,16,0,184,186,1,0,0,0,185,
        177,1,0,0,0,185,182,1,0,0,0,186,31,1,0,0,0,187,188,5,43,0,0,188,
        189,5,38,0,0,189,190,3,38,19,0,190,191,5,39,0,0,191,33,1,0,0,0,192,
        195,5,43,0,0,193,195,3,28,14,0,194,192,1,0,0,0,194,193,1,0,0,0,195,
        196,1,0,0,0,196,197,5,38,0,0,197,198,3,42,21,0,198,199,5,39,0,0,
        199,35,1,0,0,0,200,201,5,38,0,0,201,202,3,42,21,0,202,203,5,39,0,
        0,203,37,1,0,0,0,204,205,5,19,0,0,205,206,5,42,0,0,206,209,3,38,
        19,0,207,209,5,19,0,0,208,204,1,0,0,0,208,207,1,0,0,0,209,39,1,0,
        0,0,210,213,3,42,21,0,211,213,1,0,0,0,212,210,1,0,0,0,212,211,1,
        0,0,0,213,41,1,0,0,0,214,215,3,44,22,0,215,216,5,42,0,0,216,217,
        3,42,21,0,217,220,1,0,0,0,218,220,3,44,22,0,219,214,1,0,0,0,219,
        218,1,0,0,0,220,43,1,0,0,0,221,222,3,46,23,0,222,223,5,37,0,0,223,
        224,3,46,23,0,224,227,1,0,0,0,225,227,3,46,23,0,226,221,1,0,0,0,
        226,225,1,0,0,0,227,45,1,0,0,0,228,229,3,48,24,0,229,230,3,60,30,
        0,230,231,3,48,24,0,231,234,1,0,0,0,232,234,3,48,24,0,233,228,1,
        0,0,0,233,232,1,0,0,0,234,47,1,0,0,0,235,236,6,24,-1,0,236,237,3,
        50,25,0,237,243,1,0,0,0,238,239,10,2,0,0,239,240,7,1,0,0,240,242,
        3,50,25,0,241,238,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,
        1,0,0,0,244,49,1,0,0,0,245,243,1,0,0,0,246,247,6,25,-1,0,247,248,
        3,52,26,0,248,254,1,0,0,0,249,250,10,2,0,0,250,251,7,2,0,0,251,253,
        3,52,26,0,252,249,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,
        1,0,0,0,255,51,1,0,0,0,256,254,1,0,0,0,257,258,6,26,-1,0,258,259,
        3,54,27,0,259,265,1,0,0,0,260,261,10,2,0,0,261,262,7,3,0,0,262,264,
        3,54,27,0,263,260,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,53,1,0,0,0,267,265,1,0,0,0,268,269,5,22,0,0,269,272,
        3,54,27,0,270,272,3,56,28,0,271,268,1,0,0,0,271,270,1,0,0,0,272,
        55,1,0,0,0,273,274,5,33,0,0,274,277,3,56,28,0,275,277,3,58,29,0,
        276,273,1,0,0,0,276,275,1,0,0,0,277,57,1,0,0,0,278,279,5,40,0,0,
        279,280,3,44,22,0,280,281,5,41,0,0,281,290,1,0,0,0,282,290,3,36,
        18,0,283,290,3,34,17,0,284,290,3,28,14,0,285,290,5,43,0,0,286,290,
        5,18,0,0,287,290,5,19,0,0,288,290,5,20,0,0,289,278,1,0,0,0,289,282,
        1,0,0,0,289,283,1,0,0,0,289,284,1,0,0,0,289,285,1,0,0,0,289,286,
        1,0,0,0,289,287,1,0,0,0,289,288,1,0,0,0,290,59,1,0,0,0,291,292,7,
        4,0,0,292,61,1,0,0,0,293,298,5,43,0,0,294,295,5,38,0,0,295,296,3,
        42,21,0,296,297,5,39,0,0,297,299,1,0,0,0,298,294,1,0,0,0,298,299,
        1,0,0,0,299,300,1,0,0,0,300,301,5,21,0,0,301,302,3,44,22,0,302,63,
        1,0,0,0,303,304,5,13,0,0,304,305,5,40,0,0,305,306,3,44,22,0,306,
        307,5,41,0,0,307,308,3,6,3,0,308,309,3,80,40,0,309,310,3,66,33,0,
        310,311,3,70,35,0,311,65,1,0,0,0,312,313,3,68,34,0,313,314,3,66,
        33,0,314,317,1,0,0,0,315,317,1,0,0,0,316,312,1,0,0,0,316,315,1,0,
        0,0,317,67,1,0,0,0,318,319,5,15,0,0,319,320,5,40,0,0,320,321,3,44,
        22,0,321,322,5,41,0,0,322,323,3,6,3,0,323,324,3,80,40,0,324,69,1,
        0,0,0,325,326,5,14,0,0,326,327,3,6,3,0,327,328,3,80,40,0,328,331,
        1,0,0,0,329,331,1,0,0,0,330,325,1,0,0,0,330,329,1,0,0,0,331,71,1,
        0,0,0,332,333,5,3,0,0,333,334,5,43,0,0,334,335,5,4,0,0,335,336,3,
        44,22,0,336,337,5,5,0,0,337,338,3,44,22,0,338,339,3,6,3,0,339,340,
        3,80,40,0,340,73,1,0,0,0,341,342,5,1,0,0,342,345,3,44,22,0,343,345,
        5,1,0,0,344,341,1,0,0,0,344,343,1,0,0,0,345,75,1,0,0,0,346,349,3,
        78,39,0,347,349,1,0,0,0,348,346,1,0,0,0,348,347,1,0,0,0,349,77,1,
        0,0,0,350,351,3,80,40,0,351,352,3,78,39,0,352,355,1,0,0,0,353,355,
        3,80,40,0,354,350,1,0,0,0,354,353,1,0,0,0,355,79,1,0,0,0,356,371,
        3,64,32,0,357,371,3,72,36,0,358,367,5,6,0,0,359,367,5,7,0,0,360,
        367,3,22,11,0,361,367,3,10,5,0,362,367,3,30,15,0,363,367,3,62,31,
        0,364,367,3,26,13,0,365,367,3,74,37,0,366,358,1,0,0,0,366,359,1,
        0,0,0,366,360,1,0,0,0,366,361,1,0,0,0,366,362,1,0,0,0,366,363,1,
        0,0,0,366,364,1,0,0,0,366,365,1,0,0,0,367,368,1,0,0,0,368,369,5,
        45,0,0,369,371,3,6,3,0,370,356,1,0,0,0,370,357,1,0,0,0,370,366,1,
        0,0,0,371,81,1,0,0,0,33,91,95,101,105,110,118,123,126,130,137,142,
        150,185,194,208,212,219,226,233,243,254,265,271,276,289,298,316,
        330,344,348,354,366,370
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'var'", "'dynamic'", 
                     "'bool'", "'number'", "'string'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'<-'", "'not'", "'and'", "'or'", "'='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'...'", "'['", "']'", 
                     "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "RETURN", "FUNC", "FOR", "UNTIL", "BY", 
                      "BREAK", "CONTINUE", "VAR", "DYNAMIC", "BOOL_TYPE", 
                      "NUM_TYPE", "STR_TYPE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "BOOL", "NUMBER", "STRING", "ASSIGN", "NOT", 
                      "AND", "OR", "EQUAL", "STR_EQUAL", "NOT_EQUAL", "LESS", 
                      "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "STR_CONCAT", "OPEN_IDX", "CLOSE_IDX", 
                      "OPEN_BRK", "CLOSE_BRK", "SEP", "ID", "COMMENT", "NEWLINE", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_dclr = 2
    RULE_newline_list = 3
    RULE_newline_prime = 4
    RULE_var_dclr = 5
    RULE_para_list = 6
    RULE_para_prime = 7
    RULE_para_dclr = 8
    RULE_var_type = 9
    RULE_func_imp = 10
    RULE_block = 11
    RULE_func_dclr = 12
    RULE_func_call_stmt = 13
    RULE_func_call_expr = 14
    RULE_arr_dclr = 15
    RULE_array = 16
    RULE_arr_acs = 17
    RULE_arr_elmt = 18
    RULE_num_prime = 19
    RULE_expr_list = 20
    RULE_expr_prime = 21
    RULE_expr = 22
    RULE_expr1 = 23
    RULE_expr2 = 24
    RULE_expr3 = 25
    RULE_expr4 = 26
    RULE_expr5 = 27
    RULE_expr6 = 28
    RULE_expr7 = 29
    RULE_cmpr_type = 30
    RULE_assgn_expr = 31
    RULE_if_stmt = 32
    RULE_elif_prime = 33
    RULE_elif_stmt = 34
    RULE_else_stmt = 35
    RULE_for_stmt = 36
    RULE_return_stmt = 37
    RULE_stmt_list = 38
    RULE_stmt_prime = 39
    RULE_stmt = 40

    ruleNames =  [ "program", "declaration", "dclr", "newline_list", "newline_prime", 
                   "var_dclr", "para_list", "para_prime", "para_dclr", "var_type", 
                   "func_imp", "block", "func_dclr", "func_call_stmt", "func_call_expr", 
                   "arr_dclr", "array", "arr_acs", "arr_elmt", "num_prime", 
                   "expr_list", "expr_prime", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "cmpr_type", 
                   "assgn_expr", "if_stmt", "elif_prime", "elif_stmt", "else_stmt", 
                   "for_stmt", "return_stmt", "stmt_list", "stmt_prime", 
                   "stmt" ]

    EOF = Token.EOF
    RETURN=1
    FUNC=2
    FOR=3
    UNTIL=4
    BY=5
    BREAK=6
    CONTINUE=7
    VAR=8
    DYNAMIC=9
    BOOL_TYPE=10
    NUM_TYPE=11
    STR_TYPE=12
    IF=13
    ELSE=14
    ELIF=15
    BEGIN=16
    END=17
    BOOL=18
    NUMBER=19
    STRING=20
    ASSIGN=21
    NOT=22
    AND=23
    OR=24
    EQUAL=25
    STR_EQUAL=26
    NOT_EQUAL=27
    LESS=28
    GREATER=29
    LESS_EQUAL=30
    GREATER_EQUAL=31
    ADD=32
    SUB=33
    MUL=34
    DIV=35
    MOD=36
    STR_CONCAT=37
    OPEN_IDX=38
    CLOSE_IDX=39
    OPEN_BRK=40
    CLOSE_BRK=41
    SEP=42
    ID=43
    COMMENT=44
    NEWLINE=45
    WS=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48
    ERROR_CHAR=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.newline_list()
            self.state = 83
            self.declaration()
            self.state = 84
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dclr(self):
            return self.getTypedRuleContext(ZCodeParser.DclrContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.dclr()
                self.state = 87
                self.newline_list()
                self.state = 88
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.dclr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def var_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Var_dclrContext,0)


        def func_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_dclrContext,0)


        def func_imp(self):
            return self.getTypedRuleContext(ZCodeParser.Func_impContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dclr




    def dclr(self):

        localctx = ZCodeParser.DclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dclr)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [8, 9, 10, 11, 12]:
                    self.state = 93
                    self.var_dclr()
                    pass
                elif token in [2]:
                    self.state = 94
                    self.func_dclr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                self.match(ZCodeParser.NEWLINE)
                self.state = 98
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.func_imp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_newline_list)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Newline_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_prime




    def newline_prime(self):

        localctx = ZCodeParser.Newline_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_newline_prime)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.match(ZCodeParser.NEWLINE)
                self.state = 108
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(ZCodeParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def arr_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_dclrContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_dclr




    def var_dclr(self):

        localctx = ZCodeParser.Var_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_dclr)
        self._la = 0 # Token type
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(ZCodeParser.VAR)
                self.state = 113
                self.match(ZCodeParser.ID)
                self.state = 114
                self.match(ZCodeParser.ASSIGN)
                self.state = 115
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 11, 12]:
                    self.state = 116
                    self.var_type()
                    pass
                elif token in [9]:
                    self.state = 117
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 120
                self.match(ZCodeParser.ID)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 121
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 122
                    self.expr()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.arr_dclr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Para_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para_list




    def para_list(self):

        localctx = ZCodeParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_list)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.para_prime()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Para_dclrContext,0)


        def SEP(self):
            return self.getToken(ZCodeParser.SEP, 0)

        def para_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Para_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para_prime




    def para_prime(self):

        localctx = ZCodeParser.Para_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para_prime)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.para_dclr()
                self.state = 133
                self.match(ZCodeParser.SEP)
                self.state = 134
                self.para_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.para_dclr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_para_dclr




    def para_dclr(self):

        localctx = ZCodeParser.Para_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.var_type()
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 140
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 141
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL_TYPE(self):
            return self.getToken(ZCodeParser.BOOL_TYPE, 0)

        def NUM_TYPE(self):
            return self.getToken(ZCodeParser.NUM_TYPE, 0)

        def STR_TYPE(self):
            return self.getToken(ZCodeParser.STR_TYPE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_type




    def var_type(self):

        localctx = ZCodeParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_impContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_dclrContext,0)


        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_imp




    def func_imp(self):

        localctx = ZCodeParser.Func_impContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.func_dclr()
            self.state = 147
            self.newline_list()
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.state = 148
                self.block()
                pass
            elif token in [1]:
                self.state = 149
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 152
            self.match(ZCodeParser.NEWLINE)
            self.state = 153
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_listContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block




    def block(self):

        localctx = ZCodeParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ZCodeParser.BEGIN)
            self.state = 156
            self.match(ZCodeParser.NEWLINE)
            self.state = 157
            self.newline_list()
            self.state = 158
            self.stmt_list()
            self.state = 159
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Para_listContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_dclr




    def func_dclr(self):

        localctx = ZCodeParser.Func_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZCodeParser.FUNC)
            self.state = 162
            self.match(ZCodeParser.ID)
            self.state = 163
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 164
            self.para_list()
            self.state = 165
            self.match(ZCodeParser.CLOSE_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_stmt




    def func_call_stmt(self):

        localctx = ZCodeParser.Func_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ZCodeParser.ID)
            self.state = 168
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 169
            self.expr_list()
            self.state = 170
            self.match(ZCodeParser.CLOSE_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call_expr




    def func_call_expr(self):

        localctx = ZCodeParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_call_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.ID)
            self.state = 173
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 174
            self.expr_list()
            self.state = 175
            self.match(ZCodeParser.CLOSE_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(ZCodeParser.Var_typeContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_dclr




    def arr_dclr(self):

        localctx = ZCodeParser.Arr_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr_dclr)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.var_type()
                self.state = 178
                self.array()
                self.state = 179
                self.match(ZCodeParser.ASSIGN)
                self.state = 180
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.var_type()
                self.state = 183
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def num_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Num_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.ID)
            self.state = 188
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 189
            self.num_prime()
            self.state = 190
            self.match(ZCodeParser.CLOSE_IDX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_acsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_acs




    def arr_acs(self):

        localctx = ZCodeParser.Arr_acsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arr_acs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 193
                self.func_call_expr()
                pass


            self.state = 196
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 197
            self.expr_prime()
            self.state = 198
            self.match(ZCodeParser.CLOSE_IDX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_elmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_elmt




    def arr_elmt(self):

        localctx = ZCodeParser.Arr_elmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arr_elmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 201
            self.expr_prime()
            self.state = 202
            self.match(ZCodeParser.CLOSE_IDX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def SEP(self):
            return self.getToken(ZCodeParser.SEP, 0)

        def num_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Num_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_num_prime




    def num_prime(self):

        localctx = ZCodeParser.Num_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_num_prime)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(ZCodeParser.NUMBER)
                self.state = 205
                self.match(ZCodeParser.SEP)
                self.state = 206
                self.num_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(ZCodeParser.NUMBER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_list




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_list)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 22, 33, 38, 40, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.expr_prime()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def SEP(self):
            return self.getToken(ZCodeParser.SEP, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_prime




    def expr_prime(self):

        localctx = ZCodeParser.Expr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_prime)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.expr()
                self.state = 215
                self.match(ZCodeParser.SEP)
                self.state = 216
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr1Context,i)


        def STR_CONCAT(self):
            return self.getToken(ZCodeParser.STR_CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.expr1()
                self.state = 222
                self.match(ZCodeParser.STR_CONCAT)
                self.state = 223
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr2Context,i)


        def cmpr_type(self):
            return self.getTypedRuleContext(ZCodeParser.Cmpr_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr1




    def expr1(self):

        localctx = ZCodeParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr1)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.expr2(0)
                self.state = 229
                self.cmpr_type()
                self.state = 230
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(ZCodeParser.Expr2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 243
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 238
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 239
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 240
                    self.expr3(0) 
                self.state = 245
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(ZCodeParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 254
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 249
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 250
                    _la = self._input.LA(1)
                    if not(_la==32 or _la==33):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 251
                    self.expr4(0) 
                self.state = 256
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(ZCodeParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 260
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 261
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 262
                    self.expr5() 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr5(self):
            return self.getTypedRuleContext(ZCodeParser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr5




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr5)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(ZCodeParser.NOT)
                self.state = 269
                self.expr5()
                pass
            elif token in [18, 19, 20, 33, 38, 40, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def expr6(self):
            return self.getTypedRuleContext(ZCodeParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(ZCodeParser.Expr7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr6




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(ZCodeParser.SUB)
                self.state = 274
                self.expr6()
                pass
            elif token in [18, 19, 20, 38, 40, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.expr7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def arr_elmt(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_elmtContext,0)


        def arr_acs(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_acsContext,0)


        def func_call_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_exprContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr7




    def expr7(self):

        localctx = ZCodeParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr7)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.match(ZCodeParser.OPEN_BRK)
                self.state = 279
                self.expr()
                self.state = 280
                self.match(ZCodeParser.CLOSE_BRK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.arr_elmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 283
                self.arr_acs()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.func_call_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 285
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 286
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 287
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 288
                self.match(ZCodeParser.STRING)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cmpr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LESS_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_EQUAL, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def GREATER_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_EQUAL, 0)

        def STR_EQUAL(self):
            return self.getToken(ZCodeParser.STR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_cmpr_type




    def cmpr_type(self):

        localctx = ZCodeParser.Cmpr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_cmpr_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4261412864) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assgn_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assgn_expr




    def assgn_expr(self):

        localctx = ZCodeParser.Assgn_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assgn_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(ZCodeParser.ID)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 294
                self.match(ZCodeParser.OPEN_IDX)
                self.state = 295
                self.expr_prime()
                self.state = 296
                self.match(ZCodeParser.CLOSE_IDX)


            self.state = 300
            self.match(ZCodeParser.ASSIGN)
            self.state = 301
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def elif_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_primeContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(ZCodeParser.IF)
            self.state = 304
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 305
            self.expr()
            self.state = 306
            self.match(ZCodeParser.CLOSE_BRK)
            self.state = 307
            self.newline_list()
            self.state = 308
            self.stmt()
            self.state = 309
            self.elif_prime()
            self.state = 310
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmtContext,0)


        def elif_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_prime




    def elif_prime(self):

        localctx = ZCodeParser.Elif_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_elif_prime)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.elif_stmt()
                self.state = 313
                self.elif_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt




    def elif_stmt(self):

        localctx = ZCodeParser.Elif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(ZCodeParser.ELIF)
            self.state = 319
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 320
            self.expr()
            self.state = 321
            self.match(ZCodeParser.CLOSE_BRK)
            self.state = 322
            self.newline_list()
            self.state = 323
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_stmt




    def else_stmt(self):

        localctx = ZCodeParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_else_stmt)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(ZCodeParser.ELSE)
                self.state = 326
                self.newline_list()
                self.state = 327
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(ZCodeParser.FOR)
            self.state = 333
            self.match(ZCodeParser.ID)
            self.state = 334
            self.match(ZCodeParser.UNTIL)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(ZCodeParser.BY)
            self.state = 337
            self.expr()
            self.state = 338
            self.newline_list()
            self.state = 339
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(ZCodeParser.RETURN)
                self.state = 342
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(ZCodeParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_list




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_list)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 6, 7, 8, 9, 10, 11, 12, 13, 16, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.stmt_prime()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_prime




    def stmt_prime(self):

        localctx = ZCodeParser.Stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_prime)
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.stmt()
                self.state = 351
                self.stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def block(self):
            return self.getTypedRuleContext(ZCodeParser.BlockContext,0)


        def var_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Var_dclrContext,0)


        def arr_dclr(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_dclrContext,0)


        def assgn_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Assgn_exprContext,0)


        def func_call_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Func_call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.if_stmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.for_stmt()
                pass
            elif token in [1, 6, 7, 8, 9, 10, 11, 12, 16, 43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 366
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 358
                    self.match(ZCodeParser.BREAK)
                    pass

                elif la_ == 2:
                    self.state = 359
                    self.match(ZCodeParser.CONTINUE)
                    pass

                elif la_ == 3:
                    self.state = 360
                    self.block()
                    pass

                elif la_ == 4:
                    self.state = 361
                    self.var_dclr()
                    pass

                elif la_ == 5:
                    self.state = 362
                    self.arr_dclr()
                    pass

                elif la_ == 6:
                    self.state = 363
                    self.assgn_expr()
                    pass

                elif la_ == 7:
                    self.state = 364
                    self.func_call_stmt()
                    pass

                elif la_ == 8:
                    self.state = 365
                    self.return_stmt()
                    pass


                self.state = 368
                self.match(ZCodeParser.NEWLINE)
                self.state = 369
                self.newline_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr2_sempred
        self._predicates[25] = self.expr3_sempred
        self._predicates[26] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




