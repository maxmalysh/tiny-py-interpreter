from enum import Enum
import operator

#
# Some useful stuff here:
# http://greentreesnakes.readthedocs.org/en/latest/index.html
# https://docs.python.org/3/reference/expressions.html#calls
# https://docs.python.org/3/reference/executionmodel.html#naming
#

builtInFunctions = {
    'print' : print,
    'input' : input,
    'exit'  : exit,
    'len'   : len,
    'str'   : str,
    'int'   : int,
    'float' : float,
    'type'  : type,
}

nameMemory = {}
nameMemory.update(builtInFunctions)


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
        if type(self.body) is not list:
            return self.body.eval()
        else:
            return [stmt.eval() for stmt in self.body]


class EvalExpression(AST):
    def __init__(self, body):
        super().__init__()
        self.body = body

    def eval(self):
        return self.body.eval()

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
    def __init__(self, target, value:Expression):
        super().__init__()
        self.target = target
        self.value = value

    def eval(self):
        lValue = self.target.eval()
        rValue = self.value.eval()
        nameMemory[lValue] = rValue



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


# class ExprStmt(Statement):
#     def __init__(self, value:Expression):
#         super().__init__()
#         self.value = value

#class PassStmt(Statement):
#    def eval(self):
#        return None

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
        self.func = func   # name
        self.args = args

    def eval(self):
        func = self.func.eval()
        evalArgs = [ arg.eval() for arg in self.args ]
        return func(*evalArgs)

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
    class Context(Enum):
        Load = 1
        Store = 2
        Del = 3

    def __init__(self, id, ctx:Context):
        super().__init__()
        self.id = id
        self.ctx = ctx

    def eval(self):
        if self.ctx == Name.Context.Load:
            return nameMemory[self.id]
        elif self.ctx == Name.Context.Store:
            return self.id
        else:
            raise NotImplementedError()

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
