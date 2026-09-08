from typing import Iterable, Sequence, SupportsFloat, List

Number = SupportsFloat

def _to_floats(seq: Iterable[Number]) -> List[float]:
    try:
        return [float(x) for x in seq]
    except TypeError as e:
        raise TypeError("mean/median expect an iterable of numbers") from e

def mean(numbers: Sequence[Number]) -> float:
    vals = _to_floats(numbers)
    if len(numbers) <= 0:
        raise ValueError("Empty list")
    return sum(vals) / len(vals)


def median(numbers: Sequence[Number]) -> float:
    vals = _to_floats(numbers)
    if len(numbers) <= 0:
        raise ValueError("Empty list")
    n = len(vals)
    vals.sort()
    mid = n // 2
    if n % 2 == 1:
        return vals[mid]
    else:
        return (vals[mid - 1] + vals[mid]) / 2.0
