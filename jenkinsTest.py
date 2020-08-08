import sys
users = [
    (0,"Bob", "password"),
    (1,"Rolf", "bob123"),
    (2,"Jose", "longp4ssword"),
    (3,"username", "1234"),
    ]

user_map = {user[1] : user for user in users}

print(user_map)
print(user_map["Jose"])

user_input = sys.argv[1]
passwd_input = sys.argv[2]

#destructuring Tuple
_,username,password=user_map[user_input]

if password == passwd_input:
    print("Correct Password")
else:
    print("Incorrect Password")

