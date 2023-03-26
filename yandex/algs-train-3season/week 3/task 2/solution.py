st = input()
tab = st.split()
n = int(tab[0])
k = int(tab[1])

dp = [0]*35
dp[1] = 1
dp[2] = 1

for i in range(3, k):
    dp[i] = 2 * dp[i-1]

i = 3
while i <= n:
    dp[i] = 2 * dp[i-1] - dp[i-k-1]
    i += 1
print(dp[n])
