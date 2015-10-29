from pprint import pprint
import sys

import antlr4
from antlr4.tree.Trees import Trees
from AST import AST

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
    parse_tree = parser.file_input()

    # Traverse the parse tree
    listener = CustomListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, parse_tree)

    # String, containing parse tree representation
    parseTreeString = Trees.toStringTree(parse_tree, recog=parser)

    # Build an AST
    ast = AST(tree=parse_tree)

    if len(sys.argv) >= 3 and sys.argv[2] == "--ast":
        #print(str(ast))
        #print(parseTreeString)
        #print(pprint(Utils.sExprToDict(parseTreeString)))
        pass


# Все присваивания (следует из отсутствия списков) - только для одной переменной, возвращается тоже только одно значение

# Отсутствуют:
# Списки и словари (коллекции)
# Классы
# Исключения
# Типизированные и дефолтные параметры в функциях
# Оператор for (не имеет смысла без коллекций)
# Star operator (не имеет смысла без списков)
# global/nonlocal
# Лямбда-выражения
# Генераторы и yield
# Ключевое слово with
# Двоичные (байтовые) литералы
# Двоичные числа, восьмеричные числа, числа с плавающей запятой
# Сокращенные формы арифметических операций (e.g. +=)
# else для циклов (while ...: [ ...] else: [...] )

# Возможно, многое из этого можно добавить без особого труда, но я бы не рисковал,
# так как не могу оценить объем работы для следующего этапа.

