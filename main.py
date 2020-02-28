def squares_intersect(s1, s2):
    
    # Assigns the positions of the points (edges of the squares) based on a (x,y,s) coordinate system where s is the length of the squares.
    
    x1 = s1[0]
    y1 = s1[1]
    w1 = s1[2]
    h1 = s1[2]
    x2 = s2[0]
    y2 = s2[1]
    w2 = s2[2]
    h2 = s2[2]
    
    # Checks for any points of intersection by comparing the relative positions of the sum of (x+w) or (y+h) to... 
    # the x or y coordinates of the other square.

    if ((x1+w1<x2) or (x2+w2<x1) or (y1+h1<y2) or (y2+h2<y1)):
        return False
    else:
        return True
