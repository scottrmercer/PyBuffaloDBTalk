import os

import pandas as pd
from sqlalchemy import create_engine

con = create_engine('postgres://postgres:postgres@postgres')

# create a sample dataframe
df_sample = pd.DataFrame(
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    columns=["a", "b", "c"])

# write to db
df_sample.to_sql(name="sample", con=con, index=False)

# read from db
print(pd.read_sql(sql="SELECT * FROM sample", con=con))
