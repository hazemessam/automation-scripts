## [gitstart.py](gitstart.py)
Python script automates the process of:
- Creating a remote GitHub repo.
- Initializing a local repo.
- Connecting the local repo to the remote repo.
- Pushing the init commit to the remote repo.

### Requirements:
-   Install `PyGithub` package.
    ```
    $ pip3 install PyGithub=1.54
    ```
-   Generate a GitHub token then add it to your environment variables with name `GIT_TOKEN`. 

### Usage:
```
$ python3 gitstart.py
> Remote repo name [test-dir]: test-repo
> Public repo (yes/no) [yes]:
> Init commit msg [init commit]:
Initialized empty Git repository in /home/hazem/test/test-dir/.git/
[master (root-commit) bbe1e12] init commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 227 bytes | 227.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/hazemessam/test-repo.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
All done!
```
