## 配置
### 全局配置
git config --global ... 
git config --list 显示当前git配置  
git config -e [global] 编辑git配置文件  

### 当前仓库配置
### 别名 
git alias 



## 初始化仓库
git init .   在当前目录下生成一个git仓库  
git init name  生成了一个名字叫 name的git仓库  
生成了一个.git 隐藏目录 
## 暂存/生成版本库
### git add
git add .  
git add xx.py   
git add **.md   
git add 目录名字  # 包括其子目录  
git add -p  # 对于同一个文件的多处变化可以实现分次提交


> 如果当前目录下有几个文件想要纳入版本控制，需要先用 git add 命令告诉 Git 开始对这些文件进行跟踪，然后提交

git rm [file1] [file2] # 删除工作区文件,并放入暂存区  
git rm --cached [file] # 停止追踪指定文件,但该文件会保留在工作目录  
git mv [file-original] [file-renamed] 改名文件,放入暂存区   



## 代码提交
git commit -m "说明"   添加到版本库      
git commit [file1] [file2] -m "message" 提交暂存区指定文件到版本库   
提交一次新的commit,替代上一次提交  
> 如果代码没有变化,则用来改写上一次的提交信息message 
> git commit --amend -m "message" 

git commit -v  提交时显示所有的diff信息  
git commit -a 提交工作区自上一次commit之后的变化,直接到仓库  
重做上一次commit,并包括指定文件的新变化  
> git commit --amend [file1] [file2]

## 远程仓库
### 添加远程仓库
要添加一个新的远程仓库，可以指定一个简单的名字，以便将来引用,命令格式如下：  
git remote add [shortname] [url]
```bash
git remote add origin https://github.com/wsyshengyun/pyqt5_test.git  
git push -u origin master   
```
git remote  查看当前有哪些远程仓库  
git remote -v  查看当前有哪些远程仓库 - 详细信息  
### 删除远程仓库 
git  remote rm [别名]  

### 远程同步
下载远程仓库的所有变动    
> Git fetch [remote]

显示某个远程仓库的信息  
> git remote show [remote]

增加一个新的一次仓库,并命名  
> git remote add [shortname] [url]

取回远程仓库的变化, 并与本地仓库合并   
> git pull [remote] [branch]

上传本地指定分支到一次仓库  
> git push [remote] [branch]

强行推送当前分支到远程仓库,即使有冲突   
> git push [remote] --force 

推送所有分支到远程仓库   
> git push [remote] --all 


## 连选 
## 变基
git rebase 
git rebase -i HEAD~~~ 
git rebase -i HEAD~3  等效于上面~~~
合并commit成为一个,以HEAD开始,总共3个commit

> 合并commi必须从HEAD开始,不能只合并中间几个commit


## 分支
### 查看分支
git branch  显示所有本地分支    
git branch -r  显示所有远程分支    
git branch -a  显示所有 本地分支 和 远程分支    

### 创建分支
git branch  dev   创建一个新分支, 但停留在当前分支     
git branch -b dev  创建一个新分支, 并切换到该分支   
git branch -v    显示当前分支 以及 分支的版本号     
git branch [dev] [commit]  新建分支, 并指定commit    
新建分支,与指定远程分支建立追踪关系   
git branch --track [dev] [remote-dev]   
### 删除分支
git branch -d [dev]
删除远程分支
> git push origin --delete [dev]
> git branch -dr [remove/branch]
### 检出分支
git checkout dev   切换到分支dev | 并更新工作区   
git checkout -   切换上一个分支 | 并更新工作区   

### 分支的名字 
dev  
dev/01  
dev/name   
> 主分支		master		主分支，所有提供给用户使用的正式版本，都在这个主分支上发布
开发分支		dev 		开发分支，永远是功能最新最全的分支  
功能分支		feature-*	新功能分支，某个功能点正在开发阶段  
发布版本		release-*	发布定期要上线的功能  
修复分支		bug-*		修复线上代码的 bug   

### 合并分支
git merge dev   合并指定分支dev到当前分支  
选择一个commit 合并到当前分支   
> 合并分支可能会出现的问题?
1 可能会由于同一文件修改的情况,出现冲突



### 游离分支

> 有时候我们打开一个工程就开始写代码，等到提交的时候的时候才发现处于no branch。
>  即Not currently on any branch.那现在我们怎么切换到分支并提交代码呢。
>  什么叫no branch：即游离状态,HEAD指针没有指向任何分支，而是直接指向一个commit对象

#### 第一步：

git reflog 找到需要恢复的commit ，记下前面的commit id
 git branch temp  312f7d7 新建一个名字叫temp的分支，用这个分支代替之前的临时分支并且拥有想要恢复的commit， 312f7d7为要恢复的commit id
 git push origin temp推送到仓库
 git checkout master切换到主分支
 git merge temp 将temp合并到master

这里合并一直提示“Already up-to-date”，但当前分支和 master 分支代码不同步。

#### 第二步：

合并 强行push
 git checkout master；
 git reset --hard dev;
 git push --force origin master

 

## checkout 检出 
$ git checkout master     #//取出master版本的head。
$ git checkout tag_name    #//在当前分支上 取出 tag_name 的版本
$ git checkout  master file_name  #//放弃当前对文件file_name的修改
$ git checkout  commit_id file_name  #//取文件file_name的 在commit_id是的版本。commit_id为 git commit 时的sha值。

$ git checkout -b dev/1.5.4 origin/dev/1.5.4

### 从远程dev/1.5.4分支取得到本地分支/dev/1.5.4
$ git checkout -- hello.rb
###这条命令把hello.rb从HEAD中签出.
$ git checkout .
### 这条命令把 当前目录所有修改的文件 从HEAD中签出并且把它恢复成未修改时的样子.
### 注意：在使用 git checkout 时，如果其对应的文件被修改过，那么该修改会被覆盖掉。//原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/git/git_checkout.html


## clone 
git clone [repo] ; repo 仓库的url名字     
git clone [repo]  [ directory ] ; directory 本地目录   
几种效果等价的git clone写法：

```
git clone http://github.com/CosmosHua/locate new
git clone http://github.com/CosmosHua/locate.git new
git clone git://github.com/CosmosHua/locate new
git clone git://github.com/CosmosHua/locate.git new
```
git clone 时，可以所用不同的协议，包括 ssh, git, https 等，其中最常用的是 ssh，因为速度较快，还可以配置公钥免输入密码。各种写法如下：

```
git clone git@github.com:fsliurujie/test.git         --SSH协议
git clone git://github.com/fsliurujie/test.git          --GIT协议
git clone https://github.com/fsliurujie/test.git      --HTTPS协议
```

## 标签
列出所有标签  
> git tag  

新建一个tag在当前commit  
> git tag [tagname]

新建一个tag在指定commit  
> Git tag [tagname] [commit]
> git tag -a [tagname] [commit]   #TODO 加一个-a有什么作用呢?

删除本地标签  
> git tag -d [tagname]

删除远程标签  
> git push ogigin :refs/tags/[tagname]  
 git push [remote] - - delete [tagname] 同上

查看标签信息  
> git show [tagname]

提交指定标签  
> git push [remote] [tag]  # remote : origin


## 查看信息
显示所有变更的文件      
显示当前版本的历史  
显示commit历史, 以及每次commit发生变更的文件  
搜索提交的历史,根据关键词  
显示某个commit之后的所有变动,每个commit占据一行  
显示某个commit之后的所有变动, 其提交说明必须符合搜索条件  
显示某个文件的版本历史,包括文件改名   
显示指定文件的相关的每一次diff  
显示过去5次提交   
显示所有的提交过的用户,按提交次数排序  
显示指定文件是什么人在什么时候修改过   
显示暂存区和工作区的差异   
显示暂存区和上一个commit的差异  
显示工作区与当前分支最新commit之间差异  
显示两次提交之间的差异  
显示今天你写了多少行代码  
显示某次提交发生变化的文件  
显示某次提交时,某个文件的内容  
显示当前分支的最近几次提交      


显示所有变更的文件      
> git status

显示当前分支版本的历史  
> git log

显示commit历史, 以及每次commit发生变更的文件  
>  git log --stat

搜索提交的历史,根据关键词  
> git log -S [keyword]

显示某个commit之后的所有变动,每个commit占据一行  
> git log [tag] HEAD --pretty=format:%s

显示某个commit之后的所有变动, 其提交说明必须符合搜索条件  
>  git log [tag] HEAD --grep feature 

显示某个文件的版本历史,包括文件改名   
>  git log --follow [file]
> git whatchanged [file]

显示指定文件的相关的每一次diff  
>  git log -p [file]

显示过去5次提交   
> git log -5 --pretty --oneline

显示所有的提交过的用户,按提交次数排序  
>  git shortlog -sn

显示指定文件是什么人在什么时候修改过   
> git blae [file]

显示暂存区和工作区的差异   
> git diff

显示暂存区和上一个commit的差异  
>  git diff --cached [file]

显示工作区与当前分支最新commit之间差异  
> git diff HEAD

显示两次提交之间的差异  
>  git diff [first-branch] ...[second-branch]

显示今天你写了多少行代码  
> git diff --shortstat "@{0 day ago}"

显示某次提交的元数据和内容变化
> git show [commit]

显示某次提交发生变化的文件  
> git show --name-only [commit]

显示某次提交时,某个文件的内容  
>  git show [commit]:[filename]

显示当前分支的最近几次提交      
> git reflog

## 撤销 
回复暂存区指定文件到工作区    
> git checkout [file]
> git checkout .  所有文件

恢复某个commit的指定文件到暂存区和工作区   
> git checkout [commit] [file]

重置暂存区的指定文件,与上一次commit保持一致,但工作区不变   
> git reset [file]

重置暂存区和工作区, 与上一次commit保持一致   
> Git reset --hard 

重置当前分支的指针为指定commit, 同时重置暂存区, 工作区不变   
> git reset [commit]

重置当前分支的HEAD为指定commit, 同事重置暂存区和工作区, 与指定commit一致  
> git reset --hard [commit]

重置当前分支的HEAD为指定commit, 但是保持暂存区和工作区不变  
> git reset --keep [commit]

新建一个commit，用来撤销指定commit  
后者的所有变化都将被前者抵消，并且应用到当前分支  
> git revert [commit]

暂时将未提交的变化移除，稍后再移入    
> git stash
> git stash pop

## 提示

这里合并一直提示“Already up-to-date”，但当前分支和 master 分支代码不同步。
当前分支  变基  B
当前分支在最前面  :  B > 当前分支 
将B分支合并到A分支;切换到A分支
当然有区别
A 和 B 合并之后不是 A 也不是 B 而是 C
A 合并 B 和 B 合并 A 的差别是左右和右左的顺序区别，结果没区别
合并之后把 A reset 成 C 那就是 A 获得了 B 的变化，B 不变
## 总的
可以产生冲突的操作有哪些?
> pull
merge
rebase
cherry-pick
unstash changes
apply a patch
