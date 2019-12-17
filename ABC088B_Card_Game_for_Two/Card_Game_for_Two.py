

#input
print("input N")
input1 = "4"

print("input ai ai+1 ...an")
input2 = "20 18 2 18"
list = list(map(int,input2.split()))
list.sort(reverse=True)

sum1 = sum(list[0::2])
sum2 = sum(list[1::2])
print(sum1 - sum2)
