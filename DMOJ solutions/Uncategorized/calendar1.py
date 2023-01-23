import sys
input = sys.stdin.readline
a = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', "癸"]
b = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申','酉', '戌', '亥']
for _ in range(int(input())):
    y = int(input())
    y -= 1984
    print(a[y%10]+b[y%12])