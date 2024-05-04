#Comment on ID code registration
Full_Name = input("Input your full name:")
Age = int(input("DOB:"))
CountrySide = input("CountrySide:")
Robot = input("How many days are in a week?!?:")
if Robot == "7":
	print("your ID CODE is: web890@")
else:
	print("registration not sucessful")
#Comment on passcodes generator
import getpass
password = getpass.getpass("ID code")
if password == "web890@":
	import random
	import string
	def generate_password(length):
		character = string.ascii_letters + string.digits + string.punctuation
		password = "".join(random.choice(character)for i in range(length))
		return password
	password_lenght = 12
	generated_password = (generate_password(password_lenght))
	print("Generate_password:", generated_password)
	import pyotp
	secret_key = pyotp.random_base32()
	totp = pyotp.TOTP(secret_key)
	two_factor_code = totp.now()
	
	print("secret_key:", secret_key)
	print("2FA code:", two_factor_code)
else:
	print("Not a User")
	