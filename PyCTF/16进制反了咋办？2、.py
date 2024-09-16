with open('zip','rb') as f:
    with open('zip1','wb') as g:
        g.write(f.read()[::-1])