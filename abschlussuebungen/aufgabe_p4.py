
def find_missing_number(numbers):
    # erwartete summe ausrechnen
    expected = 0
    for i in range(numbers[0], numbers[len(numbers)-1]+1):
        expected += i
    print("expected =", expected)

    # aktuelle summe ausrechnen
    actual = 0
    for i in range(len(numbers)):
        actual += numbers[i]
    print("actual =", actual)

    # vergleichen und ergebnis zurückgeben
    return expected - actual


###
missing = find_missing_number([1,2,3,4,6,7,8])
print("fehlende zahl:", missing)
missing = find_missing_number([10, 11, 12, 14, 15, 16, 17]) 
print("fehlende zahl:", missing)
missing = find_missing_number([22,23,25,26,27,28,29,30,31,32,33]) 
print("fehlende zahl:", missing)
