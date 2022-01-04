

class Bezier:


    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def lerp(self, n1, n2, perc):
        diff = n2 - n1
        return n1 + ( diff * perc )

    def bezier(self, i):

        # The Green Lines
        xa = self.lerp( 0 , self.x1 , i )
        ya = self.lerp( 0 , self.y1 , i )
        xb = self.lerp( self.x1 , self.x2 , i )
        yb = self.lerp( self.y1 , self.y2 , i )
        xc = self.lerp( self.x2 , 1 , i )
        yc = self.lerp( self.y2 , 1 , i )

        # The Blue Line
        xm = self.lerp( xa , xb , i )
        ym = self.lerp( ya , yb , i )
        xn = self.lerp( xb , xc , i )
        yn = self.lerp( yb , yc , i )

        # The Black Dot
        y = self.lerp( ym , yn , i )
        return y


bez = Bezier(0.17,0.67,0.87,0.42)

iiii = [ (i+1)*0.01 for i in range(0,100) ]

for i in iiii:
    print(bez.bezier(i) * 255)
