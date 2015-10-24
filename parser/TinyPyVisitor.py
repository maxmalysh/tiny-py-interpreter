# Generated from /Users/apple/Development/tiny-py-interpreter/parser/TinyPy.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TinyPyParser import TinyPyParser
else:
    from TinyPyParser import TinyPyParser

# This class defines a complete generic visitor for a parse tree produced by TinyPyParser.

class TinyPyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TinyPyParser#file_input.
    def visitFile_input(self, ctx:TinyPyParser.File_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#stmt.
    def visitStmt(self, ctx:TinyPyParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#simple_stmt.
    def visitSimple_stmt(self, ctx:TinyPyParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#small_stmt.
    def visitSmall_stmt(self, ctx:TinyPyParser.Small_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#expr_stmt.
    def visitExpr_stmt(self, ctx:TinyPyParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#testlist_expr.
    def visitTestlist_expr(self, ctx:TinyPyParser.Testlist_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#expr.
    def visitExpr(self, ctx:TinyPyParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#xor_expr.
    def visitXor_expr(self, ctx:TinyPyParser.Xor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#and_expr.
    def visitAnd_expr(self, ctx:TinyPyParser.And_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#shift_expr.
    def visitShift_expr(self, ctx:TinyPyParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#arith_expr.
    def visitArith_expr(self, ctx:TinyPyParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#term.
    def visitTerm(self, ctx:TinyPyParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#factor.
    def visitFactor(self, ctx:TinyPyParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#atom.
    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#number.
    def visitNumber(self, ctx:TinyPyParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#integer.
    def visitInteger(self, ctx:TinyPyParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#string.
    def visitString(self, ctx:TinyPyParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#pass_stmt.
    def visitPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        return self.visitChildren(ctx)



del TinyPyParser