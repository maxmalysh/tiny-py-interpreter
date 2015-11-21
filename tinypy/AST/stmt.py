from enum import Enum
from AST.ast import Statement, Expression
from AST.expr import AddOp, SubOp, MultOp, DivOp, ModOp, BitAndOp, BitOrOp, BitXorOp, LshiftOp, RshiftOp, Name

import AST.ast
from AST.ast import Namespace




class ReturnStmt(Statement):
    def __init__(self):
        super().__init__()


#
# An if statement.
#    test holds a single node, such as a Compare node.
#    body and orelse each hold a list of nodes.
#
# elif clauses don’t have a special representation in the AST, but rather
# appear as extra If nodes within the orelse section of the previous one.
#
# Optional clauses such as else are stored as an empty list if they’re not present.
#
class IfStmt(Statement):
    def __init__(self, test, body:[], orelse:[]):
        super().__init__()
        self.test = test
        self.body = body
        self.orelse = orelse

    def eval(self):
        test = self.test.eval()
        if test == True:
            return [stmt.eval() for stmt in self.body]
        else:
            return [stmt.eval() for stmt in self.orelse]


class WhileStmt(Statement):
    def __init__(self, test, body:[], orelse:[]):
        super().__init__()
        self.test = test
        self.body = body

    def eval(self):
        result = []

        # FIXME: CHECK FOR TWO NESTED "WHILE"
        while self.test.eval() == True:
            result.append([stmt.eval() for stmt in self.body])

        return result


# An assignment. targets is a list of nodes, and value is a single node.
#
# Multiple nodes in targets represents assigning the same value to each.
# Unpacking is represented by putting a Tuple or List within targets.
class AssignStmt(Statement):
    def __init__(self, target, value:Expression):
        super().__init__()
        self.target = target
        self.value = value

    def eval(self):
        lValue = self.target.eval()
        rValue = self.value.eval()
        Namespace.INSTANCE.content[lValue] = rValue



class AugAssignStmt(AssignStmt):
    opTable = {
        '+=' : AddOp,
        '-=' : SubOp,
        '*=' : MultOp,
        '/=' : DivOp,
        '%=' : ModOp,
        '&=' : BitAndOp,
        '|=' : BitOrOp,
        '^=' : BitXorOp,
        '<<=' : LshiftOp,
        '>>=' : RshiftOp,
    }

    def __init__(self, name, value, op):
        nameNodeLoad  = Name(id=name, ctx=Name.Context.Load)
        nameNodeStore = Name(id=name, ctx=Name.Context.Store)

        binOp = AugAssignStmt.opTable[op](left=nameNodeLoad, right=value)
        super().__init__(target=nameNodeStore, value=binOp)








# class ExprStmt(Statement):
#     def __init__(self, value:Expression):
#         super().__init__()
#         self.value = value

#class PassStmt(Statement):
#    def eval(self):
#        return None





