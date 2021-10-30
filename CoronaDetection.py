t=int(input())
for i in range(t):
    ans=[]
    plistm=[]
    st=input().split()
    ind=[]
    for i in range(0,len(st[0])-len(st[1])+1):
        pword=''
        pword+=st[0][i:i+len(st[1])]
        plistm.append(pword)
        if st[1] == pword:
            ans.append(i)
        count=0
        for j in range(len(pword)):
            if pword[j]==st[1][j]:
                count+=1
                if count==len(pword)-1:
                    ans.append(i)
                    break
    
    anss=list(set(ans))
    anss.sort()
    if anss==[]:
        print("No Match!")
    else:
        for j in anss:
            print(j,end=' ')
        print()


