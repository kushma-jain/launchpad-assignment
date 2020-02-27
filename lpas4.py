// to eleminate the duplicates
numbers = [1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
unique_numbers = []

for number in numbers:
	if number not in unique_numbers:
		unique_numbers.append(number)

print(unique_numbers)