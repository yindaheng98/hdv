# hdv

some High Definition Video datasets.

And some related tools.

## Intro

[Inter4K](https://alexandrosstergiou.github.io/datasets/Inter4K/index.html)

[UGC dataset](https://media.withyoutube.com/)

[UVG Dataset](https://ultravideo.fi/#testsequences)

[Xiph.org Video Test Media](https://media.xiph.org/video/derf/)

## Download them

### Inter4K

Download Inter4K.zip from [Google Drive](https://tinyurl.com/inter4KUHD)

```sh
unzip Inter4K.zip -d datasets/orig/videos/
```

### 1080P UGC dataset

```sh
gsutil ls gs://ugc-dataset/vp9_compressed_videos/*1080P*orig.mp4
gsutil ls gs://ugc-dataset/original_videos_h264/*1080P*.mp4

mkdir videos
gsutil -m cp gs://ugc-dataset/vp9_compressed_videos/*1080P*orig.mp4 datasets/orig/videos/
gsutil -m cp gs://ugc-dataset/original_videos_h264/*1080P*.mp4 datasets/orig/videos/
```

## Generate Dataset

```sh
python dataset_gen.py
```