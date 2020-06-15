import random
import matplotlib
import matplotlib.pyplot as plt

n,m=map(int,input().split())

g=[[] for i in range(0,n+1)]
w=[0 for i in range(0,n+1)]
posx=[0 for i in range(0,n+1)]
posy=[0 for i in range(0,n+1)]
vis=[0 for i in range(0,n+1)]
pre=[0 for i in range(0,n+1)]
q=[0 for i in range(0,n+1)]
dep=[0 for i in range(0,n+1)]
fig=plt.figure()

for i in range(0,m):
	x,y=map(int,input().split())
	assert(x!=y)
	#x,y=0,0
	#while x==y:
		#x,y=random.randint(1,n),random.randint(1,n)
	g[x].append(y)
	g[y].append(x)

for i in range(1,n+1):
	g[i]=set(g[i])

def rand_color():
	#return '#'+''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],6))
	return ''.join(random.sample(['red','black','blue','yellow','purple','cyan'],1))

def draw_path(x,y,z):
	path=matplotlib.path.Path([x,y,z],[1,3,3])
	patch=matplotlib.patches.PathPatch(path,fc="None",ec=rand_color())
	fig.add_subplot(111).add_patch(patch)

def bfs(start):
	he,ta=0,1
	q[1]=start
	vis[start]=1
	while he!=ta:
		he+=1
		k1=q[he]
		for j in g[k1]:
			if vis[j]==0:
				vis[j]=1
				pre[j]=k1
				ta+=1
				q[ta]=j
	#print("q:"+str(q))

def dfs(k1,k2):
	isleaf=1
	dep[k1]=dep[k2]+1
	for j in g[k1]:
		if pre[j]==k1:
			isleaf=0
			posy[j]=posy[k1]-100
			dfs(j,k1)
			w[k1]+=w[j]
	if isleaf:
		w[k1]=50

def dfs2(k1,k2):
	if k1:
		plt.text(posx[k1],posy[k1],str(k1))
	lst=posx[k1]-w[k1]/2;
	for j in g[k1]:
		if pre[j]==k1:
			posx[j]=lst+w[j]/2
			dfs2(j,k1)
			#print([[posx[k1],posx[j]],[posy[k1],posy[j]]])
			if k1:
				plt.plot([posx[k1],posx[j]],[posy[k1],posy[j]])
			lst=lst+w[j]

def dfs3(k1,k2):
	for j in g[k1]:
		#print("dfs3:"+str([k1,j]))
		if pre[j]==k1:
			dfs3(j,k1)
		elif dep[j]!=dep[k1]:
			if j==k2:
				pass
			else:
				#print("qwq"+str([k1,j]))
				plt.plot([posx[k1],posx[j]],[posy[k1],posy[j]])
		else:
			#print("qaq:"+str([k1,j]))
			draw_path([posx[k1],posy[k1]],[(posx[k1]+posx[j])/2,posy[k1]-50],[posx[j],posy[j]])

for i in range(1,n+1):
	if not vis[i]:
		g[0].append(i)
		bfs(i)
dfs(0,0)
dfs2(0,0)
#print("dep:"+str(dep))
dfs3(0,0)
#draw_path([0,0],[50,50],[100,0])
#draw_path([0,0],[25,50],[50,0])
#draw_path([50,0],[75,50],[100,0])
#plt.plot(posx,posy,'r.')
plt.show()
