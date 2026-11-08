from string_class import MyString

sr = MyString(initialize_with_random=True)

try:
    sr[2] = 'X'
except TypeError as e:
    print(e)

try:
    sr[0] = '1'
except TypeError as e:
    print(e)

try:
    sr = sr + 'A'
except TypeError as e:
    print(e)

try:
    sr = sr * -1
except ValueError as e:
    print(e)

try:
    sr.return_index('cA')
except TypeError as e:
    print(e)