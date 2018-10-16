def context():
    stuff = {"mom": "Мама", "window": "раму", "cat": "кошка"}
    return stuff


def swapper(**internals):
    def wrapper():
        return "{mom} мыла {window}, а {cat} лежала кверху мехом".format(mom="", window="", cat="")

