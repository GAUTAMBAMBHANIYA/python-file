import time
timer = time.strftime('%H:%M:%S')
print("your time is :",timer)
hour=int(time.strftime('%H'))
print(hour)
if (hour>6 and hour<=12):
    print("good morning sir!")
elif(hour>12 and hour<=18):
    print("good afternoon sir!")
elif(hour>18 and hour<=21):
    print("good evening sir!")
else:
    print("good night sir!")


# import time
# import pyttsx3

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# # Ask for the user's name
# name = input("Enter your name: ")

# # Get current hour
# hour=int(time.strftime('%H'))

# # Choose greeting based on time
# if 5 <= hour < 12:
#     greeting = "Good morning"
# elif 12 <= hour < 18:
#     greeting = "Good afternoon"
# else:
#     greeting = "Good evening"

# # Combine greeting with name
# message = f"{greeting}, {name}"

# # Print and speak the message
# print(message)
# engine.say(message)
# engine.runAndWait()

