INF = 1000000


# weight[] initial cost array including unavailable packet
# W capacity of bag
def MinimumWeight(weight, n, V):
    # weights[] and value[] arrays
    # weights[] array to store cost of 'i' kg packet of orange
    # value[] array weight of packet of orange
    weights = list()
    value = list()

    # traverse the original cost[] array and skip
    # unavailable packets and make weights[] and value[]
    # array. size variable tells the available number
    # of distinct weighted packets.
    size = 0
    for i in range(n):
        if weight[i] != -1:
            weights.append(weight[i])
            value.append(i + 1)
            size += 1

    n = size
    min_weight = [[0 for i in range(V + 1)] for j in range(n + 1)]

    # fill 0th row with infinity
    for i in range(V + 1):
        min_weight[0][i] = INF

        # fill 0th column with 0
    for i in range(1, n + 1):
        min_weight[i][0] = 0

    # now check for each weight one by one and fill the
    # matrix according to the condition
    for i in range(1, n + 1):
        for j in range(1, V + 1):
            # value[i-1]>j means capacity of bag is
            # less than weight of item
            if value[i - 1] > j:
                min_weight[i][j] = min_weight[i - 1][j]

                # here we check we get minimum cost either
            # by including it or excluding it
            else:
                min_weight[i][j] = min(min_weight[i - 1][j], min_weight[i][j - value[i - 1]] + weights[i - 1])

                # exactly weight W can not be made by given weights
    if min_weight[n][V] == INF:
        return -1
    else:
        return min_weight[n][V]

    # Driver program to run the test case


cost = [20, 10, 4, 50, 100]
V = 6
n = len(cost)

print(MinimumWeight(cost, n, V))
