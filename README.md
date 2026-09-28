# git练习

这是给你练手用的 Git 仓库（就在桌面上）。它不是从网上克隆来的，是本地新建的，
所以你可以随便改、随便删，玩坏了也没有任何后果。

## 里面有什么

- `hello.py` —— 一个很小的 Python 文件
- `学习笔记.md` —— 随便写，用来产生"改动"
- `练习记录.md` —— 这个仓库做过哪些操作的记录
- `.gitignore` —— 告诉 Git 哪些文件不用管（比如 `__pycache__`）

## 你可以拿它练什么

1. 改一行 `hello.py`，然后用 GitHub Desktop 打开这个文件夹，commit 一次
2. 在 Desktop 里新建分支，改点东西，再切回 main，感受"文件变回去"
3. 把 `try-yourself` 分支合并到 main（它现在还没合并，留给你练手）
4. 撤销改动：Desktop 里点 Discard changes，或命令行 `git restore 文件名`
5. 玩坏了就整个文件夹删掉，让我重新生成一个

## 怎么打开

GitHub Desktop：`File` → `Add local repository` → 选这个 `git练习` 文件夹
