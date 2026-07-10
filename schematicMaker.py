import mcschematic
# Creating schematic object
schem = mcschematic.MCSchematic()
try :
    code = open("program.mc", "r")
except :
    print("Machine Code file (program.mc) not found! Press return to continue...")
    input()

n = 0
xOffset = 0
zOffset = 0
# Conversion
for line in code :
    linelst = list(line)
    if n % 2 == 0 :
        zOffset -= 11
    else :
        zOffset -= 2
    if n == 16 :
        n = 0
        xOffset -= 2
        zOffset = -11
    n += 1
    for i in range(0, 17) :
        if linelst[i] == "1" :
            schem.setBlock((xOffset, (i*2)-33, zOffset+11), "minecraft:stone")
        elif linelst[i] == "0" :
            schem.setBlock((xOffset, (i*2)-33, zOffset+11), "minecraft:glass")
# Saving schematic file
schem.save("schems", "program", mcschematic.Version.JE_1_21_1)