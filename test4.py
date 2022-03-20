import sys

def write(file,d):
    with open(file,"w",encoding="gbk") as fw:
        i=0
        for k ,v in d.items():
            if i == 1:
                print()
                fw.write("\n")
                fw.write(k)
                fw.write("\n")
            else:
                fw.write(k)
                fw.write("\n")
            for j in v:
                print("{:} {:}".format(j[0],j[1]))
                fw.write("{:} {:}".format(j[0],j[1]))
                fw.write("\n")
                i=1
def qiuhepaixu(file, file1, s=''):
    with open(file, "r", encoding="gbk") as f:
        ls = f.readlines()
        ls = [i.rstrip().split() for i in ls]
        d = {}
        for i in ls:
            n = i[0]
            li1 = []
            num = 0
            for j in ls:
                if n in j:
                    num += int(j[-1])
                    li1.append(j[1:])

        li1 = sorted(li1, key=lambda x: (int(x[1]), x[0]), reverse=True)
        li1.insert(0, [n, num])
        d[n] = li1
d = dict(sorted(list(d.items()), key=lambda x: (x[1][0][1], x[0]), reverse=True))
if not s:
    write(file1, d)
else:
    ls = {}
    ls[s] =d[s]
    write(file1, ls)
if len(sys.argv) == 1:
    qiuhepaixu("yq_in_04.txt", "yq_out_04.txt")
elif len(sys.argv) == 3:
    qiuhepaixu(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 4:
    qiuhepaixu(sys.argv[1], sys.argv[2], sys.argv[3])
