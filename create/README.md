## [create.py](create.py)
Automate the process of creating a remote GitHub repo and initializing a local repo and pushing its files to the remote repo all with one command.

### Requirements:
-   Install `PyGithub` package.
    ```
    $ pip3 install PyGithub=1.54
    ```
-   Generate a GitHub token then add it to your environment variables with name `GIT_TOKEN`. 

### Usage:
```
$ ./create.py
> Enter repo name (default: test): testrepo
> Is it a private repo (y/n) (default: public): y
> Enter initial commit msg (default: init commit):

Initialized empty Git repository in /home/hazem/test/.git/
[master (root-commit) afc2f6f] init commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 test.py
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 215 bytes | 215.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/hazemessam/testrepo.git
 * [new branch]      master -> master
All done!
```
