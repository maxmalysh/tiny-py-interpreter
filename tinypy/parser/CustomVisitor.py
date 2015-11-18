import collections

from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor

from AST import ast

class CustomVisitor(TinyPyVisitor):
    def __init__(self):
        super().__init__()

    # def aggregateResult(self, aggregate, nextResult):
    #     if (aggregate is not list or aggregate is not tuple):
    #         return [aggregate, nextResult]
    #
    #     # if aggregate == None:
    #     #     aggregate = []
    #     #
    #     # if nextResult == None:
    #     #     return aggregate
    #
    #     return aggregate.append(nextResult)


    #
    # Starting rules
    #
    def visitEval_input(self, ctx:TinyPyParser.Eval_inputContext):
        return self.visit(ctx.test())



    #
    #
    #






    #
    # Arithmetic
    #

    def visitFactorExpr(self, ctx:TinyPyParser.FactorExprContext):
        return self.visit(ctx.factor())

    def visitAddSub(self, ctx:TinyPyParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == TinyPyParser.ADD:
            return ast.AddOp(left, right)
        elif ctx.op.type == TinyPyParser.MINUS:
            return ast.SubOp(left, right)
        else:
            raise ValueError("Unexpected op type")

    def visitMulDivMod(self, ctx:TinyPyParser.MulDivModContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if ctx.op.type == TinyPyParser.STAR:
            return ast.MultOp(left, right)
        elif ctx.op.type == TinyPyParser.DIV:
            return ast.DivOp(left, right)
        else:
            raise ValueError("Unexpected op type")




    #
    # @factor rule
    #
    def visitUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        operand = ctx.factor().accept(self)
        return ast.UnaryOp(op=ctx.op.getText(), operand=operand)

    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitFuncInvokExpr(self, ctx:TinyPyParser.FuncInvokExprContext):
        raise NotImplementedError()

    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        if ctx.NONE() != None:
            return ast.NameConstant('None')
        elif ctx.TRUE() != None:
            return ast.NameConstant('True')
        elif ctx.FALSE() != None:
            return ast.NameConstant('False')
        elif ctx.NAME() != None:
            # FIXME (context should be fixed!!!)
            return ast.Name(id=ctx.NAME().getText(), ctx=ctx)
        else:
            return self.visitChildren(ctx)

    def visitNumber(self, ctx:TinyPyParser.NumberContext):
         return self.visitChildren(ctx)

    def visitString(self, ctx:TinyPyParser.StringContext):
        if ctx.STRING_LITERAL() != None:
            return ast.Str(ctx.STRING_LITERAL().getText())
        else:
            raise ValueError()

    def visitInteger(self, ctx:TinyPyParser.IntegerContext):
        if ctx.DECIMAL_INTEGER() != None:
            decimal = int(ctx.DECIMAL_INTEGER().getText())
            return ast.Num(decimal)
        elif ctx.HEX_INTEGER() != None:
            hex = int(ctx.HEX_INTEGER().getText(), 16)
            return ast.Num(hex)
        else:
            raise ValueError()


class CleaningVisitor(TinyPyParser):
    def __init__(self):
        super().__init__()

