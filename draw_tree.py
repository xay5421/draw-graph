import matplotlib.pyplot as plt

#n,m=map(int,input().split())
#n=map(int,input().split())
n=int(input())
m=n-1

g=[[] for i in range(0,n+1)]
w=[0 for i in range(0,n+1)]
posx=[0 for i in range(0,n+1)]
posy=[0 for i in range(0,n+1)]

for i in range(0,m):
    x,y=map(int,input().split())
    g[x].append(y),g[y].append(x)

def dfs(k1,k2):
    isleaf=1
    for j in g[k1]:
        if j!=k2:
            isleaf=0
            posy[j]=posy[k1]-100
            dfs(j,k1)
            w[k1]+=w[j]
    if isleaf:
        w[k1]=50

def dfs2(k1,k2):
    plt.text(posx[k1],posy[k1],str(k1))
    lst=posx[k1]-w[k1]/2;
    for j in g[k1]:
        if j!=k2:
            posx[j]=lst+w[j]/2
            dfs2(j,k1)
            #print([[posx[k1],posx[j]],[posy[k1],posy[j]]])
            plt.plot([posx[k1],posx[j]],[posy[k1],posy[j]])
            lst=lst+w[j]

dfs(1,0)
dfs2(1,0)
#plt.plot(posx,posy,'r.')
plt.show()
