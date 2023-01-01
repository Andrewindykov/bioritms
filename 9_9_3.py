def is_string(lst):
    return all(isinstance(i, str) for i in lst)

print(is_string(('1','2','3','sdf')))