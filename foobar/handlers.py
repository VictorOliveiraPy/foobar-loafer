import asyncio


async def print_handler(message, *args):
    print(f'message is {message}')
    print(f'args is {args}')

    await asyncio.sleep(0.1)
    return True


async def error_handler(exc_info, message):
    """ do not delete the message that originated the error """
    print(f'exception {exc_info} received')

    return False


print_handler('ola tudo certo')
