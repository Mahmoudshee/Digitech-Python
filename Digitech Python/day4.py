# this programe checks on the user inputs and validate it 

print("This programe needs the credentials to verify them to grant access to users")
print()

username = input("Enter your username: ")
password = input("Enter your password: ")


if username == "kenty" and password == "kenty1234":
    print("signed in successfully!!")

elif username != "kenty" and password == "kenty1234":
    print("check your credentials and try again")

else:
    print("Wrong credentials")