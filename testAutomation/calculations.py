import math
def calculate_sum(num):
    sum = 0
    for i in range(0, num):
        sum += i
    return sum

def calculate_even_odd_sum(num):
    even_sum = odd_sum = 0
    for i in range(0, num):
        if(i % 2 == 0):
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum