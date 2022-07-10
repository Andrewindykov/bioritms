def tagz(s,tag='h1',up=True):
    if up:
        return f'<{tag.upper()}>{s}</{tag.upper()}>'
    else:
        return f'<{tag.lower()}>{s}</{tag.lower()}>'

s_in=input()

print(tagz(s_in,tag='div'))
print(tagz(s_in,tag='div',up=False))