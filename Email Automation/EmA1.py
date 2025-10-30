import yagmail

# Initialize the yagmail.SMTP object with your email credentials
yag = yagmail.SMTP(user="", password="")

# Define the recipient, subject, and body of the email
to = ""
cc = ""
bcc = ""
subject = ""
body = ""
attachments = []

# Wrap in a try-except block to handle potential errors such as invalid email addresses or password
try:
    yag.send(to=to, subject=subject, contents=body)
    print("Email sent successfully!")
except:
    print("Failed to send email.")
