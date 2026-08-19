# Song recommendations:
print("Choose your mood:")

try:
    mood = int(input("(1) happy, (2) sad, (3) angry: "))
    
    if mood == 1:
        print("Song recommendations: 'Happy' by Pharrell Williams & 'Don't Stop Me Now' by Queen.")
    
    elif mood == 2:
        print("Song recommendations: 'Someone Like You' by Adele & 'Tears in Heaven' by Eric Clapton.")
    
    elif mood == 3:
        print("Song recommendations: 'In the Air Tonight' by Phil Collins & 'O Fortuna' by Carl Orff.")
    
    else:
        print("Enter a number from 1 to 3.")

except ValueError:
    print("Enter a number from 1 to 3.")