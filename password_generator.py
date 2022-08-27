import string
import random


if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter the length of the password you want! \n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)
    # print("Your password is: \n")
    # print("".join(s[0:plen]))

    # If we don't want to use random.shuffle then we can do the same by using random.sample as given below 
    print("Your password is: \n")
    print("".join(random.sample(s,plen)))


    





