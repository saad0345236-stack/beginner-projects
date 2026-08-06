# Quiz master program:
print("Welcome to this quiz!")
print("Try to answer all 5 upcoming questions")

score = 0

question_1 = int(input("In which year did 'United Nations' form?" ))

if question_1 == 1945:
    print("That's correct!")
    score += 1
else:
    print("WRONG!")

question_2 = input("Who was the first person sent into space? What was their name? ").lower()

if question_2 == 'yuri gagarin':
    print("That is the right answer!")
    score += 1
else:
    print("FALSE!")

question_3 = input("What is the most widely spoken home language in South Africa ").lower()

if question_3 == 'isizulu':
    print("That was a tough one, but you got it right!")
    score += 1
else:
    print("That is incorrect!")

print(f"Your final score is {score}")