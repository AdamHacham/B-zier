import numpy as np
import matplotlib.pyplot as plt

def Binomial(n,k):
     
    if n==k or k==0:
        return 1
    elif 0<k<n:
        return Binomial(n-1,k) + Binomial(n-1,k-1)
    else:
        return 0


def bernstein(i,n,t) :
    return Binomial(n,i)*(t**i)*((1-t)**(n-i))


def besier(points,nbr=1000):
    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nbr)

    polynomial_array = np.array([ bernstein(i, nPoints-1, t) for i in range(0, nPoints)   ])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals




points=[[1,1],[2,3],[4,3],[3,1]]    
xpoints = [p[0] for p in points]
ypoints = [p[1] for p in points]
xvals, yvals = besier(points, nbr=1000)
plt.plot(xvals, yvals)
plt.plot(xpoints, ypoints, "ro")
for nr in range(len(points)):
    plt.text(points[nr][0], points[nr][1], nr)
plt.show()

