import protonmail.models
from getpass import getpass
# Login
client = Client(Username="obsoletehaden", 
                blocking=True)  # It's async by default

# If using different keys for login and mailbox you must unlock separately                
client.api.login(getpass())
# Create a draft
r = client.create_draft()
draft = r.Message
draft.Subject = "Hello from python!"
draft.DecryptedBody = "JS got you down huh?"
draft.ToList = [
    EmailAddress(Address="user@example.com", Name="User"), 
    EmailAddress(Address="user@protonmail.com"), 
]

# Save the draft if needed
r = client.save_draft(draft)

# Now send it
r = client.send_message(draft)
if r.Code != 1000:
    print(r.Error)
