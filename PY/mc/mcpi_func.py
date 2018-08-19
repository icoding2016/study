from mcpi import minecraft
from mcpi import block
import math
import time

g_debug=True
def log(s):
    global g_debug
    if g_debug:
        print(s)

# 'global mc' (minecraft instance)
gmc = None


def init(addr="localhost", port=4711):
    global gmc
    if not gmc:
        gmc = minecraft.Minecraft.create(addr, port)
    return gmc

# param: x, y, z -- center location;
# l -- side length
# block: block type
def createFlatSquare(x, y, z, l, blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    x1 = x - int(l/2)
    z1 = z - int(l/2)
    x2 = x1 + l
    z2 = z1 + l
    gmc.setBlocks(x1, y, z1, x2, y, z2, blk)


# parameters:
# x, y, z: center point
# r: radius
# hight: hight (thicknes)    start from 1
# blk: block type
def createPie(x, y, z, radius, hight=1, blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    for angle in range(0, 180):
        x1 = x - radius * math.cos(math.radians(angle))
        x2 = x + radius * math.cos(math.radians(angle))
        z1 = z - radius * math.sin(math.radians(angle))
        z2 = z + radius * math.sin(math.radians(angle))
        gmc.setBlocks(x1, y, z1, x2, y + hight -1, z2, blk)
    #log("createPie: {},{},{}, r={}, hight={}, blk={}".format(x, y, z, r, hight, blk))


# parameters:
# x, y, z: center point
# r: radius
# blk: block type
def createFlatPie(x, y, z, radius, blk=block.COBBLESTONE):
    createPie(x, y, z, radius, hight=1, blk=blk)


# parameters:
# x, y, z: center point
# r: radius
# blk: block type
def createCircle(x, y, z, radius,blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    for angle in [i * 0.1 for i in range(0, 3600)]:
        x1 = x + radius * math.cos(math.radians(angle))
        z1 = z + radius * math.sin(math.radians(angle))
        gmc.setBlock(x1, y, z1, blk)

# parameters:
# x, y, z: center point
# r: radius
# blk: block type
def createSphere(x, y, z, radius,blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    log("createSphere ({}, {}, {}), r={}".format(x, y, z, radius))
    for angle in [i for i in range(-90, 90)]:
        y1 = y - radius * math.sin(math.radians(angle))
        r = radius * math.cos(math.radians(angle))
        createFlatPie(x, y1, z, r, blk)
        log("angle {}, @({}, {}, {}), r={}".format(angle, x, y1, z, r))


# parameters:
# x, y, z: center point
# r: radius
# blk: block type
def createSemiSphere(x, y, z, radius, upperHalf=True, blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    log("createSemiSphere ({}, {}, {}), r={}".format(x, y, z, radius))
    for angle in [i for i in range(0, 90)]:
        if upperHalf:
            y1 = y + radius * math.sin(math.radians(angle))
        else:
            y1 = y - radius * math.sin(math.radians(angle))
        r1 = radius * math.cos(math.radians(angle))
        s= "angle {},({}, {}, {}),r={}".format(angle, int(x), int(y1), int(z), int(r1))
        log(s)
        gmc.postToChat(s)
        #time.sleep(3)
        createFlatPie(x, y1, z, r1, blk)


# parameters:
# x, y, z: center point
# r: radius
# blk: block type
def createHollowSphere(x, y, z, radius,blk=block.COBBLESTONE):
    global gmc
    if not gmc:
        init()
    for angle in [i for i in range(-90, 90)]:
        y1 = y - radius * math.sin(math.radians(angle))
        r = radius * math.cos(math.radians(angle))
        createCircle(x, y1, z, r, blk)


# param: x, y, z -- center location of the floor;
# l -- side length
# block: block type
def createHollowCube(x, y, z, length, width, hight, blk=block.COBBLESTONE):
    if length < 3 or width < 3 or hight < 3:
        print("Sides should >= 3")
        return
    global gmc
    if not gmc:
        init()
    x1 = x - int(length/2)
    z1 = z - int(width/2)
    x2 = x1 + length
    z2 = z1 + width
    gmc.setBlocks(x1, y, z1, x2, y + hight, z2, blk)
    gmc.setBlocks(x1 + 1, y + 1, z1 + 1, x2 - 1, y + hight - 1, z2 - 1, block.AIR)

'''
def test():
    init()
    x, y, z = gmc.player.getPos()
    print("current position {},{},{}:".format(x,y,z))

    #createPie(x, y-100, z, radius=200, hight=200, blk=block.AIR)     #clear around

    #createFlatSquare(x+60, y, z+60, l=100);      print("createFlatSquare..")
    #createFlatPie(x+60, 100, z+60, radius=50);      print("createFlatPie..")
    #createSphere(x, y+150, z, radius=15);      print("createSphere..")
    #createSemiSphere(x-30, y, z+30, upperHalf=False, radius=15, blk=block.AIR);      print("createSemiSphere..")
    #gmc.setBlock(x,y-1,z,block.GLASS)
    #createHollowSphere(x, y, z, radius=6, blk=block.GLASS);      print("createHollowSphere..")
    #createCircle(x, 90, z, radius=50);      print("createCircle..")
    #createSemiSphere(x+30, y, z-30, upperHalf=True, radius=15, blk=block.STONE);      print("createSemiSphere..")

    #createPie(x + 60, y, z + 60, radius=20, hight=10);     print("createFlatPie..")
    #createSemiSphere(x + 20, y+4, z +20, radius=15, upperHalf=False, blk=block.WOOD);     print("createSemiSphere..")

    #createHollowCube(x+2, y, z+2, length=16, width=16, hight=10)
    gmc.player.setPos(x, y+20, z)

if __name__ == "__main__":
    test()
'''