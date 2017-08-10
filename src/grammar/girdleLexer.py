# Generated from java-escape by ANTLR 4.5
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\16")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\b\3\b\5\b\61\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\6\fE\n\f\r\f\16\fF\3\f\3\f\3\r\3\r\7\rM\n\r\f\r\16")
        buf.write("\rP\13\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\5\5\2\13\f\17\17\"\"\7\2\13\f")
        buf.write("\17\17\"\"*+\60\60\b\2\13\f\17\17\"\"*+\60\60??S\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5")
        buf.write("\37\3\2\2\2\7\"\3\2\2\2\t&\3\2\2\2\13(\3\2\2\2\r*\3\2")
        buf.write("\2\2\17\60\3\2\2\2\21\62\3\2\2\2\239\3\2\2\2\25@\3\2\2")
        buf.write("\2\27D\3\2\2\2\31J\3\2\2\2\33\34\7>\2\2\34\35\7?\2\2\35")
        buf.write("\36\7@\2\2\36\4\3\2\2\2\37 \7q\2\2 !\7t\2\2!\6\3\2\2\2")
        buf.write("\"#\7c\2\2#$\7p\2\2$%\7f\2\2%\b\3\2\2\2&\'\7*\2\2\'\n")
        buf.write("\3\2\2\2()\7+\2\2)\f\3\2\2\2*+\7\60\2\2+\16\3\2\2\2,-")
        buf.write("\7p\2\2-.\7q\2\2.\61\7v\2\2/\61\7\u0080\2\2\60,\3\2\2")
        buf.write("\2\60/\3\2\2\2\61\20\3\2\2\2\62\63\7h\2\2\63\64\7q\2\2")
        buf.write("\64\65\7t\2\2\65\66\7c\2\2\66\67\7n\2\2\678\7n\2\28\22")
        buf.write("\3\2\2\29:\7g\2\2:;\7z\2\2;<\7k\2\2<=\7u\2\2=>\7v\2\2")
        buf.write(">?\7u\2\2?\24\3\2\2\2@A\7?\2\2AB\7@\2\2B\26\3\2\2\2CE")
        buf.write("\t\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3\2")
        buf.write("\2\2HI\b\f\2\2I\30\3\2\2\2JN\n\3\2\2KM\n\4\2\2LK\3\2\2")
        buf.write("\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2O\32\3\2\2\2PN\3\2\2\2")
        buf.write("\6\2\60FN\3\b\2\2")
        return buf.getvalue()


class girdleLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    Lparen = 4
    Rparen = 5
    Dot = 6
    Not = 7
    Forall = 8
    Exists = 9
    Implies = 10
    Whitespace = 11
    Variable = 12

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            "'<=>'", "'or'", "'and'", "'('", "')'", "'.'", "'forall'", "'exists'", 
            "'=>'" ]

    symbolicNames = [ u"<INVALID>",
            "Lparen", "Rparen", "Dot", "Not", "Forall", "Exists", "Implies", 
            "Whitespace", "Variable" ]

    ruleNames = [ "T__0", "T__1", "T__2", "Lparen", "Rparen", "Dot", "Not", 
                  "Forall", "Exists", "Implies", "Whitespace", "Variable" ]

    grammarFileName = "girdle.g4"

    def __init__(self, input=None):
        super().__init__(input)
        #self.checkVersion("4.5")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


