li=open("linkgraph.txt",'r').read().split("\n")
mll=[]
for fl in li:
    ml=fl.split(" ")[0]
    mll.append(ml)
    print(ml)

str1="\n".join(mll)
f2=open("lg_ml_test.txt",'w')
f2.write(str1)
