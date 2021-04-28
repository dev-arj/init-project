width = 13
height = 3
print('-' * width)
for i in range(height):
    print('|',  f'{i:^3d}' * 3, '|')
print('-' * width)
