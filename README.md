# Automation Scripts

## Scripts:
- [create.py](#createpy)
- [ytb.py](#ytbpy)
- [ptime.py](#ptimepy)
- [mkpdf.py](#mkpdfpy)
- [randlink.py](#randlinkpy)

---

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

---

## [ytb.py](ytb.py)
Download or get the direct link to download youtube streams as videos or audios.

### Requirements:
-   Install `pafy` package.
    ```
    $ pip3 install pafy
    ```
- Add downloads directory path to your environment variables with name `DOWNLOADS_DIR`.

### Usage:
```
$ ./ytb.py https://www.youtube.com/watch?v=OKEhEgD3uV4
Title: Dependency Inversion (DIP) - SOLID Design Principles
-----------------------------------------------------------
0) mp4@360p -> 12.4MB
1) mp4@720p -> 27.0MB
2) m4a@48k -> 0.1MB
3) m4a@128k -> 0.1MB
4) webm@160k -> 0.1MB
Choose Stream: 3
----------------
0) Get Link
1) Download
Choose Action: 0
----------------
https://manifest.googlevideo.com/api/manifest/dash/expire/1627562151/ei/R0wCYY7XGKqCp-oPzaicgAY/ip/156.197.128.160/id/38a1211200f7b95e/source/youtube/requiressl/yes/playback_host/r1---sn-uxaxjvhxbt2u-2nqd.googlevideo.com/mh/cE/mm/31%2C29/mn/sn-uxaxjvhxbt2u-2nqd%2Csn-hgn7yn7s/ms/au%2Crdu/mv/m/mvi/1/pl/21/tx/24047099/txs/24047098%2C24047099%2C24047100%2C24047101%2C24047102%2C24047103%2C24047104/hfr/all/as/fmp4_audio_clear%2Cwebm_audio_clear%2Cwebm2_audio_clear%2Cfmp4_sd_hd_clear%2Cwebm2_sd_hd_clear/initcwndbps/241250/vprv/1/mt/1627540368/fvip/3/keepalive/yes/fexp/24001373%2C24007246/beids/9466586/itag/0/sparams/expire%2Cei%2Cip%2Cid%2Csource%2Crequiressl%2Ctx%2Ctxs%2Chfr%2Cas%2Cvprv%2Citag/sig/AOq0QJ8wRQIgANFSe7oqw1GDzdXryFx14lW1UQYACFFumnu-FYxjjXUCIQCBp8JZw1PeFsQxEOje1yw3gCerpxiPSqaZjuXxTTzu7Q%3D%3D/lsparams/playback_host%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps/lsig/AG3C_xAwRgIhAPp0lbXa14CnHsq7oN8Hn_GWp2rYkNryANgOgvqwMPBiAiEA3yJ94x8Fxkt_RtHfbtUPCon7nnKTQbrey9FPf-_MDd0%3D
```

```
$ ./ytb.py https://www.youtube.com/watch?v=OKEhEgD3uV4
Title: Dependency Inversion (DIP) - SOLID Design Principles
-----------------------------------------------------------
0) mp4@360p -> 12.4MB
1) mp4@720p -> 27.0MB
2) m4a@48k -> 0.1MB
3) m4a@128k -> 0.1MB
4) webm@160k -> 0.1MB
Choose Stream: 3
----------------
0) Get Link
1) Download
Choose Action: 1
----------------
Downloading to /mnt/c/Users/Hazem/Downloads
  75,932.0 Bytes [100.00%] received. Rate: [ 566 KB/s].  ETA: [0 secs]
```

---

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

## [mkpdf.py](mkpdf.py)
Convert ordered images inside a folder to a pdf file with the name of the folder.

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