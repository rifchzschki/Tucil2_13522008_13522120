import matplotlib.pyplot as plt
import time
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
        
    def draw(control_points, iteration):
        curve = Bezier_dac.curve(*control_points, iteration)
        x = [x[0] for x in curve]
        y = [y[1] for y in curve]
        # print(x)
        xmax = max([x[0] for x in control_points])
        ymax = max([y[1] for y in control_points])
        xmin = min([x[0] for x in control_points])
        ymin = min([y[1] for y in control_points])
        plt.figure()
        countx = (xmax-xmin)*0.01
        county = (ymax-ymin)*0.01
        for i in range(len(x)):
            if(i%10==0):
                countx +=0.01
                county +=0.01
                plt.xlim(xmin-countx,xmax+countx)
                plt.ylim(ymin-county,ymax+county)
                plt.plot(
                    x[:i],y[:i],'r-'
                )
                plt.pause(0.00001)
        
        plt.plot(
            [x[0] for x in control_points],
            [y[1] for y in control_points],
            'green',
        )
        plt.plot(
            [x[0] for x in control_points],
            [y[1] for y in control_points],
            'ro',
        )
        plt.show()
        

class Bezier_bf(): # brute force
    def coordinates(self, points, iteration):
        x=[]
        y=[]
        if iteration<=1:
            x,y=zip(*points)
        else:
            for i in range (iteration):
                newx = (1 -( i / (iteration - 1)))**2 * points[0][0] + 2 * (1 -( i / (iteration - 1))) *( i / (iteration - 1)) * points[1][0] + (i / (iteration - 1))**2 * points[2][0]
                newy = (1 -( i / (iteration - 1)))**2 * points[0][1] + 2 * (1 -( i / (iteration - 1))) *( i / (iteration - 1)) * points[1][1] + (i / (iteration - 1))**2 * points[2][1]
                x.append(newx);y.append(newy)
        return x,y

    def draw_coordinates(self, points, iteration):
        start=time.time()
        x,y = self.coordinates(points, iteration)
        plt.plot(x, y, label='Curve')
        plt.scatter(*zip(*points), color='red', label='Control')
        plt.plot(*zip(*points), color='green')
        plt.legend()
        plt.title(f'Bezier Curve - Brute Force ({time.time()-start} detik)')
        plt.show()
    




if __name__ =='__main__':
    iteration=int(input("Masukkan jumlah iterasi: "))
    # Example usage with three control points
    # control_points = [(-20, 2), (2, 5), (5, 0)]
    control_points=[]
    for i in range(3):
        control=input("Masukkan koordinat titk kontrol <x,y> : ")
        try:
            x, y = map(float, control.split(','))#Format in put "x, y"
            tuple_control = (x, y)
        except ValueError:
            print("Input invalid. Masukkan input dalam format 'x, y'")
        control_points.append(tuple_control)
    print("Pilih algoritma")
    print("1. Divide and Conquer")
    print("2. Brute Force")
    try:
        algo = int(input())
        if algo == 1:
            Bezier_dac.draw(control_points, iteration)
        elif algo == 2:
            a=Bezier_bf()
            a.draw_coordinates(control_points, iteration)
        else:
            raise ValueError("Input harus 1 atau 2")
    except ValueError as error:
        print(error)

    # Brute force
    # a=Bezier_bf()
    # a.draw_coordinates(control_points, iteration)
