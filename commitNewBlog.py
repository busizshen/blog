import os


os.system('hexo g')
os.chdir(r'./public')
os.system("python commitScript.py")