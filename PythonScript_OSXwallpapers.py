import sqlite3
from os.path import expanduser

# db_path found from: http://superuser.com/questions/664184
db_path = expanduser("~/Library/Application Support/Dock/desktoppicture.db")
wallpaper_dir = expanduser("~/Pictures/wallpaper/nature")

conn = sqlite3.connect(db_path)
c = conn.cursor()
data_table = list(c.execute('SELECT * FROM data'))

print(data_table)

# The current wallpaper is the last element in the data table.
print("{}/{}".format(wallpaper_dir, data_table[-1][0]))