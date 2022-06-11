## 下载安装GIT

## 配置秘钥

### 初始化自己的用户名和邮箱 < 全局配置 > 
在bash上
```config
git config --global user.name "输入你的用户名"
git config --global user.email "输入你的邮箱"
```

### 生成秘钥
由于你的本地 Git 仓库和 GitHub 仓库之间的传输是通过SSH加密的，所以我们需要配置验证信息：
使用以下命令生成 SSH Key：
> ssh-keygen -t rsa -C "邮箱名称"
（首先 ssh-keygen 会确认   密钥的存储位置（默认是 .ssh/id_rsa），
然后它会要求你输入两次密钥口令。 如果你不想在使用密钥时输入口令，将其留空即可。 <<<留空吧,不然以后要经常输入密码>>
然而，如果你使用了密码，那么请确保添加了 -o 选项，它会以比默认格式更能抗暴力破解的格式保存私钥。 你也可以用 ssh-agent 工具来避免每次都要输入密码）。

### 查看秘钥
秘钥的位置
> windows
> c:\Users\w3986\.ssh\
> c:\Users\w3986\.ssh\id_rsa
> c:\Users\w3986\.ssh\id_rsa.pub

### 使用秘钥
打开 id_rsa.pub 复制里面的内容到github  
点击自己的头像 > 点击settings > ssh Keys  >> 在key里面添加秘钥


## 个人访问令牌
settings > Developer settings > Personal access tokens   
点击 "Generate new token"
就可以生成一个token 
### token 属性 
1 Note 名称 : 可以指明用于那里 比如pycharm/ Ubuntu cmd 之类   
2 有效日期 7天, 30天, 90天...  
3 权限   
    repo     
    workflow  
    write:packages   
    delete:packages  
    admin:org  
    admin:public_key  
    admin:repo_hook  
    admin:org_hook  
    gist  
    notifi  cations
    user  更新  个人信息  
    delete_rep  o  删除仓库  
    admin:enterp  rise    
    admin:gpg_key    生成token  
    
### token 用途 
可用来代替HTTPSS上的GIt密码;赋予一些工具操作git的能力  
1, 比如在命令行上第一次push代码的时候,要输入邮箱名和token(在github上生成一个)  
2, pycharm   
> 可以创建多个token 用于不同的地方


