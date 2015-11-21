import collections
from AST.ExprVisitor import ExprVisitorMixin
from AST.StmtVisitor import StmtVisitorMixin

from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor

from AST import ast

class CustomVisitor(StmtVisitorMixin, ExprVisitorMixin, TinyPyVisitor):

    #
    # Start rules
    #
    def visitEval_input(self, ctx:TinyPyParser.Eval_inputContext):
        return ast.EvalExpression(self.visit(ctx.test()))



    #
    # Single input is used only in interpreted mode
    #
    def visitSingle_input(self, ctx:TinyPyParser.Single_inputContext):
        if ctx.compound_stmt() != None:
            return ast.Interactive(self.visit(ctx.compound_stmt()))

        elif ctx.simple_stmt() != None:
            return ast.Interactive(self.visit(ctx.simple_stmt()))

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

