def change_alpha(img,alpha=255):
    width,height=img.get_size()
    for x in range(0,width):
        for y in range(0,height):
            r,g,b,old_alpha=img.get_at((x,y))
            if old_alpha>0: img.set_at((x,y),(r,g,b,alpha))