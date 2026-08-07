# Quiz master program version 2:
print("Welcome to this quiz!")
print("Try to answer all 5 questions")

score = 0

question_1 = input("In which year did 'United Nations' form?" )

if question_1 == '1945':
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

question_4 = input("What's the name of the largest planet in our solar system? ").lower()

if question_4 == 'jupiter':
    print("Jupiter is the right answer.")
    score += 1
else:
    print("That's not the right answer!")

question_5 = input("Final question! When did World War II end? Which year? ")

if question_5 == '1945':
    print("That is correct!")
    score += 1
else:
    print("Wrong...")

name = input("Your name is? ").capitalize()
print(f"Okay, {name}. Your final score is {score}")

percentage = (score / 5) * 100
print(f"Your accuracy rate is {percentage}%")