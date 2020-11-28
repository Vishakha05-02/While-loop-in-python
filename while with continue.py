i = 0
a = 'Vishakha'
while i < len(a):
    if a[i] == 'a' or a[i] == 'b':
        i += 1
        continue
    print('Current Letter :', a[i])
    i +=1