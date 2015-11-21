from parser.TinyPyParser import TinyPyParser
from parser.TinyPyVisitor import TinyPyVisitor
import AST.ast as ast



class StmtVisitorMixin(TinyPyVisitor):

    #
    # Base statements
    #

    # Returns list of statements
    def visitSimple_stmt(self, ctx:TinyPyParser.Simple_stmtContext):
        statements = []

        for smallStmt in ctx.small_stmt():
            statement = self.visit(smallStmt)
            if statement != None:
                statements.append(statement)

        return statements


    #
    # Compound statements
    #


    def visitSuite(self, ctx:TinyPyParser.SuiteContext):
        if ctx.simple_stmt() != None:
            return self.visit(ctx.simple_stmt())

        statements = []

        for stmt in ctx.stmt():
            if stmt.simple_stmt() != None:
                statements += self.visit(stmt.simple_stmt())
            else:
                statements.append(self.visit(stmt))

        return statements


    def visitIf_stmt(self, ctx:TinyPyParser.If_stmtContext):
        test = self.visit(ctx.test())
        suite = self.visit(ctx.suite())
        orelse = []

        if ctx.if_else() != None:
            orelse = self.visit(ctx.if_else().suite())

        for node in ctx.if_elif():
            nodeTest = self.visit(node.test())
            nodeSuite = self.visit(node.suite())
            # FIXME - PUT ELIF CONDITIONS TO THE ORELSE

        return ast.IfStmt(test=test, body=suite, orelse=orelse)


    def visitWhile_stmt(self, ctx:TinyPyParser.While_stmtContext):
        test = self.visit(ctx.test())
        suite = self.visit(ctx.suite())

        return ast.WhileStmt(test=test, body=suite, orelse=[])

    #
    # Small statements
    #

    def visitExprStmtAssign(self, ctx:TinyPyParser.ExprStmtAssignContext):
        name = ctx.NAME().getText()
        expr = self.visit(ctx.test())

        nameNode = ast.Name(id=name, ctx=ast.Name.Context.Store)

        return ast.AssignStmt(target=nameNode, value=expr)


    def visitExprStmtAugmented(self, ctx:TinyPyParser.ExprStmtAugmentedContext):
        name = ctx.NAME().getText()
        value = self.visit(ctx.test())
        op = ctx.augassign().getText()

        return ast.AugAssignStmt(name=name, value=value, op=op)

