# bismillah

import math

points = [ ( 9,2 ),( 8,3 ),( 7,4 ),( 6,5 ) ]

def euclideanDistance( point1,point2 ):
    x1,y1 = point1
    x2,y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
 

distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)