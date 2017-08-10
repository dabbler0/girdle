# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .girdleListener import girdleListener
else:
    from girdleListener import girdleListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\16")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4+\n\4\3\5\3\5\3\5\3\5\3\5\5\5\62\n\5\3\6\3")
        buf.write("\6\5\6\66\n\6\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\5\bD\n\b\3\t\3\t\3\t\3\t\3\t\5\tK\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\nR\n\n\3\13\3\13\3\13\5\13W\n\13\3\f\6")
        buf.write("\fZ\n\f\r\f\16\f[\3\r\3\r\3\r\3\r\3\r\5\rc\n\r\3\16\3")
        buf.write("\16\3\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\2\2e\2!\3\2\2\2\4#\3\2\2\2\6*\3\2\2\2\b\61\3\2\2\2\n")
        buf.write("\65\3\2\2\2\f<\3\2\2\2\16C\3\2\2\2\20J\3\2\2\2\22Q\3\2")
        buf.write("\2\2\24V\3\2\2\2\26Y\3\2\2\2\30b\3\2\2\2\32d\3\2\2\2\34")
        buf.write("\"\5\26\f\2\35\36\7\6\2\2\36\37\5\4\3\2\37 \7\7\2\2 \"")
        buf.write("\3\2\2\2!\34\3\2\2\2!\35\3\2\2\2\"\3\3\2\2\2#$\5\6\4\2")
        buf.write("$\5\3\2\2\2%&\7\n\2\2&\'\7\16\2\2\'(\7\b\2\2(+\5\4\3\2")
        buf.write(")+\5\b\5\2*%\3\2\2\2*)\3\2\2\2+\7\3\2\2\2,-\7\13\2\2-")
        buf.write(".\7\16\2\2./\7\b\2\2/\62\5\4\3\2\60\62\5\n\6\2\61,\3\2")
        buf.write("\2\2\61\60\3\2\2\2\62\t\3\2\2\2\63\66\5\f\7\2\64\66\5")
        buf.write("\16\b\2\65\63\3\2\2\2\65\64\3\2\2\2\66\13\3\2\2\2\678")
        buf.write("\5\20\t\289\7\f\2\29:\5\4\3\2:=\3\2\2\2;=\5\20\t\2<\67")
        buf.write("\3\2\2\2<;\3\2\2\2=\r\3\2\2\2>?\5\20\t\2?@\7\3\2\2@A\5")
        buf.write("\4\3\2AD\3\2\2\2BD\5\20\t\2C>\3\2\2\2CB\3\2\2\2D\17\3")
        buf.write("\2\2\2EF\5\22\n\2FG\7\4\2\2GH\5\20\t\2HK\3\2\2\2IK\5\22")
        buf.write("\n\2JE\3\2\2\2JI\3\2\2\2K\21\3\2\2\2LM\5\24\13\2MN\7\5")
        buf.write("\2\2NO\5\24\13\2OR\3\2\2\2PR\5\24\13\2QL\3\2\2\2QP\3\2")
        buf.write("\2\2R\23\3\2\2\2ST\7\t\2\2TW\5\2\2\2UW\5\2\2\2VS\3\2\2")
        buf.write("\2VU\3\2\2\2W\25\3\2\2\2XZ\5\30\r\2YX\3\2\2\2Z[\3\2\2")
        buf.write("\2[Y\3\2\2\2[\\\3\2\2\2\\\27\3\2\2\2]c\7\16\2\2^_\7\6")
        buf.write("\2\2_`\5\26\f\2`a\7\7\2\2ac\3\2\2\2b]\3\2\2\2b^\3\2\2")
        buf.write("\2c\31\3\2\2\2de\5\4\3\2ef\7\2\2\3f\33\3\2\2\2\r!*\61")
        buf.write("\65<CJQV[b")
        return buf.getvalue()


class girdleParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'<=>'", u"'or'", u"'and'", u"'('", 
                     u"')'", u"'.'", u"<INVALID>", u"'forall'", u"'exists'", 
                     u"'=>'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"Lparen", u"Rparen", u"Dot", u"Not", u"Forall", u"Exists", 
                      u"Implies", u"Whitespace", u"Variable" ]

    RULE_primary_fol_expression = 0
    RULE_fol_expression = 1
    RULE_fol_universal_quantifier = 2
    RULE_fol_existential_quantifier = 3
    RULE_fol_implication_or_equivalence = 4
    RULE_fol_implication = 5
    RULE_fol_equivalence = 6
    RULE_fol_disjunction = 7
    RULE_fol_conjunction = 8
    RULE_fol_negation = 9
    RULE_expression = 10
    RULE_primary_expression = 11
    RULE_line = 12

    ruleNames =  [ "primary_fol_expression", "fol_expression", "fol_universal_quantifier", 
                   "fol_existential_quantifier", "fol_implication_or_equivalence", 
                   "fol_implication", "fol_equivalence", "fol_disjunction", 
                   "fol_conjunction", "fol_negation", "expression", "primary_expression", 
                   "line" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Lparen=4
    Rparen=5
    Dot=6
    Not=7
    Forall=8
    Exists=9
    Implies=10
    Whitespace=11
    Variable=12

    def __init__(self, input:TokenStream):
        super().__init__(input)
        #self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Primary_fol_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(girdleParser.ExpressionContext,0)


        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_primary_fol_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterPrimary_fol_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitPrimary_fol_expression(self)




    def primary_fol_expression(self):

        localctx = girdleParser.Primary_fol_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_primary_fol_expression)
        try:
            self.state = 31
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(girdleParser.Lparen)
                self.state = 28
                self.fol_expression()
                self.state = 29
                self.match(girdleParser.Rparen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_universal_quantifier(self):
            return self.getTypedRuleContext(girdleParser.Fol_universal_quantifierContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_expression(self)




    def fol_expression(self):

        localctx = girdleParser.Fol_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fol_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.fol_universal_quantifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_universal_quantifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Variable(self):
            return self.getToken(girdleParser.Variable, 0)

        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def fol_existential_quantifier(self):
            return self.getTypedRuleContext(girdleParser.Fol_existential_quantifierContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_universal_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_universal_quantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_universal_quantifier(self)




    def fol_universal_quantifier(self):

        localctx = girdleParser.Fol_universal_quantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fol_universal_quantifier)
        try:
            self.state = 40
            token = self._input.LA(1)
            if token in [girdleParser.Forall]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(girdleParser.Forall)
                self.state = 36
                self.match(girdleParser.Variable)
                self.state = 37
                self.match(girdleParser.Dot)
                self.state = 38
                self.fol_expression()

            elif token in [girdleParser.Lparen, girdleParser.Not, girdleParser.Exists, girdleParser.Variable]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.fol_existential_quantifier()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_existential_quantifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Variable(self):
            return self.getToken(girdleParser.Variable, 0)

        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def fol_implication_or_equivalence(self):
            return self.getTypedRuleContext(girdleParser.Fol_implication_or_equivalenceContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_existential_quantifier

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_existential_quantifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_existential_quantifier(self)




    def fol_existential_quantifier(self):

        localctx = girdleParser.Fol_existential_quantifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_fol_existential_quantifier)
        try:
            self.state = 47
            token = self._input.LA(1)
            if token in [girdleParser.Exists]:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(girdleParser.Exists)
                self.state = 43
                self.match(girdleParser.Variable)
                self.state = 44
                self.match(girdleParser.Dot)
                self.state = 45
                self.fol_expression()

            elif token in [girdleParser.Lparen, girdleParser.Not, girdleParser.Variable]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.fol_implication_or_equivalence()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_implication_or_equivalenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_implication(self):
            return self.getTypedRuleContext(girdleParser.Fol_implicationContext,0)


        def fol_equivalence(self):
            return self.getTypedRuleContext(girdleParser.Fol_equivalenceContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_implication_or_equivalence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_implication_or_equivalence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_implication_or_equivalence(self)




    def fol_implication_or_equivalence(self):

        localctx = girdleParser.Fol_implication_or_equivalenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fol_implication_or_equivalence)
        try:
            self.state = 51
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.fol_implication()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.fol_equivalence()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_implicationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_disjunction(self):
            return self.getTypedRuleContext(girdleParser.Fol_disjunctionContext,0)


        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_implication

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_implication(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_implication(self)




    def fol_implication(self):

        localctx = girdleParser.Fol_implicationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fol_implication)
        try:
            self.state = 58
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.fol_disjunction()
                self.state = 54
                self.match(girdleParser.Implies)
                self.state = 55
                self.fol_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.fol_disjunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_equivalenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_disjunction(self):
            return self.getTypedRuleContext(girdleParser.Fol_disjunctionContext,0)


        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_equivalence

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_equivalence(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_equivalence(self)




    def fol_equivalence(self):

        localctx = girdleParser.Fol_equivalenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_fol_equivalence)
        try:
            self.state = 65
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.fol_disjunction()
                self.state = 61
                self.match(girdleParser.T__0)
                self.state = 62
                self.fol_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.fol_disjunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_disjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_conjunction(self):
            return self.getTypedRuleContext(girdleParser.Fol_conjunctionContext,0)


        def fol_disjunction(self):
            return self.getTypedRuleContext(girdleParser.Fol_disjunctionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_disjunction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_disjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_disjunction(self)




    def fol_disjunction(self):

        localctx = girdleParser.Fol_disjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fol_disjunction)
        try:
            self.state = 72
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.fol_conjunction()
                self.state = 68
                self.match(girdleParser.T__1)
                self.state = 69
                self.fol_disjunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.fol_conjunction()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_conjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_negation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(girdleParser.Fol_negationContext)
            else:
                return self.getTypedRuleContext(girdleParser.Fol_negationContext,i)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_conjunction

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_conjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_conjunction(self)




    def fol_conjunction(self):

        localctx = girdleParser.Fol_conjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fol_conjunction)
        try:
            self.state = 79
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.fol_negation()
                self.state = 75
                self.match(girdleParser.T__2)
                self.state = 76
                self.fol_negation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.fol_negation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fol_negationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Not(self):
            return self.getToken(girdleParser.Not, 0)

        def primary_fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Primary_fol_expressionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_fol_negation

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterFol_negation(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitFol_negation(self)




    def fol_negation(self):

        localctx = girdleParser.Fol_negationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fol_negation)
        try:
            self.state = 84
            token = self._input.LA(1)
            if token in [girdleParser.Not]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(girdleParser.Not)
                self.state = 82
                self.primary_fol_expression()

            elif token in [girdleParser.Lparen, girdleParser.Variable]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.primary_fol_expression()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(girdleParser.Primary_expressionContext)
            else:
                return self.getTypedRuleContext(girdleParser.Primary_expressionContext,i)


        def getRuleIndex(self):
            return girdleParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitExpression(self)




    def expression(self):

        localctx = girdleParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 86
                self.primary_expression()
                self.state = 89 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==girdleParser.Lparen or _la==girdleParser.Variable):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Primary_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Variable(self):
            return self.getToken(girdleParser.Variable, 0)

        def expression(self):
            return self.getTypedRuleContext(girdleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return girdleParser.RULE_primary_expression

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitPrimary_expression(self)




    def primary_expression(self):

        localctx = girdleParser.Primary_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primary_expression)
        try:
            self.state = 96
            token = self._input.LA(1)
            if token in [girdleParser.Variable]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.match(girdleParser.Variable)

            elif token in [girdleParser.Lparen]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(girdleParser.Lparen)
                self.state = 93
                self.expression()
                self.state = 94
                self.match(girdleParser.Rparen)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fol_expression(self):
            return self.getTypedRuleContext(girdleParser.Fol_expressionContext,0)


        def EOF(self):
            return self.getToken(girdleParser.EOF, 0)

        def getRuleIndex(self):
            return girdleParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, girdleListener ):
                listener.exitLine(self)




    def line(self):

        localctx = girdleParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.fol_expression()
            self.state = 99
            self.match(girdleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




