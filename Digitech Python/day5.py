# We are performing the for loop in our programs

# for number in range(10):
#     if number %2 == 1:
#         print(number )


# We are performing the while loop in our programs

trial = 3
attempt = 0

while attempt < trial:
    value = input("Enter the password")
    if value == "kenty1234":
        print("log in successfully")
        break
    else:
        print("the pasword is wrong try again!!")
        attempt+=1

else:
    print("you failed number of attempts are over!!")
