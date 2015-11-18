from enum import Enum

#
# Some useful stuff here:
# http://greentreesnakes.readthedocs.org/en/latest/index.html
# https://docs.python.org/3/reference/expressions.html#calls


class AST(object):
    def eval(self):
        raise NotImplementedError()


""" Input types """
class Module(AST):
    def __init__(self, body:[]):
        super().__init__()
        self.body = body

    def eval(self):
        for stmt in self.body:
            stmt.eval()


class Interactive(AST):
    def __init__(self, body:[]):
        super().__init__()
        self.body = body

    def eval(self):
        for stmt in self.body:
            stmt.eval()

""" Base node types """


class Expression(AST):
    def __init__(self):
        super().__init__()


class Statement(AST):
    def __init__(self):
        super().__init__()


""" Statements begin here """


class FunctionDef(Statement):
    def __init__(self, ):
        super().__init__()


class ReturnStmt(Statement):
    def __init__(self):
        super().__init__()


# An assignment. targets is a list of nodes, and value is a single node.
#
# Multiple nodes in targets represents assigning the same value to each.
# Unpacking is represented by putting a Tuple or List within targets.
class AssignStmt(Statement):
    def __init__(self, targets, value:Expression):
        super().__init__()
        self.targets = targets
        self.value = value


class WhileStmt(Statement):
    def __init__(self):
        super().__init__()


class IfStmt(Statement):
    def __init__(self):
        super().__init__()


class ExprStmt(Statement):
    def __init__(self, value:Expression):
        super().__init__()
        self.value = value

""" Expressions begin here """


#
# Binary operations
#

class BinOp(Expression):
    def __init__(self, left:Expression, right:Expression):
        super().__init__()
        self.left = left
        self.right = right

class AddOp(BinOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class SubOp(BinOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class MultOp(BinOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class DivOp(BinOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


#
# Unary operations
#
class UnaryOp(Expression):
    def __init__(self, op, operand:Expression):
        super().__init__()
        self.op = op
        self.operand = operand

    def eval(self):
        if self.op == '+':
            return self.operand.eval()
        elif self.op == '-':
            return -(self.operand.eval())
        else:
            raise ValueError('Unsupported unary operation!')




#
# Function call
#     @param func is the function, which will often be a Name object.
#     @args holds a list of the arguments passed by position.
#
class CallExpr(Expression):
    def __init__(self, func, args):
        super().__init__()
        self.func = func
        self.args = args

    def eval(self):
        raise NotImplementedError()

#
# Leaf values
#
class Num(Expression):

    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value


class Str(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        return self.value


#
# Represents None, False and True literals.
#
class NameConstant(Expression):
    nameTable = { 'None' : None, 'True': True, 'False': False }

    def __init__(self, name):
        super().__init__()
        self.name = name

    def eval(self):
        try:
            return NameConstant.nameTable[self.name]
        except KeyError:
            raise ValueError("Wrong name constant")

#
# A variable name.
#     @id holds the name as a string
#     @ctx is one of the following types: @Load / @Store / @Del
#
class Name(Expression):
    def __init__(self, id, ctx):
        super().__init__()
        self.id = id
        self.ctx = ctx

