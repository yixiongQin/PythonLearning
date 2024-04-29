weight = int(input('Weight: '))
unit = input('(L)bs or (K)g:')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'Your are {converted:.2f} kilos')
else:
    converted = weight / 0.45
    print(f'Your are {converted:.2f} pounds')

    # output:
    # Weight: 72
    # (L)bs or (K)g:k
    # Your are 160.00 pounds