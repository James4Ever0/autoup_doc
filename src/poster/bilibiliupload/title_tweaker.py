import jieba
import random
from better_profanity import profanity
import l33t
from mText import Markov
# this is just demostration.

sysrand = random.SystemRandom()

def randomConcat(x,limit=80):
    if len(x)>limit:
        y = random.choice(list(range(len(x)-limit)))
        return x[y:y+limit]
    return x

def minmax(_min,_max):
    assert _max>_min
    _range = _max-_min
    return sysrand.random()*_range+_min

def randomInject(string,x):
    l = len(string)
    lp = list(range(0,l))
    sysrand.shuffle(lp)
    f = lp[0]
    a, b = string[0:f], string[f:l]
    return a+x+b

def spacing(string,space):
    assert len(space)>1
    return space.join(string)

def randomSpacing(string,space,gfactor):
    out = ""
    for x in string:
        factor = gfactor()
        factor = round(factor)
        assert factor>=1
        out += x+space*factor
    return out

def leetspeak(string):
    return l33t.l33t(string)

def randomLeet(string,k=0.5):
    y=""
    for x in string:
        if sysrand.random()>k:
            x=leetspeak(x)
        y+=x
    return y

def censor(string):
    return profanity.censor(string)

def markov(string):
    mk = Markov()
    mk.add_to_dict(string)
    return mk.create_sentence()
