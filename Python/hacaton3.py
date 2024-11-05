import hashlib
def abecedario[ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
a  = "a9e34a35bab4e3adb6523535ef271cefd97deb74afc00cc5195ce32c737c8388"
for i in range(100000000):
     
    z = hashlib.sha256(str(i).encode()).hexdigest()
    if z == a:
        print(i)