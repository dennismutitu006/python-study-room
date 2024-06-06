#unctions – or other callable objects – can be annotated using collections.abc.Callable 
#or typing.Callable. Callable[[int], str] signifies a function that takes a single parameter of type int and returns a str.

from collections.abc import Callable, Awaitable

def feeder(get_next_item: Callable[[], str]) -> None:
    ...  # Body

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    ...  # Body

async def on_update(value: str) -> None:
    ...  # Body

callback: Callable[[str], Awaitable[None]] = on_update

#If a literal ellipsis ... is given as the argument list, it indicates that a callable with any arbitrary parameter list would be acceptable:

def concat(x: str, y: str) -> str:
    return x + y

x: Callable[..., str]
x = str     # OK
x = concat  # Also OK
