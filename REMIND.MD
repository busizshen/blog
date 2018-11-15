npm install hexo -g，开始安装Hexo

hexo -v，检查hexo是否安装成功

hexo init，初始化


npm install，安装所需要的组件

hexo g，首次体验Hexo

hexo s，开启服务器

hexo new post “博客名” 新建博客

hexo d -g，生成以及部署

需要安装一个扩展：npm install hexo-deployer-git --save


git remote rm origin
git remote add origin [url]

…or create a new repository on the command line

echo "# JavaCode" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/busizshen/JavaCode.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin git@github.com:busizshen/busizshen.github.io.git
git push -u origin master





hexo new "postName" #新建文章
hexo new page "pageName" #新建页面
hexo generate #生成静态页面至public目录
hexo server #开启预览访问端口（默认端口4000，'ctrl + c'关闭server）
hexo deploy #将.deploy目录部署到GitHub
hexo help # 查看帮助
hexo version #查看Hexo的版本
