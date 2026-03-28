file1="genia/genia_train_dev.json"
file2= "genia/genia_train_dev_context.json"
f1= open(file1)
f2= open(file2)
r1=f1.read()
r2= f2.read()
i=0
j=0
print(r1[400:420])
print(r2[400:420])
# for u,v in zip(r1,r2):
#     if u!=v:
#         i+=1
#     else :
#         j+=1
#     if i > 0:
#         print(u,v)
#         break
print(j)