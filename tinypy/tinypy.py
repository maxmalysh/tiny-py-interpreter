import sys
import argparse

import antlr4
from antlr4.tree.Trees import Trees

from parser.AST import AST
from parser.Errors import CustomErrorStrategy
from parser.CustomLexer import CustomLexer
from parser.CustomListener import CustomListener
from parser.TinyPyParser import TinyPyParser
from shell.shell import InteractiveShell

if __name__ == '__main__':
    argParser = argparse.ArgumentParser(description='Process some integers.')
    argParser.add_argument('filename', type=str, nargs='?',
                           help='Filename')
    argParser.add_argument('--ast', dest='ast', action='store_true',
                           help='Show flattened parse tree for the input')
    argParser.add_argument('--pt',  dest='parse_tree',  action='store_true',
                           help='Show parse tree for the input')

    #
    # Parse arguments
    #
    argParser.set_defaults(ast=False, parse_tree=False)
    args = argParser.parse_args()


    if len(sys.argv) == 1:
        shell = InteractiveShell(args)
        shell.print_greeting()
        shell.loop()
        exit()
    else:
        input_stream = antlr4.FileStream(args.filename)

        # Instantiate an run generated lexer
        lexer = CustomLexer(input_stream)
        tokens = antlr4.CommonTokenStream(lexer)

        # Instantiate and run generated parser
        parser = TinyPyParser(tokens)
        parser._errHandler = CustomErrorStrategy()

        try:
            parse_tree = parser.file_input()
        except Exception as e:
            exit(-1)

        # Traverse the parse tree
        listener = CustomListener()
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, parse_tree)


        # Build an AST
        ast = AST(tree=parse_tree)

        if args.parse_tree:
            parseTreeString = Trees.toStringTree(parse_tree, recog=parser)
            print(parseTreeString)

        if args.ast:
            print(ast)




