from antlr4.error.Errors import RecognitionException, ParseCancellationException
from antlr4.error.Errors import CancellationException
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.Parser import Parser
from antlr4.Token import Token
from TinyPyLexer import TinyPyLexer


class IndentationErr(RecognitionException):
    def __init__(self, line):
        super().__init__(message="unindent does not match any outer indentation level")
        self.line = line

class CustomErrorStrategy(DefaultErrorStrategy):
    def reportError(self, recognizer:Parser, e:RecognitionException):
        if isinstance(e, IndentationErr):
            self.reportIndendationError(recognizer, e)
        else:
            super().reportError(recognizer, e)

    def reportIndendationError(self, recognizer:Parser, e:IndentationErr):
        offendingToken = Token()
        offendingToken.line = e.line
        offendingToken.column = 0
        recognizer.notifyErrorListeners(e.message, offendingToken, e)
        raise ParseCancellationException(e)
