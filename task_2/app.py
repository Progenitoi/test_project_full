import hashlib


class CodeStore(object):
    def __init__(self, *args):
        self.storage = [hashlib.md5(string.encode('utf-8')) for string in args]

    def check(self, lookup):
        for md5_obj in self.storage:
            if md5_obj.hexdigest() == hashlib.md5(lookup.encode('utf-8')).hexdigest():
                return md5_obj
            
