from tinypy.parser.TinyPyListener import TinyPyListener


class CustomListener(TinyPyListener):
    def __init__(self):
        super(TinyPyListener, self).__init__()
        self.indent = 0

    # Enter a parse tree produced by TinyPyParser#expr.
    # def enterExpr(self, ctx:TinyPyParser.ExprContext):
    #     print(' ' * self.indent + 'expr:' + ctx.getText())
    #     self.indent += 1
    #
    # # Exit a parse tree produced by TinyPyParser#expr.
    # def exitExpr(self, ctx:TinyPyParser.ExprContext):
    #     self.indent -= 1
    #
    #
    # # Enter a parse tree produced by TinyPyParser#const.
    # def enterConst(self, ctx:TinyPyParser.ConstContext):
    #     print(' ' * self.indent + 'const:' + ctx.NUM().getText())
    #
    # # Exit a parse tree produced by TinyPyParser#const.
    # def exitConst(self, ctx:TinyPyParser.ConstContext):
    #     pass
    #
