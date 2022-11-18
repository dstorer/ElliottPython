import pytest

def findConsecutiveMax(array):
    maxCharacter=""
    numMax=0
    lastChar=""
    numCurrent=1
    try:
        list(array)
    except:
        raise TypeError('Input must be an array or list.')        
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
    res = findConsecutiveMax(["","a","a","z","y","y","","y","z","z","z"])
    assert res=="y"
    res = findConsecutiveMax(["z","a","a","z","y","y","","y","z","z",""])
    assert res=="y"
    res = findConsecutiveMax(["z","a","a","z","y","y","","","y","z","z","z"])
    assert res=="y"
    res = findConsecutiveMax(["z","a","a","z","y","","y","","y","z","z","z"])
    assert res=="y"
    res = findConsecutiveMax(["y","y","y","z","a","y","","y","z","z","z"])
    assert res=="y"
    res = findConsecutiveMax(["y","y","y","z","a","y","","y","z","z","z","z"])
    assert res=="z"
    res = findConsecutiveMax(["y",1,"y","z","a","y","","y","z","z","z","z"])
    assert res=="z"
    res = findConsecutiveMax(["y",1,1,1,"a","y","","y","z","z","z"])
    assert res==1
    res = findConsecutiveMax([1,1,1,"a","a","y","","y","z","z","z"])
    assert res==1
    res = findConsecutiveMax([1,1,1,"a","a","y","","y",2,2,2,2])
    assert res==2
    res = findConsecutiveMax([1,1,1,"a","a","y","","y",2,2,"",2,2])
    assert res==2

def test_inputString():
    res = findConsecutiveMax("abc")
    assert res == "a"
    with pytest.raises(TypeError,match='Input must be an array or list.'):
        res = findConsecutiveMax(1)
    with pytest.raises(TypeError,match='Input must be an array or list.'):
        res = findConsecutiveMax(1.5)
        
