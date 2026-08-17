# Practicing Drill:
def summarize_numbers(number1, number2, number3):
    total = number1 + number2 + number3

    average = total / 3.0

    find_number = [number1, number2, number3]
    largest = 0
    smallest = find_number[0]

    for number in find_number:
        if number > largest:
            largest = number
    
    for digit in find_number:
        if digit < smallest:
            smallest = digit
    
    summarized = {"Total": total, "Average": average, "Largest": largest, "Smallest": smallest}

    return summarized

print(summarize_numbers(3, 4, 7))