def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "scalene"

def course_result(coursework, final, attendance):
    if not (0 <= coursework <= 100 and 0 <= final <= 100 and 0 <= attendance <= 100):
        raise ValueError
    if attendance < 75:
        return "fail"
    total = coursework + final
    if total >= 50 and final >= 40:
        return "pass"
    return "fail"

def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_below(n):
    return [i for i in range(2, n) if is_prime(i)]

def first_repeated(values):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return values[i]
    return None

def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            count += 1
    return count

def calculator(command):
    match command.split():
        case ["add", x, y]:
            return float(x) + float(y)
        case ["sub", x, y]:
            return float(x) - float(y)
        case ["mul", x, y]:
            return float(x) * float(y)
        case ["div", x, y]:
            return float(x) / float(y)
        case _:
            raise ValueError

def parse_int(text, default=None):
    try:
        return int(text)
    except ValueError:
        return default

def stats(*numbers):
    if not numbers:
        return None
    min_val = numbers[0]
    max_val = numbers[0]
    total = 0
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        total += num
    return min_val, max_val, total / len(numbers)

