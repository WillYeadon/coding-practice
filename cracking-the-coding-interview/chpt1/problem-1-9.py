def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s3 = s1 + s1
    if s2 in s3:
        return True
    else:
        return False
    
strings = [("waterbottle", "terbottlewa"), ("waterbottle", "aterbotttew"),
           ("waterbottle", "rbottlewete"), ("waterbottle", "ottlewaterb")] 

for i in strings:
    print(stringRotation(i[0], i[1]))    