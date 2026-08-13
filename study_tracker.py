# Study tracker:
import datetime

try:
    hours = int(input("Study hours: "))
except ValueError:
    print("Enter an integer.")

subject = input("Subject: ").capitalize()

study = {
    'hours': hours,
    'subject': subject,
    'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
}

print(f"You studied {study['subject']} for {study['hours']} hours today on {study['date']}.")