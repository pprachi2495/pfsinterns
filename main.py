import string
import random

if __name__ == "__main__":
       
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation

        plen = int(input("Enter the length of the Password: "))
        s = []

        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
    
        password = ''.join(s[:plen])
        print("Generated Password: ",password)
        



      