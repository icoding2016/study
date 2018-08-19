from mcpi import minecraft
from mcpi import block
import math
import time

class Mcapi(object):
    mc = None
    debug_enable = None
    
    def __init__(self, addr='localhost', port=4711):
        self._initMc_(addr, port)
        self.debug_enable = True

    def log(self, s):
        if self.debug_enable:
            print(s)

    def _initMc_(self, addr='localhost', port=4711):
        if not self.mc:
            self.mc = minecraft.Minecraft.create(addr, port)

    def getMc(self):
        return self.mc

     # param: x, y, z -- center location;
    # l -- side length
    # block: block type
    def createFlatSquare(self, x, y, z, l, blk=block.COBBLESTONE):
        x1 = x - int(l/2)
        z1 = z - int(l/2)
        x2 = x1 + l
        z2 = z1 + l
        self.mc.setBlocks(x1, y, z1, x2, y, z2, blk)
    
    # parameters:
    # x, y, z: center point
    # r: radius
    # hight: hight (thicknes)    start from 1
    # blk: block type
    def createPie(self, x, y, z, radius, hight=1, blk=block.COBBLESTONE):
        for angle in range(0, 180):
            x1 = x - radius * math.cos(math.radians(angle))
            x2 = x + radius * math.cos(math.radians(angle))
            z1 = z - radius * math.sin(math.radians(angle))
            z2 = z + radius * math.sin(math.radians(angle))
            self.mc.setBlocks(x1, y, z1, x2, y + hight -1, z2, blk)
        #self.log("createPie: {},{},{}, r={}, hight={}, blk={}".format(x, y, z, r, hight, blk))
    
    # parameters:
    # x, y, z: center point
    # r: radius
    # blk: block type
    def createFlatPie(self, x, y, z, radius, blk=block.COBBLESTONE):
        self.createPie(x, y, z, radius, hight=1, blk=blk)
    
    # parameters:
    # x, y, z: center point
    # r: radius
    # blk: block type
    def createCircle(self, x, y, z, radius,blk=block.COBBLESTONE):
        for angle in [i * 0.1 for i in range(0, 3600)]:
            x1 = x + radius * math.cos(math.radians(angle))
            z1 = z + radius * math.sin(math.radians(angle))
            self.mc.setBlock(x1, y, z1, blk)
    
    # parameters:
    # x, y, z: center point
    # r: radius
    # blk: block type
    def createSphere(self, x, y, z, radius,blk=block.COBBLESTONE):
        self.log("createSphere ({}, {}, {}), r={}".format(x, y, z, radius))
        for angle in [i for i in range(-90, 90)]:
            y1 = y - radius * math.sin(math.radians(angle))
            r = radius * math.cos(math.radians(angle))
            self.createFlatPie(x, y1, z, r, blk)
            self.log("angle {}, @({}, {}, {}), r={}".format(angle, x, y1, z, r))

    # parameters:
    # x, y, z: center point
    # r: radius
    # blk: block type
    def createSemiSphere(self, x, y, z, radius, upperHalf=True, blk=block.COBBLESTONE):
        self.log("createSemiSphere ({}, {}, {}), r={}".format(x, y, z, radius))
        for angle in [i for i in range(0, 90)]:
            if upperHalf:
                y1 = y + radius * math.sin(math.radians(angle))
            else:
                y1 = y - radius * math.sin(math.radians(angle))
            r1 = radius * math.cos(math.radians(angle))
            s= "angle {},({}, {}, {}),r={}".format(angle, int(x), int(y1), int(z), int(r1))
            self.log(s)
            self.mc.postToChat(s)
            #time.sleep(3)
            self.createFlatPie(x, y1, z, r1, blk)

    # parameters:
    # x, y, z: center point
    # r: radius
    # blk: block type
    def createHollowSphere(self, x, y, z, radius,blk=block.COBBLESTONE):
        for angle in [i for i in range(-90, 90)]:
            y1 = y - radius * math.sin(math.radians(angle))
            r = radius * math.cos(math.radians(angle))
            self.createCircle(x, y1, z, r, blk)

    # param: x, y, z -- center location of the floor;
    # l -- side length
    # block: block type
    def createHollowCube(self, x, y, z, length, width, hight, blk=block.COBBLESTONE):
        if length < 3 or width < 3 or hight < 3:
            print("Sides should >= 3")
            return

        x1 = x - int(length/2)
        z1 = z - int(width/2)
        x2 = x1 + length
        z2 = z1 + width
        self.mc.setBlocks(x1, y, z1, x2, y + hight, z2, blk)
        self.mc.setBlocks(x1 + 1, y + 1, z1 + 1, x2 - 1, y + hight - 1, z2 - 1, block.AIR)
