import asyncio

PLUGINS = dict()


# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func


def register(pattern):
    def wrapper(func):
        print("Running decorator")
        PLUGINS[pattern] = func
        return func

    return wrapper


@register("say_hello")
async def say_hello(name):
    return f"Hello {name}"


@register("be_awesoem")
async def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


print(PLUGINS)


# async def run():
#     print(await PLUGINS["say_hello"]("lel"))


# asyncio.get_event_loop().run_until_complete(run())
