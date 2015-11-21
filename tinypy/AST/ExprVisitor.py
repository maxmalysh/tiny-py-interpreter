from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor
import AST.ast as ast


class ExprVisitorMixin(TinyPyVisitor):

    #
    # Tests (comparisons)
    #

    def visitComparison(self, ctx:TinyPyParser.ComparisonContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        op = ctx.comp_op().getText()
        return ast.BinaryComp(left=left, right=right, op=op)

    def visitNotTest(self, ctx:TinyPyParser.NotTestContext):
        test = self.visit(ctx.test())
        return ast.UnaryComp(operand=test, op=ast.Compare.Op.NOT)

    def visitAndTest(self, ctx:TinyPyParser.AndTestContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return ast.BinaryComp(left=left, right=right, op=ast.Compare.Op.AND)

    def visitOrTest(self, ctx:TinyPyParser.AndTestContext):
        left  = self.visit(ctx.test(0))
        right = self.visit(ctx.test(1))
        return ast.BinaryComp(left=left, right=right, op=ast.Compare.Op.OR)

    #
    # Arithmetic (@expr rule)
    #

    binaryExprTable = {
        TinyPyParser.ADD         : ast.AddOp,
        TinyPyParser.MINUS       : ast.SubOp,
        TinyPyParser.STAR        : ast.MultOp,
        TinyPyParser.DIV         : ast.DivOp,
        TinyPyParser.MOD         : ast.ModOp,
        TinyPyParser.LEFT_SHIFT  : ast.LshiftOp,
        TinyPyParser.RIGHT_SHIFT : ast.RshiftOp,
        TinyPyParser.AND_OP      : ast.BitAndOp,
        TinyPyParser.XOR         : ast.BitXorOp,
        TinyPyParser.OR_OP       : ast.BitOrOp,
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
        return ast.UnaryOp(op=ctx.op.text, operand=operand)


    def visitParenExpr(self, ctx:TinyPyParser.ParenExprContext):
        return self.visit(ctx.test())


    def visitAtom(self, ctx:TinyPyParser.AtomContext):
        if ctx.NONE() != None:
            return ast.NameConstant('None')
        elif ctx.TRUE() != None:
            return ast.NameConstant('True')
        elif ctx.FALSE() != None:
            return ast.NameConstant('False')
        elif ctx.NAME() != None:
            return ast.Name(id=ctx.NAME().getText(), ctx=ast.Name.Context.Load)

        # Visit funcinvoke / number / string
        return self.visitChildren(ctx)


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

        funcName = ast.Name(name, ast.Name.Context.Load)
        return ast.CallExpr(func=funcName, args=args)

    #
    # Strings and numbers
    #

    def visitNumber(self, ctx:TinyPyParser.NumberContext):
        if ctx.integer() != None:
            return self.visit(ctx.integer())

        elif ctx.FLOAT_NUMBER() != None:
            number = float(ctx.FLOAT_NUMBER().getText())
            return ast.Num(number)

        raise ValueError()

    def visitInteger(self, ctx:TinyPyParser.IntegerContext):
        if ctx.DECIMAL_INTEGER() != None:
            decimal = int(ctx.DECIMAL_INTEGER().getText())
            return ast.Num(decimal)

        elif ctx.HEX_INTEGER() != None:
            hex = int(ctx.HEX_INTEGER().getText(), 16)
            return ast.Num(hex)

        raise ValueError()

    def visitString(self, ctx:TinyPyParser.StringContext):
        node = ctx.STRING_LITERAL()
        if node != None:
            text = node.getText()[1:-1]
            return ast.Str(text)

        raise ValueError()
