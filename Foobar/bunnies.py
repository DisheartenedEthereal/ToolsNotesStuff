import itertools
def solution(l):

    nl = []
    snl = sorted(nl,reverse=True)
    srt = []
    for L in range(0, len(l)+1):
            for subset in itertools.permutations(l, L):
                oldstr = str(subset)
                newstr = oldstr.replace("(", "")
                subs = newstr.replace(")","")
                subs2 = subs.replace(",","")
                subs3 = subs2.replace(" ","")
                srt.append(''.join(str(subs3)))
    srt.remove("")
    srt = [ int(x) for x in srt ]
    
    prefinal = []
    for i in srt:
        if i % 3 == 0:
            prefinal.append(i)
        else :
            pass
    final = sorted(prefinal,reverse=True)
    if len(final) == 0:
        return 0 
    else:
        return final[0]
