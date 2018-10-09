def context():
    stuff = {"mom": "Мама", "window": "раму", "cat": "кошка"}
    return stuff


def swapper(internals):
    def wrapper():
        d = internals()
        a = None
        b = None
        c = None
        for x, y in d.items():
            if x == "mom":
                a = y
            elif x == "window":
                b = y
            elif x == "cat":
                c = y
        if not a:
            print("мыла ", b, ", а ", c, " лежала кверху мехом")
        elif not b:
            print(a, " мыла, а ", c, "лежала кверху мехом")
        elif not c:
            print(a, " мыла ", b, ", а лежала кверху мехом")
        else:
            print(a, " мыла ", b, " a ", c, " лежала кверху мехом")
    return wrapper
