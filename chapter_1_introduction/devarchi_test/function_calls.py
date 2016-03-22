fruit = ['orange', 'apple', 'orange', 'grape', 'kiwi', 'apple']  # init the array


# reports the frequency of every item in a list
def analize_list(list):
    counts = {}
    for item in list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


# let's analyze a list
counts = analize_list(fruit)
print(counts)
