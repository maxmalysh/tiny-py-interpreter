# Generated from /Users/apple/Development/tiny-py-interpreter/parser/TinyPy.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TinyPyParser import TinyPyParser
else:
    from TinyPyParser import TinyPyParser

# This class defines a complete listener for a parse tree produced by TinyPyParser.
class TinyPyListener(ParseTreeListener):

    # Enter a parse tree produced by TinyPyParser#file_input.
    def enterFile_input(self, ctx:TinyPyParser.File_inputContext):
        pass

    # Exit a parse tree produced by TinyPyParser#file_input.
    def exitFile_input(self, ctx:TinyPyParser.File_inputContext):
        pass


    # Enter a parse tree produced by TinyPyParser#stmt.
    def enterStmt(self, ctx:TinyPyParser.StmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#stmt.
    def exitStmt(self, ctx:TinyPyParser.StmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#simple_stmt.
    def enterSimple_stmt(self, ctx:TinyPyParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#simple_stmt.
    def exitSimple_stmt(self, ctx:TinyPyParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#small_stmt.
    def enterSmall_stmt(self, ctx:TinyPyParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#small_stmt.
    def exitSmall_stmt(self, ctx:TinyPyParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#expr_stmt.
    def enterExpr_stmt(self, ctx:TinyPyParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#expr_stmt.
    def exitExpr_stmt(self, ctx:TinyPyParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#testlist_expr.
    def enterTestlist_expr(self, ctx:TinyPyParser.Testlist_exprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#testlist_expr.
    def exitTestlist_expr(self, ctx:TinyPyParser.Testlist_exprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#expr.
    def enterExpr(self, ctx:TinyPyParser.ExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#expr.
    def exitExpr(self, ctx:TinyPyParser.ExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#xor_expr.
    def enterXor_expr(self, ctx:TinyPyParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#xor_expr.
    def exitXor_expr(self, ctx:TinyPyParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#and_expr.
    def enterAnd_expr(self, ctx:TinyPyParser.And_exprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#and_expr.
    def exitAnd_expr(self, ctx:TinyPyParser.And_exprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#shift_expr.
    def enterShift_expr(self, ctx:TinyPyParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#shift_expr.
    def exitShift_expr(self, ctx:TinyPyParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#arith_expr.
    def enterArith_expr(self, ctx:TinyPyParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#arith_expr.
    def exitArith_expr(self, ctx:TinyPyParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#term.
    def enterTerm(self, ctx:TinyPyParser.TermContext):
        pass

    # Exit a parse tree produced by TinyPyParser#term.
    def exitTerm(self, ctx:TinyPyParser.TermContext):
        pass


    # Enter a parse tree produced by TinyPyParser#factor.
    def enterFactor(self, ctx:TinyPyParser.FactorContext):
        pass

    # Exit a parse tree produced by TinyPyParser#factor.
    def exitFactor(self, ctx:TinyPyParser.FactorContext):
        pass


    # Enter a parse tree produced by TinyPyParser#atom.
    def enterAtom(self, ctx:TinyPyParser.AtomContext):
        pass

    # Exit a parse tree produced by TinyPyParser#atom.
    def exitAtom(self, ctx:TinyPyParser.AtomContext):
        pass


    # Enter a parse tree produced by TinyPyParser#number.
    def enterNumber(self, ctx:TinyPyParser.NumberContext):
        pass

    # Exit a parse tree produced by TinyPyParser#number.
    def exitNumber(self, ctx:TinyPyParser.NumberContext):
        pass


    # Enter a parse tree produced by TinyPyParser#integer.
    def enterInteger(self, ctx:TinyPyParser.IntegerContext):
        pass

    # Exit a parse tree produced by TinyPyParser#integer.
    def exitInteger(self, ctx:TinyPyParser.IntegerContext):
        pass


    # Enter a parse tree produced by TinyPyParser#string.
    def enterString(self, ctx:TinyPyParser.StringContext):
        pass

    # Exit a parse tree produced by TinyPyParser#string.
    def exitString(self, ctx:TinyPyParser.StringContext):
        pass


    # Enter a parse tree produced by TinyPyParser#pass_stmt.
    def enterPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#pass_stmt.
    def exitPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        pass


