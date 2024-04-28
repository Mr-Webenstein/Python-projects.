First_Name = input("First_Name:")
Last_Name = input("Last_Name:")
Nickname = input("Nickname:")
Age = int(input("Age(18-30):"))
if Age >= 18 and Age <= 30:
	print("Age grade supported")
else:
	print("Age grade not supported")
Gender = input("Gender:")
Riddle = int(input("How many side does a star have?:"))
if Riddle == 6:
	print("Registration successful, your PASSCODE: is BI6070")
	import random
	import string
	def generate_password(lenght):
		character = string.ascii_letters + string.digits + string.punctuation
		password = "".join(random.choice(character)for i in range(lenght))
		return password
	password_lenght = 12
	generated_password = (generate_password(password_lenght))
	print("Generate_password", generated_password)
else:
	print("Registration unsuccessful tryagain...")

