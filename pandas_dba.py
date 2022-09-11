# import pandas as pd
# data = {"Prenom": ["Sylvie", "Gilles", "Sylvain", "Thomas"], "Age": [18.0, 23.0, 25.0, 40.0]}
# df = pd.DataFrame(data)
# print(df)

# today = datetime.datetime.now()
# date_time = today.strftime('%d/%M/%Y,%h:%m:%s')
# print(date_time)

import pandas as pd
notes = {
         "DATE: pd.Series([18.0, 20.0, 17.0], index=["Sylvie", "Gilles", "Sylvain"]),
         "TIME": pd.Series([15.0, 7.0, 10.0, 20.0], index=["Sylvie", "Gilles", "Sylvain", "Thomas"]),
    }

df = pd.DataFrame(notes)
df.to_csv('wordTable.csv', encoding='utf8', sep=';')
print(df)
