import os
while True:
    N=int(input("Enter how many row coloum want:--"))
    print("""==============================================
==================================================
=================================================""")

    a=[]
    for i in range(N):
      l=[]
      for j in range(N):
        l.append(0)
      a.append(l)

    k=1
    i=0
    j=N//2

    while(k<=N*N):
      a[i][j]=k
      k=k+1
      ni=(i-1)%N
      nj=(j+1)%N
      if(a[ni][nj]!=0):
        i=(i+2)%N
        j=(j-1)%N
      else:
        i=ni
        j=nj
    for k in a:
        print(k)
    print("""
    
    """)
    a= input("press END for ending and CONTINUE for contine:---")
    os.system("cls")
    if a=="end" or a=="END":
        

        break
    else:
        continue

