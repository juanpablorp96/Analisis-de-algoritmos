
def hotel(array):
    hotels = array
    best_path = [0] * len(hotels)
    stop = [0] * len(hotels)
    for i in range(0, len(hotels)):
        best_path[i] = pow((200 - hotels[i]), 2)
        stop[i] = 0
        for j in range(0, i):
            if (best_path[j] + pow(200 - (hotels[i] - hotels[j]), 2)) < best_path[i]:
                best_path[i] = best_path[j] + pow(200 - (hotels[i] - hotels[j]), 2)
                stop[i] = j + 1

    print("Minimal penalty: ", best_path)
    final_path = " "
    index = len(stop) - 1
    while index >= 0:
        final_path = str((index + 1)) + " " + final_path
        index = stop[index] - 1

    print(stop)
    print("Stop at: ", final_path)


hotel([0, 200, 100, 400, 800, 10, 1000])
