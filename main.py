# 11
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 12
def square_list(lst):
    for i in range(len(lst)):
        lst[i] **= 2

# 13
def print_student(name, surname, age, score):
    print(f"Ism: {name}\nFamiliya: {surname}\nYosh: {age}\nBall: {score}")

# 14
def print_div_by_5(start, end):
    for i in range(start, end + 1):
        if i % 5 == 0:
            print(i)

# 15
def print_dict(d):
    for k, v in d.items():
        print(f"{k}: {v}")
