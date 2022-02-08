students = ['quinto', 'rishi', 'tatiana', 'luke', 'theo']
print(students[0:2])
print(students)
students.append('justin')
students.append('quinto')
print(students[3:len(students)])
# print(students[3:])

print(students[:3])

for student in students[:3]:
    print(f'Hello, {student.title()}')

# new_students_list = students[:]
new_students_list = students
print(new_students_list)
print(students)

new_students_list.append('jason')
print(new_students_list)
print(students)

# print(f'Number of students: {len(students)}')

# for student in students:
#     print(f'Hello, {student.title()}!')

# ** TYPE ERROR **
# start = input('Enter a starting number: ')
# end = input('Enter a ending number: ')

# start = int(input('Enter a starting number: '))
# end = int(input('Enter a ending number: '))
# incr = int(input('How much would you like to increment? '))

# for value in range(start, end+1, incr):
#     print(value)

# for value in range(end+1):
#     print(value)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# numbers = []
# for num in range(1, 1_000_001):
#     numbers.append(num)
# print(f'{min(numbers)} - {max(numbers)}')
# print(sum(numbers))

# numbers = list(range(1, 1000001))
#
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# for x in range(0, 20, 2):
#     print(x+1)

# for i in range(1, 11):
#     print(i*i*i)

# cubes = [i ** 3 for i in range(1, 11)]
# for i in cubes:
#     print(i)
