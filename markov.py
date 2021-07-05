import random
import jieba
articlelength=1000
txt=[]
with open("in.txt","r",encoding="utf8") as fp:
    txt=fp.read()
words=jieba.lcut(txt)
M={}
for i in range(2, len(words)):
    s1 = words[i-2] + '`' + words[i-1]
    s2 = words[i]
    if s1 not in M:
        M[s1] = {}
        M[s1]['`'] = 0
    if s2 not in M[s1]:
        M[s1][s2] = 0
    M[s1]['`'] += 1
    M[s1][s2] += 1

a = random.randint(1, len(words)-1)
state = words[a-1] + '`' + words[a]
with open("out.txt", "w", encoding="utf8") as fpw:
    fpw.write(words[a-1] + words[a])
    for i in range(0, articlelength):
        pos = random.randint(1, M[state]['`'])
        cnt = 0
        for nextword in M[state]:
            if nextword != '`':
                cnt+=M[state][nextword]
                if(cnt >= pos):
                    fpw.write(nextword)
                    state = state.split('`')[1] + '`' + nextword
                    break
        





    

