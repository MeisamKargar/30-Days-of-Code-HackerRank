# Enter your code here. Read input from STDIN. Print output to STDOUT
user = int(input())
dicts = {}

for _ in range(user):
    name, phone = input().split()
    dicts[name] = phone
    
while True:
    try:
        query = input()
        
        if query in dicts:
            print(f'{query}={dicts[query]}')
        else:
            print("Not found")
    except EOFError:
        break
    
