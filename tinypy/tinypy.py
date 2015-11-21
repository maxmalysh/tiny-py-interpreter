import argparse

import antlr4
from antlr4.tree.Trees import Trees

from parser.CST import CstFlattened, CstFiltered
from parser.Errors import CustomErrorStrategy
from parser.CustomLexer import CustomLexer
from parser.CustomListener import CustomListener
from parser.TinyPyParser import TinyPyParser
from shell.shell import InteractiveShell

def eval_string(input_string, args=None):
    input_stream = antlr4.InputStream(input_string)

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = TinyPyParser(tokens)
    parser._errHandler = CustomErrorStrategy()

    try:
        parse_tree = parser.eval_input()
    except Exception as e:
        exit(-1)

    # Traverse the parse tree
    listener = CustomListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # Evaluate it...
    from AST.AstBuilder import CustomVisitor

    visitor = CustomVisitor()
    ast = visitor.visitEval_input(parse_tree)
    print(ast)
    print(ast.eval())

    if not args:
        return

    # Build a flattened syntax tree
    cst = CstFlattened(tree=parse_tree)

    if args.parse_tree:
        parseTreeString = Trees.toStringTree(parse_tree, recog=parser)
        print(parseTreeString)

    if args.cst:
        print(cst)


#
# TODO (current scope):
# 1. Add IF to the visitor
# 2. Add IF to the AST (check it)
# 3. Add WHILE to the visitor
# 4. Append to the lists of the statements on the highest level (or somewhere in the middle)
# 5. Refactor visitor
# 6. Refactor AST
#
#
# TODO:
# 1. Intelligent display hook for the shell mode
# 2. Proper memory management & variable scope handling
# 3. Exception handling
# 4. Unit tests
# 5. Change stdin/stdout reads to the input / print
#

#
# Known problems:
# 1) Unicode characters are not erased properly (have to use input() instead of sys.stdin)
# 2) Statement evaluation resulsts are passed to the displayhook as a nested structure
#
#
if __name__ == '__main__':
    argParser = argparse.ArgumentParser()
    argParser.add_argument('filename', type=str, nargs='?',
                           help='Path to the script file.')
    argParser.add_argument('-c', dest='eval_input', type=str,
                           help='Program passed in as string')
    argParser.add_argument('--cst', dest='cst', action='store_true',
                           help='Show flattened concreted syntax tree for the input (parse tree)')
    argParser.add_argument('--tokens',  dest='parse_tree',  action='store_true',
                           help='Show string representation of a parse tree for the input')

    #
    # Parse arguments
    #
    argParser.set_defaults(cst=False, parse_tree=False)
    args = argParser.parse_args()
    # print(args)

    if args.eval_input != None:
        eval_string(args.eval_input, args)
    elif args.filename == None:
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


        # Build a flattened syntax tree
        cst = CstFiltered(tree=parse_tree)

        if args.parse_tree:
            parseTreeString = Trees.toStringTree(parse_tree, recog=parser)
            print(parseTreeString)

        if args.cst:
            print(cst)




