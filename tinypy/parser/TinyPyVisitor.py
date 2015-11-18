# Generated from /Users/apple/Development/tiny-py-interpreter/tinypy/parser/TinyPy.g4 by ANTLR 4.5.1
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


    # Visit a parse tree produced by TinyPyParser#single_input.
    def visitSingle_input(self, ctx:TinyPyParser.Single_inputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#eval_input.
    def visitEval_input(self, ctx:TinyPyParser.Eval_inputContext):
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


    # Visit a parse tree produced by TinyPyParser#compound_stmt.
    def visitCompound_stmt(self, ctx:TinyPyParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#if_stmt.
    def visitIf_stmt(self, ctx:TinyPyParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#while_stmt.
    def visitWhile_stmt(self, ctx:TinyPyParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#funcdef.
    def visitFuncdef(self, ctx:TinyPyParser.FuncdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#parameters.
    def visitParameters(self, ctx:TinyPyParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#param_argslist.
    def visitParam_argslist(self, ctx:TinyPyParser.Param_argslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#suite.
    def visitSuite(self, ctx:TinyPyParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#expr_stmt.
    def visitExpr_stmt(self, ctx:TinyPyParser.Expr_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#flow_stmt.
    def visitFlow_stmt(self, ctx:TinyPyParser.Flow_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#return_stmt.
    def visitReturn_stmt(self, ctx:TinyPyParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#pass_stmt.
    def visitPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#break_stmt.
    def visitBreak_stmt(self, ctx:TinyPyParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#continue_stmt.
    def visitContinue_stmt(self, ctx:TinyPyParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#test.
    def visitTest(self, ctx:TinyPyParser.TestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#or_test.
    def visitOr_test(self, ctx:TinyPyParser.Or_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#and_test.
    def visitAnd_test(self, ctx:TinyPyParser.And_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#not_test.
    def visitNot_test(self, ctx:TinyPyParser.Not_testContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#comparison.
    def visitComparison(self, ctx:TinyPyParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#comp_op.
    def visitComp_op(self, ctx:TinyPyParser.Comp_opContext):
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


    # Visit a parse tree produced by TinyPyParser#unaryExpr.
    def visitUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#parenExpr.
    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#funcInvokExpr.
    def visitFuncInvokExpr(self, ctx:TinyPyParser.FuncInvokExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#atomExpr.
    def visitAtomExpr(self, ctx:TinyPyParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#atom.
    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#funcinvoke.
    def visitFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#arglist.
    def visitArglist(self, ctx:TinyPyParser.ArglistContext):
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



del TinyPyParser