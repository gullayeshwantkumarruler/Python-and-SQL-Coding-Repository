s="aaaaccddd"
d=dict()
for ch in s:
    d[ch]=d.get(ch,0)+1
# print(d)
for k,v in sorted(d.items()):



s="aaaaccddd"
z=""
for i in sorted(set(s)):
    z=z+ str(s.count(i))+i
print(z)
    
    

s="a4d3c2"
req_str=""
for i in range(len(s)):
    if s[i].isdigit():
        req_str=req_str+(s[i-1]*int(s[i]))
print("".join(sorted(req_str)))



s="fghjkjhgfghjjhcasdf12343mn----b23"
alphabets=[]
digits=[]
special=[]
for i in s:
    if i.isalpha():
        alphabets.append(i)
    elif i.isdigit():
        digits.append(i)
    else:
        special.append(i)
final_string="".join(sorted(alphabets)+sorted(digits)+special)
print(final_string)



s="abcd efgh"
l=s.split()
z=[]
print(l)
for i in l:
    z.append(i[::-1])
l1=l[::-1]
print(l1)
s1=" ".join(l1)
print(s1)
print(z)
z1=" ".join(z)
print(z1)



message="abcdefghijkabcdefjhijlmnohijkfdfff"
freq_dict=dict()
freq_dict=freq_dict.fromkeys(set(message),0)
for i in message:
    freq_dict[i]=freq_dict[i]+1
print(freq_dict)
