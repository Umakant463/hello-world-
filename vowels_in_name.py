# Check if the name character has vowels in it.

vowels = 'aeiOu'
name = 'naveen'

for i in name.lower():
    for k in vowels.lower():
        if i==k : print(f'we have vowels {i}  at index ', name.index(i))
