first = 564
second = 765
third = 46
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second != third:
    print(0)