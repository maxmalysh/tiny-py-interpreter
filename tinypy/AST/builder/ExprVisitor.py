from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor

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

        firstSymbolType = ctx.comp_op().children[0].symbol.type

        if firstSymbolType == TinyPyParser.IN:
            op = AST.expr.Compare.Op.IN
        elif firstSymbolType == TinyPyParser.IS:
            op = AST.expr.Compare.Op.IS

        if len(ctx.comp_op().children) == 2:
            secondSymbolType = ctx.comp_op().children[1].symbol.type

            if firstSymbolType == TinyPyParser.NOT and secondSymbolType == TinyPyParser.IN:
                op = AST.expr.Compare.Op.NOT_IN
            elif firstSymbolType == TinyPyParser.IS and secondSymbolType == TinyPyParser.NOT:
                op = AST.expr.Compare.Op.IS_NOT
            else:
                raise ValueError("Unexpected binary comparison operation")

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

        # Visit other nodes:  collectiondefs / nameaccess / number / string
        return self.visitChildren(ctx)


    #
    # Name access: PlainName, FuncInvoke, SubName
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

    def visitSubName(self, ctx:TinyPyParser.SubNameContext):
        nameNode = AST.expr.Name(id = ctx.NAME().getText(), ctx=AST.expr.Name.Context.Load)
        subscript = self.visit(ctx.subscript())
        return AST.stmt.Subscript(value=nameNode, slice=subscript, ctx=AST.stmt.Subscript.Context.Load)

    #
    # Index and slice operations
    #

    def visitSubscriptIndex(self, ctx:TinyPyParser.SubscriptIndexContext):
        test = self.visit(ctx.test())
        return AST.stmt.Index(value=test)

    def visitSubscriptSlice(self, ctx:TinyPyParser.SubscriptSliceContext):
        lower = upper = None

        if ctx.test(0) != None:
            lower = self.visit(ctx.test(0))

        if ctx.test(1) != None:
            upper = self.visit(ctx.test(1))

        return AST.stmt.Slice(lower=lower, upper=upper, step=None)
    #
    # Collection definitions
    #

    def visitDictMaker(self, ctx:TinyPyParser.DictMakerContext):
        if ctx.dictorsetmaker() != None:
            return self.visit(ctx.dictorsetmaker())

        return AST.expr.DictContainer({})

    def visitSetmaker(self, ctx:TinyPyParser.SetmakerContext):
        result = set({})
        for test in ctx.test():
            result.add(self.visit(test))
        return AST.expr.SetContainer(result)


    def visitDictormaker(self, ctx:TinyPyParser.DictormakerContext):
        if ctx.test(0) != None:
            left = self.visit(ctx.test(0))
            right = self.visit(ctx.test(1))
            return AST.expr.DictContainer({left : right})

        if ctx.dictormaker(0) != None:
            left = self.visit(ctx.dictormaker(0))
            right = self.visit(ctx.dictormaker(1))

            result = left.copy()
            result.update(right)

            if type(result) is not AST.expr.DictContainer:
                return AST.expr.DictContainer(result)
            else:
                return result

    def visitListMaker(self, ctx:TinyPyParser.ListMakerContext):
        if ctx.testlist_comp() == None:
            return AST.expr.ListContainer([])

        return AST.expr.ListContainer(self.visit(ctx.testlist_comp()))

    def visitTupleMaker(self, ctx:TinyPyParser.TupleMakerContext):
        if ctx.testlist_comp() == None:
            return AST.expr.TupleContainer(())

        return AST.expr.TupleContainer(tuple(self.visit(ctx.testlist_comp())))

    def visitTestlist_comp(self, ctx:TinyPyParser.Testlist_compContext):
        if ctx.test() != None:
            return [self.visit(ctx.test())]

        if ctx.testlist_comp(1) == None:
            return self.visit(ctx.testlist_comp(0))

        left = self.visit(ctx.testlist_comp(0))
        right = self.visit(ctx.testlist_comp(1))
        result = []

        if type(left) is list:
            result += left
        else:
            result.append(left)

        if type(right) is list:
            result += right
        else:
            result.append(right)

        return result

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
