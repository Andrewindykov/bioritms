def get_data_fig (*args,**kwargs):
    per=0
    for x in args:
        per+=x
    print(per, kwargs)
    return per

a=get_data_fig(3, 4, 5, type=True, color=256, closed=False, width=5)
print(a)