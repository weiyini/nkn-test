import codecs

txt = codecs.open('yq_in_03.txt', 'r')
line = txt.readline()   # 以行的形式进行读取文件
list1 = []
list2 = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
data7 = []
data8 = []
data9 = []
data10 = []
sum1 = int()
#in1 = input()

while line:
    a = line.split()
    b = a[1:3]  # 提出地区和数量的列
    c = a[2:3]
    list1.append(b)  # 将地区和数量添加在新列表中
    list2.append(c)
    line = txt.readline()
txt.close()

txt2 = open("yq_out_04.txt", "w")  #
for j in list2:
    txt2.writelines(j)
    txt2.write('\n')
txt2.close()

txt1 = open("yq_out_03.txt", "w")  # 把地区和数量暂存在yq_out.txt中
for i in list1:
    txt1.writelines(i)
    txt1.write('\n')
txt1.close()

with open("yq_out_03.txt", 'r', ) as t:
    line = t.readlines()
    for i1, rows in enumerate(line):
        if i1 in range(0, 12):
            data1.append(rows)

    for i2, rows in enumerate(line):
        if i2 in range(13, 24):
            data2.append(rows)

    for i3, rows in enumerate(line):
        if i3 in range(25, 45):
            data3.append(rows)

    for i4, rows in enumerate(line):
        if i4 in range(46, 58):
            data4.append(rows)

    for i5, rows in enumerate(line):
        if i5 in range(59, 72):
            data5.append(rows)

    for i6, rows in enumerate(line):
        if i6 in range(73, 88):
            data6.append(rows)

    for i7, rows in enumerate(line):
        if i7 in range(89, 101):
            data7.append(rows)

    for i8, rows in enumerate(line):
        if i8 in range(102, 120):
            data8.append(rows)

    for i9, rows in enumerate(line):
        if i9 in range(121, 129):
            data9.append(rows)
t.close()

'''with open("yq_out_04.txt", 'r', ) as k:
    line = k.readlines()
    for i1, rows in enumerate(line):
        if i1 in range(0, 12):
            data1.append(rows)

    for i2, rows in enumerate(line):
        if i2 in range(13, 24):
            data2.append(rows)

    for i3, rows in enumerate(line):
        if i3 in range(25, 45):
            data3.append(rows)

    for i4, rows in enumerate(line):
        if i4 in range(46, 58):
            data4.append(rows)

    for i5, rows in enumerate(line):
        if i5 in range(59, 72):
            data5.append(rows)

    for i6, rows in enumerate(line):
        if i6 in range(73, 88):
            data6.append(rows)

    for i7, rows in enumerate(line):
        if i7 in range(89, 101):
            data7.append(rows)

    for i8, rows in enumerate(line):
        if i8 in range(102, 120):
            data8.append(rows)

    for i9, rows in enumerate(line):
        if i9 in range(121, 129):
            data9.append(rows)
k.close()'''

'''with open("yq_out_04.txt", "w", ) as g:
    g.write('浙江省\n')
    for i1 in range(len(data1)):
        g.writelines(data1[i1])
    g.write('\n江西省\n')
    for i2 in range(len(data2)):
        g.writelines(data2[i2])
    g.write('\n广东省\n')
    for i3 in range(len(data3)):
        g.writelines(data3[i3])
    g.write('\n江苏省\n')
    for i4 in range(len(data4)):
        g.writelines(data4[i4])
    g.write('\n湖南省\n')
    for i5 in range(len(data5)):
        g.writelines(data5[i5])
    g.write('\n安徽省\n')
    for i6 in range(len(data6)):
        g.writelines(data6[i6])
    g.write('\n陕西省\n')
    for i7 in range(len(data7)):
        g.writelines(data7[i7])
    g.write('\n河南省\n')
    for i8 in range(len(data8)):
        g.writelines(data8[i8])
    g.write('\n贵州省\n')
    for i9 in range(len(data9)):
        g.writelines(data9[i9])
    for i10 in range(len(data10)):
        g.writelines(data10[i10])
#print('输出到yq_out_03.txt完成')
g.close()'''



# #写入
with open("yq_out_03.txt", "w", ) as f:
    f.write('浙江省\n')
    for i1 in range(len(data1)):
        f.writelines(data1[i1])
    f.write('\n江西省\n')
    for i2 in range(len(data2)):
        f.writelines(data2[i2])
    f.write('\n广东省\n')
    for i3 in range(len(data3)):
        f.writelines(data3[i3])
    f.write('\n江苏省\n')
    for i4 in range(len(data4)):
        f.writelines(data4[i4])
    f.write('\n湖南省\n')
    for i5 in range(len(data5)):
        f.writelines(data5[i5])
    f.write('\n安徽省\n')
    for i6 in range(len(data6)):
        f.writelines(data6[i6])
    f.write('\n陕西省\n')
    for i7 in range(len(data7)):
        f.writelines(data7[i7])
    f.write('\n河南省\n')
    for i8 in range(len(data8)):
        f.writelines(data8[i8])
    f.write('\n贵州省\n')
    for i9 in range(len(data9)):
        f.writelines(data9[i9])
    for i10 in range(len(data10)):
        f.writelines(data10[i10])
#print('输出到yq_out_03.txt完成')
f.close()
'''
with open("yq_out_03.txt", 'r', ) as h:
    line = h.read()
    if in1 == "yq yq_in_03.txt yq_out_03.txt 浙江省":
        print(data1)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 江西省":
        print(data2)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 广东省":
        print(data3)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 江苏省":
        print(data4)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 湖南省":
        print(data5)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 安徽省":
        print(data6)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 陕西省":
        print(data7)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 河南省":
        print(data8)
    if in1 == "yq yq_in_03.txt yq_out_03.txt 贵州省":
        print(data9)
    if in1 == "yq yq_in_03.txt yq_out_03.txt":
        print(line)
h.close()'''

with open("yq_out_04.txt", "w", ) as q:

    q.writelines()
    for j1, rows in enumerate(line):
        if j1 in range(0, 12):
            sum1.append(rows)
    sum1 = str(data1)
    print(sum1)

q.close()