''''def fibonach(num: int) -> int:
    if num <= 3:
        return num
    else:
        return fibonach(num - 2) + fibonach(num - 1)

for i in range(7):
    print(fibonach(i))''''

def min2max(nList: list, n: int, minEl: int, maxEl: int, maxIdx: int) -> list:
    if n == len(nList):
        nList[maxIdx] = minEl
        return nList
    else:
        if minEl > nList[n]:
            minEl = nList[n]
        if maxEl < nList[n]:
            maxEl = nList[n] 
            maxIdx = n
        min2max(nList, n + 1, minEl, maxEl, maxIdx)
        return maxEl, maxIdx
    
nLst = [1, 2, 3, 4, 5]
print(min2max(nLst, 0, nLst[0], nLst[0], maxIdx = 0))


