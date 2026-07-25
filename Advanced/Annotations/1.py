def calculate(a: int,b: int) -> int:
    return a+b

print(calculate(10, 20))

def calculate_maximum(a: int, b: int, c: int) -> None:
    print(f"Maximum of a,b,c = {a,b,c}")

calculate_maximum(20,30,15)


def max_marks(marks: list[int]) -> int:
    return max(marks)
marks = [86, 20, 60, 79, 92,"abc"]

ans = max_marks(marks)
print(f"Maximum marks = {ans}")

