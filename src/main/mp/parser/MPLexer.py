# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0259\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3")
        buf.write("J\3J\3K\3K\3L\3L\3M\3M\3N\6N\u01bb\nN\rN\16N\u01bc\3N")
        buf.write("\3N\3O\5O\u01c2\nO\3O\7O\u01c5\nO\fO\16O\u01c8\13O\3P")
        buf.write("\6P\u01cb\nP\rP\16P\u01cc\3Q\6Q\u01d0\nQ\rQ\16Q\u01d1")
        buf.write("\3Q\5Q\u01d5\nQ\3Q\7Q\u01d8\nQ\fQ\16Q\u01db\13Q\3Q\7Q")
        buf.write("\u01de\nQ\fQ\16Q\u01e1\13Q\3Q\3Q\5Q\u01e5\nQ\3Q\6Q\u01e8")
        buf.write("\nQ\rQ\16Q\u01e9\5Q\u01ec\nQ\3Q\7Q\u01ef\nQ\fQ\16Q\u01f2")
        buf.write("\13Q\3Q\5Q\u01f5\nQ\3Q\6Q\u01f8\nQ\rQ\16Q\u01f9\3Q\3Q")
        buf.write("\5Q\u01fe\nQ\3Q\6Q\u0201\nQ\rQ\16Q\u0202\5Q\u0205\nQ\5")
        buf.write("Q\u0207\nQ\3R\3R\3R\3R\7R\u020d\nR\fR\16R\u0210\13R\3")
        buf.write("R\3R\3R\3S\3S\5S\u0217\nS\3S\3S\3T\3T\5T\u021d\nT\3U\3")
        buf.write("U\3U\3U\7U\u0223\nU\fU\16U\u0226\13U\3U\3U\3U\3V\3V\7")
        buf.write("V\u022d\nV\fV\16V\u0230\13V\3V\3V\3W\3W\3W\3W\7W\u0238")
        buf.write("\nW\fW\16W\u023b\13W\3X\3X\3X\5X\u0240\nX\3X\7X\u0243")
        buf.write("\nX\fX\16X\u0246\13X\3X\3X\3Y\3Y\3Y\3Y\7Y\u024e\nY\fY")
        buf.write("\16Y\u0251\13Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\4\u0224\u022e\2[\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\u009b\64\u009d\65\u009f\66\u00a1\67\u00a38")
        buf.write("\u00a59\u00a7:\u00a9;\u00ab<\u00ad=\u00af>\u00b1?\u00b3")
        buf.write("@\3\2$\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHh")
        buf.write("h\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aa")
        buf.write("c|\n\2$$))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4\2\f\f\17")
        buf.write("\17\7\2\13\f\16\17$$))^^\2\u0259\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\3\u00b5\3\2\2\2\5\u00b7\3\2\2\2\7\u00b9\3\2\2\2\t\u00bb")
        buf.write("\3\2\2\2\13\u00bd\3\2\2\2\r\u00bf\3\2\2\2\17\u00c1\3\2")
        buf.write("\2\2\21\u00c3\3\2\2\2\23\u00c5\3\2\2\2\25\u00c8\3\2\2")
        buf.write("\2\27\u00ca\3\2\2\2\31\u00cc\3\2\2\2\33\u00cf\3\2\2\2")
        buf.write("\35\u00d1\3\2\2\2\37\u00d4\3\2\2\2!\u00d6\3\2\2\2#\u00d8")
        buf.write("\3\2\2\2%\u00da\3\2\2\2\'\u00dd\3\2\2\2)\u00e0\3\2\2\2")
        buf.write("+\u00e6\3\2\2\2-\u00ef\3\2\2\2/\u00f3\3\2\2\2\61\u00f6")
        buf.write("\3\2\2\2\63\u00fd\3\2\2\2\65\u0100\3\2\2\2\67\u0103\3")
        buf.write("\2\2\29\u0108\3\2\2\2;\u010d\3\2\2\2=\u0114\3\2\2\2?\u011a")
        buf.write("\3\2\2\2A\u0120\3\2\2\2C\u0124\3\2\2\2E\u012d\3\2\2\2")
        buf.write("G\u0137\3\2\2\2I\u013b\3\2\2\2K\u0140\3\2\2\2M\u0146\3")
        buf.write("\2\2\2O\u014c\3\2\2\2Q\u014f\3\2\2\2S\u0154\3\2\2\2U\u015c")
        buf.write("\3\2\2\2W\u0164\3\2\2\2Y\u016b\3\2\2\2[\u016f\3\2\2\2")
        buf.write("]\u0173\3\2\2\2_\u0176\3\2\2\2a\u017a\3\2\2\2c\u017e\3")
        buf.write("\2\2\2e\u0183\3\2\2\2g\u0185\3\2\2\2i\u0187\3\2\2\2k\u0189")
        buf.write("\3\2\2\2m\u018b\3\2\2\2o\u018d\3\2\2\2q\u018f\3\2\2\2")
        buf.write("s\u0191\3\2\2\2u\u0193\3\2\2\2w\u0195\3\2\2\2y\u0197\3")
        buf.write("\2\2\2{\u0199\3\2\2\2}\u019b\3\2\2\2\177\u019d\3\2\2\2")
        buf.write("\u0081\u019f\3\2\2\2\u0083\u01a1\3\2\2\2\u0085\u01a3\3")
        buf.write("\2\2\2\u0087\u01a5\3\2\2\2\u0089\u01a7\3\2\2\2\u008b\u01a9")
        buf.write("\3\2\2\2\u008d\u01ab\3\2\2\2\u008f\u01ad\3\2\2\2\u0091")
        buf.write("\u01af\3\2\2\2\u0093\u01b1\3\2\2\2\u0095\u01b3\3\2\2\2")
        buf.write("\u0097\u01b5\3\2\2\2\u0099\u01b7\3\2\2\2\u009b\u01ba\3")
        buf.write("\2\2\2\u009d\u01c1\3\2\2\2\u009f\u01ca\3\2\2\2\u00a1\u0206")
        buf.write("\3\2\2\2\u00a3\u0208\3\2\2\2\u00a5\u0216\3\2\2\2\u00a7")
        buf.write("\u021c\3\2\2\2\u00a9\u021e\3\2\2\2\u00ab\u022a\3\2\2\2")
        buf.write("\u00ad\u0233\3\2\2\2\u00af\u023c\3\2\2\2\u00b1\u0249\3")
        buf.write("\2\2\2\u00b3\u0256\3\2\2\2\u00b5\u00b6\7*\2\2\u00b6\4")
        buf.write("\3\2\2\2\u00b7\u00b8\7+\2\2\u00b8\6\3\2\2\2\u00b9\u00ba")
        buf.write("\7]\2\2\u00ba\b\3\2\2\2\u00bb\u00bc\7_\2\2\u00bc\n\3\2")
        buf.write("\2\2\u00bd\u00be\7=\2\2\u00be\f\3\2\2\2\u00bf\u00c0\7")
        buf.write(".\2\2\u00c0\16\3\2\2\2\u00c1\u00c2\7?\2\2\u00c2\20\3\2")
        buf.write("\2\2\u00c3\u00c4\7<\2\2\u00c4\22\3\2\2\2\u00c5\u00c6\7")
        buf.write("\60\2\2\u00c6\u00c7\7\60\2\2\u00c7\24\3\2\2\2\u00c8\u00c9")
        buf.write("\7-\2\2\u00c9\26\3\2\2\2\u00ca\u00cb\7,\2\2\u00cb\30\3")
        buf.write("\2\2\2\u00cc\u00cd\7>\2\2\u00cd\u00ce\7@\2\2\u00ce\32")
        buf.write("\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0\34\3\2\2\2\u00d1\u00d2")
        buf.write("\7>\2\2\u00d2\u00d3\7?\2\2\u00d3\36\3\2\2\2\u00d4\u00d5")
        buf.write("\7/\2\2\u00d5 \3\2\2\2\u00d6\u00d7\7\61\2\2\u00d7\"\3")
        buf.write("\2\2\2\u00d8\u00d9\7@\2\2\u00d9$\3\2\2\2\u00da\u00db\7")
        buf.write("@\2\2\u00db\u00dc\7?\2\2\u00dc&\3\2\2\2\u00dd\u00de\7")
        buf.write("<\2\2\u00de\u00df\7?\2\2\u00df(\3\2\2\2\u00e0\u00e1\5")
        buf.write("g\64\2\u00e1\u00e2\5\u0087D\2\u00e2\u00e3\5m\67\2\u00e3")
        buf.write("\u00e4\5e\63\2\u00e4\u00e5\5y=\2\u00e5*\3\2\2\2\u00e6")
        buf.write("\u00e7\5i\65\2\u00e7\u00e8\5\u0081A\2\u00e8\u00e9\5\177")
        buf.write("@\2\u00e9\u00ea\5\u008bF\2\u00ea\u00eb\5u;\2\u00eb\u00ec")
        buf.write("\5\177@\2\u00ec\u00ed\5\u008dG\2\u00ed\u00ee\5m\67\2\u00ee")
        buf.write(",\3\2\2\2\u00ef\u00f0\5o8\2\u00f0\u00f1\5\u0081A\2\u00f1")
        buf.write("\u00f2\5\u0087D\2\u00f2.\3\2\2\2\u00f3\u00f4\5\u008bF")
        buf.write("\2\u00f4\u00f5\5\u0081A\2\u00f5\60\3\2\2\2\u00f6\u00f7")
        buf.write("\5k\66\2\u00f7\u00f8\5\u0081A\2\u00f8\u00f9\5\u0091I\2")
        buf.write("\u00f9\u00fa\5\177@\2\u00fa\u00fb\5\u008bF\2\u00fb\u00fc")
        buf.write("\5\u0081A\2\u00fc\62\3\2\2\2\u00fd\u00fe\5k\66\2\u00fe")
        buf.write("\u00ff\5\u0081A\2\u00ff\64\3\2\2\2\u0100\u0101\5u;\2\u0101")
        buf.write("\u0102\5o8\2\u0102\66\3\2\2\2\u0103\u0104\5\u008bF\2\u0104")
        buf.write("\u0105\5s:\2\u0105\u0106\5m\67\2\u0106\u0107\5\177@\2")
        buf.write("\u01078\3\2\2\2\u0108\u0109\5m\67\2\u0109\u010a\5{>\2")
        buf.write("\u010a\u010b\5\u0089E\2\u010b\u010c\5m\67\2\u010c:\3\2")
        buf.write("\2\2\u010d\u010e\5\u0087D\2\u010e\u010f\5m\67\2\u010f")
        buf.write("\u0110\5\u008bF\2\u0110\u0111\5\u008dG\2\u0111\u0112\5")
        buf.write("\u0087D\2\u0112\u0113\5\177@\2\u0113<\3\2\2\2\u0114\u0115")
        buf.write("\5\u0091I\2\u0115\u0116\5s:\2\u0116\u0117\5u;\2\u0117")
        buf.write("\u0118\5{>\2\u0118\u0119\5m\67\2\u0119>\3\2\2\2\u011a")
        buf.write("\u011b\5g\64\2\u011b\u011c\5m\67\2\u011c\u011d\5q9\2\u011d")
        buf.write("\u011e\5u;\2\u011e\u011f\5\177@\2\u011f@\3\2\2\2\u0120")
        buf.write("\u0121\5m\67\2\u0121\u0122\5\177@\2\u0122\u0123\5k\66")
        buf.write("\2\u0123B\3\2\2\2\u0124\u0125\5o8\2\u0125\u0126\5\u008d")
        buf.write("G\2\u0126\u0127\5\177@\2\u0127\u0128\5i\65\2\u0128\u0129")
        buf.write("\5\u008bF\2\u0129\u012a\5u;\2\u012a\u012b\5\u0081A\2\u012b")
        buf.write("\u012c\5\177@\2\u012cD\3\2\2\2\u012d\u012e\5\u0083B\2")
        buf.write("\u012e\u012f\5\u0087D\2\u012f\u0130\5\u0081A\2\u0130\u0131")
        buf.write("\5i\65\2\u0131\u0132\5m\67\2\u0132\u0133\5k\66\2\u0133")
        buf.write("\u0134\5\u008dG\2\u0134\u0135\5\u0087D\2\u0135\u0136\5")
        buf.write("m\67\2\u0136F\3\2\2\2\u0137\u0138\5\u008fH\2\u0138\u0139")
        buf.write("\5e\63\2\u0139\u013a\5\u0087D\2\u013aH\3\2\2\2\u013b\u013c")
        buf.write("\5\u008bF\2\u013c\u013d\5\u0087D\2\u013d\u013e\5\u008d")
        buf.write("G\2\u013e\u013f\5m\67\2\u013fJ\3\2\2\2\u0140\u0141\5o")
        buf.write("8\2\u0141\u0142\5e\63\2\u0142\u0143\5{>\2\u0143\u0144")
        buf.write("\5\u0089E\2\u0144\u0145\5m\67\2\u0145L\3\2\2\2\u0146\u0147")
        buf.write("\5e\63\2\u0147\u0148\5\u0087D\2\u0148\u0149\5\u0087D\2")
        buf.write("\u0149\u014a\5e\63\2\u014a\u014b\5\u0095K\2\u014bN\3\2")
        buf.write("\2\2\u014c\u014d\5\u0081A\2\u014d\u014e\5o8\2\u014eP\3")
        buf.write("\2\2\2\u014f\u0150\5\u0087D\2\u0150\u0151\5m\67\2\u0151")
        buf.write("\u0152\5e\63\2\u0152\u0153\5{>\2\u0153R\3\2\2\2\u0154")
        buf.write("\u0155\5g\64\2\u0155\u0156\5\u0081A\2\u0156\u0157\5\u0081")
        buf.write("A\2\u0157\u0158\5{>\2\u0158\u0159\5m\67\2\u0159\u015a")
        buf.write("\5e\63\2\u015a\u015b\5\177@\2\u015bT\3\2\2\2\u015c\u015d")
        buf.write("\5u;\2\u015d\u015e\5\177@\2\u015e\u015f\5\u008bF\2\u015f")
        buf.write("\u0160\5m\67\2\u0160\u0161\5q9\2\u0161\u0162\5m\67\2\u0162")
        buf.write("\u0163\5\u0087D\2\u0163V\3\2\2\2\u0164\u0165\5\u0089E")
        buf.write("\2\u0165\u0166\5\u008bF\2\u0166\u0167\5\u0087D\2\u0167")
        buf.write("\u0168\5u;\2\u0168\u0169\5\177@\2\u0169\u016a\5q9\2\u016a")
        buf.write("X\3\2\2\2\u016b\u016c\5\177@\2\u016c\u016d\5\u0081A\2")
        buf.write("\u016d\u016e\5\u008bF\2\u016eZ\3\2\2\2\u016f\u0170\5e")
        buf.write("\63\2\u0170\u0171\5\177@\2\u0171\u0172\5k\66\2\u0172\\")
        buf.write("\3\2\2\2\u0173\u0174\5\u0081A\2\u0174\u0175\5\u0087D\2")
        buf.write("\u0175^\3\2\2\2\u0176\u0177\5k\66\2\u0177\u0178\5u;\2")
        buf.write("\u0178\u0179\5\u008fH\2\u0179`\3\2\2\2\u017a\u017b\5}")
        buf.write("?\2\u017b\u017c\5\u0081A\2\u017c\u017d\5k\66\2\u017db")
        buf.write("\3\2\2\2\u017e\u017f\5\u0091I\2\u017f\u0180\5u;\2\u0180")
        buf.write("\u0181\5\u008bF\2\u0181\u0182\5s:\2\u0182d\3\2\2\2\u0183")
        buf.write("\u0184\t\2\2\2\u0184f\3\2\2\2\u0185\u0186\t\3\2\2\u0186")
        buf.write("h\3\2\2\2\u0187\u0188\t\4\2\2\u0188j\3\2\2\2\u0189\u018a")
        buf.write("\t\5\2\2\u018al\3\2\2\2\u018b\u018c\t\6\2\2\u018cn\3\2")
        buf.write("\2\2\u018d\u018e\t\7\2\2\u018ep\3\2\2\2\u018f\u0190\t")
        buf.write("\b\2\2\u0190r\3\2\2\2\u0191\u0192\t\t\2\2\u0192t\3\2\2")
        buf.write("\2\u0193\u0194\t\n\2\2\u0194v\3\2\2\2\u0195\u0196\t\13")
        buf.write("\2\2\u0196x\3\2\2\2\u0197\u0198\t\f\2\2\u0198z\3\2\2\2")
        buf.write("\u0199\u019a\t\r\2\2\u019a|\3\2\2\2\u019b\u019c\t\16\2")
        buf.write("\2\u019c~\3\2\2\2\u019d\u019e\t\17\2\2\u019e\u0080\3\2")
        buf.write("\2\2\u019f\u01a0\t\20\2\2\u01a0\u0082\3\2\2\2\u01a1\u01a2")
        buf.write("\t\21\2\2\u01a2\u0084\3\2\2\2\u01a3\u01a4\t\22\2\2\u01a4")
        buf.write("\u0086\3\2\2\2\u01a5\u01a6\t\23\2\2\u01a6\u0088\3\2\2")
        buf.write("\2\u01a7\u01a8\t\24\2\2\u01a8\u008a\3\2\2\2\u01a9\u01aa")
        buf.write("\t\25\2\2\u01aa\u008c\3\2\2\2\u01ab\u01ac\t\26\2\2\u01ac")
        buf.write("\u008e\3\2\2\2\u01ad\u01ae\t\27\2\2\u01ae\u0090\3\2\2")
        buf.write("\2\u01af\u01b0\t\30\2\2\u01b0\u0092\3\2\2\2\u01b1\u01b2")
        buf.write("\t\31\2\2\u01b2\u0094\3\2\2\2\u01b3\u01b4\t\32\2\2\u01b4")
        buf.write("\u0096\3\2\2\2\u01b5\u01b6\t\33\2\2\u01b6\u0098\3\2\2")
        buf.write("\2\u01b7\u01b8\t\34\2\2\u01b8\u009a\3\2\2\2\u01b9\u01bb")
        buf.write("\t\35\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\bN\2\2\u01bf\u009c\3\2\2\2\u01c0\u01c2\t")
        buf.write("\36\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c6\3\2\2\2\u01c3")
        buf.write("\u01c5\t\37\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c8\3\2\2")
        buf.write("\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u009e")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c9\u01cb\t\34\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u00a0\3\2\2\2\u01ce\u01d0\t")
        buf.write("\34\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\3\2\2\2")
        buf.write("\u01d3\u01d5\7\60\2\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u01d9\3\2\2\2\u01d6\u01d8\t\34\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01eb\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01de\t\34\2\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4\t")
        buf.write("\6\2\2\u01e3\u01e5\7/\2\2\u01e4\u01e3\3\2\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e8\t\34\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01df\3")
        buf.write("\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u0207\3\2\2\2\u01ed\u01ef")
        buf.write("\t\34\2\2\u01ee\u01ed\3\2\2\2\u01ef\u01f2\3\2\2\2\u01f0")
        buf.write("\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f4\3\2\2\2")
        buf.write("\u01f2\u01f0\3\2\2\2\u01f3\u01f5\7\60\2\2\u01f4\u01f3")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f7\3\2\2\2\u01f6")
        buf.write("\u01f8\t\34\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2")
        buf.write("\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0204")
        buf.write("\3\2\2\2\u01fb\u01fd\t\6\2\2\u01fc\u01fe\7/\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3\2\2\2")
        buf.write("\u01ff\u0201\t\34\2\2\u0200\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0205\3\2\2\2\u0204\u01fb\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0207\3\2\2\2\u0206\u01cf\3\2\2\2\u0206\u01f0\3")
        buf.write("\2\2\2\u0207\u00a2\3\2\2\2\u0208\u020e\7$\2\2\u0209\u020a")
        buf.write("\7^\2\2\u020a\u020d\t \2\2\u020b\u020d\n!\2\2\u020c\u0209")
        buf.write("\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2")
        buf.write("\u0210\u020e\3\2\2\2\u0211\u0212\7$\2\2\u0212\u0213\b")
        buf.write("R\3\2\u0213\u00a4\3\2\2\2\u0214\u0217\5\u00a7T\2\u0215")
        buf.write("\u0217\5\u00adW\2\u0216\u0214\3\2\2\2\u0216\u0215\3\2")
        buf.write("\2\2\u0217\u0218\3\2\2\2\u0218\u0219\bS\2\2\u0219\u00a6")
        buf.write("\3\2\2\2\u021a\u021d\5\u00a9U\2\u021b\u021d\5\u00abV\2")
        buf.write("\u021c\u021a\3\2\2\2\u021c\u021b\3\2\2\2\u021d\u00a8\3")
        buf.write("\2\2\2\u021e\u021f\7*\2\2\u021f\u0220\7,\2\2\u0220\u0224")
        buf.write("\3\2\2\2\u0221\u0223\13\2\2\2\u0222\u0221\3\2\2\2\u0223")
        buf.write("\u0226\3\2\2\2\u0224\u0225\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0225\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227\u0228\7")
        buf.write(",\2\2\u0228\u0229\7+\2\2\u0229\u00aa\3\2\2\2\u022a\u022e")
        buf.write("\7}\2\2\u022b\u022d\13\2\2\2\u022c\u022b\3\2\2\2\u022d")
        buf.write("\u0230\3\2\2\2\u022e\u022f\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022f\u0231\3\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232\7")
        buf.write("\177\2\2\u0232\u00ac\3\2\2\2\u0233\u0234\7\61\2\2\u0234")
        buf.write("\u0235\7\61\2\2\u0235\u0239\3\2\2\2\u0236\u0238\n\"\2")
        buf.write("\2\u0237\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u00ae\3\2\2\2\u023b")
        buf.write("\u0239\3\2\2\2\u023c\u0244\7$\2\2\u023d\u023f\7^\2\2\u023e")
        buf.write("\u0240\t \2\2\u023f\u023e\3\2\2\2\u0240\u0243\3\2\2\2")
        buf.write("\u0241\u0243\n!\2\2\u0242\u023d\3\2\2\2\u0242\u0241\3")
        buf.write("\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245")
        buf.write("\3\2\2\2\u0245\u0247\3\2\2\2\u0246\u0244\3\2\2\2\u0247")
        buf.write("\u0248\bX\4\2\u0248\u00b0\3\2\2\2\u0249\u024f\7$\2\2\u024a")
        buf.write("\u024e\n#\2\2\u024b\u024c\7^\2\2\u024c\u024e\t \2\2\u024d")
        buf.write("\u024a\3\2\2\2\u024d\u024b\3\2\2\2\u024e\u0251\3\2\2\2")
        buf.write("\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3")
        buf.write("\2\2\2\u0251\u024f\3\2\2\2\u0252\u0253\7^\2\2\u0253\u0254")
        buf.write("\n \2\2\u0254\u0255\bY\5\2\u0255\u00b2\3\2\2\2\u0256\u0257")
        buf.write("\13\2\2\2\u0257\u0258\bZ\6\2\u0258\u00b4\3\2\2\2\"\2\u01bc")
        buf.write("\u01c1\u01c4\u01c6\u01cc\u01d1\u01d4\u01d9\u01df\u01e4")
        buf.write("\u01e9\u01eb\u01f0\u01f4\u01f9\u01fd\u0202\u0204\u0206")
        buf.write("\u020c\u020e\u0216\u021c\u0224\u022e\u0239\u023f\u0242")
        buf.write("\u0244\u024d\u024f\7\b\2\2\3R\2\3X\3\3Y\4\3Z\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LB = 1
    RB = 2
    LQ = 3
    RQ = 4
    SEMI = 5
    CM = 6
    EQ = 7
    COL = 8
    DD = 9
    ADD = 10
    MUL = 11
    NOTEQ = 12
    LESSTN = 13
    LESSEQ = 14
    SUBNE = 15
    DIVSI = 16
    GRETN = 17
    GREEQ = 18
    ASSI = 19
    BREAK = 20
    CONTINUE = 21
    FOR = 22
    TO = 23
    DOWNTO = 24
    DO = 25
    IF = 26
    THEN = 27
    ELSE = 28
    RETURN = 29
    WHILE = 30
    BEGIN = 31
    END = 32
    FUNCTION = 33
    PROCEDURE = 34
    VAR = 35
    TRUE = 36
    FALSE = 37
    ARRAY = 38
    OF = 39
    REAL = 40
    BOOLEAN = 41
    INTEGER = 42
    STRING = 43
    NOT = 44
    AND = 45
    OR = 46
    DIV = 47
    MOD = 48
    WITH = 49
    WS = 50
    ID = 51
    INTLIT = 52
    REALLIT = 53
    STRINGLIT = 54
    CMT = 55
    BLKCMT = 56
    TRACMT = 57
    BLCMT = 58
    LINECMT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'['", "']'", "';'", "','", "'='", "':'", "'..'", 
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'>'", "'>='", 
            "':='" ]

    symbolicNames = [ "<INVALID>",
            "LB", "RB", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", "DD", "ADD", 
            "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", "GRETN", 
            "GREEQ", "ASSI", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
            "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", "END", 
            "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", 
            "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", 
            "DIV", "MOD", "WITH", "WS", "ID", "INTLIT", "REALLIT", "STRINGLIT", 
            "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LB", "RB", "LQ", "RQ", "SEMI", "CM", "EQ", "COL", "DD", 
                  "ADD", "MUL", "NOTEQ", "LESSTN", "LESSEQ", "SUBNE", "DIVSI", 
                  "GRETN", "GREEQ", "ASSI", "BREAK", "CONTINUE", "FOR", 
                  "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "A", 
                  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", 
                  "X", "Y", "Z", "NUM", "WS", "ID", "INTLIT", "REALLIT", 
                  "STRINGLIT", "CMT", "BLKCMT", "TRACMT", "BLCMT", "LINECMT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[80] = self.STRINGLIT_action 
            actions[86] = self.UNCLOSE_STRING_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            actions[88] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:len(self.text) - 1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


