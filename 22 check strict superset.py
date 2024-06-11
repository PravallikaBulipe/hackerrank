a = set(map(int, input().split()))
c=0
for i in range(int(input())):
    st = set(map(int, input().split()))
    
    if len(st.difference(a))==0 and (len(a)-len(st))>=1:
        output ='True'
    else:
        c+=1

if c==0:
    print(output)
else:
    print('False')
