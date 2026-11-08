from string_class import MyString

def run():
    s = MyString('')
    s1 = MyString('abcd')
    print(s1)

    sr = MyString(initialize_with_random=True)
    print(sr)
    print(sr[2])

    sr[2] = 'x'
    print(sr)

    s2 = MyString('abcabcabc')
    s2.replace('ab', 'xy', 3)
    print(s2)

    sr.insert(1, 'z')
    sr.insert(8, 'y')
    print(sr)

    sr.remove_character('x')
    print(sr)

    s3 = MyString('hello')
    s4 = s3 + sr
    print(s4)

    s5 = sr * 2
    print(s5)

    s6 = MyString('abcabcbabc')
    print(f"{s6.return_index('ca')}")

    sr = MyString('abxyd')
    sr.rotate(2)
    print(sr)

run()