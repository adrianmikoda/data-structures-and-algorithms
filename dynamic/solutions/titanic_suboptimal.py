# suboptimal solution
# O(mn) time complexity


def titanic(W, M, D):
    codes = {}
    s = ""
    for c, code in M:
        codes[c] = code
    
    for c in W:
        s += codes[c]

    n = len(s)

    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0

    for i in range(n+1):
        for j in D:
            d = M[j][1]
            if i >= len(d)-1:
                if s[i-len(d):i] == d:
                    dp[i] = min(dp[i], dp[i-len(d)] + 1)
    
    return dp[n]


W = 'SOS'
M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
     ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
     ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
     ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
     ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
     ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
     ('Y', '-.--'), ('Z', '--..')]
D = [0, 4, 13, 19, 25]
print(titanic(W, M, D))