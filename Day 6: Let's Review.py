# Enter your code here. Read input from STDIN. Print output to 
# Function to separate even and odd indexed characters
def seperate_char(s):
    first_section = s[::2]
    second_section = s[1::2]
    return first_section, second_section
    
T = int(input())

for _ in range(T):
    s = input()
    even_char, odd_char = seperate_char(s)
    print(f'{even_char} {odd_char}')
