
message = "Welcome to Kaun Banega Crorepati!"
print(message)

amount = 1000000  # Initial prize amount

questions = [
    ["1. Which gear is worn by batters to protect their legs in cricket?",
     "A: Helmet", "B: Gloves", "C: Pads", "D: Bails", "C"],
    
    ["2. In North India, which of these best describes 'Bhangar' and 'Khadar'?",
     "A: Coniferous forests", "B: Sandy deserts", "C: Alluvial deposits", "D: Icy slopes", "C"],
    
    ["3. Where did Netaji Subhas Chandra Bose raise the national flag in 1943?",
     "A: Port Blair", "B: Guwahati", "C: Kohima", "D: Minicoy", "A"],
    
    ["4. In which country is the largest city a port called 'abode of peace'?",
     "A: Somalia", "B: Oman", "C: Tanzania", "D: Brunei", "D"],

    ["5. Who was the first recorded English child born in North America?",
     "A: Virginia Dare", "B: Virginia Hall", "C: Virginia Sink", "D: Virginia Coffy", "A"]
]

for q in questions:
    print(f"this is question for the ${amount}\n")
    print(q[0])
    print(f"{q[1]}            {q[2]}")
    print(f"{q[3]}            {q[4]}")
    
    ans = input("Your answer (A/B/C/D): ").strip().upper()

    if ans == q[5]:
        print("✅ Correct!")
        print(f"You won ₹{amount}")
        amount *= 2
    else:
        print("❌ Wrong! Game Over.")
      
        break

    

print("Thanks for playing KBC!")

