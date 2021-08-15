"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""

path_win_list=[r'']
path_unix_list=[]

for path in path_win_list:
    dir_list=path.split('\\')
    unix_path='/'.join(dir_list)
    path_unix_list.append(unix_path)

for path in path_unix_list:
    print(path)