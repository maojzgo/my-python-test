import json
obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=True)
s2 = json.dumps(obj, ensure_ascii=False)
print(s1)
print(s2)