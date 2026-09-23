def is_disarium(number):
    num_str=str(number)
    total_sum=sum(int(digit)**(index+1)for index,digit in enumerate(num_str))
    return total_sum == number
def find_disariums_in_range(start,end):
    return[num for num in range(start,end+1)if is_disarium (num)]
test_num=(int(input("Enter a Number: ")))
ran=(int(input("Enter the Range: ")))
if is_disarium(test_num):
    print(f"✅ {test_num} is a Disarium number.")
else:
    print(f"❌ {test_num} is NOT a Disarium number.")
print(f"Disarium numbers: {find_disariums_in_range(1, ran)}")