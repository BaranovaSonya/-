a = 'm i'
mat = ['m',' ','i']
mat[0] = ['*         *','* *   * *','*   *    *','*         *','*         *']
mat[1] = [' ',' ',' ',' ',' ']
mat[2] = ['*','  ','*','*','*','*']
alf = ['m',' ', 'i']
ch = [alf.index(z) for z in a]
for i in range(len(mat[0])):
    for y in range(len(ch)):
        print(mat[ch[y]][i],end = ' ')
    print()
    

