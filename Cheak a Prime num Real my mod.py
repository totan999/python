# var = 1
# You can also use a condition like: (var >= 1)
# while True:
#   try:
#       num = int(input("Enter your number:\n"))
#   except Exception as e:


def totan():  # Created a function, where store my program, i can call this program is any where!!
    while True:
        try:
            num = int(input("Enter your number:\n"))
            i = 1
            if int(num) > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        print(num, "is not a prime number.")
                        print(i, "times", num // i, "is", num, end=" ")
                        print("(", i, "*", num // i, "=", num, ")", sep="")
                        print("Please try again.", end="\n\n")
                        break
                    else:
                        print(num, "is a prime number.")
                        break
            else:
                print(num, "is not a prime number.")
                print(i, "times", num // i, "is", num, end=" ")
                print("(", i, "*", num // i, "=", num, ")", sep="")
                print("Please try again")
                print("\n")
                print("Do you want to try again?")
            ii = input("type 'y' for YES and 'n' for NO:\n")
            if ii == "y":
                continue
            elif ii == "n":
                print("Thanks for using my code.")
                break
            else:
                print("Wrong input! Please try again.")
                while True:
                    ii = input("type 'y' for YES and 'n' for NO:\n")
                    if ii == "y":
                        break
                    elif ii == "n":
                        print("Thanks for using my code.")
                        exit(0)
        except ValueError:
            print("Please input a vaild number, and try again")


print("This program is store in totan() function")

totan()