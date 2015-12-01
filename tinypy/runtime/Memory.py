

#
# Looks like we have to pass namespace instance to every @Name node;
# Alternatively, we can make every node being able to retreive namespace by its own.
# How? Probably, enclosing statement should provide such API, so we'll pass enclosing statements
# as arguments for expressions, and @Expression will have a method "retrieve namespace"
#
import runtime.Errors

class Namespace:

    INSTANCE = None

    builtInFunctions = {
        'print' : print,
        'input' : input,
        'exit'  : exit,
        'len'   : len,
        'str'   : str,
        'int'   : int,
        'float' : float,
        'type'  : type,
        'range' : range,
        'set'   : set,
        'max'   : max,
        'min'   : min,
    }

    def __init__(self, outerScope):
        self.outerScope = outerScope
        self.content = {}
        if self.outerScope == None:
            self.content.update(Namespace.builtInFunctions)

    def get(self, name):
        try:
            # Search in the current scope first
            return self.content[name]
        except KeyError:
            if self.outerScope != None:
                return self.outerScope.get(name)

            raise runtime.Errors.NameError("name %s is not defined" % name)

    def set(self, name, value):
        self.content[name] = value



Namespace.INSTANCE = Namespace(None)
CurrentNamespace = Namespace.INSTANCE
