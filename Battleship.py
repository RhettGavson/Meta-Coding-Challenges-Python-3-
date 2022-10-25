# This is a function that calculates odd of hitting a battleship in a battleship game
R = 4
C = 3

G =  [[1,0,1],
     [1,0,1],
     [0,1,1],
     [1,0,1]]

#print (G)
print(G)


total = R*C
ship = 0
for x in range(0,R):
     for y in range(0,C):
          if G[x][y] == 1:
               ship += 1
               print(ship)

probability = ship/total
print(probability)