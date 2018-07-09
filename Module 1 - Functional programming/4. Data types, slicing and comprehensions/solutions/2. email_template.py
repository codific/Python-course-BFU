recipient_email = input("Enter recipient's email: ")
sender_email = input("Enter sender's email: ")

recipient_name = recipient_email.split('@')[0].capitalize()
sender_name = sender_email.split('@')[0].capitalize()

template = f'''
Dear {recipient_name},

It is good to hear that you're learning Python.

Regards,
{sender_name}
'''

print(template)