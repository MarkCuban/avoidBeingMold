class PrefixMetaclass(type):
    def __new__(cls, name, bases, attrs):

        _attrs = (('my_'+ name, value) for name, value in attrs.items())
        _attrs = dict((name, value) for name, value in _attrs)
        _attrs['echo'] = lambda self, phrase: phrase

        return type.__new__(cls, name, bases, _attrs)

class Foo(metaclass = PrefixMetaclass):
    name = 'Foo'

    def bar(self):
        print('bar')

class Bar(Foo):
    prop = 'bar'

f = Foo()
b = Bar()

print(b.my_prop)