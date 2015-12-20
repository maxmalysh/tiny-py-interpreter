import argparse, time
from enum import Enum

import antlr4
from antlr4.tree.Trees import Trees
from AST.builder.Builder import CustomVisitor

from parser.CST import CstFlattened, CstFiltered
from parser.Errors import CustomErrorStrategy, CustomErrorListener
from parser.CustomLexer import CustomLexer
from parser.TinyPyParser import TinyPyParser
from shell.shell import InteractiveShell


class InputType:
    File = 1
    SingleInput = 2
    Expression = 3

    parserRuleFor = {
        File        : TinyPyParser.file_input,
        SingleInput : TinyPyParser.single_input,
        Expression  : TinyPyParser.eval_input,
    }

    visitorRuleFor = {
        File        : CustomVisitor.visitFile_input,
        SingleInput : CustomVisitor.visitSingle_input,
        Expression  : CustomVisitor.visitEval_input,
    }


def tinypy_eval(content, firstRule: InputType, args=None):
    totalTime = time.time()
    input_stream = antlr4.InputStream(content)

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = TinyPyParser(tokens)
    parser._errHandler = CustomErrorStrategy()

    error_listener = CustomErrorListener()
    parser.addErrorListener(error_listener)

    # Traverse the parse tree
    parseTime = time.time()
    try:
        parse_tree = InputType.parserRuleFor[firstRule](parser)
    except Exception as e:
        return -1
    parseTime = time.time() - parseTime

    if error_listener.errors_encountered != 0:
        return -1

    # Print parse trees if need (full or flattened)
    if args.parse_tree:
        parseTreeString = Trees.toStringTree(parse_tree, recog=parser)
        print(parseTreeString)

    if args.cst:
        cst = CstFiltered(tree=parse_tree)
        print(cst)

    # Build an AST
    astBuildTime = time.time()

    visitor = CustomVisitor()
    ast = InputType.visitorRuleFor[firstRule](visitor, parse_tree)

    astBuildTime = time.time() - astBuildTime

    if ast == None:
        return -1

    if args.parse_only:
        return 0

    # Evaluate the AST we've built
    evalTime = time.time()
    try:
        ast.eval()
    except BaseException as e:
        print(e.__class__.__name__ + ": " + str(e))
        return -1

    evalTime = time.time() - evalTime

    totalTime = time.time() - totalTime

    if args.print_timings:
        timings = [
            ('Parsing',         parseTime),
            ('Building an AST', astBuildTime),
            ('Evaluating',      evalTime),
            ('Total time',      totalTime),
            ('Etc', totalTime-parseTime-astBuildTime-evalTime)
        ]
        print("#"*80)
        for timing in timings:
            print((timing[0]+": %.3f ms") % (timing[1]*1000))

    return 0


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
    argParser.add_argument('--timings', dest='print_timings', action='store_true',
                           help='Print time spend during parsing, building an AST and evaluating.')
    #
    # Parse arguments
    #
    argParser.set_defaults(cst=False, parse_tree=False)
    args = argParser.parse_args()

    if args.filename == None and not args.eval_input:
        shell = InteractiveShell(args)
        shell.print_greeting()
        shell.loop()
    if args.eval_input != None:
        firstRule = InputType.SingleInput
        content = args.eval_input
    else:
        firstRule = InputType.File

        with open(args.filename) as file_contents:
            content = file_contents.read()

    content += '\n'
    retvalue = tinypy_eval(content, firstRule, args)
    exit(retvalue)


