import json

# fdict=f.read().split("\n")[0:-1]
#
# actual_list={}
# for dict in fdict:
#     key=dict.split(":")[0]
#     print(key)
#     list_val=dict.split(":")[1]
#     js=json.loads(list_val)
#     actual_list[key]=js
# print(actual_list)
import sys

from baseconvert import base

arr_of_arr=[[["AP890101-0001", 13, [2]], ["AP890101-0001", 9, [2]]],
    [["AP890101-0001", 14, [3]], ["AP890101-0003", 11, [3]], ["AP890103-0194", 10, [437]], ["AP890103-0191", 8, [437]], ["AP890103-0193", 2, [437]]],
            [["AP890104-0217", 6, [403]],["AP890104-0218", 5, [403]]]]




# obj={}
# ids= open("all_doc_ids.txt").read().split("\n")
# count=1
# for id in ids:
#     obj[id]=count
#     count+=1
# f2=open("doc_ids_to_hash.json", 'w')
# json.dump(obj,f2)





def listTOString(li):
    strf=""
    for sl in li:
        strf+=str(sl[0])+" "+str(sl[1])+" ";
        for pos in sl[2]:
            strf+=str(pos)+" "
    return strf

# print(listTOString([[2,1,[3,5]],[2,416,[437,45]],[1,697,[403]]]) )



def convert_to_tuples(line):
    arr = line.strip().split()
    list_final = []
    i = 0
    while i < len(arr):
        count = int(arr[i])
        substr = arr[i + 1:i + 2 + count]
        i += count + 2
        list_final.append((count," ".join(substr)))
    return list_final



#
# s=base(8650,10,32,string=True)
# print(s)
#
# i=base(s,64,10,string=True)
# print(i)
#
# f=open("file_name_docs.json",'r')
# js=json.load(f)
# new_js={}
# count=1
# for k,v in js.items():
#     new_js[count]=k
#     count+=1
# f.close()
#
# f=open("batch_Ends_With.json", 'w')
# json.dump(new_js,f)

def toHex(i):
    return (i)[2:]




# convert_to_tuples("2 1 12 831 2 419 244 252 2 688 34 191 1 136 426 1 140 132 1 155 545 1 175 504 1 250 17 1 425 442 1 463 53 1 477 71 1 675 175 1 856 247 1 893 325 1 980 542 1 1013 181")