# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
class triangle():
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        self.a = [self.B[0]-self.C[0], self.B[1]-self.C[1]]
        self.b = [self.C[0]-self.A[0], self.C[1]-self.A[1]]
        self.c = [self.B[0]-self.A[0], self.B[1]-self.A[1]]
        self.am = (self.a[0]**2 + self.a[1]**2)**0.5
        self.bm = (self.b[0]**2 + self.b[1]**2)**0.5
        self.cm = (self.c[0]**2 + self.c[1]**2)**0.5
    def calc_square(self):
        self.square = abs(self.c[0]*self.b[1] - self.c[1]*self.b[0])/2
    def calc_h(self):
        self.calc_square()
        self.h = self.square*2/self.am
    def calc_P(self):
        self.P = self.am + self.bm + self.cm

tri_1 = triangle([0,0],[0,1],[10,0])
tri_1.calc_square()
tri_1.calc_h()
tri_1.calc_P()
print('Task1','\nSquare = ',tri_1.square,'\nh = ',tri_1.h,'\nP = ',tri_1.P,sep='')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class equal_trapezium():
    def __init__(self,A,B,C,D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.base1 = [self.A[0]-self.D[0], self.A[1]-self.D[1]]
        self.base2 = [self.B[0]-self.C[0], self.B[1]-self.C[1]]
        self.edge1 = [self.B[0]-self.A[0], self.B[1]-self.A[1]]
        self.edge2 = [self.D[0]-self.C[0], self.D[1]-self.C[1]]
        self.base1m = (self.base1[0]**2 + self.base1[1]**2)**0.5
        self.base2m = (self.base2[0]**2 + self.base2[1]**2)**0.5
        self.edge1m = (self.edge1[0]**2 + self.edge1[1]**2)**0.5
        self.edge2m = (self.edge2[0]**2 + self.edge2[1]**2)**0.5
    def check_trap(self):
        base_square = self.base1[0]*self.base2[1] - self.base1[1]*self.base1[0]
        if base_square == 0 and self.edge1m == self.edge2m:
            self.check = True
        else:
            self.check = False
    def calc_P(self):
        self.P = self.base1 + self.base2 + self.edge1 + self.edge2
    def calc_square(self):
        self.square = abs(self.base1[0]*self.edge1[1] - self.base1[1]*self.edge1[0])/2 +\
                      abs(self.base2[0]*self.edge2[1] - self.base2[1]*self.edge2[0])/2

trap_1 = equal_trapezium([0,0],[1,1],[9,1],[10,0])
trap_1.check_trap()
trap_1.calc_P()
trap_1.calc_square()
print('\n\nTask2','\nCheck = ',trap_1.check,\
      '\nBase1 = ',trap_1.base1m,'\nBase2 = ',trap_1.base2m,\
      '\nEdge1 = ',trap_1.edge1m,'\nEdge2 = ',trap_1.edge2m,\
      '\nP = ',trap_1.P,'\nSquare = ',trap_1.square,sep='')
