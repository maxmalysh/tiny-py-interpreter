import sys
from pprint import pprint


import antlr4
from antlr4.tree.Trees import Trees
import AST
from Errors import CustomErrorStrategy
import Utils

from CustomLexer import CustomLexer
from CustomListener import CustomListener
from TinyPyParser import TinyPyParser


class InteractiveShell:
    greeting = "Ctrl + D to feed the input\n" + \
               "Ctrl + C to stop the loop\n"

    def __init__(self):
        pass


    def reset_recognizers(self, input_stream):
        # Instantiate an run generated lexer
        self.lexer = CustomLexer(input_stream)
        self.tokens = antlr4.CommonTokenStream(self.lexer)

        # Instantiate and run generated parser
        self.parser = TinyPyParser(self.tokens)
        self.parser._errHandler = CustomErrorStrategy()

    def loop(self):
        #while True:
            try:
                single_input = sys.stdin.read()


                print("We have read the following line: [" + single_input.replace('\n', '\\n') + "]")
                #print("Codepoints: ", [ord(c) for c in single_input])


                input_stream = antlr4.InputStream(single_input)
                #input_stream.data.append(-1)


                # Instantiate an run generated lexer
                self.lexer = CustomLexer(input_stream)
                self.tokens = antlr4.CommonTokenStream(self.lexer)


                # Instantiate and run generated parser
                self.parser = TinyPyParser(self.tokens)
                self.parser._errHandler = CustomErrorStrategy()


                parse_tree = self.parser.single_input()

                print("Tokens we got so far...")
                indents = dedents = newline = 0
                for token in self.tokens.tokens:
                    print(AST.nameFor(token.type))
                    if   token.type == TinyPyParser.INDENT: indents  += 1
                    elif token.type == TinyPyParser.DEDENT: dedents  += 1
                    elif token.type == TinyPyParser.NEWLINE: newline += 1

                print("%d | %d | %d" %(indents, dedents, newline))

                # Simple statement should end with 0 indents, 0 dedents, 1 newline and then EOF
                # 1-line compound statement should end with NEWLINE, NEWLINE, EOF with 0 indents / dedents
                # multiline compound statement have 1+ indents/dedents of the same amount and DEDENT-NEWLINE-EOF


                # String, containing parse tree representation
                full_parse_tree = Trees.toStringTree(parse_tree, recog=self.parser)

                ast = AST.AST(tree=parse_tree)
                print(ast.__str__(True))
                #print(full_parse_tree)
            except antlr4.RecognitionException as e:
                print("Caught" + str(e) )

    def print_greeting(self):
        print(self.greeting)

if __name__ == '__main__':
    shell = InteractiveShell()
    shell.print_greeting()
    shell.loop()


