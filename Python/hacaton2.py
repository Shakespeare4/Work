import hashlib
a  = "5dcf0e60378b30c6b6af03207a56576a1ff08b2a77326108043e96893475a8bd"
for i in range(100000000):
      
    z = hashlib.sha256(str(i).encode()).hexdigest()
    if z == a:
        print(i)






 



