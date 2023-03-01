out = ([(32378705212527221932533135623025613595963369358012709914405728339671376614223, 38819487114166870880675338440641088611989492705115139486764232196545036238308), (69842940699001444947118319642196642553073776903718332284726491807873962548236, 1127970563606141788355784463430840738461580530412738073901802949073783286569)], [33082007294158079418055255250651287057268988898076721118577189144520265609885, 19578527221092256596976211624992080916527291735895293318129442461499039920649], 7996126452357077558188292125102089195166096108454754869330317110485612838555)

b = []
for i in out[0]:
    b.append(i[0])
    b.append(i[1])

print(b)
print("---------------------------")

print(out[1])
print("---------------------------")

print(out[2])
print("---------------------------")

print("message = 12")

# create arg
print("---------------------------")

arg = str(b) + "," + str(out[1]) + "," + str(out[2]) + "," + str(12)
print(arg)

# check if all pointsd are on the secp256k1 curve
print("---------------------------")
def isOnSECP256K1Curve(x, y):
    p = "0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F"
    p = int(p, 16)
    return (y*y - (x*x*x + 7)) % p == 0

for i in out[0]:
    print(isOnSECP256K1Curve(i[0], i[1]))


# check if the point is on the secp256k1 curve
print("---------------------------")
def isOnCurve(point):
    p = "0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F"
    p = int(p, 16)
    point = int(point, 16)
    # check if the point is on the secp256k1 curve
    return (point*point*point + 7) % p == 0

point = "0x9a69b41c3a73d3f9411216d8e8ec81003645382c67861da75f61424ec45f1c0c027e68a185f1ea4e408222f7d0c5c6ca50c6bf767f185061e7a6df264c28eb29"
# print(isOnCurve(point))

# tranform hex point to int point
print("---------------------------")
def hexToPoint(point):
    x = int(point[0], 16)
    y = int(point[1], 16)
    return (x,y)

print("len : ", len([32378705212527221932533135623025613595963369358012709914405728339671376614223,38819487114166870880675338440641088611989492705115139486764232196545036238308,69842940699001444947118319642196642553073776903718332284726491807873962548236,1127970563606141788355784463430840738461580530412738073901802949073783286569]))