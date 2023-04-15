set_1 = {1, 2, 3}
set_2 = {2, 5, 7}
set_3 = {4, 5, 6, 8}

# 1. avelacnel tarre
set_1.add(4)
print(set_1)

# 2. hanel 2 set iraric
new_set = set_1.difference(set_2)
print(set_1)


# 3. hanum e trvac set ic myusi tarrery
set_1.difference_update(set_2)
print(set_1)

# 4. erku seteri bolor tarrery aranc krknvoxneri
new_set_1 = set_1.symmetric_difference(set_2)
print(new_set_1)

# 5. jnjum e erku seteri mej nuyn tarerry
set_1.symmetric_difference_update(set_2)
print(set_1)

# 6. erku seteri hatumn e
new_set_2 = set_1.intersection(set_2)
print(new_set_2)

# 7. jnjum e erkrord seti het voch yndhanur tarrery
set_1.intersection_update(set_2)
print(set_1)

#  8. seteri miavorumy 
new_set_3 = set_1.union(set_2)
print(new_set_3)

#  9. 1i mej avelacnum e bolor ayn tarery voronq chkain
set_1.update(set_2)
print(set_1)

# 10. setic hanum e yntrvac tarry (ete chka apa error chi talis)
set_1.discard(5)
print(set_1)

# 11. setic hanum e yntrvac tarry (ete chka apa error e talis)
set_1.remove(7)
print(set_1)

# 12. hanum e arajin elementy
set_2.pop()
print(set_2)

# 13. nor set e talis nuyn naxordov
new_set_4 = set_2.copy()
print(new_set_4)

# 14. jnjum e bolor tarrery
set_2.clear()
print(set_2)

# 15. veradardznum e true kam flase ete arajin seti tarry erkrodic che kam erkrordic e
new_set_5 = set_3.isdisjoint(set_1)
print(new_set_5)

# 16. veradardznum e true kam flase ete arajin seti tarrery amboxjutyamb patkanum en erkrodin kam chen patkanum
new_set_6 = set_3.issubset(set_1)
print(new_set_6)

# 17. veradardznum e true kam flase ete erkrord seti tarrery amboxjutyamb patkanum en arajinin kam chen patkanum
new_set_7 = set_3.issuperset(set_1)


# tuple nuyn listn e bayc tuple i arjeqnery anpopox en

tuple_ = (1, 2, "a", 4, "b", "a", [1, 2])

# 18. hashvum ev talis e trvac tarri qanaky
count_ = tuple_.count("a")
print(count_)

# 19. talis e trvac tarri indexy (ete krknvox e talis e araji handipaci indexy)
index_ = tuple_.index("a")
print(index_)
