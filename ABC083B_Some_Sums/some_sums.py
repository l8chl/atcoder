
def calc_sum_of_digit(num):
    sum_of_digit = 0
    while 1:
        sum_of_digit += num % 10
        num = num // 10
        if num == 0:
            break
    return sum_of_digit

#decrare
sum = 0

#input
print("input N A B")
list = "100 4 16"
N,A,B = map(int,list.split())

for count in range(N+1):
    sumOfDigit = calc_sum_of_digit(count)
    if A <= sumOfDigit <= B:
        sum += count

print(sum)
