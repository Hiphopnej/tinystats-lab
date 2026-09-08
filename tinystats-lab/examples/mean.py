from tinystats import mean

# Ett exempel på när man försöker ta medelvärdet av en tom lista vilket ger ett fel
try:
    print(mean([]))
except ValueError as e:
    print(e)

# Ett exempel på när man försöker skrive ut en siffra bokstavligt vilket ger ett fel
try:
    mean([1,2,"three"])
except ValueError as e:
    print(e)

# Ett exempel på när man försöker skriva två olika listor vilket ger ett fel
try:
    print(mean([1,2,3],[2,3,4]))
except TypeError as e:
    print(e)