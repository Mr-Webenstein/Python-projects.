import pyotp
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key)
two_factor_code = totp.now()

print("secret_key:", secret_key)
print("2FA pass code:", two_factor_code)
