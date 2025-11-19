strs = ["flower","flow","flight"]
prefix = ""
for j in range(len(strs[0])):
    char = strs[0][j]
    for i in range(1, len(strs)):
        if j >= len(strs[i]) or strs[i][j] != char:
            print(prefix)
            continue
    prefix += char
