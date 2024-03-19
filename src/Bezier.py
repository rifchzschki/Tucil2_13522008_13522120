import matplotlib.pyplot as plt
import time
import os
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
        
    def draw(n, control_points, iteration):
        curve = []
        start = time.time()
        for i in range(n-2):
            print(i)
            curve+=(Bezier_dac.curve(*control_points[i:i+3], iteration))

        print(curve)   
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
        elif(len(x)>100):
            n=5
        else:
            n=1
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
        # print(in_end)
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
    def coordinates(self, points, iteration):# Brute force akan membagi kurva menjadi jumlah iterasi, lalu menghitung nilai titik di tiap bagian, lalu menghubungkannya
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
        # a=iteration
        # for i in range (a): #supaya jumlah titik per iterasi sama dengan DnC
        #     if i==0:
        #         iteration=3
        #     else:
        #         iteration=iteration*2 -1
        iteration=(2**iteration)+1#supaya jumlah titik per iterasi same dengan DnC
        x,y = self.coordinates(points, iteration)
        end=time.time()-start
        print(list(zip(x,y)))
        plt.scatter(*zip(*points), color='red')
        plt.plot(*zip(*points), color='green')  
        plt.plot(x, y)
        plt.title(f'Bezier Curve - Brute Force ({end} detik)')
        plt.show()
    




if __name__ =='__main__':
    iter_in = True
    while(iter_in):
        if os.name == 'nt':  # Jika sistem operasi adalah Windows
            os.system('cls')
        else:  # Untuk sistem operasi lainnya (Unix/Linux/MacOS)
            os.system('clear')
        print("Mari buat Bezier curve terbaik anda!")
        n = int(input("Masukkan jumlah control points: "))
        iteration=int(input("Masukkan jumlah iterasi: "))
        iter_in =  False
        # Example usage with three control points
        # control_points = [(-20, 2), (2, 5), (5, 0)]
        control_points=[]
        i = 0
        while(i<n):
            control=input("Masukkan koordinat titk kontrol <x,y> : ")
            try:
                x, y = map(float, control.split(','))#Format in put "x, y"
                tuple_control = (x, y)
                control_points.append(tuple_control)
                i+=1
            except ValueError:
                print("Input invalid. Masukkan input dalam format 'x, y'")
        if n==3:
            print("Pilih algoritma")
            print("1. Divide and Conquer")
            print("2. Brute Force")
            try:
                algo = int(input())
                if algo == 1:
                    Bezier_dac.draw(n, control_points, iteration)
                elif algo == 2:
                    a=Bezier_bf()
                    a.draw_coordinates(control_points, iteration)
                else:
                    raise ValueError("Input harus 1 atau 2")
            except ValueError as error:
                print(error)
            plt.close()
        else:
            print("Algoritma Brute Force tidak mendukung titik kontrol selain tiga.")
            print("Program akan menggunakan algoritma Divide and Conquer.")
            Bezier_dac.draw(n, control_points, iteration)
            plt.close()
        is_iter = input("Lagi ?(y/n)")
        if(is_iter == 'y'):
            iter_in = True
        else:
            print("Bye-bye...\nsampai jumpa nanti")
