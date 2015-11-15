import sys
from pprint import pprint


import antlr4
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.tree.Trees import Trees
import AST
from Errors import CustomErrorStrategy, CustomErrorListener, BufferedErrorListener
import Utils

from CustomLexer import CustomLexer
from CustomListener import CustomListener
from TinyPyParser import TinyPyParser


class InteractiveShell:
    greeting =  "Press Ctrl + C to exit\n"

    def __init__(self):
        self.readMore = False
        pass


    def reset_recognizers(self, input_stream):
        # Instantiate an run generated lexer
        self.lexer = CustomLexer(input_stream)
        self.tokens = antlr4.CommonTokenStream(self.lexer)

        # Instantiate and run generated parser
        self.parser = TinyPyParser(self.tokens)
        self.parser._errHandler = CustomErrorStrategy()

    def loop(self):
        while True:
            try:
                if self.readMore:
                    sys.stdout.write("... ")
                    sys.stdout.flush()
                    single_input += sys.stdin.readline()
                else:
                    sys.stdout.write(">>> ")
                    sys.stdout.flush()
                    single_input = sys.stdin.readline()

                #print("We have read the following text: [" + single_input.replace('\n', '\\n') + "]")
                #print("Codepoints: ", [ord(c) for c in single_input])

                input_stream = antlr4.InputStream(single_input)

                # Instantiate and run generated lexer
                self.lexer = CustomLexer(input_stream)
                self.tokens = antlr4.CommonTokenStream(self.lexer)


                # Setting up error handling stuff
                error_handler = CustomErrorStrategy()
                error_listener = CustomErrorListener()
                buffered_errors = BufferedErrorListener()
                error_listener.addDelegatee(buffered_errors)

                self.parser = TinyPyParser(self.tokens)
                self.parser._errHandler = error_handler

                self.parser.removeErrorListeners()
                self.parser.addErrorListener(error_listener)

                # Parse input
                parse_tree = self.parser.single_input()

                # Just debug info
                #self.checkTokens(error_listener)


                if error_listener.input_unfinished:
                    # User has not finished his input yet, read the next line and repeat
                    self.readMore = True
                    continue
                elif error_listener.errors_encountered > 0:
                    # Errors encountered, start over
                    print(buffered_errors.buffer)
                    self.readMore = False
                    continue
                else:
                    # Successfully parsed the input, next time start over
                    self.readMore = False

                # Let's build an AST now...
                ast = AST.AST(tree=parse_tree)
                print(ast)

                # String, containing parse tree representation
                #print(Trees.toStringTree(parse_tree, recog=self.parser))

                # Evaluate it...
                # ...

            except antlr4.RecognitionException as e:
                print("Caught" + str(e) )


    def checkTokens(self, error_listener):
        print("Tokens we got so far...")
        indents = dedents = newline = eofs = 0
        for token in self.tokens.tokens:
            print(AST.nameFor(token.type))
            if token.type == TinyPyParser.INDENT:
                indents += 1
            elif token.type == TinyPyParser.DEDENT:
                dedents += 1
            elif token.type == TinyPyParser.NEWLINE:
                newline += 1
            elif token.type == TinyPyParser.EOF:
                eofs += 1

        # Simple statement should end with 0 indents, 0 dedents, 1 newline and then EOF
        # 1-line compound statement should end with NEWLINE, NEWLINE, EOF with 0 indents / dedents
        # multiline compound statement have 1+ indents/dedents of the same amount and DEDENT-NEWLINE-EOF
        print("%d | %d | %d | %d" % (indents, dedents, newline, eofs))
        print("Got %d errors and %d" % (error_listener.errors_encountered, error_listener.input_unfinished))


    def print_greeting(self):
        print(self.greeting)

if __name__ == '__main__':
    shell = InteractiveShell()
    shell.print_greeting()
    shell.loop()


