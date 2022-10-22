for code in range (3):
    code=input('Enter the PIN code: ')
    if code!= '0805':
        print ('Incorect...')
    else:
        print('Correct')
        break
if code!= '0805':
    print('Sorry, your payment card has been blocked.')