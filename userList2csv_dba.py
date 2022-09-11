import pandas as pd

filename = "/etc/passwd"
df = pd.read_csv('group.csv', sep=';')

with open(filename, "r") as f:
    for line in f:
        usrname = line.split(":")[0]
        userid = line.split(":")[2]
        group = line.split(":")[3]
        group_id = line.split(":")[2]
        membre_list = line.split(":")[3]

        n = pd.DataFrame([[
            group
            , group_id
            , membre_list]]
            , columns=['group', 'group_id', 'membre_list'])
        df = df.append(n)
        df.to_csv('group.csv', sep=';', index=False)
