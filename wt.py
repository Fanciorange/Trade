with open("/data/users/zzp/Trade/features.json",'r')as f:
    s = f.read()
import json 
mp = json.loads(s)
mp = [t[0] for t in mp]
print(mp)
with open("/data/users/zzp/Trade/features.json",'w')as f:
    f.write(json.dumps(mp))