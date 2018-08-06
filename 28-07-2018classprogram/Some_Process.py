import os
def File_to_Listwrds(fname):
    if not os.path.isfile(fname):
       return[]
       wordlst = []
    with open(fname,'r') as fob:
             wordlst = []
             for walk in fob:
                 flst = walk.strip("\n").split()
                 wordlst.extend(flst)
             return wordlst
def search_word(wlst,word):
    rlst=[]
    for walk in wlst:
        if word in walk:
            rlst.append(walk)
    return rlst

def word_count(wlst,word):
    count = 0
    for walk in wlst:
        if walk == word:
            count +=1
    return count
