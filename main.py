import math
import random

def generateRoom(position, generatedDungeon, roomMinSize, roomMaxSize):

# Incomplete, generates individual rooms

    generatedRoom = [[" " for i in range(roomMaxSize)] for j in range(roomMaxSize)]
    roomWidth = random.randint(roomMinSize, roomMaxSize) - 1
    roomHeight = random.randint(roomMinSize, roomMaxSize) - 1
    roomWidthOffset = random.randint(1, (roomMaxSize - roomWidth)) - 1
    roomHeightOffset = random.randint(1, (roomMaxSize - roomHeight)) - 1
    generatedRoom[0 + roomWidthOffset][0 + roomHeightOffset] = '+'
    for i in range(1, roomWidth):
        generatedRoom[i + roomWidthOffset][0 + roomHeightOffset] = '#'
    generatedRoom[roomWidth + roomWidthOffset][0 + roomHeightOffset] = '+'
    for i in range(1, roomHeight):
        generatedRoom[roomWidth + roomWidthOffset][i + roomHeightOffset] = '#'
    generatedRoom[roomWidth + roomWidthOffset][roomHeight + roomHeightOffset] = '+'
    for i in range(1, roomWidth):
        generatedRoom[i + roomWidthOffset][roomHeight + roomHeightOffset] = '#'
    generatedRoom[0 + roomWidthOffset][roomHeight + roomHeightOffset] = '+'
    for i in range(1, roomHeight):
        generatedRoom[0 + roomWidthOffset][i + roomHeightOffset] = '#'
    for i in range(1, roomWidth):
        for j in range(1, roomHeight):
            generatedRoom[i + roomWidthOffset][j + roomHeightOffset] = '.'
    return generatedRoom

def updateDungeon(position, generatedDungeon, generatedRoom):

# Overwrites a cell of the dungeon with a generated room

    for i in range(roomMaxSize):
        for j in range(roomMaxSize):
            generatedDungeon[position[0]+i][position[1]+j] = generatedRoom[i][j]
    return generatedDungeon

def generateDungeon(roomTotal, dungeonDensity, roomMinSize, roomMaxSize, dungeonSize):

# Generates the dungeon array
    
    generatedDungeon = [[" " for i in range(dungeonSize)] for j in range(dungeonSize)]
    cellIndices = []
    for i in range(int(dungeonSize/roomMaxSize)):
        for j in range(int(dungeonSize/roomMaxSize)):
            cellIndices.append((i*roomMaxSize, j*roomMaxSize))
    dungeonRooms = random.sample(cellIndices, roomTotal)
    for position in dungeonRooms:
        generatedRoom = generateRoom(position, generatedDungeon, roomMinSize, roomMaxSize)
        generatedDungeon = updateDungeon(position, generatedDungeon, generatedRoom)
    return generatedDungeon

def printDungeon(generatedDungeon, dungeonSize):

# Prints dungeon to output.txt

    print('', end='', file=open("output.txt", "w"))
    for i in range(dungeonSize):
        for j in range(dungeonSize):
            print(generatedDungeon[i][j], end='', file=open("output.txt", "a"))
        print("", file=open("output.txt", "a"))

roomTotal = -1
while(roomTotal >= 101 or roomTotal <= 0):
    roomTotal = int(input("How many rooms should there be (between 1 and 100)? "))
    if(roomTotal >= 101 or roomTotal <= 0):
        print("Invalid input.")
dungeonDensity = -1
while(dungeonDensity >= 4 or dungeonDensity <= 0):
    dungeonDensity = int(input("How dense should the dungeon be (1-3, where 1 is sparse, 3 is dense (option 1 is very slow)))? "))
    if(dungeonDensity >= 4 or dungeonDensity <= 0):
        print("Invalid input.")
roomMinSize = -1
while(roomMinSize >= 15 or roomMinSize <= 4):
    roomMinSize = int(input("How small should the rooms be (5-15)? "))
    if(roomMinSize >= 15 or roomMinSize <= 4):
        print("Invalid input.")
roomMaxSize = -1
while(roomMaxSize >= 16 or roomMaxSize < roomMinSize):
    roomMaxSize = int(input("How large should the rooms be (room minimum size - 15)? "))
    if(roomMaxSize >= 16 or roomMaxSize < roomMinSize):
        print("Invalid input.")
print("Generating dungeon...")
dungeonSize = -1
if(dungeonDensity == 1):
    dungeonSize = roomMaxSize * roomTotal * roomTotal
elif(dungeonDensity == 2):
    dungeonSize = roomMaxSize * roomTotal
elif(dungeonDensity == 3):
    dungeonSize = roomMaxSize * math.ceil(math.sqrt(roomTotal))

# Need to rework dungeonSize generation
# Size 3 is too small, size 2 is too big, size 1 is way too big
# Should generate on a range between sizes 2 and 3

generatedDungeon = generateDungeon(roomTotal, dungeonDensity, roomMinSize, roomMaxSize, dungeonSize)
printDungeon(generatedDungeon, dungeonSize)