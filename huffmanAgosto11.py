import heapq # una cola de prioridad
import math # para el logaritmo
frec = [] #aca guardo cuantas veces aparece cada letra
pq = [] # esta es mi cola de prioridad
arb = [] # esta es mi lista de adyacencia del arbol(codigo)
cod = {} # este es un mapa que mapea simbolo a codigo
alph = "abcdefghijklmnopqrstuvwxyz " # mi alfabeto
def dfs(ind,camino): #funcion DFS (Depth first search) busca recursivamente las hojas del arbol
	global arb,cod
	act = arb[ind]
	if len(act)==1: #ESTOY en una hoja
		#print(act,camino)
		cod[act[0]]=camino
		return
	dfs(act[0],camino+"0") # caso recursivo
	dfs(act[1],camino+"1")
	
def Huffman(x):
	global frec,alph,pq,arb,cod #me deja modificar frec
	n = len(x)
	frec = [0 for i in range(len(alph))]
	#aca estamos viendo las frecuencias
	for i in range(n):
		frec[alph.index(x[i])]+=1
	ent = 0.0 #esta variable es la entropia de la distribucion de los simbolos
	for i in range(len(frec)):
		if frec[i]==0:
			continue
		#calculamos la entropia y metemos en la cola de prioridad a todos los simbolos
		ent-=(frec[i]/len(x)*math.log2(frec[i]/len(x)))
		heapq.heappush(pq,(frec[i],len(arb)))
		arb.append([alph[i]])
	print(pq)
	
	while len(pq)>1: #mientras haya al menos dos elementos en la cola de prioridad
		mi = heapq.heappop(pq) #sacamos al mas pequegno
		mi2 = heapq.heappop(pq) #y al segundo mas pequegno
		heapq.heappush(pq,(mi[0]+mi2[0],len(arb))) #y los unimos en un simbolo que tiene la suma de las frecuencias
		arb.append([mi[1],mi2[1]])
	print(arb)
	dfs(len(arb)-1,"")
	print(cod)
	xx = ""
	#aca codificamos x.
	for i in range(len(x)):
		xx+=cod[x[i]]
	print(xx,len(xx),ent*len(x))
	print(len(x)*8)
Huffman("esto es un codigo de huffman y ya me canse")
