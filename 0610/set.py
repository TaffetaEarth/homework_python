s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = {}
print(s1.isdisjoint(s2))
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
s3.intersection_update(s1, s2)
print(s3, s1, s2)
