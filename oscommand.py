import os


commitmsg="脚本更新"

print(os.system('git add .'))

print(os.system('git pull origin  master'))

print(os.system('git commit -m "%s"'%(commitmsg)))

print(os.system('git push -u origin master'))