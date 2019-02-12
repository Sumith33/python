def duplicate_count(s):
    return len([x for x in set(s) if s.count(x) > 1])
s = "sasasppoo"
print(duplicate_count(s))
