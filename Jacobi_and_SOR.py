
def diag(A):
	n=len(A)
	return [[0]*i+ [A[i][i]]+[0]*(n-1-i) for i in range(n)]
def tril(A):
	n=len(A)
	return [A[i][0:i]+[0]*(n-i) for i in range(n)]
def triu(A):
	n=len(A)
	return [[0]*(1+i)+A[i][i+1:] for i in range(n)]
def inversion(A):
	n=len(A)
	return [[0]*i +[1.0/A[i][i]]+[0]*(n-1-i) for i in range(n)]
def add(A,B):
	n=len(A)
	m=len(A[0])
	return [[A[i][j]+B[i][j] for j in range(m)] for i in range(n)]
def mul(A,B):
	n=len(A)
	m=len(B[0])
	k=len(A[0])
	C=[]
	for i in range(n):
		cl=[]
		for j in range(m):
			num=0
			for l in range(k):
				num+=A[i][l]*B[l][j]
			cl.append(num)
		C.append(cl)
	return C
		
def mulnum(A,n):
	return [[n*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def abs_minus(A,B):
	return [[abs(A[i][j]- B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]

def cross_det(A):
	a=1
	for i in range(len(A)):
		a*A[i][i]
	return a

def submatrix(A,i0,j0):
	return [[A[i][j] for j in range(len(A[0])) if j!=j0] for i in range(len(A)) if i!=i0]

def transposition(A):
	n=len(A)
	m=len(A[0])
	return [[A[j][i] for j in range(n)] for i in range(m)]

def inversion1(A):
	return mulnum(transposition([[((-1)**(i+j))*cross_det(submatrix(A,i,j)) for j in range(len(A[0]))] for i in range(len(A))]),1.0/cross_det(A))


def precision(A,n):
	return [[ round(A[i][j],n) for j in range(len(A[0]))] for i in range(len(A))]

def Jacobi():
	A = [[1.0/(i+j-1) for i in range(1,11)] for j in range(1,11)]
	b = [[1.0/i] for i in range(1,11)]
#	A=[[9,-1,-1],[-1,12,-1],[-1,-1,15]]
#	b=[[21],[30],[39]]
	D=diag(A)
	Al=tril(A)
	Ar=triu(A)
	Di=inversion(D)
	x=[[0]]*10
	BJ=mulnum(mul(Di,add(Al,Ar)),-1)
	f=mul(Di,b)
	e=10**(-4)
	relerr=10*e+1
	n=0
	while relerr>e and n<100:
		x1=add(mul(BJ,x),f)
		n+=1
		relerr=max(abs_minus(x1,x),key=lambda x:x[0])[0]
		x=x1
#		print(x)
	return [precision(x,6),precision(abs_minus(mul(A,x),b),6),n]




def SOR():
	A = [[1.0/(i+j-1) for i in range(1,11)] for j in range(1,11)]
	b = [[1.0/i] for i in range(1,11)]
#	A=[[9,-1,-1],[-1,12,-1],[-1,-1,15]]
#	b=[[21],[30],[39]]
	D=diag(A)
	Al=tril(A)
	Ar=triu(A)
	Di=inversion(D)
	x=[[0]]*10
	w=0.965758
	e=10**(-4)
	relerr=e*10+1
	B=mul(inversion1(add(D,mulnum(Al,w))),add(mulnum(D,1-w),mulnum(Ar,-w)))
	f=mulnum(mul(inversion1(add(D,mulnum(Al,w))),b),w)
	n=0
	while relerr>e and n<100:
		x1=add(mul(B,x),f)
		n+=1
		relerr=max(abs_minus(x1,x),key=lambda x:x[0])[0]
		x=x1
#		print(x)
	return [precision(x,6),precision(abs_minus(mul(A,x),b),6),n]

	
re=Jacobi()
print()
print("Jacobi:")
if(re[2]>=100):
	print("Error,No result!")
else:
	print("Result:",re[0])
	print("Deviation: ",re[1])
	print("number: ",re[2])

re=SOR()
print()
print("SOR:")
if(re[2]>=100):
	print("Error,No result!")
else:
	print("Result:",re[0])
	print("Deviation: ",re[1])
	print("number: ",re[2])

