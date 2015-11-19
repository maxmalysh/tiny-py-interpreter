import collections

from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor

from AST import ast

class CustomVisitor(TinyPyVisitor):
    def __init__(self):
        super().__init__()


    #
    # TODO: add this:
    # def buildFrom(self, input, startRule)
    #

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
    # Start rules
    #
    def visitEval_input(self, ctx:TinyPyParser.Eval_inputContext):
        return ast.EvalExpression(self.visit(ctx.test()))

    def visitSingle_input(self, ctx:TinyPyParser.Single_inputContext):
        if ctx.simple_stmt() != None:
            return ast.Interactive(self.visit(ctx.simple_stmt()))
        elif ctx.compound_stmt() != None:
            return ast.Interactive(self.visit(ctx.compound_stmt()))

        return None

    def visitFile_input(self, ctx:TinyPyParser.File_inputContext):
        i = 0
        statements = []

        while i < len(ctx.children):
            statement =  self.visit(ctx.stmt(i))
            if statement != None:
                statements.append(statement)

        return ast.Module(body=statements)

    #
    # Base statements
    #
    def visitSimple_stmt(self, ctx:TinyPyParser.Simple_stmtContext):
        i = 0
        statements = []

        for smallStmt in ctx.small_stmt():
            statement = self.visit(smallStmt)
            if statement != None:
                statements.append(statement)


        # while i < len(ctx.children):
        #     statement =  self.visit(ctx.small_stmt(i))
        #     if statement != None:
        #         statements.append(statement)

        return statements


    #
    # Compound statements
    #


    #
    # Small statements
    #

    def visitExprStmtAssign(self, ctx:TinyPyParser.ExprStmtAssignContext):
        name = ctx.NAME().getText()
        expr = self.visit(ctx.expr())

        nameNode = ast.Name(id=name, ctx=ast.Name.Context.Store)

        return ast.AssignStmt(target=nameNode, value=expr)

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
        return ast.UnaryOp(op=ctx.op.text, operand=operand)

    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        if ctx.NONE() != None:
            return ast.NameConstant('None')
        elif ctx.TRUE() != None:
            return ast.NameConstant('True')
        elif ctx.FALSE() != None:
            return ast.NameConstant('False')
        elif ctx.NAME() != None:
            return ast.Name(id=ctx.NAME().getText(), ctx=ast.Name.Context.Load)
        else:
            return self.visitChildren(ctx)


    def visitFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        name = ctx.NAME().getText()
        args = []

        if ctx.arglist() != None:
            for argStmt in ctx.arglist().test():
                arg = self.visit(argStmt)
                if arg != None:
                    args.append(arg)

        funcName = ast.Name(name, ast.Name.Context.Load)
        return ast.CallExpr(func=funcName, args=args)


    def visitNumber(self, ctx:TinyPyParser.NumberContext):
         return self.visitChildren(ctx)


    def visitInteger(self, ctx:TinyPyParser.IntegerContext):
        if ctx.DECIMAL_INTEGER() != None:
            decimal = int(ctx.DECIMAL_INTEGER().getText())
            return ast.Num(decimal)
        elif ctx.HEX_INTEGER() != None:
            hex = int(ctx.HEX_INTEGER().getText(), 16)
            return ast.Num(hex)
        else:
            raise ValueError()

    def visitString(self, ctx:TinyPyParser.StringContext):
        node = ctx.STRING_LITERAL()
        if node != None:
            text = node.getText()[1:-1]
            return ast.Str(text)

        raise ValueError()


class CleaningVisitor(TinyPyParser):
    def __init__(self):
        super().__init__()

