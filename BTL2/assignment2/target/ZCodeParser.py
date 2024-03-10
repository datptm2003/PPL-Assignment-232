# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("\u0177\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3^\n\3\3\4\3\4\5\4b\n\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4h\n\4\3\5\3\5\5\5l\n\5\3\6\3\6\3\6\5\6q\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7y\n\7\3\7\3\7\3\7\5\7~\n\7\3\7\5\7")
        buf.write("\u0081\n\7\3\b\3\b\5\b\u0085\n\b\3\t\3\t\3\t\3\t\3\t\5")
        buf.write("\t\u008c\n\t\3\n\3\n\3\n\5\n\u0091\n\n\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\5\f\u0099\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00bc\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\23\3\23\5\23\u00c5\n\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\5\25\u00d3\n")
        buf.write("\25\3\26\3\26\5\26\u00d7\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u00de\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u00e5\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\5\31\u00ec\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u00f4\n\32\f\32\16\32\u00f7")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u00ff\n\33\f")
        buf.write("\33\16\33\u0102\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u010a\n\34\f\34\16\34\u010d\13\34\3\35\3\35\3\35\5")
        buf.write("\35\u0112\n\35\3\36\3\36\3\36\5\36\u0117\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0124")
        buf.write("\n\37\3 \3 \3!\3!\3!\3!\3!\5!\u012d\n!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\5#\u013f\n")
        buf.write("#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5%\u014d\n%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\5\'\u015b\n\'\3(\3")
        buf.write("(\5(\u015f\n(\3)\3)\3)\3)\5)\u0165\n)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\5*\u0171\n*\3*\3*\5*\u0175\n*\3*\2\5\62")
        buf.write("\64\66+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPR\2\7\3\2\f\16\3\2\31\32\3")
        buf.write("\2\"#\3\2$&\3\2\33!\2\u017c\2T\3\2\2\2\4]\3\2\2\2\6g\3")
        buf.write("\2\2\2\bk\3\2\2\2\np\3\2\2\2\f\u0080\3\2\2\2\16\u0084")
        buf.write("\3\2\2\2\20\u008b\3\2\2\2\22\u008d\3\2\2\2\24\u0092\3")
        buf.write("\2\2\2\26\u0094\3\2\2\2\30\u009d\3\2\2\2\32\u00a3\3\2")
        buf.write("\2\2\34\u00a9\3\2\2\2\36\u00ae\3\2\2\2 \u00bb\3\2\2\2")
        buf.write("\"\u00bd\3\2\2\2$\u00c4\3\2\2\2&\u00ca\3\2\2\2(\u00d2")
        buf.write("\3\2\2\2*\u00d6\3\2\2\2,\u00dd\3\2\2\2.\u00e4\3\2\2\2")
        buf.write("\60\u00eb\3\2\2\2\62\u00ed\3\2\2\2\64\u00f8\3\2\2\2\66")
        buf.write("\u0103\3\2\2\28\u0111\3\2\2\2:\u0116\3\2\2\2<\u0123\3")
        buf.write("\2\2\2>\u0125\3\2\2\2@\u0127\3\2\2\2B\u0131\3\2\2\2D\u013e")
        buf.write("\3\2\2\2F\u0140\3\2\2\2H\u014c\3\2\2\2J\u014e\3\2\2\2")
        buf.write("L\u015a\3\2\2\2N\u015e\3\2\2\2P\u0164\3\2\2\2R\u0174\3")
        buf.write("\2\2\2TU\5\b\5\2UV\5\4\3\2VW\7\2\2\3W\3\3\2\2\2XY\5\6")
        buf.write("\4\2YZ\5\b\5\2Z[\5\4\3\2[^\3\2\2\2\\^\5\6\4\2]X\3\2\2")
        buf.write("\2]\\\3\2\2\2^\5\3\2\2\2_b\5\f\7\2`b\5\32\16\2a_\3\2\2")
        buf.write("\2a`\3\2\2\2bc\3\2\2\2cd\7/\2\2de\5\b\5\2eh\3\2\2\2fh")
        buf.write("\5\26\f\2ga\3\2\2\2gf\3\2\2\2h\7\3\2\2\2il\5\n\6\2jl\3")
        buf.write("\2\2\2ki\3\2\2\2kj\3\2\2\2l\t\3\2\2\2mn\7/\2\2nq\5\n\6")
        buf.write("\2oq\7/\2\2pm\3\2\2\2po\3\2\2\2q\13\3\2\2\2rs\7\n\2\2")
        buf.write("st\7-\2\2tu\7\27\2\2u\u0081\5.\30\2vy\5\24\13\2wy\7\13")
        buf.write("\2\2xv\3\2\2\2xw\3\2\2\2yz\3\2\2\2z}\7-\2\2{|\7\27\2\2")
        buf.write("|~\5.\30\2}{\3\2\2\2}~\3\2\2\2~\u0081\3\2\2\2\177\u0081")
        buf.write("\5 \21\2\u0080r\3\2\2\2\u0080x\3\2\2\2\u0080\177\3\2\2")
        buf.write("\2\u0081\r\3\2\2\2\u0082\u0085\5\20\t\2\u0083\u0085\3")
        buf.write("\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085\17")
        buf.write("\3\2\2\2\u0086\u0087\5\22\n\2\u0087\u0088\7,\2\2\u0088")
        buf.write("\u0089\5\20\t\2\u0089\u008c\3\2\2\2\u008a\u008c\5\22\n")
        buf.write("\2\u008b\u0086\3\2\2\2\u008b\u008a\3\2\2\2\u008c\21\3")
        buf.write("\2\2\2\u008d\u0090\5\24\13\2\u008e\u0091\7-\2\2\u008f")
        buf.write("\u0091\5\"\22\2\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2")
        buf.write("\2\u0091\23\3\2\2\2\u0092\u0093\t\2\2\2\u0093\25\3\2\2")
        buf.write("\2\u0094\u0095\5\32\16\2\u0095\u0098\5\b\5\2\u0096\u0099")
        buf.write("\5\30\r\2\u0097\u0099\5L\'\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\7/\2\2")
        buf.write("\u009b\u009c\5\b\5\2\u009c\27\3\2\2\2\u009d\u009e\7\22")
        buf.write("\2\2\u009e\u009f\7/\2\2\u009f\u00a0\5\b\5\2\u00a0\u00a1")
        buf.write("\5N(\2\u00a1\u00a2\7\23\2\2\u00a2\31\3\2\2\2\u00a3\u00a4")
        buf.write("\7\4\2\2\u00a4\u00a5\7-\2\2\u00a5\u00a6\7*\2\2\u00a6\u00a7")
        buf.write("\5\16\b\2\u00a7\u00a8\7+\2\2\u00a8\33\3\2\2\2\u00a9\u00aa")
        buf.write("\7-\2\2\u00aa\u00ab\7*\2\2\u00ab\u00ac\5*\26\2\u00ac\u00ad")
        buf.write("\7+\2\2\u00ad\35\3\2\2\2\u00ae\u00af\7-\2\2\u00af\u00b0")
        buf.write("\7*\2\2\u00b0\u00b1\5*\26\2\u00b1\u00b2\7+\2\2\u00b2\37")
        buf.write("\3\2\2\2\u00b3\u00b4\5\24\13\2\u00b4\u00b5\5\"\22\2\u00b5")
        buf.write("\u00b6\7\27\2\2\u00b6\u00b7\5.\30\2\u00b7\u00bc\3\2\2")
        buf.write("\2\u00b8\u00b9\5\24\13\2\u00b9\u00ba\5\"\22\2\u00ba\u00bc")
        buf.write("\3\2\2\2\u00bb\u00b3\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bc")
        buf.write("!\3\2\2\2\u00bd\u00be\7-\2\2\u00be\u00bf\7(\2\2\u00bf")
        buf.write("\u00c0\5(\25\2\u00c0\u00c1\7)\2\2\u00c1#\3\2\2\2\u00c2")
        buf.write("\u00c5\7-\2\2\u00c3\u00c5\5\36\20\2\u00c4\u00c2\3\2\2")
        buf.write("\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7")
        buf.write("\7(\2\2\u00c7\u00c8\5,\27\2\u00c8\u00c9\7)\2\2\u00c9%")
        buf.write("\3\2\2\2\u00ca\u00cb\7(\2\2\u00cb\u00cc\5,\27\2\u00cc")
        buf.write("\u00cd\7)\2\2\u00cd\'\3\2\2\2\u00ce\u00cf\7\25\2\2\u00cf")
        buf.write("\u00d0\7,\2\2\u00d0\u00d3\5(\25\2\u00d1\u00d3\7\25\2\2")
        buf.write("\u00d2\u00ce\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3)\3\2\2")
        buf.write("\2\u00d4\u00d7\5,\27\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7+\3\2\2\2\u00d8\u00d9")
        buf.write("\5.\30\2\u00d9\u00da\7,\2\2\u00da\u00db\5,\27\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00de\5.\30\2\u00dd\u00d8\3\2\2\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00de-\3\2\2\2\u00df\u00e0\5\60\31")
        buf.write("\2\u00e0\u00e1\7\'\2\2\u00e1\u00e2\5\60\31\2\u00e2\u00e5")
        buf.write("\3\2\2\2\u00e3\u00e5\5\60\31\2\u00e4\u00df\3\2\2\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5/\3\2\2\2\u00e6\u00e7\5\62\32\2\u00e7")
        buf.write("\u00e8\5> \2\u00e8\u00e9\5\62\32\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00ec\5\62\32\2\u00eb\u00e6\3\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\61\3\2\2\2\u00ed\u00ee\b\32\1\2\u00ee\u00ef")
        buf.write("\5\64\33\2\u00ef\u00f5\3\2\2\2\u00f0\u00f1\f\4\2\2\u00f1")
        buf.write("\u00f2\t\3\2\2\u00f2\u00f4\5\64\33\2\u00f3\u00f0\3\2\2")
        buf.write("\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\63\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8\u00f9")
        buf.write("\b\33\1\2\u00f9\u00fa\5\66\34\2\u00fa\u0100\3\2\2\2\u00fb")
        buf.write("\u00fc\f\4\2\2\u00fc\u00fd\t\4\2\2\u00fd\u00ff\5\66\34")
        buf.write("\2\u00fe\u00fb\3\2\2\2\u00ff\u0102\3\2\2\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u0101\3\2\2\2\u0101\65\3\2\2\2\u0102\u0100")
        buf.write("\3\2\2\2\u0103\u0104\b\34\1\2\u0104\u0105\58\35\2\u0105")
        buf.write("\u010b\3\2\2\2\u0106\u0107\f\4\2\2\u0107\u0108\t\5\2\2")
        buf.write("\u0108\u010a\58\35\2\u0109\u0106\3\2\2\2\u010a\u010d\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\67")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\7\30\2\2\u010f")
        buf.write("\u0112\58\35\2\u0110\u0112\5:\36\2\u0111\u010e\3\2\2\2")
        buf.write("\u0111\u0110\3\2\2\2\u01129\3\2\2\2\u0113\u0114\7#\2\2")
        buf.write("\u0114\u0117\5:\36\2\u0115\u0117\5<\37\2\u0116\u0113\3")
        buf.write("\2\2\2\u0116\u0115\3\2\2\2\u0117;\3\2\2\2\u0118\u0119")
        buf.write("\7*\2\2\u0119\u011a\5.\30\2\u011a\u011b\7+\2\2\u011b\u0124")
        buf.write("\3\2\2\2\u011c\u0124\5&\24\2\u011d\u0124\5$\23\2\u011e")
        buf.write("\u0124\5\36\20\2\u011f\u0124\7-\2\2\u0120\u0124\7\24\2")
        buf.write("\2\u0121\u0124\7\25\2\2\u0122\u0124\7\26\2\2\u0123\u0118")
        buf.write("\3\2\2\2\u0123\u011c\3\2\2\2\u0123\u011d\3\2\2\2\u0123")
        buf.write("\u011e\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0120\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0123\u0122\3\2\2\2\u0124=\3\2\2")
        buf.write("\2\u0125\u0126\t\6\2\2\u0126?\3\2\2\2\u0127\u012c\7-\2")
        buf.write("\2\u0128\u0129\7(\2\2\u0129\u012a\5,\27\2\u012a\u012b")
        buf.write("\7)\2\2\u012b\u012d\3\2\2\2\u012c\u0128\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\7\27\2")
        buf.write("\2\u012f\u0130\5.\30\2\u0130A\3\2\2\2\u0131\u0132\7\17")
        buf.write("\2\2\u0132\u0133\7*\2\2\u0133\u0134\5.\30\2\u0134\u0135")
        buf.write("\7+\2\2\u0135\u0136\5\b\5\2\u0136\u0137\5R*\2\u0137\u0138")
        buf.write("\5D#\2\u0138\u0139\5H%\2\u0139C\3\2\2\2\u013a\u013b\5")
        buf.write("F$\2\u013b\u013c\5D#\2\u013c\u013f\3\2\2\2\u013d\u013f")
        buf.write("\3\2\2\2\u013e\u013a\3\2\2\2\u013e\u013d\3\2\2\2\u013f")
        buf.write("E\3\2\2\2\u0140\u0141\7\21\2\2\u0141\u0142\7*\2\2\u0142")
        buf.write("\u0143\5.\30\2\u0143\u0144\7+\2\2\u0144\u0145\5\b\5\2")
        buf.write("\u0145\u0146\5R*\2\u0146G\3\2\2\2\u0147\u0148\7\20\2\2")
        buf.write("\u0148\u0149\5\b\5\2\u0149\u014a\5R*\2\u014a\u014d\3\2")
        buf.write("\2\2\u014b\u014d\3\2\2\2\u014c\u0147\3\2\2\2\u014c\u014b")
        buf.write("\3\2\2\2\u014dI\3\2\2\2\u014e\u014f\7\5\2\2\u014f\u0150")
        buf.write("\7-\2\2\u0150\u0151\7\6\2\2\u0151\u0152\5.\30\2\u0152")
        buf.write("\u0153\7\7\2\2\u0153\u0154\5.\30\2\u0154\u0155\5\b\5\2")
        buf.write("\u0155\u0156\5R*\2\u0156K\3\2\2\2\u0157\u0158\7\3\2\2")
        buf.write("\u0158\u015b\5.\30\2\u0159\u015b\7\3\2\2\u015a\u0157\3")
        buf.write("\2\2\2\u015a\u0159\3\2\2\2\u015bM\3\2\2\2\u015c\u015f")
        buf.write("\5P)\2\u015d\u015f\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015d")
        buf.write("\3\2\2\2\u015fO\3\2\2\2\u0160\u0161\5R*\2\u0161\u0162")
        buf.write("\5P)\2\u0162\u0165\3\2\2\2\u0163\u0165\5R*\2\u0164\u0160")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165Q\3\2\2\2\u0166\u0175")
        buf.write("\5B\"\2\u0167\u0175\5J&\2\u0168\u0171\7\b\2\2\u0169\u0171")
        buf.write("\7\t\2\2\u016a\u0171\5\30\r\2\u016b\u0171\5\f\7\2\u016c")
        buf.write("\u0171\5 \21\2\u016d\u0171\5@!\2\u016e\u0171\5\34\17\2")
        buf.write("\u016f\u0171\5L\'\2\u0170\u0168\3\2\2\2\u0170\u0169\3")
        buf.write("\2\2\2\u0170\u016a\3\2\2\2\u0170\u016b\3\2\2\2\u0170\u016c")
        buf.write("\3\2\2\2\u0170\u016d\3\2\2\2\u0170\u016e\3\2\2\2\u0170")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\7/\2\2")
        buf.write("\u0173\u0175\5\b\5\2\u0174\u0166\3\2\2\2\u0174\u0167\3")
        buf.write("\2\2\2\u0174\u0170\3\2\2\2\u0175S\3\2\2\2#]agkpx}\u0080")
        buf.write("\u0084\u008b\u0090\u0098\u00bb\u00c4\u00d2\u00d6\u00dd")
        buf.write("\u00e4\u00eb\u00f5\u0100\u010b\u0111\u0116\u0123\u012c")
        buf.write("\u013e\u014c\u015a\u015e\u0164\u0170\u0174")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDclr" ):
                return visitor.visitDclr(self)
            else:
                return visitor.visitChildren(self)




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
                if token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                    self.state = 93
                    self.var_dclr()
                    pass
                elif token in [ZCodeParser.FUNC]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_prime" ):
                return visitor.visitNewline_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dclr" ):
                return visitor.visitVar_dclr(self)
            else:
                return visitor.visitChildren(self)




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
                if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                    self.state = 116
                    self.var_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
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
                if _la==ZCodeParser.ASSIGN:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = ZCodeParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_list)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.para_prime()
                pass
            elif token in [ZCodeParser.CLOSE_BRK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_prime" ):
                return visitor.visitPara_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_dclr" ):
                return visitor.visitPara_dclr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = ZCodeParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.BOOL_TYPE) | (1 << ZCodeParser.NUM_TYPE) | (1 << ZCodeParser.STR_TYPE))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_imp" ):
                return visitor.visitFunc_imp(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [ZCodeParser.BEGIN]:
                self.state = 148
                self.block()
                pass
            elif token in [ZCodeParser.RETURN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dclr" ):
                return visitor.visitFunc_dclr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_stmt" ):
                return visitor.visitFunc_call_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call_expr" ):
                return visitor.visitFunc_call_expr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_dclr" ):
                return visitor.visitArr_dclr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_acs" ):
                return visitor.visitArr_acs(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_elmt" ):
                return visitor.visitArr_elmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_prime" ):
                return visitor.visitNum_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = ZCodeParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr_list)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.expr_prime()
                pass
            elif token in [ZCodeParser.CLOSE_BRK]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_prime" ):
                return visitor.visitExpr_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = ZCodeParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr5)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(ZCodeParser.NOT)
                self.state = 269
                self.expr5()
                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.SUB, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = ZCodeParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expr6)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(ZCodeParser.SUB)
                self.state = 274
                self.expr6()
                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpr_type" ):
                return visitor.visitCmpr_type(self)
            else:
                return visitor.visitChildren(self)




    def cmpr_type(self):

        localctx = ZCodeParser.Cmpr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_cmpr_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL) | (1 << ZCodeParser.STR_EQUAL) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS) | (1 << ZCodeParser.GREATER) | (1 << ZCodeParser.LESS_EQUAL) | (1 << ZCodeParser.GREATER_EQUAL))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssgn_expr" ):
                return visitor.visitAssgn_expr(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==ZCodeParser.OPEN_IDX:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_prime" ):
                return visitor.visitElif_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt" ):
                return visitor.visitElif_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = ZCodeParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_list)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.stmt_prime()
                pass
            elif token in [ZCodeParser.END]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_prime" ):
                return visitor.visitStmt_prime(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.if_stmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.for_stmt()
                pass
            elif token in [ZCodeParser.RETURN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.BEGIN, ZCodeParser.ID]:
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
         




