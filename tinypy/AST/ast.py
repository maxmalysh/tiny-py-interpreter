#
# Some useful stuff here:
# http://greentreesnakes.readthedocs.org/en/latest/index.html
# https://docs.python.org/3/reference/expressions.html#calls
# https://docs.python.org/3/reference/executionmodel.html#naming
#


class Namespace:

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

    def __init__(self, outerScope):
        self.outerScope = outerScope
        self.content = {}

    def get(self, name):
        # search in current scope
        try:
            return self.content[name]
        except KeyError:
            return self.outerScope.get(name)
        finally:
            # FIXME: replace by own runtime exception
            raise NameError()

    def set(self, name):
        pass



    INSTANCE = None

Namespace.INSTANCE = Namespace(None)
Namespace.INSTANCE.content.update(Namespace.builtInFunctions)

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






