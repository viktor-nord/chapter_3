numbers = [1, 2, 7, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[-1])
message = f"My first number is {numbers[0]}."
print(message)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))

numbers.append(6)
print(numbers)
numbers.insert(0, 1337)
print(numbers)
numbers.insert(3, 420)
print(numbers)
del numbers[0]
print(numbers)

removed_number = numbers.pop()
print(removed_number)
print(numbers)


second_removed_number = numbers.pop(2)
print(second_removed_number)
print(numbers)
numbers[2] = 9000
print(numbers)

wrong_number = 3
numbers.remove(wrong_number)
print(numbers)
