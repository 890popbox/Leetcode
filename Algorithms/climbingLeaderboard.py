# Remove duplicates in place O(N)
# Scan players score against ranks O(N * R), N is how much rounds a player played, R is amount of distinct ranks
def climbingLeaderboard(ranked, player):
    # Remove duplicates in place from the player ranks
    index = 1
    for r in range(1, len(ranked)):
        if ranked[r - 1] != ranked[r]:
            ranked[index] = ranked[r]
            index += 1
    # Index is now the last place in the ranked array
    index -= 1
    # Check the players score as it increases and store the ranks they achieve
    output = []
    for p in player:
        # If the rank is less than or equal to the current players score, move it up
        while index >= 0 and ranked[index] <= p:
            index -= 1
        # Index is moved twice, one move represents the rank it would be, the second represents the spot it is in
        output.append(index + 2)
    return output


# Creating the test case
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
print(climbingLeaderboard([1], [1, 1]))
