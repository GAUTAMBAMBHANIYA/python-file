# f string

#formet
str="string"
c=f"this is a f{str}"
print(c)

# if you want to print the {} so you can do {{}}
print(f"this is a{{amount}}")


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {95:.2f} dollars"
print(txt)


price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)