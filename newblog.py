import os,sys
title=sys.argv[1]
print("标题:"+title)
# os.chdir(r'./public')
# os.system("python commitScript.py")
os.system("hexo new post %s"%(title))
