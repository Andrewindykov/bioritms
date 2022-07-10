def get_data_fig(*args,**kwargs):
    # per=0
    # for x in args:
    #     per+=x
    # #print(per)
    # se=("type", "color", "closed", "width")
    # res=[per]
    # for k in se:
    #     if k in kwargs:
    #         res.append(kwargs[k])
    # res2=tuple(res)
    # return res2
    
    kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs]
    return (sum(args), *kwargs)


print (get_data_fig(3, 4, 5, type=True, color=256, closed=False, width=5))
