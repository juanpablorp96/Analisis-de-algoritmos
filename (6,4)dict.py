
dictionary = ["it", "was", "the", "best", "of", "times"]
s = "itwasthebestoftimes"
size = len(s)
dp = [-1] * (size + 1)
dp[0] = 0
res = []
for i in range(0, size):
    if dp[i] != -1:
        for j in range(i + 1, size + 1):
            length = j
            substr = s[i:length]
            if substr in dictionary:
                res.append(substr + " ")
                dp[length] = dp[i] + 1
print(dp)
print("result: ", res)
