# question 1
def hello_name(user_name):
    messege = f"hello_{user_name}!"
    print(messege)
    

hello_name("Milad")

# question 2
def first_odd():
    for num in range(1,101):
        if num % 2 != 0:
            print(num)


first_odd()

# question3
def max_num_in_list (a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

Milad = [10, 20, 30, 40]
print(max_num_in_list (Milad))

# question 4
def is_leap_year(a_year):
    if a_year % 4 != 0:
        return False
    elif a_year % 4 == 0:
        if (a_year % 100 == 0) and (a_year % 400 != 0):
            return False
        else:
            return True
    return False
        

print(is_leap_year(2020))

# questuion 5
def is_consecutive(a_list):
    return sorted(is_consecutive) == list(range(min(1), max(1)+1))
        

milad = [1,2,4,6,5]
print(is_consecutive(milad))




    
