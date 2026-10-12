
# 1 
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"



# 2
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)



# 3
def split_evenly(total, people):
    per_person = total // people
    remainder = total % people
    return per_person, remainder



# 4
def initials(full_name):
    names = full_name.split()
    result = ""
    i = 0
    while i < len(names):
        result += names[i][0].upper()
        i += 1
    return result



# 5
def is_palindrome_word(word):
    cleaned = word.strip().lower()
    return cleaned == cleaned[::-1]



# 6
def mask_email(email):
    at_index = email.index("@")
    username = email[:at_index]
    domain = email[at_index:]
    
    if len(username) <= 2:
        masked_user = username[0] + "*" * (len(username) - 1)
    else:
        masked_user = username[0] + "*" * (len(username) - 2) + username[-1]
        
    return masked_user + domain



# 7
def middle(values):
    mid_index = len(values) // 2
    return values[mid_index]


# 8
def rotate_left(values, k):
    if not values:
        return []
    k = k % len(values)
    return values[k:] + values[:k]


# 9
def fib_list(n):
    result = []
    a, b = 0, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result


# 10
def collatz_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


print(seconds_to_hms(3665)) #output: 01:01:05

print(celsius_to_fahrenheit(37)) #output: 98.6

print(split_evenly(10, 3)) #output: (3, 1)

print(initials("John Doe")) #output: JD

print(is_palindrome_word("Racecar")) #output: True

print(mask_email("AbdallahEl@gmail.com")) #output: A********l@gmail.com

print(middle([1, 2, 3, 4, 5])) #output: 3

print(rotate_left([1, 2, 3, 4, 5], 2)) #output: [3, 4, 5, 1, 2]

print(fib_list(7)) #output: [0, 1, 1, 2, 3, 5, 8]

print(collatz_steps(6)) #output: 8

