# val = [1, 5, 22.2, 'ttit', {}, []]
val = ['a', 'b', 'c']
type_val = list(map(type, val))
for t in type_val:
    if t != str:
        print(t, ' != ', 'str!')
    else:
        print('-------------!!!', t, ' == ', 'str!!!-------------')

def test_def(a, b):
    c = a + b

print(test_def(1,2))


val_separator = ', '
val_str = val_separator.join(val)

print("(" + val_str + ")")