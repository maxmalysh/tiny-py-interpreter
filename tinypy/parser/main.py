import sys

import antlr4
from antlr4.tree.Trees import Trees

from parser.AST import AST
from parser.Errors import CustomErrorStrategy
from parser.CustomLexer import CustomLexer
from parser.CustomListener import CustomListener
from parser.TinyPyParser import TinyPyParser


if __name__ == '__main__':
    #file = "tests/8.txt"
    file = sys.argv[1]
    input_stream = antlr4.FileStream(file)

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = TinyPyParser(tokens)
    parser._errHandler = CustomErrorStrategy()

    try:
        parse_tree = parser.file_input()
    except Exception as e:
        #print("Bailing out.")
        exit(-1)

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


