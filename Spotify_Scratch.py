# Final Project Scratch

# Packages
import pandas as pd

# read in csv with pandas

music = pd.read_csv('/Users/reaganmatlock/documents/545_COSC/final_project/music.csv')

music.head()
music.info()

# Remove columns ID and Name

music = music.drop('id', 1)
music = music.drop('name', 1)

music.head()
music.info()


# Decades Variable

#music.loc[1,1]
#len(music)
music['year'][1201] >= 1930
music.year[1201] >= 1930

music['decade'] = 1

music.head()
music.info()

for i in music.iterrows():
    if music.year[i] >= 1920 & music.year[i] < 1930:
        music['decade'][i] = 1920
    elif music.year[i] >= 1930 & music.year[i] < 1940:
        music['decade'][i] = 1930
    elif music.year[i] >= 1940 & music.year[i] < 1950:
        music['decade'][i] = 1940
    elif music.year[i] >= 1950 & music.year[i] < 1960:
        music['decade'][i] = 1950
    elif music.year[i] >= 1960 & music.year[i] < 1970:
        music['decade'][i] = 1960
    elif music.year[i] >= 1970 & music.year[i] < 1980:
        music['decade'][i] = 1970
    elif music.year[i] >= 1980 & music.year[i] < 1990:
        music['decade'][i] = 1980
    elif music.year[i] >= 1990 & music.year[i] < 2000:
        music['decade'][i] = 1990
    elif music.year[i] >= 2000 & music.year[i] < 2010:
        music['decade'][i] = 2000
    elif music.year[i] >= 2010 & music.year[i] < 2020:
        music['decade'][i] = 2010
else:
    music['decade'][i] = 2020



