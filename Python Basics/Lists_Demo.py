students = ['rudra', 'jason', 'luke', 'sara']
# print(f'Hello, {students[0]}.')
# print(f'Hello, {students[1]}.')
# print(f'Hello, {students[2]}.')
# print(f'Hello, {students[3]}.')

# i = 0
# print(f'Hello, {students[i]}.')
# i = i+1
# print(f'Hello, {students[i]}.')
# i = i+1
# print(f'Hello, {students[i]}.')
# i = i+1
# print(f'Hello, {students[i]}.')

print(f'{students[-1]} is the last student on the list.')

students[0] = students[0].upper()
# students[0] = 'rudra'.upper()
# students[0] = 'RUDRA'
print(f'{students[0]} is the updated first student on the list.')

students.append('rishi')
print(students)

students.insert(0, 'vishnu')
print(students)

students.insert(3, 'quinto')
print(students)

# new_student = input("What do you want to add? ==> ")
# students.append(new_student)
# print(students)

del students[-1]
print(students)

leaving_s = students.pop()
print(f'Goodbye, {leaving_s}')
print(students)

students.remove('RUDRA')
print(students)
