import sys

import antlr4
from antlr4.tree.Trees import Trees

from AST.builder.Builder import CustomVisitor
from parser.CustomLexer import CustomLexer
from parser.TinyPyParser import TinyPyParser
from parser.Errors import CustomErrorStrategy, CustomErrorListener, BufferedErrorListener
from parser import CST
import runtime.Errors

class InteractiveShell:
    greeting =  "Call exit() to quit\n"

    def __init__(self, args):
        self.args = args
        self.single_input = ""
        self.readMore = False
        pass

    def loop(self):
        while True:
            try:
                if self.readMore:
                    sys.stdout.write("... ")
                    sys.stdout.flush()
                    self.single_input += sys.stdin.readline()
                else:
                    sys.stdout.write(">>> ")
                    sys.stdout.flush()
                    self.single_input = sys.stdin.readline()

                input_stream = antlr4.InputStream(self.single_input)

                # Instantiate and run generated lexer
                self.lexer = CustomLexer(input_stream)
                self.tokens = antlr4.CommonTokenStream(self.lexer)

                # Setting up error handling stuff
                error_handler = CustomErrorStrategy()
                error_listener = CustomErrorListener()
                buffered_errors = BufferedErrorListener()
                error_listener.addDelegatee(buffered_errors)

                # Run parser and set error handler
                self.parser = TinyPyParser(self.tokens)
                self.parser._errHandler = error_handler

                # Remove default terminal error listener & and our own
                self.parser.removeErrorListeners()
                self.parser.addErrorListener(error_listener)

                # Parse input
                parse_tree = self.parser.single_input()

                # Determine what to do next
                if error_listener.input_unfinished or self.lexer.opened < 0:
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

                # Build a flattened syntax tree
                cst = CST.CstFiltered(tree=parse_tree)

                # Print some stuff... (if needed)
                if self.args.cst:
                    print(cst)

                if self.args.parse_tree:
                    parseTreeString = Trees.toStringTree(parse_tree, recog=self.parser)
                    print(parseTreeString)

                # Evaluate it...
                visitor = CustomVisitor()
                ast = visitor.visitSingle_input(parse_tree)
                if ast == None:
                    continue

                if self.args.parse_only:
                    continue

                results = ast.eval()

                #
                # ast.eval() returns list of statements; loop through them and print
                #
                if results != None:
                    for statement in results:
                        if statement != None:
                            sys.displayhook(statement)

                #if results != None:
                #    sys.displayhook(results)

            except antlr4.RecognitionException as e:
                print("Caught" + str(e) )
            except runtime.Errors.BaseRuntimeException as e:
                print(e.__class__.__name__ + ": " + str(e))
            ##
            ## Add here our own super class of the own exception system
            ##
            #except KeyboardInterrupt as e:
            #    print("\n" + e.__class__.__name__)
            #    print("Type exit() to quit")
            #except Exception as e:
            #    print(e.__class__.__name__ + ": " + str(e))

    def print_greeting(self):
        print(self.greeting)
