from pyotp import TOTP

def send_otp(request):
secret_key = TOTP.random_base32()
totp = TOTP(secret_key)