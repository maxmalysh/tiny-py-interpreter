from enum import Enum
import operator

from AST.ast import Expression


#
# Binary operations
#
import runtime.Memory


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
        left  = self.left.eval()
        right = self.right.eval()

        if right == 0:
            raise ZeroDivisionError()

        return  left/right

class ModOp(BinOp):
    def eval(self):
        return self.left.eval() % self.right.eval()

class LshiftOp(BinOp):
    def eval(self):
        return self.left.eval() << self.right.eval()

class RshiftOp(BinOp):
    def eval(self):
        return self.left.eval() >> self.right.eval()

class BitAndOp(BinOp):
    def eval(self):
        return self.left.eval() & self.right.eval()

class BitXorOp(BinOp):
    def eval(self):
        return self.left.eval() ^ self.right.eval()

class BitOrOp(BinOp):
    def eval(self):
        return self.left.eval() | self.right.eval()

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
# Comparisons
#

class Compare(Expression):

    class Op(Enum):
        AND = 1
        OR  = 2
        NOT = 3
        IN  = 4
        IS  = 5
        NOT_IN = 6
        IS_NOT = 7

    opTable = {
        '<'  : operator.lt,
        '>'  : operator.gt,
        '==' : operator.eq,
        '>=' : operator.ge,
        '<=' : operator.le,
        '!=' : operator.ne,
        Op.AND : operator.__and__,
        Op.OR  : operator.__or__,
        Op.NOT : operator.__not__,
        Op.IS  : operator.is_,
        Op.IS_NOT : operator.is_not,
    }

    def __init__(self, op):
        super().__init__()
        self.op = op

class BinaryComp(Compare):
    def __init__(self, left, right, op):
        super().__init__(op=op)
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        return Compare.opTable[self.op](left, right)

class UnaryComp(Compare):
    def __init__(self, operand, op):
        super().__init__(op=op)
        self.operand = operand

    def eval(self):
        operand = self.operand.eval()
        return Compare.opTable[self.op](operand)


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
    class Context(Enum):
        Load = 1
        Store = 2
        Del = 3

    def __init__(self, id, ctx:Context):
        super().__init__()
        self.id = id
        self.ctx = ctx
        self.nameSpace = runtime.Memory.CurrentNamespace

    def eval(self):
        if self.ctx == Name.Context.Load:
            return self.getNamespace().get(name=self.id)
        elif self.ctx == Name.Context.Store:
            return self.id
        else:
            raise NotImplementedError()

    def getNamespace(self):
        return self.nameSpace
#
# Function call
#     @param func is the function, which will often be a Name object.
#     @args holds a list of the arguments passed by position.
#
class CallExpr(Expression):
    def __init__(self, func, args):
        super().__init__()
        self.func = func   # name
        self.args = args

    def eval(self):
        func = self.func.eval()
        evalArgs = [ arg.eval() for arg in self.args ]
        return func(*evalArgs)


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