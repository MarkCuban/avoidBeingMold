class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

#sol = Solution()
#n = 5
#print(sol.generateParenthesis(n))

#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 2, 4, 3, 1]

#tmp = set()                ///set
#ret = 0
#for l in lst:
#    tmp.add(l)

#tmp = []                  ///lst
#for l in lst:
#    if l not in tmp:
#        tmp.append(l)

#print(tmp)

def foo(*args, **kwargs):
    print('args = ', args) 
    print('kwargs = ', kwargs)
    print('---------------------------------------')

foo('a', 'b', 3, c=2, e=None, f='abc')


a = [1, 2, 3, 4, 5]
#b = [2, 3]
b = a.copy()

b[0] = 3
#print(a)
#print([x for x in a if x not in b])

a = 1
b = 2
a, b = b, a

#print(a, b)

class Display():
    def display(self):
        print('in Display class')

class loggerMixin():
    def log(self):
        print('maxin log')

    def display(self):
        print('display in mixin')
        super().display()
        self.log()

class myClass(loggerMixin, Display):
    def log(self):
        super().log()

#my_class = myClass()
#my_class.display()


def log(func):
    print('log')
    return func

@log
def fun(arg):
    print('fun')
    return 0

c = fun(a)

def my_gen():
    for i in range(0, 10):
        yield i+1

#print([i for i in range(0, 10)])

from copy import deepcopy, copy

a = [1,3,4,5,6,7,8]
b = a
c = copy(a)
d = deepcopy(a)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

def extendList(val, lst=[]):
    lst.append(val)
    return lst

lst1 = extendList(10)
lst2 = extendList(123, [])
lst3 = extendList('a')

print(lst1, lst2, lst3)

def multipliers():
    return [lambda x: i*x for i in range(4)]

m = multipliers()

func = [lambda x: i*x for i in range(4)]

i = 0
for i in func:
    print(i(2))

print([m(2) for m in multipliers()])

lists = [[]]*5
#print(lists)
lists[0] = 'a'
#for ls in lists:
#    print(id(ls), ls)
#print(lists)

lists = [1, 4, 5, 6, 7, 8, 9, 0 , 3, 23, 5,3,67, 7,5 , 3,3 ,43, 5,55, 56]

print(lists[::2])

class defaultdict(dict):
    def __missing__(self, key):
        return 0
    pass

d = defaultdict()

print(d['a'])
