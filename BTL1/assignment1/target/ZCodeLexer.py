# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u019a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00de\n\24\3")
        buf.write("\25\6\25\u00e1\n\25\r\25\16\25\u00e2\3\25\5\25\u00e6\n")
        buf.write("\25\3\25\5\25\u00e9\n\25\3\26\3\26\7\26\u00ed\n\26\f\26")
        buf.write("\16\26\u00f0\13\26\3\26\3\26\3\26\5\26\u00f5\n\26\7\26")
        buf.write("\u00f7\n\26\f\26\16\26\u00fa\13\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\7\30\u0103\n\30\f\30\16\30\u0106\13\30")
        buf.write("\3\31\3\31\5\31\u010a\n\31\3\31\6\31\u010d\n\31\r\31\16")
        buf.write("\31\u010e\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\7\62\u0151")
        buf.write("\n\62\f\62\16\62\u0154\13\62\3\63\3\63\3\63\3\63\7\63")
        buf.write("\u015a\n\63\f\63\16\63\u015d\13\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\5\64\u0166\n\64\3\65\6\65\u0169\n\65\r")
        buf.write("\65\16\65\u016a\3\65\3\65\3\66\3\66\7\66\u0171\n\66\f")
        buf.write("\66\16\66\u0174\13\66\3\66\3\66\3\66\5\66\u0179\n\66\7")
        buf.write("\66\u017b\n\66\f\66\16\66\u017e\13\66\3\66\3\66\3\67\3")
        buf.write("\67\7\67\u0184\n\67\f\67\16\67\u0187\13\67\3\67\3\67\3")
        buf.write("\67\5\67\u018c\n\67\7\67\u018e\n\67\f\67\16\67\u0191\13")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\38\38\38\2\29\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\2/\2\61\2\63\2\65")
        buf.write("\2\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'")
        buf.write("W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64\3\2\13\7\2\f\f\17")
        buf.write("\17$$))^^\3\2\62;\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5\2\n\13\16\16")
        buf.write("\"\"\2\u01ab\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\3q\3\2\2\2\5x\3\2\2\2\7}\3\2\2\2\t\u0082\3\2\2\2\13")
        buf.write("\u0086\3\2\2\2\r\u008c\3\2\2\2\17\u008f\3\2\2\2\21\u0095")
        buf.write("\3\2\2\2\23\u009e\3\2\2\2\25\u00a2\3\2\2\2\27\u00aa\3")
        buf.write("\2\2\2\31\u00af\3\2\2\2\33\u00b6\3\2\2\2\35\u00bd\3\2")
        buf.write("\2\2\37\u00c0\3\2\2\2!\u00c5\3\2\2\2#\u00ca\3\2\2\2%\u00d0")
        buf.write("\3\2\2\2\'\u00dd\3\2\2\2)\u00e0\3\2\2\2+\u00ea\3\2\2\2")
        buf.write("-\u00fe\3\2\2\2/\u0100\3\2\2\2\61\u0107\3\2\2\2\63\u0110")
        buf.write("\3\2\2\2\65\u0113\3\2\2\2\67\u0116\3\2\2\29\u0119\3\2")
        buf.write("\2\2;\u011d\3\2\2\2=\u0121\3\2\2\2?\u0124\3\2\2\2A\u0126")
        buf.write("\3\2\2\2C\u0129\3\2\2\2E\u012c\3\2\2\2G\u012e\3\2\2\2")
        buf.write("I\u0130\3\2\2\2K\u0133\3\2\2\2M\u0136\3\2\2\2O\u0138\3")
        buf.write("\2\2\2Q\u013a\3\2\2\2S\u013c\3\2\2\2U\u013e\3\2\2\2W\u0140")
        buf.write("\3\2\2\2Y\u0144\3\2\2\2[\u0146\3\2\2\2]\u0148\3\2\2\2")
        buf.write("_\u014a\3\2\2\2a\u014c\3\2\2\2c\u014e\3\2\2\2e\u0155\3")
        buf.write("\2\2\2g\u0165\3\2\2\2i\u0168\3\2\2\2k\u016e\3\2\2\2m\u0181")
        buf.write("\3\2\2\2o\u0197\3\2\2\2qr\7t\2\2rs\7g\2\2st\7v\2\2tu\7")
        buf.write("w\2\2uv\7t\2\2vw\7p\2\2w\4\3\2\2\2xy\7h\2\2yz\7w\2\2z")
        buf.write("{\7p\2\2{|\7e\2\2|\6\3\2\2\2}~\7o\2\2~\177\7c\2\2\177")
        buf.write("\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081\b\3\2\2\2\u0082")
        buf.write("\u0083\7h\2\2\u0083\u0084\7q\2\2\u0084\u0085\7t\2\2\u0085")
        buf.write("\n\3\2\2\2\u0086\u0087\7w\2\2\u0087\u0088\7p\2\2\u0088")
        buf.write("\u0089\7v\2\2\u0089\u008a\7k\2\2\u008a\u008b\7n\2\2\u008b")
        buf.write("\f\3\2\2\2\u008c\u008d\7d\2\2\u008d\u008e\7{\2\2\u008e")
        buf.write("\16\3\2\2\2\u008f\u0090\7d\2\2\u0090\u0091\7t\2\2\u0091")
        buf.write("\u0092\7g\2\2\u0092\u0093\7c\2\2\u0093\u0094\7m\2\2\u0094")
        buf.write("\20\3\2\2\2\u0095\u0096\7e\2\2\u0096\u0097\7q\2\2\u0097")
        buf.write("\u0098\7p\2\2\u0098\u0099\7v\2\2\u0099\u009a\7k\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7w\2\2\u009c\u009d\7g\2\2\u009d")
        buf.write("\22\3\2\2\2\u009e\u009f\7x\2\2\u009f\u00a0\7c\2\2\u00a0")
        buf.write("\u00a1\7t\2\2\u00a1\24\3\2\2\2\u00a2\u00a3\7f\2\2\u00a3")
        buf.write("\u00a4\7{\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6\7c\2\2\u00a6")
        buf.write("\u00a7\7o\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7e\2\2\u00a9")
        buf.write("\26\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7q\2\2\u00ac")
        buf.write("\u00ad\7q\2\2\u00ad\u00ae\7n\2\2\u00ae\30\3\2\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\u00b1\7w\2\2\u00b1\u00b2\7o\2\2\u00b2")
        buf.write("\u00b3\7d\2\2\u00b3\u00b4\7g\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\32\3\2\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb")
        buf.write("\u00bc\7i\2\2\u00bc\34\3\2\2\2\u00bd\u00be\7k\2\2\u00be")
        buf.write("\u00bf\7h\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4\7g\2\2\u00c4")
        buf.write(" \3\2\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7n\2\2\u00c7")
        buf.write("\u00c8\7k\2\2\u00c8\u00c9\7h\2\2\u00c9\"\3\2\2\2\u00ca")
        buf.write("\u00cb\7d\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7i\2\2\u00cd")
        buf.write("\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf$\3\2\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7f\2\2\u00d3")
        buf.write("&\3\2\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\u00d7\7w\2\2\u00d7\u00de\7g\2\2\u00d8\u00d9\7h\2\2\u00d9")
        buf.write("\u00da\7c\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc")
        buf.write("\u00de\7g\2\2\u00dd\u00d4\3\2\2\2\u00dd\u00d8\3\2\2\2")
        buf.write("\u00de(\3\2\2\2\u00df\u00e1\5-\27\2\u00e0\u00df\3\2\2")
        buf.write("\2\u00e1\u00e2\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e5\3\2\2\2\u00e4\u00e6\5/\30\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3\2\2\2")
        buf.write("\u00e7\u00e9\5\61\31\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9*\3\2\2\2\u00ea\u00f8\7$\2\2\u00eb\u00ed")
        buf.write("\7)\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f4\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f1\u00f5\5\63\32\2\u00f2\u00f5")
        buf.write("\5\65\33\2\u00f3\u00f5\n\2\2\2\u00f4\u00f1\3\2\2\2\u00f4")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f7\3\2\2\2")
        buf.write("\u00f6\u00ee\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fb\u00fc\7$\2\2\u00fc\u00fd\b\26\2\2\u00fd")
        buf.write(",\3\2\2\2\u00fe\u00ff\t\3\2\2\u00ff.\3\2\2\2\u0100\u0104")
        buf.write("\7\60\2\2\u0101\u0103\5-\27\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\60\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0109\t\4")
        buf.write("\2\2\u0108\u010a\t\5\2\2\u0109\u0108\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u010d\5-\27\2\u010c")
        buf.write("\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\62\3\2\2\2\u0110\u0111\7^\2")
        buf.write("\2\u0111\u0112\t\6\2\2\u0112\64\3\2\2\2\u0113\u0114\7")
        buf.write(")\2\2\u0114\u0115\7$\2\2\u0115\66\3\2\2\2\u0116\u0117")
        buf.write("\7>\2\2\u0117\u0118\7/\2\2\u01188\3\2\2\2\u0119\u011a")
        buf.write("\7p\2\2\u011a\u011b\7q\2\2\u011b\u011c\7v\2\2\u011c:\3")
        buf.write("\2\2\2\u011d\u011e\7c\2\2\u011e\u011f\7p\2\2\u011f\u0120")
        buf.write("\7f\2\2\u0120<\3\2\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123>\3\2\2\2\u0124\u0125\7?\2\2\u0125@\3\2\2")
        buf.write("\2\u0126\u0127\7?\2\2\u0127\u0128\7?\2\2\u0128B\3\2\2")
        buf.write("\2\u0129\u012a\7#\2\2\u012a\u012b\7?\2\2\u012bD\3\2\2")
        buf.write("\2\u012c\u012d\7>\2\2\u012dF\3\2\2\2\u012e\u012f\7@\2")
        buf.write("\2\u012fH\3\2\2\2\u0130\u0131\7>\2\2\u0131\u0132\7?\2")
        buf.write("\2\u0132J\3\2\2\2\u0133\u0134\7@\2\2\u0134\u0135\7?\2")
        buf.write("\2\u0135L\3\2\2\2\u0136\u0137\7-\2\2\u0137N\3\2\2\2\u0138")
        buf.write("\u0139\7/\2\2\u0139P\3\2\2\2\u013a\u013b\7,\2\2\u013b")
        buf.write("R\3\2\2\2\u013c\u013d\7\61\2\2\u013dT\3\2\2\2\u013e\u013f")
        buf.write("\7\'\2\2\u013fV\3\2\2\2\u0140\u0141\7\60\2\2\u0141\u0142")
        buf.write("\7\60\2\2\u0142\u0143\7\60\2\2\u0143X\3\2\2\2\u0144\u0145")
        buf.write("\7]\2\2\u0145Z\3\2\2\2\u0146\u0147\7_\2\2\u0147\\\3\2")
        buf.write("\2\2\u0148\u0149\7*\2\2\u0149^\3\2\2\2\u014a\u014b\7+")
        buf.write("\2\2\u014b`\3\2\2\2\u014c\u014d\7.\2\2\u014db\3\2\2\2")
        buf.write("\u014e\u0152\t\7\2\2\u014f\u0151\t\b\2\2\u0150\u014f\3")
        buf.write("\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153d\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156")
        buf.write("\7%\2\2\u0156\u0157\7%\2\2\u0157\u015b\3\2\2\2\u0158\u015a")
        buf.write("\n\t\2\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2\u015b")
        buf.write("\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3\2\2\2")
        buf.write("\u015d\u015b\3\2\2\2\u015e\u015f\b\63\3\2\u015ff\3\2\2")
        buf.write("\2\u0160\u0166\t\t\2\2\u0161\u0162\7\17\2\2\u0162\u0163")
        buf.write("\7\f\2\2\u0163\u0164\3\2\2\2\u0164\u0166\b\64\4\2\u0165")
        buf.write("\u0160\3\2\2\2\u0165\u0161\3\2\2\2\u0166h\3\2\2\2\u0167")
        buf.write("\u0169\t\n\2\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3")
        buf.write("\2\2\2\u016c\u016d\b\65\3\2\u016dj\3\2\2\2\u016e\u017c")
        buf.write("\7$\2\2\u016f\u0171\7)\2\2\u0170\u016f\3\2\2\2\u0171\u0174")
        buf.write("\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0178\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0179\5\63\32")
        buf.write("\2\u0176\u0179\5\65\33\2\u0177\u0179\n\2\2\2\u0178\u0175")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u0172\3\2\2\2\u017b\u017e\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3")
        buf.write("\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\b\66\5\2\u0180")
        buf.write("l\3\2\2\2\u0181\u018f\7$\2\2\u0182\u0184\7)\2\2\u0183")
        buf.write("\u0182\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u018b\3\2\2\2\u0187\u0185\3")
        buf.write("\2\2\2\u0188\u018c\5\63\32\2\u0189\u018c\5\65\33\2\u018a")
        buf.write("\u018c\n\2\2\2\u018b\u0188\3\2\2\2\u018b\u0189\3\2\2\2")
        buf.write("\u018b\u018a\3\2\2\2\u018c\u018e\3\2\2\2\u018d\u0185\3")
        buf.write("\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190")
        buf.write("\3\2\2\2\u0190\u0192\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0193\7^\2\2\u0193\u0194\n\6\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\b\67\6\2\u0196n\3\2\2\2\u0197\u0198\13\2")
        buf.write("\2\2\u0198\u0199\b8\7\2\u0199p\3\2\2\2\27\2\u00dd\u00e2")
        buf.write("\u00e5\u00e8\u00ee\u00f4\u00f8\u0104\u0109\u010e\u0152")
        buf.write("\u015b\u0165\u016a\u0172\u0178\u017c\u0185\u018b\u018f")
        buf.write("\b\3\26\2\b\2\2\3\64\3\3\66\4\3\67\5\38\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    FUNC = 2
    MAIN = 3
    FOR = 4
    UNTIL = 5
    BY = 6
    BREAK = 7
    CONTINUE = 8
    VAR = 9
    DYNAMIC = 10
    BOOL_TYPE = 11
    NUM_TYPE = 12
    STR_TYPE = 13
    IF = 14
    ELSE = 15
    ELIF = 16
    BEGIN = 17
    END = 18
    BOOL = 19
    NUMBER = 20
    STRING = 21
    ASSIGN = 22
    NOT = 23
    AND = 24
    OR = 25
    EQUAL = 26
    STR_EQUAL = 27
    NOT_EQUAL = 28
    LESS = 29
    GREATER = 30
    LESS_EQUAL = 31
    GREATER_EQUAL = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    MOD = 37
    STR_CONCAT = 38
    OPEN_IDX = 39
    CLOSE_IDX = 40
    OPEN_BRK = 41
    CLOSE_BRK = 42
    SEP = 43
    ID = 44
    COMMENT = 45
    NEWLINE = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'func'", "'main'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'var'", "'dynamic'", "'bool'", "'number'", 
            "'string'", "'if'", "'else'", "'elif'", "'begin'", "'end'", 
            "'<-'", "'not'", "'and'", "'or'", "'='", "'=='", "'!='", "'<'", 
            "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'...'", 
            "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "FUNC", "MAIN", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "VAR", "DYNAMIC", "BOOL_TYPE", "NUM_TYPE", "STR_TYPE", "IF", 
            "ELSE", "ELIF", "BEGIN", "END", "BOOL", "NUMBER", "STRING", 
            "ASSIGN", "NOT", "AND", "OR", "EQUAL", "STR_EQUAL", "NOT_EQUAL", 
            "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "ADD", "SUB", 
            "MUL", "DIV", "MOD", "STR_CONCAT", "OPEN_IDX", "CLOSE_IDX", 
            "OPEN_BRK", "CLOSE_BRK", "SEP", "ID", "COMMENT", "NEWLINE", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "RETURN", "FUNC", "MAIN", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "VAR", "DYNAMIC", "BOOL_TYPE", "NUM_TYPE", 
                  "STR_TYPE", "IF", "ELSE", "ELIF", "BEGIN", "END", "BOOL", 
                  "NUMBER", "STRING", "DIGIT", "DEC_PART", "EXPO_PART", 
                  "ESC_SEQ", "DBL_QUOTES", "ASSIGN", "NOT", "AND", "OR", 
                  "EQUAL", "STR_EQUAL", "NOT_EQUAL", "LESS", "GREATER", 
                  "LESS_EQUAL", "GREATER_EQUAL", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "STR_CONCAT", "OPEN_IDX", "CLOSE_IDX", "OPEN_BRK", 
                  "CLOSE_BRK", "SEP", "ID", "COMMENT", "NEWLINE", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.STRING_action 
            actions[50] = self.NEWLINE_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = '\n'

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise UncloseString(self.text[1:].replace('\n', '').replace('\r', ''))

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


