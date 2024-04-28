BI_ID = input("BI-ID::")
if BI_ID == "Mr. Webenstein":
	print("Please input your passcode")
else:
	print("Wrong User")
import getpass
password1 =getpass.getpass ("Passcode")
if password1 == "BI6070":
	print("Acess granted")
else:
		for password in range(1):
			print("Acess denied")
password = "Acess denied"
if password == "Acess denied":
	import time 
	def countdown_timer(seconds):
		while seconds > 0:
			print(seconds)
			time.sleep(1)
			seconds -= 1
		print("System automatically locked")
	countdown_timer(5)
	password2 = getpass.getpass ("System code")
if password2 == "BI1010":
	print("Sytem unlock")
else:
	print("your not a user")
def password():
	print("Baby Intelligence®")
password()
