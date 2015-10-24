import re

from antlr4.Token import CommonToken
from antlr4 import *

from TinyPyLexer import TinyPyLexer
from TinyPyParser import TinyPyParser

class CustomLexer(TinyPyLexer):

    def __init__(self, input=None):
        super().__init__(input)
        self.tokens = []       # A queue where extra tokens are pushed on (see the NEWLINE lexer rule).
        self.indents = []      # The stack that keeps track of the indentation level.
        self.opened = 0        # The amount of opened braces, brackets and parenthesis.
        self.lastToken = None  # The most recently produced token.

    def emitToken(self, token:Token):
        self._token = token
        self.tokens.append(token)

    def nextToken(self):
        # return super().nextToken()
        # Check if the end-of-file is ahead and there are still some DEDENTS expected
        if (self._input.LA(1) == Token.EOF and len(self.indents) != 0):
            # Remove any trailing EOF tokens from our buffer
            # ...

            # First emit an extra line break that serves as the end of the statement
            self.emitToken(self.commonToken(TinyPyParser.NEWLINE, '\n'))

            # Now emit as much DEDENT tokens as needed
            while len(self.indents) != 0:
                self.emitToken(self.createDedent())
                self.indents.pop()

            # Put the EOF back on the token stream
            self.emitToken(self.commonToken(TinyPyParser.EOF, "<EOF>"))

        nextToken = super().nextToken()

        if nextToken.channel == Token.DEFAULT_CHANNEL:
            # Keep track of the last token on the default channel
            self.lastToken = nextToken

        return nextToken if len(self.tokens) == 0 else self.tokens.pop(0)

    def createDedent(self):
        dedent = self.commonToken(TinyPyParser.DEDENT, "")
        dedent.line = self.lastToken.line
        return dedent

    def commonToken(self, _type, text):
        stop = self.getCharIndex() - 1
        start = stop if text == "" else stop - len(text) + 1
        return CommonToken(self._tokenFactorySourcePair, _type, self.DEFAULT_TOKEN_CHANNEL, start, stop)

    # Calculates the indentation of the provided spaces, taking the
    # following rules into account:
    #
    # "Tabs are replaced (from left to right) by one to eight spaces
    #  such that the total number of characters up to and including
    #  the replacement is a multiple of eight [...]"
    #
    #  -- https://docs.python.org/3.1/reference/lexical_analysis.html#indentation
    def getIndentationCount(self, spaces):
        count = 0
        for ch in spaces:
           if ch == '\t':
               count += 8 - (count % 8)
           else:
               count += 1
        return count


    def zefAction(self):
        newLine = re.sub("[^\r\n]+", "", self.text)
        spaces = re.sub("[\r\n]+", "", self.text)
        _next = self._input.LA(1)

        if self.opened > 0 or _next == '\r' or _next == '\n' or next == '#':
            # If we're inside a list or an a blank line, ignore all indents,
            # dedents and line breaks.
            self.skip()
        else:
            self.emitToken(self.commonToken(self.NEWLINE, newLine))

            indent = self.getIndentationCount(spaces)
            previous = self.indents[-1] if len(self.indents) != 0 else 0

            if indent != previous:
                # Skip indents of the same size as the present indent-size
                self.skip()
            elif indent > previous:
                self.indents.append(indent)
                self.emitToken(self.commonToken(TinyPyParser.INDENT, spaces))
            else:
                # Possibly emit more than 1 DEDENT token.
                while len(self.indents) != 0 and self.indents[-1] > indent:
                    self.emitToken(self.createDedent())
                    self.indents.pop()
