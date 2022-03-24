num = int(input(''))
if num > 0 and num < 10:
    print('satuan')
elif num >= 10 and num < 100:
    print('puluhan')
elif num >= 100 and num < 1000:
    print('ratusan')
elif num >= 1000 and num < 10000:
    print('ribuan')
elif num >= 10000 and num < 100000:
    print('puluhribuan')
