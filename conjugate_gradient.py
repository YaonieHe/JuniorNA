import math


VALUEN=20
VALUEH=1.0/VALUEN

def print2(A):
	for i in A:
		print(i)
	print(" ")

def F(x,y):
	return math.sin(x*VALUEH*y*VALUEH)
def G(x,y):
	return x*x*VALUEH*VALUEH+y*y*VALUEH*VALUEH

def get_A():
	S=[[1+(VALUEH**2)/4.0,-1.0/4]+[0]*(VALUEN-3)]+\
	[[0]*i+[-1.0/4,1+(VALUEH**2)/4.0,-1.0/4]+[0]*(VALUEN-4-i) \
	for i in range(VALUEN-3)]+\
	[[0]*(VALUEN-3)+[-1.0/4,1+(VALUEH**2)/4.0]]
	B=[[0]*i +[-1.0/4]+[0]*(VALUEN-2-i) for i in range(VALUEN-1)]
	A=[S[i]+B[i] +[0]*((VALUEN-1)*(VALUEN-3)) for i in range(VALUEN-1) ]
	for i in range(0,VALUEN-3):
		A+=[[0]*(i*(VALUEN-1))+B[j]+S[j]+B[j]+ \
		[0]*((VALUEN-1)*(VALUEN-4-i)) for j in range(VALUEN-1) ]
	A+=[[0]*((VALUEN-1)*(VALUEN-3))+B[i]+S[i] for i in range(VALUEN-1)]
	return A

def get_b():
	b=[]
	for i in range(1,VALUEN):
		for j in range(1,VALUEN):
			num=(VALUEH**2)*F(i,j)/4.0
			if i==1:
				num+=G(0,j)/4.0
			if j==1:
				num+=G(i,0)/4.0
			if i==VALUEN-1:
				num+=G(VALUEN,j)/4.0
			if j==VALUEN-1:
				num+=G(i,VALUEN)/4.0
			b.append([num])
	return b



def transvection2(A,B):
	n=0
	for i in range(len(A)):
		for j in range(len(A[0])):
			n+=A[i][j]*B[i][j]
	return n

def add2(A,B):
	return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mul2_0(A,a):
	return [[A[i][j]*a for j in range(len(A[0]))] for i in range(len(A))]

def mul2(A,B):
	C=[]
	n=len(A)
	m=len(B[0])
	k=len(B)
	for i in range(n):
		cl=[]
		for j in range(m):
			D=0
			for l in range(k):
				D+=A[i][l]*B[l][j]
			cl.append(D)
		C.append(cl)
	return C


def con_gra():
	global n
	A=get_A()
	b=get_b()
	x=[[0]]*((VALUEN-1)**2)
	r=add2(b,mul2_0(mul2(A,x),-1))
	v=r
	for i in range(VALUEN-1):
		if max(r,key=lambda x:abs(x[0]))==0:
			break
		t=transvection2(r,r)/transvection2(v,mul2(A,v))
		x=add2(x,mul2_0(v,t))
		r1=add2(r,mul2_0(mul2(A,v),-t))
		a = transvection2(r1,r1)/transvection2(r,r)
		v=add2(r1,mul2_0(v,a))
		r=r1
	return x

re=con_gra()

reall=[[G(0,i) for i in range(VALUEN+1)]]
for i in range(VALUEN-1):
	a=[G(i+1,0)]
	for j in range(i*VALUEN-i,(i+1)*(VALUEN-1)):
		a+=re[j]
	a+=[G(i+1,VALUEN)]
	reall.append(a)
reall+=[[G(VALUEN,i) for i in range(VALUEN+1)]]


for i in reall:
	print([round(s,5) for s in i])
