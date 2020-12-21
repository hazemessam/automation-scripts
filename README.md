# Automation Scripts

## [create.py](create.py)
Automate the process of creating a remote GitHub repo and initializing a local repo and pushing its files to the remote repo all with one command.

### Requirements:
-   install `PyGithub` package.
    ```
    $ pip3 install PyGithub=1.54
    ```
-   Generate a GitHub token then set `TOKEN_PATH` variable to the path of the file that contains the GitHub token. 

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

----

## [ptime.py](ptime.py)
Display the times of the muslims prayers and the remaining time until the next prayer in the day.

### Usage:
```
$ ./ptime.py
Fajr     ->  05:14 am  ->  (0:36)
Dhuhr    ->  11:51 am
Asr      ->  02:36 pm
Maghrib  ->  04:54 pm
Isha     ->  06:19 pm
```

---

## [makepdf.py](makepdf.py)
Convert orderd images inside a folder to a pdf file with the name of the folder.

### Requirements:
-   Install `img2pdf` package.
    ```
    $ pip3 install img2pdf=0.4.0
    ```

### Usage:
```
$ ls
1.png 2.png 3.png
$ ./makepdf.py
test.pdf was created
$ ls
1.png 2.png 3.png test.pdf
```

---

## [randlink.py](randlink.py)
Simple tool allow you to store (local or web) links and then you can pop a random link and open it.

### Requirements:
-   Set `DB_FILE_PATH` variable to the path of the file that you want store links in.

### Usage:
```
$ ./randlink.py
Usage:
    randlink [--push | --add | -a] <link>   :       add a new link
    randlink [--pop | --get | -g]           :       pop a random link then open it
    randlink [--list | -l]                  :       list all links
```
```
$ ./randlink.py --add https://www.youtube.com
$ ./randlink.py --add /home/hazem/media/test.png
$ ./randlink.py --list
https://www.youtube.com
/home/hazem/media/test.png
$ ./randlink --get
https://www.youtube.com was deleted!
Open https://www.youtube.com (y or n)? n
$ ./randlink --get
/home/hazem/media/test.png was deleted!
Open /home/hazem/media/test.png (y or n)? n
$ ./randlink --get
No links!
```