Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # three data types at input

# string
phrase = input("Enter a string: ")
print("You said " + phrase)
print(f"You said {phrase}")

# float
someFloat = float(input("Enter a float: "))
print("You entered float: " + str(someFloat))
print(f"You entered float: {someFloat}")

# int
someInt = float(input("Enter an int: "))
print("You etered int: " + str(someInt))
print(f"You entered int: {someInt}")

# string interpolation is sweet
print(f"Do Python inline, like ths: {someFloat} * {someInt} = {someFloat * someInt}")
