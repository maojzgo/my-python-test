class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self,str):
        return Chain('%s/%s' % (self._path, str))

    __repr__ = __str__

c = Chain().a.b.c

print(Chain().users('michael').repos)