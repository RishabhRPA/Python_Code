s1={1,2,3,4}
s2={4,5,6,7}
print(s1|s2) #Union
print(s1&s2) #intersaction
print(s1-s2) #differnce
print(s1^s2) # Symmetric difference
fs=([1,2,3,4])
print(fs)
fs1=0

for item in fs:
    fs1=fs1+item

print(fs1)
fs.append(9)
print(fs)
froze_set=frozenset[("Rishabh","Mango")]
print(froze_set)