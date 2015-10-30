import sys
from pprint import pprint

import antlr4
from antlr4.tree.Trees import Trees
from AST import AST
from Errors import CustomErrorStrategy

import Utils
from CustomLexer import CustomLexer
from CustomListener import CustomListener
from TinyPyParser import TinyPyParser


if __name__ == '__main__':
    input_stream = antlr4.FileStream(sys.argv[1])

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = TinyPyParser(tokens)
    parser._errHandler = CustomErrorStrategy()

    try:
        parse_tree = parser.file_input()
    except Exception as e:
        print("Bailing out. Exception: " + e)
        exit()

    # Traverse the parse tree
    listener = CustomListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # String, containing parse tree representation
    parseTreeString = Trees.toStringTree(parse_tree, recog=parser)

    # Build an AST
    ast = AST(tree=parse_tree)

    if len(sys.argv) >= 3 and sys.argv[2] == "--ast":
        print(str(ast))
        #print(parseTreeString)
        #print(pprint(Utils.sExprToDict(parseTreeString)))
        pass


