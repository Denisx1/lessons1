str = '01978464739945756348372393859684629330049968570001928376453123456789'
# i = 0
# for i in str:

#     print(i)
def count_it(sequence):
    
    num_frequency = {int(item): sequence.count(item) for item in sequence}

    
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])

    return dict(sorted_num_frequency[-3:])

print(count_it(str))    