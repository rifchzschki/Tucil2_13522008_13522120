
__all__ = ["Bezier_dac", "Bezier_bf"]
import matplotlib.pyplot as plt

class Bezier_dac(): # devided and conquer
    def get_Q(point1, point2, t=0.5):
        return [(1-t)*x + t*y for x,y in zip(point1, point2)]
    
    def curve(p0, p1, p2, n):
        if (n==0):
            return [p0, p2]
        else:
            q0 = Bezier_dac.get_Q(p0,p1)
            q1 = Bezier_dac.get_Q(p1,p2)
            r0 = Bezier_dac.get_Q(q0,q1)
            curve1 = Bezier_dac.curve(p0, q0, r0, n-1)
            curve2 = Bezier_dac.curve(r0, q1, p2, n-1)
            return curve1 + curve2[1:]
        

        

class Bezier_bf(): # brute force
    print("b")

curve = Bezier_dac.curve((0,0), (0, 2), (3,0), 10)
x = [x[0] for x in curve]
y = [y[1] for y in curve]
print(x)
plt.figure()
for i in range(len(x)):
    if(i%10==0):
        plt.plot(
            x[:i],y[:i],'r-'
        )
        plt.pause(0.00001)
plt.plot(
    [0,0,3],
    [0,2,0],
    'blue',
)
plt.plot(
    [0,0,3],
    [0,2,0],
    'ro',
)
plt.show()


