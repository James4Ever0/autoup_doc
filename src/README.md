# AutoUP

## Description

To automatically make and upload videos to bilibili.com.

## Core Tech

- https://github.com/search?q=video+segmentation
- https://github.com/MVIG-SJTU/AlphaPose
- https://www.analyticsvidhya.com/blog/2019/04/introduction-image-segmentation-techniques-python/?utm_source=blog&utm_medium=computer-vision-implementing-mask-r-cnn-image-segmentation
- https://github.com/Yonv1943/Unsupervised-Segmentation
- https://github.com/carrierlxk/COSNet
- https://github.com/rsennrich/subword-nmt
- https://github.com/mickaelChen/ReDO
- https://gitee.com/x00e0d991e368/Mask_RCNN
- https://github.com/search?q=body+pose
- https://github.com/deepfakes/faceswap
- https://github.com/search?q=video+classification
- https://github.com/weiaicunzai/awesome-image-classification
- https://gitee.com/ouhuber/Ossas_ChatBot
- https://gitee.com/x00e0d991e368/EssayKiller_v2
- https://gitee.com/DataTraveler_0817/Real-Time-Voice-Cloning
- https://github.com/tyiannak/pyAudioAnalysis
- https://github.com/search?q=music+generate
- https://github.com/danieldjohnson/biaxial-rnn-music-composition
- https://github.com/openai/jukebox
- https://github.com/librosa/librosa
- https://github.com/google/REAPER
- https://pypi.org/project/crepe
- https://github.com/ChenChengKuan/awesome-text-generation
- https://github.com/bearpelican/musicautobot
- https://www.small-text-generator.com/?m=1
- https://github.com/Tony607/colab-mask-rcnn
- https://github.com/seoungwugoh/RGMP
- https://github.com/JialeCao001/SipMask
- https://dl.acm.org/doi/10.1145/1963564.1963586
- https://pjreddie.com/darknet/yolo/
- https://github.com/CVUsers/Auto_maker

...

And, of course: scraping!

## Scraping sources

- QQ chats
- bilibili info
- baidu
- weibo

...

## Discoveries

API of bilibili posting does not allow multiple videos with identical title to be submitted simutaneously. Consider some method to tweak the title somehow.

The posting metadata can be fetched from local server, thanks to tornado.

## Roadmap

Currently collecting, mixing and uploading video is partially complete.

### TODO:

- Streaming redirection.

- Metadata generation.

- Automatic info collection.

- Advanced video mingle technique.

- TTS.

- Markov text generation.

- Automatic video categorization.

- More video processors and more video sources.

- Music scraping, Webpic scraping, (general scraping).

## Software Architecture

Cookie getter from the browser via Lazero Chrome Plugin (version Apollo), or use the embedded automatic login tool under `poster/bilibiliupload` by configuring credentials in config.yaml.

## Installation

1.  Install Lazero Plugin for Chrome (under `chrome_plugins/lazero_crx_16`
2.  Install dependencies via `./init.sh`
3.  Happy Hacking!

## Instructions

1.  Do not rely on me, cause I'm only developing my own little project.
2.  The resources are exhaustive but still, you need to try it yourself.
3.  Never give up!

## Contribution

1.  Fork the repository
2.  Create new branch
3.  Commit your code
4.  Create Pull Request


## Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
