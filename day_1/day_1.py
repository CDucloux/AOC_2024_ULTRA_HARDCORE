import time
from functools import wraps
from pathlib import Path
from typing import Any, Callable

import polars as pl
import polars.selectors as cs
from rich import print


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A cursed charm to measure the runtime of yer function.

    Parameters:
    - func (Callable): The wretched function ye seek to bind with this spell.

    Returns:
    - Callable: A wrapper, forged in time itself, to bind the original function
    and measure the very sands that slip through its hourglass.

    Prints the time it took to execute me function, down to the very last tick,
    in seconds. If ye dare.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.4f} seconds")
        return result

    return wrapper


@timer
def compute_minimal_pairwise_distance() -> int:
    """
    Hark! The Chief Historian be vanished,
    leavin’ naught but a pair o’ scattered lists like the scribblings o’ madmen.
    Useless, witless Senior Historians shuffle ’bout, squabblin’ over their misshapen notes,
    leavin’ meself, the lone soul o’ sound mind, to right their wayward wrongs.
    This function takes those cursed lists,
    pairs the smallest with the smallest,
    the second with the second, aye, and so on,
    calculatin’ the very distances that separate their befuddled reckonings.

    When all's done, it returns an int, a measure o’ their shame and me toil!
    """
    cryptic_txt_file = Path(".") / "day_1" / "input" / "day_1.txt"

    txt_dataframe = pl.read_csv(cryptic_txt_file, has_header=False, separator=" ")

    historians_lists = txt_dataframe.select(cs.integer()).rename(
        {"column_1": "list_a", "column_4": "list_b"}
    )

    sorted_list_a = historians_lists.select("list_a").sort(by="list_a")
    sorted_list_b = historians_lists.select("list_b").sort(by="list_b")

    distances = (sorted_list_b - sorted_list_a).rename({"list_b": "distances"})

    return distances.select(pl.col("distances").abs()).sum().item()


compute_minimal_pairwise_distance()
