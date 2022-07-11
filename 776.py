def get_line_list(d,a=[]):
    for i in d:
        if type(i)==list:
            print('list',i)
            get_line_list(i, a)
        else:
            print(777, i,a)
            a.append(i)
            print(888, i,a)
    return a
x=[]
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
get_line_list(d,x)
print(x)