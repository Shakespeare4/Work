import matplotlib.pyplot as plt
x = []
a = 2
y = input("Elige entre aritmetica, exponencial, geometrica o all ")
y1 = []
y2 = []
y3 = []
for i in range (7):
    x.append(i)
    y1.append(i*a)
    y2.append(i**2)
    y3.append(2**i)
if y == "aritmetica":
    plt.plot(x, y1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Aritmética")
    plt.show()
if y == "exponencial":
    plt.plot(x, y2)
    plt.ylabel('Y')
    plt.title("Exponencial")
    plt.show()
if y == "geometrica":
    plt.plot(x, y3)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Geométrica")
    plt.show()
if y == "all":
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Todo")
    plt.show()