def findConsecutiveMax(array):
    maxCharacter=""
    numMax=0
    lastChar=""
    numCurrent=1
    for i,x in enumerate(array):
        if x == "":
            continue
        if x==lastChar:
            numCurrent=numCurrent+1
        else:
            numCurrent=1
        if numCurrent>numMax:
            numMax=numCurrent
            maxCharacter=x
        lastChar=x
    return maxCharacter

def test_consecMax():
    res = findConsecutiveMax(["z","a","a","z","y","y","","y","z","z","z"])
    assert res=="y"
    
# def test_consecMax2():
#     res = findConsecutiveMax(["z","a","a","z","y","y","","y","z","z","z"])
#     assert res=="z"