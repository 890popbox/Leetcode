def findCenter(self, edges):
    # if the first digit of the edge is equal to another edges first digit, that is our answer
    # if that is not true, the second digit must be the center of the star
    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
        return edges[0][0]
    return edges[0][1]
