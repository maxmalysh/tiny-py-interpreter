import argparse

import antlr4
from antlr4.tree.Trees import Trees
from AST.builder.Builder import CustomVisitor

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
    from AST.Builder import CustomVisitor

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
# TODO:
# * Probably add lists and dicts (check what we should change in the grammar)
# * Exception handling
# * Unit tests
# * Change stdin/stdout reads to the input / print
# * Refactor different input source handling (file / shell)
# * Manually read files (don't forget unicode!)
# * Add exceptions (to the parser) for break / continue outside of loops and return outside of function definition
#

#
# Known problems:
# * Unicode characters are not erased properly (have to use input() instead of sys.stdin)
# * When reading from file, there should be no attempt to evaluate the parse tree, if minor errors were encountered
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
    argParser.add_argument('--parse', dest='parse_only', action='store_true',
                           help='Parse input without evaluating it.')
    #
    # Parse arguments
    #
    argParser.set_defaults(cst=False, parse_tree=False)
    args = argParser.parse_args()

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

        # Evaluate it...
        visitor = CustomVisitor()
        ast = visitor.visitFile_input(parse_tree)

        if ast == None:
            exit()

        if not args.parse_only:
            ast.eval()


