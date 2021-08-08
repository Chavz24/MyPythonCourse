#make a loop that prints the mext lis like this
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

grid= [['.', '.', '.', '.', '.', '.','','.'],
       ['.', 'O', 'O', '.', '.', '.','.','0'],
       ['O', 'O', 'O', 'O', '.', '.','.'],
       ['O', 'O', 'O', 'O', 'O', '.','.'],
       ['.', 'O', 'O', 'O', 'O', 'O','.'],
       ['O', 'O', 'O', 'O', 'O', '.','.'],
       ['O', 'O', 'O', 'O', '.', '.','.'],
       ['.', 'O', 'O', '.', '.', '.','.'],
       ['.', '.', '.', '.', '.', '.','.'],
       ['.', '.', '.', '.', '.', '.','.'],
       ['.', '.', '.', '.', '.', '.','.']]



d=0
while d<len(grid[d]):
    print(len(grid[d]))
    for i in range(len(grid)):
        if d>len(grid[i]):
            d=len(grid)-1
        print(grid[i][d], end='')

    d+=1
    print('')