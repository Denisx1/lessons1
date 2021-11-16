dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    dict.update(**kwargs)
biggest_dict(pozhar = 32, ya = 234, lexa = 12)
print(dict)




