# Diffrence between two 3d points

pointa = [3, 4, 5]
pointb = [1, 3, 5]

distance = ((pointa[0]-pointb[0])**2
            + (pointa[1]-pointb[1])**2
            + (pointa[2]-pointb[2])**2) ** (1/2)

print(distance)
