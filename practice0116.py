def decoratorname(func):
    def warpper(*args):
        print(func.__name__)
        func(*args)
    return warpper

@decoratorname
def func(food):
    print(food)


if __name__ == "__main__":
    func('Apple')

