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

my_class = myClass()
my_class.display()



