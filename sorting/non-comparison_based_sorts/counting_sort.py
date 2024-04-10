def counting_sort(lst):
    K = max(lst)
    counts = [0] * (K + 1)
    for el in lst:
        counts[el] += 1
    
    starting_index = 0
    for i, count in enumerate(counts):
        counts[i] = starting_index
        starting_index += count
    
    sorted_lst = [0] * len(lst)

    for el in lst:
        sorted_lst[counts[el]] = el
        counts[el] += 1
    
    print(sorted_lst)

lst = [5,5,5,4,3,2,1,0,0,0]
counting_sort(lst)