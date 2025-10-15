# #defining a function 
# def get_pass(name, age):
#     if age <= 17:
#         return f"{name},you are not allowed to go in!!"
#     else:
#         return f"{name}, you are allowed to go in!!"
    
# #generate the actual name and age
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# final = get_pass(user_name,user_age)
# print(final)





def get_acces():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        if age <= 17:
            print(f"{name},You are not allowed to go in !!")
        else:
            print(f"{name},You are allowed to go in !!")
    except:
        print("Umekosea mahali jaribu tena")

get_acces()