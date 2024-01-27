import pandas as pd
import numpy as np
import copy
import math

def merge(ttuple):
    temp_tuple=copy.deepcopy(ttuple)
    temp_tuple.sort(key=lambda interval: interval[0])
    merged = [temp_tuple[0]]
    for current in temp_tuple:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
    return merged

def sum_range(r):
    return sum([x[1]-x[0] for x in r])

def skip_range(r,s):
    x1,y1=s
    assert x1<y1
    r0=[]
    for x in r:
        x0,y0=x
        assert x0<y0
        if max(x0,x1)<min(y0,y1):
            pass
        else:
            r0.append(x)
    return r0

def skip_ranges(r,s):
    r0=copy.deepcopy(r)
    for s0 in s:
        r0=skip_range(r0,s0)
    return r0

def skip_sspan(r,s,inv=False):
    r0=[]
    for x in r:
        if (x[1]-x[0])<s:
            pass
        else:
            # only greater or equal to.
            r0.append(x)
    if inv:
        return [x for x in r if x not in r0]
    return r0
#print(csv)
#print(dir(csv))
def trial(csv,target,rate,span,skips,sspan,espan,step,rinv=False,inv=False,ahead=False):
    assert target>0 and target<1
    assert rate>0
    assert span>0 and type(span) == int
    assert sspan>0 and type(sspan) == int
    assert espan>0 and type(espan) == int
    assert step>0 and type(step) == int
    assert type(skips) == list 
    for x0,x1 in skips:
        assert x0<x1
        assert type(x0) == type(x1)
        assert type(x0) == int
    p=csv[0]
    final=p.sort_values().to_list()[-1:][0]
    s=p.groupby(pd.cut(p,np.arange(0,math.floor(final),step))).count()
#print(s)
    s0=pd.DataFrame({"density":s,"ema":s.ewm(span=espan,adjust=False).mean()})
#print(s0)
    s1=s0.shape[0]
    can=[]
# still counting. factor things out.
    for x in range(s1):
        s2=s0.iloc[x]
        den, ema=s2["density"],s2["ema"]
        if den>ema*rate and not rinv:
            print(den,ema,x)
            xs0=x*step-span
            xs1=x*step+span
            can.append([max([xs0,0]),min([final,xs1])]) 
        elif den<=ema*rate and rinv:
            print(den,ema,x)
            xs0=x*step-span
            xs1=x*step+span
            can.append([max([xs0,0]),min([final,xs1])])
 
    if ahead:
        can = skip_ranges(can,skips)
    merged=merge(can)
    print(merged)
    skipped=merged
    if not ahead:
        skipped=skip_ranges(merged,skips)
    print(skipped)
    skimmed=skip_sspan(skipped,sspan,inv=inv)
    sr=sum_range(skimmed)
    rws=sr/final
    return rws, skimmed
# get the percentage.
target=0.2
rate=1.2
span=2
skips=[[0,5],[70,80]]
sspan=5
espan=4
step=3

lr=0.1

rates=[]
rwss={}
lastrate=None
csv = pd.read_csv("danmaku.csv",header=None)

while True:
    rws, skipped=trial(csv,target,rate,span,skips,sspan,espan,step)
    print("result",rws,skipped,rate)
    lastrate=rate
    #lastrws=rws
    rwss[rate]=rws
    if rws>target:
        rate+=lr
    else:
        rate-=lr
    if rate<0 or rate>5:
        print("not found.",rate)
        break
    elif rate in rates:
        rr,rlr=rwss[rate],rwss[lastrate]
        #print(lastrate,rlr,rate,rr)
        equ=(lastrate*rlr+rate*rr)/(rlr+rr)
        print("found equllibrium.",equ)
        break
    rates.append(rate)
#change the shit accordingly?
