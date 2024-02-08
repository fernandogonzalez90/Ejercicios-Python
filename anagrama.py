def anagrama(pal1, pal2):
   print('si') if ''.join(sorted(pal1)) == ''.join(sorted(pal2)) else print('no')

anagrama('amor', 'roma')
