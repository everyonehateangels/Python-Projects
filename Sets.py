# Sets doesn't have an Index.(unlike arrays), they are unique elements so it won't have the same elements. (you can't
# change the value). You can't put an array inside of a set (same for dictionaries). But you can use Tuples instead!


# You can use it this way
mi_set = set([1,2,3,4,5])
print(type(mi_set))

print(mi_set)


# Or this way

# mi_segundo_set = {1,2,3,4,5}
# print(type(mi_segundo_set))

# print(mi_segundo_set)
# ----------------------------------------------------------------------------------------------------------------------
# Python automatically removes the repeated value.

# Combine Sets

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

# How to add an element to a Set.

s1.add(4)

# How to remove an element to a Set.
s1.remove(6)

# How to clean a Set
s1.clear()