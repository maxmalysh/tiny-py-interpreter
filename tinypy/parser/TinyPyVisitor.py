# Generated from parser/TinyPy.g4 by ANTLR 4.5.1
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


    # Visit a parse tree produced by TinyPyParser#if_elif.
    def visitIf_elif(self, ctx:TinyPyParser.If_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#if_else.
    def visitIf_else(self, ctx:TinyPyParser.If_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#while_stmt.
    def visitWhile_stmt(self, ctx:TinyPyParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#for_stmt.
    def visitFor_stmt(self, ctx:TinyPyParser.For_stmtContext):
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


    # Visit a parse tree produced by TinyPyParser#ExprStmtExpr.
    def visitExprStmtExpr(self, ctx:TinyPyParser.ExprStmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#ExprStmtAssign.
    def visitExprStmtAssign(self, ctx:TinyPyParser.ExprStmtAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#ExprStmtAugmented.
    def visitExprStmtAugmented(self, ctx:TinyPyParser.ExprStmtAugmentedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#augassign.
    def visitAugassign(self, ctx:TinyPyParser.AugassignContext):
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


    # Visit a parse tree produced by TinyPyParser#Comparison.
    def visitComparison(self, ctx:TinyPyParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#OrTest.
    def visitOrTest(self, ctx:TinyPyParser.OrTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#AndTest.
    def visitAndTest(self, ctx:TinyPyParser.AndTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#TestExpr.
    def visitTestExpr(self, ctx:TinyPyParser.TestExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#NotTest.
    def visitNotTest(self, ctx:TinyPyParser.NotTestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#comp_op.
    def visitComp_op(self, ctx:TinyPyParser.Comp_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#MulDivMod.
    def visitMulDivMod(self, ctx:TinyPyParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#BitXor.
    def visitBitXor(self, ctx:TinyPyParser.BitXorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#BitOr.
    def visitBitOr(self, ctx:TinyPyParser.BitOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#AddSub.
    def visitAddSub(self, ctx:TinyPyParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#BitAnd.
    def visitBitAnd(self, ctx:TinyPyParser.BitAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#Shifts.
    def visitShifts(self, ctx:TinyPyParser.ShiftsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#FactorExpr.
    def visitFactorExpr(self, ctx:TinyPyParser.FactorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#unaryExpr.
    def visitUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#parenExpr.
    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#atomExpr.
    def visitAtomExpr(self, ctx:TinyPyParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#atom.
    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#FuncInvoke.
    def visitFuncInvoke(self, ctx:TinyPyParser.FuncInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#PlainName.
    def visitPlainName(self, ctx:TinyPyParser.PlainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#DottedName.
    def visitDottedName(self, ctx:TinyPyParser.DottedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#SubName.
    def visitSubName(self, ctx:TinyPyParser.SubNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#DictMaker.
    def visitDictMaker(self, ctx:TinyPyParser.DictMakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#ListMaker.
    def visitListMaker(self, ctx:TinyPyParser.ListMakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#TupleMaker.
    def visitTupleMaker(self, ctx:TinyPyParser.TupleMakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#testlist_comp.
    def visitTestlist_comp(self, ctx:TinyPyParser.Testlist_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#funcinvoke.
    def visitFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#arglist.
    def visitArglist(self, ctx:TinyPyParser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#SubscriptIndex.
    def visitSubscriptIndex(self, ctx:TinyPyParser.SubscriptIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#SubscriptSlice.
    def visitSubscriptSlice(self, ctx:TinyPyParser.SubscriptSliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#dictorsetmaker.
    def visitDictorsetmaker(self, ctx:TinyPyParser.DictorsetmakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#dictormaker.
    def visitDictormaker(self, ctx:TinyPyParser.DictormakerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TinyPyParser#setmaker.
    def visitSetmaker(self, ctx:TinyPyParser.SetmakerContext):
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