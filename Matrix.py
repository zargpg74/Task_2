def Matrix(n):
    dx, dy = 1, 0
    x, y = 0, 0
    arr = [[None] * n for _ in range(n)]
    for i in range(1, n**2+1):
        arr[x][y] = i
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x+dx, y+dy
    for x in list(zip(*arr)):
        print(*x)

try:
    k = int(input("Введите число: "))
except ValueError:
    print("Введено не целое число")
    exit(1)

if k < 4 or k > 1000:
    print("Число не подходит указанному диапазону")
    exit(1)
Matrix(k)






