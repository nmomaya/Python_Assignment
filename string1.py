def MixUp(a,b):
	return b[:3]+a[3:]+" "+a[:3]+b[3:]

print( MixUp("mid","pox"))
