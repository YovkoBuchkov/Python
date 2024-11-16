num = int(input())

body = f"*{(num - 2) * ' '}*"
print(num * "*")
for _ in range(num - 2):
    print(body)
print(num * "*")
