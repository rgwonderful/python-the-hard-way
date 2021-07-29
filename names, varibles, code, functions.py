# this one is like your scripts with argv
def print_two(*args):
    argl, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok that *args is actually pointless, we can just do hypothesis
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one atgument
def print_one(arg1):
        print(f"arg1: {arg1}")

# this one take no arugments
def print_none():
    print("i got nothin'.")


print_two("Zed","shaw")
print_two_again("Zed","shaw")
print_two("Frist!")
print_none()
