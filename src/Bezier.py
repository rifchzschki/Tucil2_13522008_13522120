import matplotlib.pyplot as plt
import time
__all__ = ["Bezier_dac", "Bezier_bf"]

class Bezier_dac: # devided and conquer
    print('a')

class Bezier_bf: # brute force
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
    a=Bezier_bf()
    control_points = [(0, 0), (2, 5), (5, 0)]
    a.plot_bezier_curve_brute_force(control_points, iteration)
