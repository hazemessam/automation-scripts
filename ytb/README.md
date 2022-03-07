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
0) Get Direct Link
1) Download Stream
2) Choose Another Stream
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
