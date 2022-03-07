## [randlink.py](randlink.py)
A simple tool allows you to store (local or web) links and then you can pop a random link and open it. It will help you when you have many links to check and you don't know which one you should pick first.

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
