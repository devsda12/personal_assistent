import os

if os.path.isdir("LOL") is False:
    os.mkdir("LOL")
    print("LOL mADE")
else:
    print("LOL")

f = open("LOL/tesfile.txt", "w+")
f.write("testing testing")
f.close()