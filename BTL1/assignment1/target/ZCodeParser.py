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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u01b3\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\5\3k\n\3\3\4\3\4\3\4\3\4\3\4\5\4r\n\4\3\5\3\5\5\5")
        buf.write("v\n\5\3\5\3\5\3\5\3\5\5\5|\n\5\3\6\3\6\5\6\u0080\n\6\3")
        buf.write("\7\3\7\3\7\5\7\u0085\n\7\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008d")
        buf.write("\n\b\3\b\3\b\3\b\5\b\u0092\n\b\3\b\5\b\u0095\n\b\3\t\3")
        buf.write("\t\5\t\u0099\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00a0\n\n\3\13")
        buf.write("\3\13\3\13\5\13\u00a5\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00af\n\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00cd\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\5")
        buf.write("\24\u00d6\n\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\5\25\u00e1\n\25\3\26\3\26\5\26\u00e5\n\26\3\27\3")
        buf.write("\27\5\27\u00e9\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u00f0")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5\32\u00fa")
        buf.write("\n\32\3\33\3\33\5\33\u00fe\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\5\34\u0105\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u010c")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0113\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\7\37\u011b\n\37\f\37\16\37\u011e")
        buf.write("\13\37\3 \3 \3 \3 \3 \3 \7 \u0126\n \f \16 \u0129\13 ")
        buf.write("\3!\3!\3!\3!\3!\3!\7!\u0131\n!\f!\16!\u0134\13!\3\"\3")
        buf.write("\"\3\"\5\"\u0139\n\"\3#\3#\3#\5#\u013e\n#\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u014e\n$\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u015c\n&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\5*\u0174\n*\3+\3+\3+\3+\5+\u017a\n+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\5-\u0188\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\5/\u0196\n/\3\60\3\60\5\60\u019a\n\60\3")
        buf.write("\61\3\61\3\61\3\61\5\61\u01a0\n\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62\u01ad\n\62\3")
        buf.write("\62\3\62\5\62\u01b1\n\62\3\62\2\5<>@\63\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`b\2\t\3\2\r\17\3\2\13\f\4\2\5\5..\3\2\32")
        buf.write("\33\3\2#$\3\2%\'\3\2\34\"\2\u01bc\2d\3\2\2\2\4j\3\2\2")
        buf.write("\2\6q\3\2\2\2\b{\3\2\2\2\n\177\3\2\2\2\f\u0084\3\2\2\2")
        buf.write("\16\u0094\3\2\2\2\20\u0098\3\2\2\2\22\u009f\3\2\2\2\24")
        buf.write("\u00a1\3\2\2\2\26\u00a6\3\2\2\2\30\u00a8\3\2\2\2\32\u00aa")
        buf.write("\3\2\2\2\34\u00b3\3\2\2\2\36\u00b9\3\2\2\2 \u00bf\3\2")
        buf.write("\2\2\"\u00cc\3\2\2\2$\u00ce\3\2\2\2&\u00d5\3\2\2\2(\u00e0")
        buf.write("\3\2\2\2*\u00e4\3\2\2\2,\u00e8\3\2\2\2.\u00ef\3\2\2\2")
        buf.write("\60\u00f1\3\2\2\2\62\u00f9\3\2\2\2\64\u00fd\3\2\2\2\66")
        buf.write("\u0104\3\2\2\28\u010b\3\2\2\2:\u0112\3\2\2\2<\u0114\3")
        buf.write("\2\2\2>\u011f\3\2\2\2@\u012a\3\2\2\2B\u0138\3\2\2\2D\u013d")
        buf.write("\3\2\2\2F\u014d\3\2\2\2H\u014f\3\2\2\2J\u015b\3\2\2\2")
        buf.write("L\u015d\3\2\2\2N\u0161\3\2\2\2P\u0168\3\2\2\2R\u0173\3")
        buf.write("\2\2\2T\u0179\3\2\2\2V\u017b\3\2\2\2X\u0187\3\2\2\2Z\u0189")
        buf.write("\3\2\2\2\\\u0195\3\2\2\2^\u0199\3\2\2\2`\u019f\3\2\2\2")
        buf.write("b\u01b0\3\2\2\2de\5\n\6\2ef\5\6\4\2fg\7\2\2\3g\3\3\2\2")
        buf.write("\2hk\5\6\4\2ik\3\2\2\2jh\3\2\2\2ji\3\2\2\2k\5\3\2\2\2")
        buf.write("lm\5\b\5\2mn\5\n\6\2no\5\6\4\2or\3\2\2\2pr\5\b\5\2ql\3")
        buf.write("\2\2\2qp\3\2\2\2r\7\3\2\2\2sv\5\16\b\2tv\5\36\20\2us\3")
        buf.write("\2\2\2ut\3\2\2\2vw\3\2\2\2wx\7\60\2\2xy\5\n\6\2y|\3\2")
        buf.write("\2\2z|\5\32\16\2{u\3\2\2\2{z\3\2\2\2|\t\3\2\2\2}\u0080")
        buf.write("\5\f\7\2~\u0080\3\2\2\2\177}\3\2\2\2\177~\3\2\2\2\u0080")
        buf.write("\13\3\2\2\2\u0081\u0082\7\60\2\2\u0082\u0085\5\f\7\2\u0083")
        buf.write("\u0085\7\60\2\2\u0084\u0081\3\2\2\2\u0084\u0083\3\2\2")
        buf.write("\2\u0085\r\3\2\2\2\u0086\u0087\7\13\2\2\u0087\u0088\7")
        buf.write(".\2\2\u0088\u0089\7\30\2\2\u0089\u0095\58\35\2\u008a\u008d")
        buf.write("\5\26\f\2\u008b\u008d\7\f\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0091\7.\2\2")
        buf.write("\u008f\u0090\7\30\2\2\u0090\u0092\58\35\2\u0091\u008f")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0095\3\2\2\2\u0093")
        buf.write("\u0095\5\"\22\2\u0094\u0086\3\2\2\2\u0094\u008c\3\2\2")
        buf.write("\2\u0094\u0093\3\2\2\2\u0095\17\3\2\2\2\u0096\u0099\5")
        buf.write("\22\n\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\21\3\2\2\2\u009a\u009b\5\24\13\2")
        buf.write("\u009b\u009c\7-\2\2\u009c\u009d\5\22\n\2\u009d\u00a0\3")
        buf.write("\2\2\2\u009e\u00a0\5\24\13\2\u009f\u009a\3\2\2\2\u009f")
        buf.write("\u009e\3\2\2\2\u00a0\23\3\2\2\2\u00a1\u00a4\5\26\f\2\u00a2")
        buf.write("\u00a5\7.\2\2\u00a3\u00a5\5$\23\2\u00a4\u00a2\3\2\2\2")
        buf.write("\u00a4\u00a3\3\2\2\2\u00a5\25\3\2\2\2\u00a6\u00a7\t\2")
        buf.write("\2\2\u00a7\27\3\2\2\2\u00a8\u00a9\t\3\2\2\u00a9\31\3\2")
        buf.write("\2\2\u00aa\u00ab\5\36\20\2\u00ab\u00ae\5\n\6\2\u00ac\u00af")
        buf.write("\5\34\17\2\u00ad\u00af\5\\/\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\7\60\2")
        buf.write("\2\u00b1\u00b2\5\n\6\2\u00b2\33\3\2\2\2\u00b3\u00b4\7")
        buf.write("\23\2\2\u00b4\u00b5\7\60\2\2\u00b5\u00b6\5\n\6\2\u00b6")
        buf.write("\u00b7\5^\60\2\u00b7\u00b8\7\24\2\2\u00b8\35\3\2\2\2\u00b9")
        buf.write("\u00ba\7\4\2\2\u00ba\u00bb\t\4\2\2\u00bb\u00bc\7+\2\2")
        buf.write("\u00bc\u00bd\5\20\t\2\u00bd\u00be\7,\2\2\u00be\37\3\2")
        buf.write("\2\2\u00bf\u00c0\t\4\2\2\u00c0\u00c1\7+\2\2\u00c1\u00c2")
        buf.write("\5\64\33\2\u00c2\u00c3\7,\2\2\u00c3!\3\2\2\2\u00c4\u00c5")
        buf.write("\5\26\f\2\u00c5\u00c6\5$\23\2\u00c6\u00c7\7\30\2\2\u00c7")
        buf.write("\u00c8\58\35\2\u00c8\u00cd\3\2\2\2\u00c9\u00ca\5\26\f")
        buf.write("\2\u00ca\u00cb\5$\23\2\u00cb\u00cd\3\2\2\2\u00cc\u00c4")
        buf.write("\3\2\2\2\u00cc\u00c9\3\2\2\2\u00cd#\3\2\2\2\u00ce\u00cf")
        buf.write("\7.\2\2\u00cf\u00d0\7)\2\2\u00d0\u00d1\5\62\32\2\u00d1")
        buf.write("\u00d2\7*\2\2\u00d2%\3\2\2\2\u00d3\u00d6\7.\2\2\u00d4")
        buf.write("\u00d6\5 \21\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7)\2\2\u00d8\u00d9\5")
        buf.write("\66\34\2\u00d9\u00da\7*\2\2\u00da\'\3\2\2\2\u00db\u00dc")
        buf.write("\5*\26\2\u00dc\u00dd\7-\2\2\u00dd\u00de\5(\25\2\u00de")
        buf.write("\u00e1\3\2\2\2\u00df\u00e1\5*\26\2\u00e0\u00db\3\2\2\2")
        buf.write("\u00e0\u00df\3\2\2\2\u00e1)\3\2\2\2\u00e2\u00e5\5\60\31")
        buf.write("\2\u00e3\u00e5\58\35\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5+\3\2\2\2\u00e6\u00e9\5.\30\2\u00e7\u00e9")
        buf.write("\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("-\3\2\2\2\u00ea\u00eb\5\60\31\2\u00eb\u00ec\7-\2\2\u00ec")
        buf.write("\u00ed\5.\30\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\5\60\31")
        buf.write("\2\u00ef\u00ea\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0/\3\2")
        buf.write("\2\2\u00f1\u00f2\7)\2\2\u00f2\u00f3\5\66\34\2\u00f3\u00f4")
        buf.write("\7*\2\2\u00f4\61\3\2\2\2\u00f5\u00f6\7\26\2\2\u00f6\u00f7")
        buf.write("\7-\2\2\u00f7\u00fa\5\62\32\2\u00f8\u00fa\7\26\2\2\u00f9")
        buf.write("\u00f5\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\63\3\2\2\2\u00fb")
        buf.write("\u00fe\5\66\34\2\u00fc\u00fe\3\2\2\2\u00fd\u00fb\3\2\2")
        buf.write("\2\u00fd\u00fc\3\2\2\2\u00fe\65\3\2\2\2\u00ff\u0100\5")
        buf.write("8\35\2\u0100\u0101\7-\2\2\u0101\u0102\5\66\34\2\u0102")
        buf.write("\u0105\3\2\2\2\u0103\u0105\58\35\2\u0104\u00ff\3\2\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105\67\3\2\2\2\u0106\u0107\5:\36")
        buf.write("\2\u0107\u0108\7(\2\2\u0108\u0109\5:\36\2\u0109\u010c")
        buf.write("\3\2\2\2\u010a\u010c\5:\36\2\u010b\u0106\3\2\2\2\u010b")
        buf.write("\u010a\3\2\2\2\u010c9\3\2\2\2\u010d\u010e\5<\37\2\u010e")
        buf.write("\u010f\5H%\2\u010f\u0110\5<\37\2\u0110\u0113\3\2\2\2\u0111")
        buf.write("\u0113\5<\37\2\u0112\u010d\3\2\2\2\u0112\u0111\3\2\2\2")
        buf.write("\u0113;\3\2\2\2\u0114\u0115\b\37\1\2\u0115\u0116\5> \2")
        buf.write("\u0116\u011c\3\2\2\2\u0117\u0118\f\4\2\2\u0118\u0119\t")
        buf.write("\5\2\2\u0119\u011b\5> \2\u011a\u0117\3\2\2\2\u011b\u011e")
        buf.write("\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("=\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\b \1\2\u0120")
        buf.write("\u0121\5@!\2\u0121\u0127\3\2\2\2\u0122\u0123\f\4\2\2\u0123")
        buf.write("\u0124\t\6\2\2\u0124\u0126\5@!\2\u0125\u0122\3\2\2\2\u0126")
        buf.write("\u0129\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128?\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\b!\1\2")
        buf.write("\u012b\u012c\5B\"\2\u012c\u0132\3\2\2\2\u012d\u012e\f")
        buf.write("\4\2\2\u012e\u012f\t\7\2\2\u012f\u0131\5B\"\2\u0130\u012d")
        buf.write("\3\2\2\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132")
        buf.write("\u0133\3\2\2\2\u0133A\3\2\2\2\u0134\u0132\3\2\2\2\u0135")
        buf.write("\u0136\7\31\2\2\u0136\u0139\5B\"\2\u0137\u0139\5D#\2\u0138")
        buf.write("\u0135\3\2\2\2\u0138\u0137\3\2\2\2\u0139C\3\2\2\2\u013a")
        buf.write("\u013b\7$\2\2\u013b\u013e\5D#\2\u013c\u013e\5F$\2\u013d")
        buf.write("\u013a\3\2\2\2\u013d\u013c\3\2\2\2\u013eE\3\2\2\2\u013f")
        buf.write("\u0140\7+\2\2\u0140\u0141\58\35\2\u0141\u0142\7,\2\2\u0142")
        buf.write("\u014e\3\2\2\2\u0143\u0144\7)\2\2\u0144\u0145\5(\25\2")
        buf.write("\u0145\u0146\7*\2\2\u0146\u014e\3\2\2\2\u0147\u014e\5")
        buf.write("&\24\2\u0148\u014e\5 \21\2\u0149\u014e\7.\2\2\u014a\u014e")
        buf.write("\7\25\2\2\u014b\u014e\7\26\2\2\u014c\u014e\7\27\2\2\u014d")
        buf.write("\u013f\3\2\2\2\u014d\u0143\3\2\2\2\u014d\u0147\3\2\2\2")
        buf.write("\u014d\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a\3")
        buf.write("\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014eG")
        buf.write("\3\2\2\2\u014f\u0150\t\b\2\2\u0150I\3\2\2\2\u0151\u0152")
        buf.write("\7+\2\2\u0152\u0153\5J&\2\u0153\u0154\7,\2\2\u0154\u015c")
        buf.write("\3\2\2\2\u0155\u015c\5&\24\2\u0156\u015c\5 \21\2\u0157")
        buf.write("\u015c\7.\2\2\u0158\u015c\7\25\2\2\u0159\u015c\7\26\2")
        buf.write("\2\u015a\u015c\7\27\2\2\u015b\u0151\3\2\2\2\u015b\u0155")
        buf.write("\3\2\2\2\u015b\u0156\3\2\2\2\u015b\u0157\3\2\2\2\u015b")
        buf.write("\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3\2\2\2")
        buf.write("\u015cK\3\2\2\2\u015d\u015e\7.\2\2\u015e\u015f\7\30\2")
        buf.write("\2\u015f\u0160\58\35\2\u0160M\3\2\2\2\u0161\u0162\7.\2")
        buf.write("\2\u0162\u0163\7)\2\2\u0163\u0164\5\66\34\2\u0164\u0165")
        buf.write("\7*\2\2\u0165\u0166\7\30\2\2\u0166\u0167\58\35\2\u0167")
        buf.write("O\3\2\2\2\u0168\u0169\7\20\2\2\u0169\u016a\7+\2\2\u016a")
        buf.write("\u016b\58\35\2\u016b\u016c\7,\2\2\u016c\u016d\5\n\6\2")
        buf.write("\u016d\u016e\5b\62\2\u016e\u016f\5R*\2\u016f\u0170\5X")
        buf.write("-\2\u0170Q\3\2\2\2\u0171\u0174\5T+\2\u0172\u0174\3\2\2")
        buf.write("\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174S\3\2")
        buf.write("\2\2\u0175\u0176\5V,\2\u0176\u0177\5T+\2\u0177\u017a\3")
        buf.write("\2\2\2\u0178\u017a\5V,\2\u0179\u0175\3\2\2\2\u0179\u0178")
        buf.write("\3\2\2\2\u017aU\3\2\2\2\u017b\u017c\7\22\2\2\u017c\u017d")
        buf.write("\7+\2\2\u017d\u017e\58\35\2\u017e\u017f\7,\2\2\u017f\u0180")
        buf.write("\5\n\6\2\u0180\u0181\5b\62\2\u0181W\3\2\2\2\u0182\u0183")
        buf.write("\7\21\2\2\u0183\u0184\5\n\6\2\u0184\u0185\5b\62\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0188\3\2\2\2\u0187\u0182\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188Y\3\2\2\2\u0189\u018a\7\6\2")
        buf.write("\2\u018a\u018b\7.\2\2\u018b\u018c\7\7\2\2\u018c\u018d")
        buf.write("\58\35\2\u018d\u018e\7\b\2\2\u018e\u018f\58\35\2\u018f")
        buf.write("\u0190\5\n\6\2\u0190\u0191\5b\62\2\u0191[\3\2\2\2\u0192")
        buf.write("\u0193\7\3\2\2\u0193\u0196\58\35\2\u0194\u0196\7\3\2\2")
        buf.write("\u0195\u0192\3\2\2\2\u0195\u0194\3\2\2\2\u0196]\3\2\2")
        buf.write("\2\u0197\u019a\5`\61\2\u0198\u019a\3\2\2\2\u0199\u0197")
        buf.write("\3\2\2\2\u0199\u0198\3\2\2\2\u019a_\3\2\2\2\u019b\u019c")
        buf.write("\5b\62\2\u019c\u019d\5`\61\2\u019d\u01a0\3\2\2\2\u019e")
        buf.write("\u01a0\5b\62\2\u019f\u019b\3\2\2\2\u019f\u019e\3\2\2\2")
        buf.write("\u01a0a\3\2\2\2\u01a1\u01b1\5P)\2\u01a2\u01b1\5Z.\2\u01a3")
        buf.write("\u01ad\7\t\2\2\u01a4\u01ad\7\n\2\2\u01a5\u01ad\5\34\17")
        buf.write("\2\u01a6\u01ad\5\16\b\2\u01a7\u01ad\5\"\22\2\u01a8\u01ad")
        buf.write("\5L\'\2\u01a9\u01ad\5N(\2\u01aa\u01ad\5 \21\2\u01ab\u01ad")
        buf.write("\5\\/\2\u01ac\u01a3\3\2\2\2\u01ac\u01a4\3\2\2\2\u01ac")
        buf.write("\u01a5\3\2\2\2\u01ac\u01a6\3\2\2\2\u01ac\u01a7\3\2\2\2")
        buf.write("\u01ac\u01a8\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ac\u01aa\3")
        buf.write("\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af")
        buf.write("\7\60\2\2\u01af\u01b1\5\n\6\2\u01b0\u01a1\3\2\2\2\u01b0")
        buf.write("\u01a2\3\2\2\2\u01b0\u01ac\3\2\2\2\u01b1c\3\2\2\2)jqu")
        buf.write("{\177\u0084\u008c\u0091\u0094\u0098\u009f\u00a4\u00ae")
        buf.write("\u00cc\u00d5\u00e0\u00e4\u00e8\u00ef\u00f9\u00fd\u0104")
        buf.write("\u010b\u0112\u011c\u0127\u0132\u0138\u013d\u014d\u015b")
        buf.write("\u0173\u0179\u0187\u0195\u0199\u019f\u01ac\u01b0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "'func'", "'main'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'var'", 
                     "'dynamic'", "'bool'", "'number'", "'string'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<-'", "'not'", "'and'", 
                     "'or'", "'='", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'+'", "'-'", "'*'", "'/'", "'%'", "'...'", 
                     "'['", "']'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "RETURN", "FUNC", "MAIN", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "VAR", "DYNAMIC", "BOOL_TYPE", 
                      "NUM_TYPE", "STR_TYPE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "BOOL", "NUMBER", "STRING", "ASSIGN", "NOT", 
                      "AND", "OR", "EQUAL", "STR_EQUAL", "NOT_EQUAL", "LESS", 
                      "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "ADD", "SUB", 
                      "MUL", "DIV", "MOD", "STR_CONCAT", "OPEN_IDX", "CLOSE_IDX", 
                      "OPEN_BRK", "CLOSE_BRK", "SEP", "ID", "COMMENT", "NEWLINE", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_dclr_list = 1
    RULE_declaration = 2
    RULE_dclr = 3
    RULE_newline_list = 4
    RULE_newline_prime = 5
    RULE_var_dclr = 6
    RULE_para_list = 7
    RULE_para_prime = 8
    RULE_para_dclr = 9
    RULE_var_type = 10
    RULE_imp_var = 11
    RULE_func_imp = 12
    RULE_block = 13
    RULE_func_dclr = 14
    RULE_func_call = 15
    RULE_arr_dclr = 16
    RULE_array = 17
    RULE_arr_acs = 18
    RULE_elmt_prime = 19
    RULE_elmt = 20
    RULE_arr_list = 21
    RULE_arr_prime = 22
    RULE_arr_elmt = 23
    RULE_num_prime = 24
    RULE_expr_list = 25
    RULE_expr_prime = 26
    RULE_expr = 27
    RULE_expr1 = 28
    RULE_expr2 = 29
    RULE_expr3 = 30
    RULE_expr4 = 31
    RULE_expr5 = 32
    RULE_expr6 = 33
    RULE_expr7 = 34
    RULE_cmpr_type = 35
    RULE_str_oprnd = 36
    RULE_assgn_expr = 37
    RULE_arr_assgn = 38
    RULE_if_stmt = 39
    RULE_elif_list = 40
    RULE_elif_prime = 41
    RULE_elif_stmt = 42
    RULE_else_stmt = 43
    RULE_for_stmt = 44
    RULE_return_stmt = 45
    RULE_stmt_list = 46
    RULE_stmt_prime = 47
    RULE_stmt = 48

    ruleNames =  [ "program", "dclr_list", "declaration", "dclr", "newline_list", 
                   "newline_prime", "var_dclr", "para_list", "para_prime", 
                   "para_dclr", "var_type", "imp_var", "func_imp", "block", 
                   "func_dclr", "func_call", "arr_dclr", "array", "arr_acs", 
                   "elmt_prime", "elmt", "arr_list", "arr_prime", "arr_elmt", 
                   "num_prime", "expr_list", "expr_prime", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "cmpr_type", "str_oprnd", "assgn_expr", "arr_assgn", 
                   "if_stmt", "elif_list", "elif_prime", "elif_stmt", "else_stmt", 
                   "for_stmt", "return_stmt", "stmt_list", "stmt_prime", 
                   "stmt" ]

    EOF = Token.EOF
    RETURN=1
    FUNC=2
    MAIN=3
    FOR=4
    UNTIL=5
    BY=6
    BREAK=7
    CONTINUE=8
    VAR=9
    DYNAMIC=10
    BOOL_TYPE=11
    NUM_TYPE=12
    STR_TYPE=13
    IF=14
    ELSE=15
    ELIF=16
    BEGIN=17
    END=18
    BOOL=19
    NUMBER=20
    STRING=21
    ASSIGN=22
    NOT=23
    AND=24
    OR=25
    EQUAL=26
    STR_EQUAL=27
    NOT_EQUAL=28
    LESS=29
    GREATER=30
    LESS_EQUAL=31
    GREATER_EQUAL=32
    ADD=33
    SUB=34
    MUL=35
    DIV=36
    MOD=37
    STR_CONCAT=38
    OPEN_IDX=39
    CLOSE_IDX=40
    OPEN_BRK=41
    CLOSE_BRK=42
    SEP=43
    ID=44
    COMMENT=45
    NEWLINE=46
    WS=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49
    ERROR_CHAR=50

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
            self.state = 98
            self.newline_list()
            self.state = 99
            self.declaration()
            self.state = 100
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dclr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dclr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDclr_list" ):
                return visitor.visitDclr_list(self)
            else:
                return visitor.visitChildren(self)




    def dclr_list(self):

        localctx = ZCodeParser.Dclr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dclr_list)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.FUNC, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.declaration()
                pass
            elif token in [ZCodeParser.EOF]:
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
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.dclr()
                self.state = 107
                self.newline_list()
                self.state = 108
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
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
        self.enterRule(localctx, 6, self.RULE_dclr)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                    self.state = 113
                    self.var_dclr()
                    pass
                elif token in [ZCodeParser.FUNC]:
                    self.state = 114
                    self.func_dclr()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 117
                self.match(ZCodeParser.NEWLINE)
                self.state = 118
                self.newline_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
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
        self.enterRule(localctx, 8, self.RULE_newline_list)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
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
        self.enterRule(localctx, 10, self.RULE_newline_prime)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(ZCodeParser.NEWLINE)
                self.state = 128
                self.newline_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
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
        self.enterRule(localctx, 12, self.RULE_var_dclr)
        self._la = 0 # Token type
        try:
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(ZCodeParser.VAR)
                self.state = 133
                self.match(ZCodeParser.ID)
                self.state = 134
                self.match(ZCodeParser.ASSIGN)
                self.state = 135
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                    self.state = 136
                    self.var_type()
                    pass
                elif token in [ZCodeParser.DYNAMIC]:
                    self.state = 137
                    self.match(ZCodeParser.DYNAMIC)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 140
                self.match(ZCodeParser.ID)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 141
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 142
                    self.expr()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
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
        self.enterRule(localctx, 14, self.RULE_para_list)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
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
        self.enterRule(localctx, 16, self.RULE_para_prime)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.para_dclr()
                self.state = 153
                self.match(ZCodeParser.SEP)
                self.state = 154
                self.para_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
        self.enterRule(localctx, 18, self.RULE_para_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.var_type()
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 161
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
        self.enterRule(localctx, 20, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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


    class Imp_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_imp_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImp_var" ):
                return visitor.visitImp_var(self)
            else:
                return visitor.visitChildren(self)




    def imp_var(self):

        localctx = ZCodeParser.Imp_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_imp_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
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
        self.enterRule(localctx, 24, self.RULE_func_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.func_dclr()
            self.state = 169
            self.newline_list()
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN]:
                self.state = 170
                self.block()
                pass
            elif token in [ZCodeParser.RETURN]:
                self.state = 171
                self.return_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 174
            self.match(ZCodeParser.NEWLINE)
            self.state = 175
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
        self.enterRule(localctx, 26, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ZCodeParser.BEGIN)
            self.state = 178
            self.match(ZCodeParser.NEWLINE)
            self.state = 179
            self.newline_list()
            self.state = 180
            self.stmt_list()
            self.state = 181
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

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def para_list(self):
            return self.getTypedRuleContext(ZCodeParser.Para_listContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def MAIN(self):
            return self.getToken(ZCodeParser.MAIN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_dclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dclr" ):
                return visitor.visitFunc_dclr(self)
            else:
                return visitor.visitChildren(self)




    def func_dclr(self):

        localctx = ZCodeParser.Func_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_dclr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ZCodeParser.FUNC)
            self.state = 184
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.MAIN or _la==ZCodeParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 185
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 186
            self.para_list()
            self.state = 187
            self.match(ZCodeParser.CLOSE_BRK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def expr_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_listContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def MAIN(self):
            return self.getToken(ZCodeParser.MAIN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = ZCodeParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.MAIN or _la==ZCodeParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 190
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 191
            self.expr_list()
            self.state = 192
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
        self.enterRule(localctx, 32, self.RULE_arr_dclr)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.var_type()
                self.state = 195
                self.array()
                self.state = 196
                self.match(ZCodeParser.ASSIGN)
                self.state = 197
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.var_type()
                self.state = 200
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
        self.enterRule(localctx, 34, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.ID)
            self.state = 205
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 206
            self.num_prime()
            self.state = 207
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

        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_acs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_acs" ):
                return visitor.visitArr_acs(self)
            else:
                return visitor.visitChildren(self)




    def arr_acs(self):

        localctx = ZCodeParser.Arr_acsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arr_acs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 209
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 210
                self.func_call()
                pass


            self.state = 213
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 214
            self.expr_prime()
            self.state = 215
            self.match(ZCodeParser.CLOSE_IDX)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elmt(self):
            return self.getTypedRuleContext(ZCodeParser.ElmtContext,0)


        def SEP(self):
            return self.getToken(ZCodeParser.SEP, 0)

        def elmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elmt_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elmt_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElmt_prime" ):
                return visitor.visitElmt_prime(self)
            else:
                return visitor.visitChildren(self)




    def elmt_prime(self):

        localctx = ZCodeParser.Elmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elmt_prime)
        try:
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.elmt()
                self.state = 218
                self.match(ZCodeParser.SEP)
                self.state = 219
                self.elmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.elmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_elmt(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_elmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElmt" ):
                return visitor.visitElmt(self)
            else:
                return visitor.visitChildren(self)




    def elmt(self):

        localctx = ZCodeParser.ElmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_elmt)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.arr_elmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_list" ):
                return visitor.visitArr_list(self)
            else:
                return visitor.visitChildren(self)




    def arr_list(self):

        localctx = ZCodeParser.Arr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_arr_list)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OPEN_IDX]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.arr_prime()
                pass
            elif token in [ZCodeParser.EOF]:
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


    class Arr_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_elmt(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_elmtContext,0)


        def SEP(self):
            return self.getToken(ZCodeParser.SEP, 0)

        def arr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_prime" ):
                return visitor.visitArr_prime(self)
            else:
                return visitor.visitChildren(self)




    def arr_prime(self):

        localctx = ZCodeParser.Arr_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_arr_prime)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.arr_elmt()
                self.state = 233
                self.match(ZCodeParser.SEP)
                self.state = 234
                self.arr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.arr_elmt()
                pass


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
        self.enterRule(localctx, 46, self.RULE_arr_elmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 240
            self.expr_prime()
            self.state = 241
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
        self.enterRule(localctx, 48, self.RULE_num_prime)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(ZCodeParser.NUMBER)
                self.state = 244
                self.match(ZCodeParser.SEP)
                self.state = 245
                self.num_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
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
        self.enterRule(localctx, 50, self.RULE_expr_list)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MAIN, ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
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
        self.enterRule(localctx, 52, self.RULE_expr_prime)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expr()
                self.state = 254
                self.match(ZCodeParser.SEP)
                self.state = 255
                self.expr_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
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
        self.enterRule(localctx, 54, self.RULE_expr)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.expr1()
                self.state = 261
                self.match(ZCodeParser.STR_CONCAT)
                self.state = 262
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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
        self.enterRule(localctx, 56, self.RULE_expr1)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.expr2(0)
                self.state = 268
                self.cmpr_type()
                self.state = 269
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 279
                    self.expr3(0) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD or _la==ZCodeParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.expr4(0) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 299
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 300
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 301
                    self.expr5() 
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 64, self.RULE_expr5)
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(ZCodeParser.NOT)
                self.state = 308
                self.expr5()
                pass
            elif token in [ZCodeParser.MAIN, ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.SUB, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
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
        self.enterRule(localctx, 66, self.RULE_expr6)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(ZCodeParser.SUB)
                self.state = 313
                self.expr6()
                pass
            elif token in [ZCodeParser.MAIN, ZCodeParser.BOOL, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.OPEN_IDX, ZCodeParser.OPEN_BRK, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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

        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def elmt_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elmt_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def arr_acs(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_acsContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


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
        self.enterRule(localctx, 68, self.RULE_expr7)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.match(ZCodeParser.OPEN_BRK)
                self.state = 318
                self.expr()
                self.state = 319
                self.match(ZCodeParser.CLOSE_BRK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(ZCodeParser.OPEN_IDX)
                self.state = 322
                self.elmt_prime()
                self.state = 323
                self.match(ZCodeParser.CLOSE_IDX)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 325
                self.arr_acs()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 326
                self.func_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 327
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 328
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 329
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 330
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
        self.enterRule(localctx, 70, self.RULE_cmpr_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
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


    class Str_oprndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRK(self):
            return self.getToken(ZCodeParser.OPEN_BRK, 0)

        def str_oprnd(self):
            return self.getTypedRuleContext(ZCodeParser.Str_oprndContext,0)


        def CLOSE_BRK(self):
            return self.getToken(ZCodeParser.CLOSE_BRK, 0)

        def arr_acs(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_acsContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_str_oprnd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_oprnd" ):
                return visitor.visitStr_oprnd(self)
            else:
                return visitor.visitChildren(self)




    def str_oprnd(self):

        localctx = ZCodeParser.Str_oprndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_str_oprnd)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.match(ZCodeParser.OPEN_BRK)
                self.state = 336
                self.str_oprnd()
                self.state = 337
                self.match(ZCodeParser.CLOSE_BRK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                self.arr_acs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 342
                self.match(ZCodeParser.BOOL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 343
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 344
                self.match(ZCodeParser.STRING)
                pass


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_assgn_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssgn_expr" ):
                return visitor.visitAssgn_expr(self)
            else:
                return visitor.visitChildren(self)




    def assgn_expr(self):

        localctx = ZCodeParser.Assgn_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assgn_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.ID)
            self.state = 348
            self.match(ZCodeParser.ASSIGN)

            self.state = 349
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_assgnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def OPEN_IDX(self):
            return self.getToken(ZCodeParser.OPEN_IDX, 0)

        def expr_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_primeContext,0)


        def CLOSE_IDX(self):
            return self.getToken(ZCodeParser.CLOSE_IDX, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arr_assgn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_assgn" ):
                return visitor.visitArr_assgn(self)
            else:
                return visitor.visitChildren(self)




    def arr_assgn(self):

        localctx = ZCodeParser.Arr_assgnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arr_assgn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(ZCodeParser.ID)
            self.state = 352
            self.match(ZCodeParser.OPEN_IDX)
            self.state = 353
            self.expr_prime()
            self.state = 354
            self.match(ZCodeParser.CLOSE_IDX)
            self.state = 355
            self.match(ZCodeParser.ASSIGN)
            self.state = 356
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


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


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
        self.enterRule(localctx, 78, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.IF)
            self.state = 359
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 360
            self.expr()
            self.state = 361
            self.match(ZCodeParser.CLOSE_BRK)
            self.state = 362
            self.newline_list()
            self.state = 363
            self.stmt()
            self.state = 364
            self.elif_list()
            self.state = 365
            self.else_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_prime(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_primeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_elif_list)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
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
        self.enterRule(localctx, 82, self.RULE_elif_prime)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.elif_stmt()
                self.state = 372
                self.elif_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.elif_stmt()
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
        self.enterRule(localctx, 84, self.RULE_elif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(ZCodeParser.ELIF)
            self.state = 378
            self.match(ZCodeParser.OPEN_BRK)
            self.state = 379
            self.expr()
            self.state = 380
            self.match(ZCodeParser.CLOSE_BRK)
            self.state = 381
            self.newline_list()
            self.state = 382
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
        self.enterRule(localctx, 86, self.RULE_else_stmt)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(ZCodeParser.ELSE)
                self.state = 385
                self.newline_list()
                self.state = 386
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
        self.enterRule(localctx, 88, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(ZCodeParser.FOR)
            self.state = 392
            self.match(ZCodeParser.ID)
            self.state = 393
            self.match(ZCodeParser.UNTIL)
            self.state = 394
            self.expr()
            self.state = 395
            self.match(ZCodeParser.BY)
            self.state = 396
            self.expr()
            self.state = 397
            self.newline_list()
            self.state = 398
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
        self.enterRule(localctx, 90, self.RULE_return_stmt)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.match(ZCodeParser.RETURN)
                self.state = 401
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
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
        self.enterRule(localctx, 92, self.RULE_stmt_list)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN, ZCodeParser.MAIN, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
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
        self.enterRule(localctx, 94, self.RULE_stmt_prime)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.stmt()
                self.state = 410
                self.stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
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


        def arr_assgn(self):
            return self.getTypedRuleContext(ZCodeParser.Arr_assgnContext,0)


        def func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Func_callContext,0)


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
        self.enterRule(localctx, 96, self.RULE_stmt)
        try:
            self.state = 430
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.if_stmt()
                pass
            elif token in [ZCodeParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.for_stmt()
                pass
            elif token in [ZCodeParser.RETURN, ZCodeParser.MAIN, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.BOOL_TYPE, ZCodeParser.NUM_TYPE, ZCodeParser.STR_TYPE, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 426
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 417
                    self.match(ZCodeParser.BREAK)
                    pass

                elif la_ == 2:
                    self.state = 418
                    self.match(ZCodeParser.CONTINUE)
                    pass

                elif la_ == 3:
                    self.state = 419
                    self.block()
                    pass

                elif la_ == 4:
                    self.state = 420
                    self.var_dclr()
                    pass

                elif la_ == 5:
                    self.state = 421
                    self.arr_dclr()
                    pass

                elif la_ == 6:
                    self.state = 422
                    self.assgn_expr()
                    pass

                elif la_ == 7:
                    self.state = 423
                    self.arr_assgn()
                    pass

                elif la_ == 8:
                    self.state = 424
                    self.func_call()
                    pass

                elif la_ == 9:
                    self.state = 425
                    self.return_stmt()
                    pass


                self.state = 428
                self.match(ZCodeParser.NEWLINE)
                self.state = 429
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
        self._predicates[29] = self.expr2_sempred
        self._predicates[30] = self.expr3_sempred
        self._predicates[31] = self.expr4_sempred
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
         




