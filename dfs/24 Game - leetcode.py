def judgePoint24(cards):
    cardRep=[]
    for i in cards:
        cardRep.append((i,1))
    dp={}
    def operations(c1,c2,opr):
        #print(c1,c2)
        if opr=="+":
            return ((c1[0]*c2[1])+(c1[1]*c2[0]), c1[1]*c2[1])
        if opr=="-":
            return ((c1[0]*c2[1])-(c1[1]*c2[0]), c1[1]*c2[1])
        if opr=="*":
            return (c1[0]*c2[0], c1[1]*c2[1])
        if opr=="/":
            return (c1[0]*c2[1], c1[1]*c2[0])
    def dfs(card):
        if len(card)==0:
            return []
        if len(card)==1:
            return card
        possible=[]
        for i in range(1,len(card)):
            if dp.get((card[0],card[i])):
                ans=dp[(card[0],card[i])]
            elif dp.get((card[i],card[0])):
                ans=dp[(card[i],card[0])]
            else:
                ans=[]
                for opr in "+","-","*","/":
                    if opr=="-" or opr=="*":
                        ans.append(operations(card[0],card[i],opr))
                    ans.append(operations(card[i],card[0],opr))
                dp[(card[i],card[0])]=ans
            res=dfs(card[1:i]+card[i+1:])
            for j in ans:
                for k in res:
                    for p in "+","-","*","/":
                        cur=operations(j,k,p)
                        possible.append(cur)
                        if p=="-" or p=="/":
                            cur=operations(k,j,p)
                            possible.append(cur)
            res=dfs([card[i]]+card[1:i]+card[i+1:])
            for j in res:
                for p in "+","-","*","/":
                    cur=operations(j,card[0],p)
                    possible.append(cur)
                    if p=="-" or p=="/":
                        cur=operations(card[0],j,p)
                        possible.append(cur)
            return possible
        
        
    for i in range(1,4):
        if dp.get((cardRep[0],cardRep[i])):
            ans=dp[(cardRep[0],cardRep[i])]
        elif dp.get((cardRep[i],cardRep[0])):
            ans=dp[(cardRep[i],cardRep[0])]
        else:
            ans=[]
            for opr in "+","-","*","/":
                if opr=="-" or opr=="*":
                    ans.append(operations(cardRep[0],cardRep[i],opr))
                ans.append(operations(cardRep[i],cardRep[0],opr))
            dp[(cardRep[i],cardRep[0])]=ans
        res=dfs(cardRep[1:i]+cardRep[i+1:])
        for j in ans:
            for k in res:
                for p in "+","-","*","/":
                    cur=operations(j,k,p)
                    if cur[1]!=0 and cur[0]%cur[1]==0 and cur[0]//cur[1]==24:
                        return True
                    if p=="-" or p=="/":
                        cur=operations(k,j,p)
                    if cur[1]!=0 and cur[0]%cur[1]==0 and cur[0]//cur[1]==24:
                        return True
        res=dfs([cardRep[i]]+cardRep[1:i]+cardRep[i+1:])
        for j in res:
            for p in "+","-","*","/":
                cur=operations(j,cardRep[0],p)
                if cur[1]!=0 and cur[0]%cur[1]==0 and cur[0]//cur[1]==24:
                        return True
                if p=="-" or p=="/":
                    cur=operations(cardRep[0],j,p)
                    if cur[1]!=0 and cur[0]%cur[1]==0 and cur[0]//cur[1]==24:
                            return True
    return False

print(judgePoint24([1,2,1,2]))
