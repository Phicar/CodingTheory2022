import heapq # una cola de prioridad
import math
frec = []
pq = []
arb = []
cod = {}
alph = "abcdefghijklmnopqrstuvwxyz "
def dfs(ind,camino):
	global arb,cod
	act = arb[ind]
	if len(act)==1: #ESTOY en una hoja
		#print(act,camino)
		cod[act[0]]=camino
		return
	dfs(act[0],camino+"0")
	dfs(act[1],camino+"1")
	
def Huffman(x):
	global frec,alph,pq,arb,cod #me deja modificar frec
	n = len(x)
	frec = [0 for i in range(len(alph))]
	for i in range(n):
		frec[alph.index(x[i])]+=1
	ent = 0.0
	for i in range(len(frec)):
		if frec[i]==0:
			continue
		ent-=(frec[i]/len(x)*math.log2(frec[i]/len(x)))
		heapq.heappush(pq,(frec[i],len(arb)))
		arb.append([alph[i]])
	print(pq)
	
	while len(pq)>1:
		mi = heapq.heappop(pq)
		mi2 = heapq.heappop(pq)
		heapq.heappush(pq,(mi[0]+mi2[0],len(arb)))
		arb.append([mi[1],mi2[1]])
	print(arb)
	dfs(len(arb)-1,"")
	print(cod)
	xx = ""
	for i in range(len(x)):
		xx+=cod[x[i]]
	print(xx,len(xx),ent*len(x))
	print(len(x)*8)
Huffman("esto es un codigo de huffman y ya me canse")
