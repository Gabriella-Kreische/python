phrase = 'Course in Video Python'

print(phrase[8])
print(phrase[10:13])
print(phrase[10:23:2])
print(phrase[:5])
print(phrase[16:])
print(phrase[10::3])

print(len(phrase))
print(phrase.count('o'))
print(phrase.count('o', 0, 14)) #count in an interval
print(phrase.find('deo')) #indicate where it starts
print(phrase.find('Android')) #returns -1 because it doesnt exist
print('Course' in phrase)
phrase = phrase.replace('Python', 'Android')
print(phrase)
phrase = phrase.replace('Android', 'Python')
print(phrase)
print(phrase.upper())
print(phrase.lower())
print(phrase.title())
print(phrase.capitalize()) #only first letter uppercase
name = '  Gabi  '
print(name.strip())
print(name.rstrip())
print(name.lstrip())
print(' '.join(phrase))
print(phrase.split())


print("""ijbfiuwefjslefne
eiufbhwiauebfiau
sdeiufbewiufhiuw""")

print(phrase.upper().count('O'))