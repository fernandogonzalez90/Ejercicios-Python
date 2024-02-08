def anagrama(pal1, pal2):
   print('Anagrama') if ''.join(sorted(pal1)) == ''.join(sorted(pal2)) else print('No Anagrama')

anagrama('amor', 'roma')
