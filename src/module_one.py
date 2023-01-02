
def addition(x: int, y: int) -> int:
    if type(x) not in [int, float] or type(y) not in [int, float]:
        raise TypeError

    try:
        addition = x + y
    except Exception as e:
        raise e
    return addition

