from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor

import AST.ast as ast
import AST.expr
import AST.stmt

class ExprVisitorMixin(TinyPyVisitor):

    #
    # Tests (comparisons)
    #

    def visitComparison(self, ctx:TinyPyParser.ComparisonContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        op = ctx.comp_op().getText()
        return AST.expr.BinaryComp(left=left, right=right, op=op)

    def visitNotTest(self, ctx:TinyPyParser.NotTestContext):
        test = self.visit(ctx.test())
        return AST.expr.UnaryComp(operand=test, op=AST.expr.Compare.Op.NOT)

    def visitAndTest(self, ctx:TinyPyParser.AndTestContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.AND)

    def visitOrTest(self, ctx:TinyPyParser.AndTestContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return AST.expr.BinaryComp(left=left, right=right, op=AST.expr.Compare.Op.OR)

    #
    # Arithmetic (@expr rule)
    #

    binaryExprTable = {
        TinyPyParser.ADD         : AST.expr.AddOp,
        TinyPyParser.MINUS       : AST.expr.SubOp,
        TinyPyParser.STAR        : AST.expr.MultOp,
        TinyPyParser.DIV         : AST.expr.DivOp,
        TinyPyParser.MOD         : AST.expr.ModOp,
        TinyPyParser.LEFT_SHIFT  : AST.expr.LshiftOp,
        TinyPyParser.RIGHT_SHIFT : AST.expr.RshiftOp,
        TinyPyParser.AND_OP      : AST.expr.BitAndOp,
        TinyPyParser.XOR         : AST.expr.BitXorOp,
        TinyPyParser.OR_OP       : AST.expr.BitOrOp,
    }

    def visitGenericExpr(self, ctx):
        left  = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        try:
            return ExprVisitorMixin.binaryExprTable[ctx.op.type](left, right)
        except KeyError:
            raise ValueError("Unexpected op type")

    def visitMulDivMod(self, ctx:TinyPyParser.MulDivModContext):
        return self.visitGenericExpr(ctx)

    def visitAddSub(self, ctx:TinyPyParser.AddSubContext):
        return self.visitGenericExpr(ctx)

    def visitShifts(self, ctx:TinyPyParser.ShiftsContext):
        return self.visitGenericExpr(ctx)

    def visitBitAnd(self, ctx:TinyPyParser.BitAndContext):
        return self.visitGenericExpr(ctx)

    def visitBitXor(self, ctx:TinyPyParser.BitXorContext):
        return self.visitGenericExpr(ctx)

    def visitBitOr(self, ctx:TinyPyParser.BitOrContext):
        return self.visitGenericExpr(ctx)

    #
    # Factor rule
    #

    def visitUnaryExpr(self, ctx:TinyPyParser.UnaryExprContext):
        operand = ctx.factor().accept(self)
        return AST.expr.UnaryOp(op=ctx.op.text, operand=operand)


    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visit(ctx.test())


    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        if ctx.NONE() != None:
            return AST.expr.NameConstant('None')
        elif ctx.TRUE() != None:
            return AST.expr.NameConstant('True')
        elif ctx.FALSE() != None:
            return AST.expr.NameConstant('False')

        if ctx.dictorsetmaker() != None:
            return self.visit(ctx.dictorsetmaker())

        # Visit other nodes:  nameaccess / number / string
        return self.visitChildren(ctx)


    #
    # Name access
    #

    def visitPlainName(self, ctx:TinyPyParser.PlainNameContext):
        return AST.expr.Name(id=ctx.NAME().getText(), ctx=AST.expr.Name.Context.Load)

    def visitFuncInvoke(self, ctx:TinyPyParser.FuncInvokeContext):
        name = ctx.NAME().getText()
        args = []

        if ctx.arglist() != None:
            for argStmt in ctx.arglist().test():
                arg = self.visit(argStmt)
                if arg != None:
                    args.append(arg)

        funcName = AST.stmt.Name(name, AST.stmt.Name.Context.Load)
        return AST.expr.CallExpr(func=funcName, args=args)


    #
    # Funcinvoke and arglist
    #

    def visitFuncinvoke(self, ctx:TinyPyParser.FuncinvokeContext):
        name = ctx.NAME().getText()
        args = []

        if ctx.arglist() != None:
            for argStmt in ctx.arglist().test():
                arg = self.visit(argStmt)
                if arg != None:
                    args.append(arg)

        funcName = AST.stmt.Name(name, AST.stmt.Name.Context.Load)
        return AST.expr.CallExpr(func=funcName, args=args)

    #
    # Strings and numbers
    #

    def visitNumber(self, ctx:TinyPyParser.NumberContext):
        if ctx.integer() != None:
            return self.visit(ctx.integer())

        elif ctx.FLOAT_NUMBER() != None:
            number = float(ctx.FLOAT_NUMBER().getText())
            return AST.expr.Num(number)

        raise ValueError()

    def visitInteger(self, ctx:TinyPyParser.IntegerContext):
        if ctx.DECIMAL_INTEGER() != None:
            decimal = int(ctx.DECIMAL_INTEGER().getText())
            return AST.expr.Num(decimal)

        elif ctx.HEX_INTEGER() != None:
            hex = int(ctx.HEX_INTEGER().getText(), 16)
            return AST.expr.Num(hex)

        elif ctx.BIN_INTEGER() != None:
            bin = int(ctx.BIN_INTEGER().getText(), 2)
            return AST.expr.Num(bin)

        elif ctx.OCT_INTEGER() != None:
            oct = int(ctx.OCT_INTEGER().getText(), 8)
            return AST.expr.Num(oct)

        raise ValueError()

    def visitString(self, ctx:TinyPyParser.StringContext):
        node = ctx.STRING_LITERAL()
        if node != None:
            text = node.getText()[1:-1]
            return AST.expr.Str(text)

        raise ValueError()
