


def log(func):
    def wrapper(*argv, **kw):
        print('call %s' % func.__name__)
        return func(*argv, **kw)

    return wrapper

@log
def now():
    print('2020-5-1')


now()