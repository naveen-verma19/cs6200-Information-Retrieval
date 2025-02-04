import os

files=os.listdir("indexing/inverted-lists")
files=list(filter(lambda x:x.endswith("txt"),files))
print(files[0].split("."))

files=sorted(files,key=lambda x: int(x.split(".")[0]))
size_dict={}
tot=0
for file in files:
    size=os.path.getsize("indexing/inverted-lists/"+file)/1024/1024
    size_dict[file.split(".")[0]]=size
    tot+=size

print(size_dict)
print(tot/8)
siz=0
for k,v in size_dict.items():
    siz+=v
    if(siz>22.14):
        print(k,siz)
        siz = 0