def sum(num1, num2):
    ans = num1 + num2
    return ans

def mul(num1, num2):
    ans = num1 * num2
    return ans

def print_ans(ans):
    print(f'The answer is: ' + str(ans))

#  add sub and div functions

print('Welcome to my Calculator program.')
num1 = int(input("Enter first number: "))
num2 = int(input("Enter secon number: "))
opt = input("What would  you like to do? Enter +, -, / or * : ")

if opt == '+':
    print_ans(sum(num1, num2))