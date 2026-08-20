print("Power of 2")
num=int(input("Enter a Positive Number : "))
max_range=int(input("Enter the maximum range limit :"))
print("Power of 3")
num=int(input("Enter a Positive Number : "))
max_range=int(input("Enter the maximum range limit :"))
for i in range(1,max_range + 1):
    power = num**i
    print(f"{num}**{i}={power}")
print("Power of 3")
for i in range(1,max_range + 1):
    power = num**i
    print(f"{num}^{i}={power}")
