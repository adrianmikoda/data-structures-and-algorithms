# O(nlogn) time complexity


def snow( S ):
    S.sort()
    S = S[::-1]
    j=0
    suma=0

    while(S[j]-j>0):
        suma += (S[j]-j)
        j+=1

    return suma


S = [1, 7, 3, 4, 1]
print(snow(S))