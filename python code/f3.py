ap=open("data.txt",'a')
ap.write('\nNear the office we have bagmati bridge')
ap.close()

import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("The file does not exist")