# Google Authenticator TOTP Generator

## Description

This program implements an application that works with Google Authenticator using a Time-Based One-Time Password (TOTP) algorithm. Google Authenticator supports various OTP algorithms, and this program specifically implements the 30-second TOTP codes. This provides a method for implementing 2FA (Two-Factor Authentication) by generating One-Time Passwords.

## Installation

Before running the program, ensure you have Python installed on your system. Additionally, you will need to install the following Python packages:

```bash
pip install pyotp qrcode argparse

```
## Usage

The program can be executed with the command python3 main.py and accepts two arguments:

```--generate-qr```: This command generates a QR code as a PNG image and saves it in the same directory. Users can scan this QR code using the Google Authenticator app to set up their authentication token.

```bash
python3 main.py --generate-qr
```

```--get-otp```: This command outputs a TOTP that should match the current code displayed in the Google Authenticator app. If the code does not match, it's likely due to the time-bound nature of TOTP. Simply run the command again.

```bash
python3 main.py --get-otp
```
## Configuration

### Email
Ensure you replace the email in the script with the one you use with your Google Authenticator app to ensure seamless integration.

```python
google_auth_email = "your-email@example.com"
```

### Secret Key
You might also want to change the secret key used in the application to ensure it is unique and secure.

```python
secret_key = "YourSecretKeyHere"
```
