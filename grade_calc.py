grade=input("What is your grade?\n")
grade2=int(grade)

if 90 <= grade2:
    print('A')
elif 80 <= grade2 and grade2 < 90:
    print('B')
elif 70 <= grade2 and grade2 < 80:
    print('C')
elif 60 <= grade2 and grade2 < 70:
    print('D')
elif 60 < grade2:
        print('F')
