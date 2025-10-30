import yagmail
import os

# Initialize the yagmail.SMTP object with your email credentials
yag = yagmail.SMTP(user="", password="")

# Get Excel Automation directory for attachments
script_dir = os.path.dirname(os.path.abspath(__file__))
ea_dir = os.path.join(script_dir, "../Excel Automation")

# Define the recipient, subject, and body of the email
to = ""
cc = ""
bcc = ""
subject = ""
body = ""
attachments = [
    os.path.join(ea_dir, f) for f in os.listdir(ea_dir) if f.lower().endswith(".xlsx")
]

# Wrap in a try-except block to handle potential errors such as invalid email addresses or password
try:
    yag.send(to=to, subject=subject, contents=body)
    print("Email sent successfully!")
except:
    print("Failed to send email.")
