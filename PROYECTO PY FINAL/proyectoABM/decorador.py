def decoradorCreate(funcion):
    def wrapper(self, *args, **kwargs):
        funcion(self, *args, **kwargs)
        print("Decorador => Se agregó una nueva película")

    return wrapper


def decoradorDelete(funcion):
    def wrapper(self, *args, **kwargs):
        funcion(self, *args, **kwargs)
        print("Decorador => Se eliminó una película")

    return wrapper


def decoradorSearch(funcion):
    def wrapper(self, *args, **kwargs):
        funcion(self, *args, **kwargs)
        print("Decorador => Se encontraron estos resultado")

    return wrapper
