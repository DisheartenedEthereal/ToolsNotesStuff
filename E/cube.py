class Cube(object):
    """Intilizes a cube with dimensions and direction"""
    def __init__(self, sizeX, sizeY, direction=0):
        self.sizeX = int(sizeX)
        self.sizeY = int(sizeY)
        self.direction = direction

    def convertYAxisToXFactor(self):
        return int(self.sizeY / 3)
    def initCube(self):
        self.sizeX = x
        self.sizeY = y
        cube = [x*y]
        for i in cube:
            if i == 0:
                cube[i] = "+"
            elif i == x:
                cube[i] = "+"
            elif i == 
    def assembleCube(self,dir="none"):
        print(self.sizeY)
        print("\n" * 5)
        if dir == "none":
            print("+" + self.top + "+")
            print(self.left + ' ' * sizeX_wout_borders + self.right)
            print("+" + self.bottom+ "+")
x = Cube(9, 9)
x.initCube()
x.assembleCube()
