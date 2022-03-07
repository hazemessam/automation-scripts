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
