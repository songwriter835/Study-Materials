### 1.**安装 Git**

- Windows：[Git 官网下载安装](https://git-scm.com/)
- macOS：brew install git

- Linux：sudo apt install git

### 2.**配置用户信息（只需一次）**

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

### 3.**连接 GitHub（远程仓库）**

```bash
git remote add origin https://github.com/你的用户名/仓库名.git
git branch -M main  # 设置默认分支为 main
git push -u origin main  # 第一次推送
```



### 4.**Git 最基本的用法**

###### 1.**初始化一个项目**

```
git init
```

> 把当前文件夹变成一个 Git 仓库（会生成 .git 文件夹）



###### 2.**添加文件到 Git 管理**

```bash
git add 文件名.py
# 或添加所有改动的文件
git add .
```



###### 3.**提交（保存）修改**

```bash
git commit -m "提交说明，比如：添加了登录功能"
```



###### 4.**查看状态、提交历史**

```bash
git status     # 看哪些文件修改了
git log        # 查看历史提交记录
```

| 设置远程库 | git remote add origin URL |
| ---------- | ------------------------- |
| 推送       | git push -u origin main   |
| 拉取       | git pull                  |
| 创建分支   | git checkout -b 新分支名  |
| 切换分支   | git checkout 分支名       |
| 合并分支   | git merge 分支名          |



### 5.**SSH 连接 Git 仓库的流程**

###### 1.在终端中输入：

```bash
ls ~/.ssh
```

如果你看到类似 id_rsa 和 id_rsa.pub 文件，说明你已经有 SSH 密钥了，可以跳过下一步。



###### 2.生成 SSH 密钥（如没有）

```bash
ssh-keygen -t rsa -b 4096 -C "你的GitHub邮箱"
```

它会在 ~/.ssh 文件夹里生成两个文件：

- id_rsa（私钥，不要泄露）

- id_rsa.pub（公钥，可以上传到 GitHub）

  

###### 3.**添加 SSH 公钥到 GitHub**

1. 打开 GitHub → 点击右上角头像 → Settings → SSH and GPG keys

2. 点击 “New SSH key”

3. 粘贴你的公钥内容（使用以下命令复制）：

   ```bash
   cat ~/.ssh/id_rsa.pub
   ```

   复制输出内容粘贴进去，命名可以随便写，比如 my-laptop-ke

4. ###### **测试 SSH 连接是否成功**

   ```bash
   ssh -T git@github.com
   ```

   第一次会问你是否信任 GitHub，输入 yes 回车。

   如果看到：

   ```bash
   Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

   就说明 SSH 连接成功 ✅

### 6.**使用 SSH 方式克隆和推送仓库**

克隆仓库（SSH URL 格式）

```bash
git clone git@github.com:your-username/your-repo.git
```

推送时也会自动走 SSH，不再要求用户名密码：

```bash
git push origin main
```

### 7.分支管理

```bash
git branch：列出所有本地分支。
git branch <branch-name>：创建新分支。
git checkout <branch-name>：切换到指定分支。
git checkout -b <branch-name>：创建并切换到新分支。
git merge <branch-name>：将指定分支合并到当前分支。
```

### 8.远程仓库交互

```bash
git remote add origin https://github.com/你的用户名/仓库名.git
git remote -v 查看远程仓库
git remote set-url origin 地址 修改远程仓库地址
git remote remove origin 删除远程仓库
```

### 9.撤销操作

```bash
git reset <file>：取消对某个文件的暂存。
git reset：取消所有文件的暂存，保留工作区的修改。
git reset --hard：撤销工作区和暂存区的所有修改，回到最近一次提交的状态。
git revert <commit-hash>：撤销指定的提交，并生成一个新的提交记录。
```
### 10.使用 .gitignore 忽略编译文件
# Python 编译文件
__pycache__/
*.pyc
*.pyo
*.pyd

# macOS 系统文件
.DS_Store

# 检查当前 .gitignore 是否生效

```bash
cat .gitignore
```

# 检查当前 .gitignore 是否生效
```bash
git add .gitignore
git commit -m "Update gitignore to exclude __pycache__ and .DS_Store"
```
