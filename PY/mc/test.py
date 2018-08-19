from mcpi import block
from mcapi import Mcapi


def test():
    api = Mcapi()
    mc = api.getMc()
    x, y, z = mc.player.getPos()
    print("current position {},{},{}:".format(x,y,z))

    mc.setBlock(x, y+3, z, block.TORCH)
    mc.setBlock(x, y+5, z, block.TORCH)
    #mc.setBlock(x, y+5, z, block.TORCH)
    mc.setBlock(x, y+7, z, block.TORCH)
    #createPie(x, y-100, z, radius=200, hight=200, blk=block.AIR)     #clear around

    #createFlatSquare(x+60, y, z+60, l=100);      print("createFlatSquare..")
    #createFlatPie(x+60, 100, z+60, radius=50);      print("createFlatPie..")
    #api.createSphere(x, y, z, radius=5, blk=block.GLASS);      print("createSphere..")
    #createSemiSphere(x-30, y, z+30, upperHalf=False, radius=15, blk=block.AIR);      print("createSemiSphere..")
    #gmc.setBlock(x,y-1,z,block.GLASS)
    #createHollowSphere(x, y, z, radius=6, blk=block.GLASS);      print("createHollowSphere..")
    #createCircle(x, 90, z, radius=50);      print("createCircle..")
    #createSemiSphere(x+30, y, z-30, upperHalf=True, radius=15, blk=block.STONE);      print("createSemiSphere..")

    #createPie(x + 60, y, z + 60, radius=20, hight=10);     print("createFlatPie..")
    #createSemiSphere(x + 20, y+4, z +20, radius=15, upperHalf=False, blk=block.WOOD);     print("createSemiSphere..")

    #createHollowCube(x+2, y, z+2, length=16, width=16, hight=10)

    #mc.player.setPos(x, y-8, z)

test()