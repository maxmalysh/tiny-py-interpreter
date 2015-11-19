# Generated from /Users/apple/Development/tiny-py-interpreter/tinypy/parser/TinyPy.g4 by ANTLR 4.5.1
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


    # Enter a parse tree produced by TinyPyParser#single_input.
    def enterSingle_input(self, ctx:TinyPyParser.Single_inputContext):
        pass

    # Exit a parse tree produced by TinyPyParser#single_input.
    def exitSingle_input(self, ctx:TinyPyParser.Single_inputContext):
        pass


    # Enter a parse tree produced by TinyPyParser#eval_input.
    def enterEval_input(self, ctx:TinyPyParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by TinyPyParser#eval_input.
    def exitEval_input(self, ctx:TinyPyParser.Eval_inputContext):
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


    # Enter a parse tree produced by TinyPyParser#compound_stmt.
    def enterCompound_stmt(self, ctx:TinyPyParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#compound_stmt.
    def exitCompound_stmt(self, ctx:TinyPyParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#if_stmt.
    def enterIf_stmt(self, ctx:TinyPyParser.If_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#if_stmt.
    def exitIf_stmt(self, ctx:TinyPyParser.If_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#while_stmt.
    def enterWhile_stmt(self, ctx:TinyPyParser.While_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#while_stmt.
    def exitWhile_stmt(self, ctx:TinyPyParser.While_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#funcdef.
    def enterFuncdef(self, ctx:TinyPyParser.FuncdefContext):
        pass

    # Exit a parse tree produced by TinyPyParser#funcdef.
    def exitFuncdef(self, ctx:TinyPyParser.FuncdefContext):
        pass


    # Enter a parse tree produced by TinyPyParser#parameters.
    def enterParameters(self, ctx:TinyPyParser.ParametersContext):
        pass

    # Exit a parse tree produced by TinyPyParser#parameters.
    def exitParameters(self, ctx:TinyPyParser.ParametersContext):
        pass


    # Enter a parse tree produced by TinyPyParser#param_argslist.
    def enterParam_argslist(self, ctx:TinyPyParser.Param_argslistContext):
        pass

    # Exit a parse tree produced by TinyPyParser#param_argslist.
    def exitParam_argslist(self, ctx:TinyPyParser.Param_argslistContext):
        pass


    # Enter a parse tree produced by TinyPyParser#suite.
    def enterSuite(self, ctx:TinyPyParser.SuiteContext):
        pass

    # Exit a parse tree produced by TinyPyParser#suite.
    def exitSuite(self, ctx:TinyPyParser.SuiteContext):
        pass


    # Enter a parse tree produced by TinyPyParser#ExprStmtExpr.
    def enterExprStmtExpr(self, ctx:TinyPyParser.ExprStmtExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#ExprStmtExpr.
    def exitExprStmtExpr(self, ctx:TinyPyParser.ExprStmtExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#ExprStmtAssign.
    def enterExprStmtAssign(self, ctx:TinyPyParser.ExprStmtAssignContext):
        pass

    # Exit a parse tree produced by TinyPyParser#ExprStmtAssign.
    def exitExprStmtAssign(self, ctx:TinyPyParser.ExprStmtAssignContext):
        pass


    # Enter a parse tree produced by TinyPyParser#flow_stmt.
    def enterFlow_stmt(self, ctx:TinyPyParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#flow_stmt.
    def exitFlow_stmt(self, ctx:TinyPyParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#return_stmt.
    def enterReturn_stmt(self, ctx:TinyPyParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#return_stmt.
    def exitReturn_stmt(self, ctx:TinyPyParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#pass_stmt.
    def enterPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#pass_stmt.
    def exitPass_stmt(self, ctx:TinyPyParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#break_stmt.
    def enterBreak_stmt(self, ctx:TinyPyParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#break_stmt.
    def exitBreak_stmt(self, ctx:TinyPyParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#continue_stmt.
    def enterContinue_stmt(self, ctx:TinyPyParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by TinyPyParser#continue_stmt.
    def exitContinue_stmt(self, ctx:TinyPyParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by TinyPyParser#Comparison.
    def enterComparison(self, ctx:TinyPyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by TinyPyParser#Comparison.
    def exitComparison(self, ctx:TinyPyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by TinyPyParser#OrTest.
    def enterOrTest(self, ctx:TinyPyParser.OrTestContext):
        pass

    # Exit a parse tree produced by TinyPyParser#OrTest.
    def exitOrTest(self, ctx:TinyPyParser.OrTestContext):
        pass


    # Enter a parse tree produced by TinyPyParser#AndTest.
    def enterAndTest(self, ctx:TinyPyParser.AndTestContext):
        pass

    # Exit a parse tree produced by TinyPyParser#AndTest.
    def exitAndTest(self, ctx:TinyPyParser.AndTestContext):
        pass


    # Enter a parse tree produced by TinyPyParser#TestExpr.
    def enterTestExpr(self, ctx:TinyPyParser.TestExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#TestExpr.
    def exitTestExpr(self, ctx:TinyPyParser.TestExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#NotTest.
    def enterNotTest(self, ctx:TinyPyParser.NotTestContext):
        pass

    # Exit a parse tree produced by TinyPyParser#NotTest.
    def exitNotTest(self, ctx:TinyPyParser.NotTestContext):
        pass


    # Enter a parse tree produced by TinyPyParser#comp_op.
    def enterComp_op(self, ctx:TinyPyParser.Comp_opContext):
        pass

    # Exit a parse tree produced by TinyPyParser#comp_op.
    def exitComp_op(self, ctx:TinyPyParser.Comp_opContext):
        pass


    # Enter a parse tree produced by TinyPyParser#MulDivMod.
    def enterMulDivMod(self, ctx:TinyPyParser.MulDivModContext):
        pass

    # Exit a parse tree produced by TinyPyParser#MulDivMod.
    def exitMulDivMod(self, ctx:TinyPyParser.MulDivModContext):
        pass


    # Enter a parse tree produced by TinyPyParser#BitXor.
    def enterBitXor(self, ctx:TinyPyParser.BitXorContext):
        pass

    # Exit a parse tree produced by TinyPyParser#BitXor.
    def exitBitXor(self, ctx:TinyPyParser.BitXorContext):
        pass


    # Enter a parse tree produced by TinyPyParser#BitOr.
    def enterBitOr(self, ctx:TinyPyParser.BitOrContext):
        pass

    # Exit a parse tree produced by TinyPyParser#BitOr.
    def exitBitOr(self, ctx:TinyPyParser.BitOrContext):
        pass


    # Enter a parse tree produced by TinyPyParser#AddSub.
    def enterAddSub(self, ctx:TinyPyParser.AddSubContext):
        pass

    # Exit a parse tree produced by TinyPyParser#AddSub.
    def exitAddSub(self, ctx:TinyPyParser.AddSubContext):
        pass


    # Enter a parse tree produced by TinyPyParser#BitAnd.
    def enterBitAnd(self, ctx:TinyPyParser.BitAndContext):
        pass

    # Exit a parse tree produced by TinyPyParser#BitAnd.
    def exitBitAnd(self, ctx:TinyPyParser.BitAndContext):
        pass


    # Enter a parse tree produced by TinyPyParser#Shifts.
    def enterShifts(self, ctx:TinyPyParser.ShiftsContext):
        pass

    # Exit a parse tree produced by TinyPyParser#Shifts.
    def exitShifts(self, ctx:TinyPyParser.ShiftsContext):
        pass


    # Enter a parse tree produced by TinyPyParser#FactorExpr.
    def enterFactorExpr(self, ctx:TinyPyParser.FactorExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#FactorExpr.
    def exitFactorExpr(self, ctx:TinyPyParser.FactorExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#unaryExpr.
    def enterUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#unaryExpr.
    def exitUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#parenExpr.
    def enterParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#parenExpr.
    def exitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#funcInvokExpr.
    def enterFuncInvokExpr(self, ctx:TinyPyParser.FuncInvokExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#funcInvokExpr.
    def exitFuncInvokExpr(self, ctx:TinyPyParser.FuncInvokExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#atomExpr.
    def enterAtomExpr(self, ctx:TinyPyParser.AtomExprContext):
        pass

    # Exit a parse tree produced by TinyPyParser#atomExpr.
    def exitAtomExpr(self, ctx:TinyPyParser.AtomExprContext):
        pass


    # Enter a parse tree produced by TinyPyParser#atom.
    def enterAtom(self, ctx:TinyPyParser.AtomContext):
        pass

    # Exit a parse tree produced by TinyPyParser#atom.
    def exitAtom(self, ctx:TinyPyParser.AtomContext):
        pass


    # Enter a parse tree produced by TinyPyParser#funcinvoke.
    def enterFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        pass

    # Exit a parse tree produced by TinyPyParser#funcinvoke.
    def exitFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        pass


    # Enter a parse tree produced by TinyPyParser#arglist.
    def enterArglist(self, ctx:TinyPyParser.ArglistContext):
        pass

    # Exit a parse tree produced by TinyPyParser#arglist.
    def exitArglist(self, ctx:TinyPyParser.ArglistContext):
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


