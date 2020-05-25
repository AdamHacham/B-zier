import numpy as np
import matplotlib.pyplot as plt

def fact(x):
    if x<2 :
        return 1
    else:
        return x*fact(x-1)

def binome(n,k):
    if k > n//2:
        k = n-k
    x = 1
    y = 1
    i = n-k+1
    while i <= n:
        x = (x*i)//y
        y += 1
        i += 1
    return x

def bernstein(i,n,t) :
    return binome(n,i)*(t**i)*((1-t)**(n-i))


def besier(points,nbr=1000):
    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nbr)

    polynomial_array = np.array([ bernstein(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals



print("La suite des points {Po,...,Pn} forme le polygone de controle de Bezier.")
print("Veuillez choisir le nombre de points qui formeront le polygone de controle de Bezier souhaite : ")
ch = int(raw_input("Entrez le nombre de point souhaite : "))
print("Entrez les coordonnees du point Po")
e = float(raw_input("Entrez l'abssice  : "))
f= float(raw_input("Entrez l'ordonnee  : "))
i=1
points = np.array([[e,f]])
l= points
while i<ch : 
    print "Entrez les coordonnees du point P%d" % i
    c = float(raw_input("Entrez l'abssice : "))
    d = float(raw_input("Entrez l'ordonnee : "))
    b = np.array([[c,d]])
    l = np.concatenate((points,b),axis=0)
    points = l
    i+=1

print(l)
points=l    
xpoints = [p[0] for p in points]
ypoints = [p[1] for p in points]
xvals, yvals = besier(points, nbr=1000)
plt.plot(xvals, yvals)
plt.plot(xpoints, ypoints, "ro")
for nr in range(len(points)):
    plt.text(points[nr][0], points[nr][1], nr)
plt.show()

