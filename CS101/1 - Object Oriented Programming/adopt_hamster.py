import time

# Create your class here
class Hamster:
	# Create a __init__ method
	def __init__(self, input_name, input_breed, input_owner, input_age=0, input_friendly=False):
		self.name = input_name
		self.breed = input_breed
		self.age = input_age  # in months
		self.friendly = input_friendly
		self.hungry = False
		self.steps = 0  # move count
		self.sleep = False
		self.owner = input_owner

	# Create method to change
	# describe the hamster -- use repr for string outputs
	def __repr__(self):
		desc = f"{self.name} is a {self.breed} who is {self.age} months old."
		return desc


# Play the game
print("Hello welcome to Hampiness Pet Store! We never seen you here before! What's your name?")
my_name = input("My name is ")
print(f"Nice to meet you {my_name}! Now what breed of hamster are you looking for?")
breed = input("Type 'Syrian' or 'Gerbil'. ")

# create while loop to make sure input is right
while breed != "Syrian" and breed != "Gerbil":
	breed = input("The breed you selected is not here! Please type 'Syrian' or 'Gerbil'. ")
else:
	print("Awesome we should have that breed!")

print("Now, how many months is your hamster?")
age = input("I would like a hamster that's ")

# while loop to make sure the age is an integer
while True:
	try:
		age = int(age)
	except ValueError:
		age = input("I didn't hear you, can you repeat it again? ")
	else:
		age = int(age)
		break

# age = int(age)

if age < 6:
	print(f"Aww {age} months old! They're going to be so tiny.")
else:
	print(f"Aww {age} months old! They're easier to care since they're an adult~")

print("Are you particularly looking for a friendly one or not?")
friend = input("Type 'Yes' or 'No'. ")

# while loop to check input
while friend != "Yes" and friend != "No":
	friend = input("So do you want to hug them or not? ")
else:
	print("Awesome!")

print("Oh! I know just which hamster to get you!")
time.sleep(2)
print("Waiting...")
time.sleep(2)

print("Here you go! Aren't they adorable? What would you name them?")
ham_name = input("I'll name them ")
print("Thats such a cute name!! I'll finish the paperwork for you~")
ham_one = Hamster(ham_name, breed, my_name, age, friend)
time.sleep(2)
print("Congratulations! Here you go!")
print(ham_one)
print("Thank you for adopting a hamster!")
