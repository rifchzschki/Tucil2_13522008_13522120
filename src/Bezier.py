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
            # line = plt.plot([p0[0], p2[0]], [p0[1], p2[1]], 'ro-')
            # plt.pause(1)  # Jeda untuk animasi
            # line[0].remove()
            return curve1 + curve2[1:]
        
    def count_digit(n):
        count = 0
        while(n//10!=0):
            n//=10
            count+=1
        return count
        
    def draw(control_points, iteration):
        start = time.time()
        curve = Bezier_dac.curve(*control_points, iteration)
        end = time.time() - start 
        x = [x[0] for x in curve]
        y = [y[1] for y in curve]
        # print(x)
        xmax = max([x[0] for x in control_points])
        ymax = max([y[1] for y in control_points])
        xmin = min([x[0] for x in control_points])
        ymin = min([y[1] for y in control_points])
        # plt.figure()
        countx = (xmax-xmin)*0.01
        county = (ymax-ymin)*0.01
        if(len(x)>1000):
            n = 10**(Bezier_dac.count_digit(len(x))-1)
            print(len(x))
            print(2)
        elif(len(x)>100):
            n=5
            print(3)
        else:
            n=1
            print(4)
        for i in range(len(x)):
            if(i%n==0):
                countx +=0.01
                county +=0.01
                plt.xlim(xmin-countx,xmax+countx)
                plt.ylim(ymin-county,ymax+county)
                plt.plot(
                    x[:i+1],y[:i+1],'r-'
                )
                plt.pause(0.00001)
                in_end = i
        print(in_end)
        plt.plot(x[in_end+1:-1],y[in_end+1:-1],'r-')

        plt.title(f'Bezier Curve - Divided and Conquer ({end} detik)')
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
    def bezier_curve_brute_force(self, points, iteration):
        x=[]
        y=[]
        if iteration==1:
            x,y=zip(*points)
        else:
            for t in range (iteration):
                newx = (1 - t / (iteration - 1))**2 * points[0][0] + 2 * (1 - t / (iteration - 1)) * t / (iteration - 1) * points[1][0] + (t / (iteration - 1))**2 * points[2][0]
                newy = (1 - t / (iteration - 1))**2 * points[0][1] + 2 * (1 - t / (iteration - 1)) * t / (iteration - 1) * points[1][1] + (t / (iteration - 1))**2 * points[2][1]
                x.append(newx);y.append(newy)
        return x,y

    def plot_bezier_curve_brute_force(self, points, iteration):
        start=time.time()
        iteration=(2*iteration)+1 #Diubah supaya jumlah titik hasil iterasi sesuai dengan divide and conquer
        x,y = self.bezier_curve_brute_force(points, iteration)
        plt.plot(x, y, label='Brute Force')
        plt.scatter(*zip(*points), color='red', label='Control Points')
        plt.legend()
        plt.title(f'Bezier Curve - Brute Force ({time.time()-start} detik)')
        plt.show()
    




if __name__ =='__main__':
    iteration=int(input("Masukkan jumlah iterasi: "))
    # Example usage with three control points
    control_points = [(-20, 2), (2, 5), (5, 0)]

    # Divided and Conquer
    Bezier_dac.draw(control_points, iteration)

    # Brute force
    # a=Bezier_bf()
    # a.plot_bezier_curve_brute_force(control_points, iteration)
