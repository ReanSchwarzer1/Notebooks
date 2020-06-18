# Program 1

n = int(input())
dic = dict()
for i in range(1, n+1):
	dic[i] = i**2

print(dic)

# Program 2

n = int(input("Enter rows: "))
m = int(input("Enter cols: "))

print([[x*y for x in range(m)] for y in range(n)])

#Program 3

numbers = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        numbers.append(s)
print(",".join(numbers))

# Program 4

list_nums = input("Enter list of numbers: ")
list_nums = list_nums.split(',')

squares = [int(x)**2 for x in list_nums if int(x) % 2 == 1]
print(",".join(map(str, squares)))