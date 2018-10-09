import hashlib


class CodeStore(object):
    def __init__(self, *args):
        self.args = args
        self.storage = []
    def hashes(self):
        strings = self.args
        strings = strings.encode('utf-8')
        hashes = hashlib.md5(strings)
        self.storage.append(hashes)
    def check(self):
        strings = self.args
        strings = strings.encode('utf-8')
        hashes = hashlib.md5(strings)
        for i in self.storage:
            if hashes == i:
                return 'Match found'
            else:
                return 'Match not found'
