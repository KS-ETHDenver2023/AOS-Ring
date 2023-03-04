out = ([(115185473299647925444517437276795129670496237591884117069305290769490785372619, 77315467441032930729971643386403848327495819100754888420609510070437620990962), (69842940699001444947118319642196642553073776903718332284726491807873962548236, 1127970563606141788355784463430840738461580530412738073901802949073783286569)], [114070909771798144061033143658994727919231429968475036840050448285267762423138, 1802546309282196647977732518169973279415824827658044092793845717176648895681], 115446977612368562129913005937141401631043489879524287482172437913868108576226)
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

print("Public key x: ", str(int("fea8aae454369d6347279ce06deff495a0503817f0cc109c9dfae0a6960c89cb",16)))
print("Public key y: ", str(int("aaef00f9c16a07d2440cf459a287f74459c88b83b69b0b15d6a4c5f78837c3f2",16)))