import pyotp 
import qrcode 
import argparse

def generate_qr(secret_key, email, issuer='My Secure App'):
    # Generate the provisioning URI for the TOTP
    totp_auth = pyotp.totp.TOTP(secret_key).provisioning_uri(name=email, issuer_name=issuer)
    
    # Create and save the QR code
    imgage = qrcode.make(totp_auth)
    imgage.save("qr_code.png")
    print("QR code generated and saved as qr_code.png")

def get_otp(secret_key):
    # Create a TOTP object
    totp = pyotp.TOTP(secret_key)
    
    # Generate a current OTP
    otp = totp.now()
    print(f"Current OTP: {otp}")

if __name__ == '__main__':

    # Argument parsing
    parser = argparse.ArgumentParser(description='Generate QR code and TOTP for Google Authenticator')
    parser.add_argument('--generate-qr', action='store_true', help='Generate QR code for Google Authenticator')
    parser.add_argument('--get-otp', action='store_true', help='Get current OTP from Google Authenticator')

    args = parser.parse_args()

    ################# CHANGE YOUR KEY AS DESIRE ####################
    secret_key = "ThisIsASecretKey"

    ################# ENTER YOUR EMAIL HERE ########################
    google_auth_email = "andrewle0915@gmail.com"

    if args.generate_qr:
        generate_qr(secret_key, google_auth_email)
    elif args.get_otp:
        get_otp(secret_key)
    else:
        print("No valid command provided. Use --generate-qr or --get-otp.")
