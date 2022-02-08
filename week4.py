username = input("Please enter username")
print(f"Username entered {username}")
if username == "Admin":
    print("Hello Admin. Would you like to see a status report?")
elif username != "Admin": 
    print (f"Hello {username} thank you for logging in again.")
