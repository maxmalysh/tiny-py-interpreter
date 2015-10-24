import sys

import antlr4

from CustomLexer import CustomLexer
from CustomListener import CustomListener
from TinyPyParser import TinyPyParser


#
# https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Python+Target
# https://github.com/ianpreston/antlrdemo
# https://theantlrguy.atlassian.net/wiki/display/ANTLR4/ANTLR+4+Documentation
#

#
# See:
# 1. https://github.com/antlr/grammars-v4/blob/master/peoplecode/PeopleCode.g4
# 2. https://github.com/antlr/grammars-v4/blob/master/python3/Python3.g4
# 3. https://github.com/ianpreston/antlrdemo/blob/master/Hello.bnf
# 4. http://mattjquinn.com/2014/01/19/antlr4-case-study.html
# 5. https://theantlrguy.atlassian.net/wiki/display/ANTLR4/Python+Target
# 6.
# 7. http://webcache.googleusercontent.com/search?q=cache:0cLr5diMWdQJ:https://erezsh.wordpress.com/2008/07/12/python-parsing-1-lexing/+&cd=10&hl=en&ct=clnk&gl=ru&lr=lang_en%7Clang_ru&client=safari
# 8.
# 9. https://docs.python.org/2/reference/lexical_analysis.html#indentation
#

if __name__ == '__main__':
    input_stream = antlr4.FileStream(sys.argv[1])

    # Instantiate an run generated lexer
    lexer = CustomLexer(input_stream)
    tokens = antlr4.CommonTokenStream(lexer)

    # Instantiate and run generated parser
    parser = TinyPyParser(tokens)
    parse_tree = parser.file_input()

    # Traverse the parse tree
    listener = CustomListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # print(Trees.toStringTree(parse_tree, parser))
