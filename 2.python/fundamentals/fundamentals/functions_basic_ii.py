#1.Countdown
def countdown(n):
    list = []
    for i in range(n, -1, -1):
        list.append(i)
    return list

#2.Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

#3.First Plus Length
def first_plus_length(list):
    return list[0] + len(list)

#4.Values Greater than Second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list =[]
    for i in list:
        if i > list[1]:
            new_list.append(i)
    print(len(new_list))
    return new_list

#5.This Length, That Value
def length_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
