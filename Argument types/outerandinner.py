# #inner function
def outer():
    print('outer function')
    def inner():
        print('Inner function')
    return inner
inner=outer()
inner()


