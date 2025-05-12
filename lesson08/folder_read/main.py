import sys
import os
import datetime

#print(sys.argv[1])
if len(sys.argv) > 1:
    DIR_NAME = sys.argv[1] + '\\'
else:
    DIR_NAME = '.\\'
#print(DIR_NAME)

files = os.listdir(DIR_NAME)
cnt = len(files)
print(f'\n\tСодержимое папки: {DIR_NAME[0:-1]}', end='\n\n')
table_header = '{:20} {:7} {}'
print(table_header.format('Создан', 'Тип', 'Имя'))

for file in files:
    ful_name = DIR_NAME + file
    # print(ful_name)
    data_info = int(os.stat(ful_name).st_ctime)
    file_create_time = str(datetime.datetime.fromtimestamp(data_info))
    #print(file_create_time)
    #print(data_info)

    if os.path.isdir(ful_name):
        print(table_header.format(file_create_time, 'Каталог', file), )
        #print(f'Каталог: {file}')
    elif os.path.isfile(ful_name):
        print(table_header.format(file_create_time, 'Файл', file), )

        #print(file_create_time)
        #print(f'Файл: {file}')

print('-' * 30)
print(f'количество файлов: {cnt}')
