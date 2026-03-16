import math
# 1) KNN classification

# dataset
data = [
["A",1,2,"Red"],
["B",2,3,"Red"],
["C",3,1,"Blue"],
["D",6,5,"Blue"]
]

x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))

dist = []

# distance calculation
for p in data:
    name = p[0]
    px = p[1]
    py = p[2]
    label = p[3]
    d = math.sqrt((x-px)**2 + (y-py)**2)
    dist.append([d,name,label])

# sorting
dist.sort()

print("Nearest Neighbors:")

k = 3
red = 0
blue = 0

for i in range(k):

    d = dist[i][0]
    name = dist[i][1]
    label = dist[i][2]

    print(name,"Distance:",round(d,2))

    if label == "Red":
        red += 1
    else:
        blue += 1

if red > blue:
    print("Predicted Class: Red")
else:
    print("Predicted Class: Blue")

# 2) Changing k value
import math

data = [
["A",1,2,"Red"],
["B",2,3,"Red"],
["C",3,1,"Blue"],
["D",6,5,"Blue"]
]

x = 2
y = 2

dist = []

for p in data:
    px = p[1]
    py = p[2]
    label = p[3]

    d = math.sqrt((x-px)**2 + (y-py)**2)
    dist.append([d,label])

dist.sort()

def predict(k):
    red = 0
    blue = 0

    for i in range(k):

        label = dist[i][1]

        if label == "Red":
            red += 1
        else:
            blue += 1

    if red > blue:
        return "Red"
    else:
        return "Blue"

print("Prediction Results")

print("K = 1 ->",predict(1))
print("K = 3 ->",predict(3))
print("K = 4 ->",predict(4))


# 3) Student pass or fail 
import math

data = [
[2,60,"Fail"],
[5,80,"Pass"],
[6,85,"Pass"],
[1,50,"Fail"]
]

study = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance: "))

dist = []

for p in data:
    h = p[0]
    a = p[1]
    label = p[2]

    d = math.sqrt((study-h)**2 + (attendance-a)**2)
    dist.append([d,label])

dist.sort()

k = 3
pass_count = 0
fail_count = 0

for i in range(k):
    label = dist[i][1]

    if label == "Pass":
        pass_count += 1
    else:
        fail_count += 1

if pass_count > fail_count:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")
