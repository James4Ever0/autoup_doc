#!/bin/bash
#seedme=$(cat .seed)
#hackme=$(node tools/bv2av.js -bv2av $seedme)
#echo about to download $hackme
mkdir -p collector/video_download
# what about the metadata?
# collect later.
cat .seed | xargs -iwhatever python3 collector/Bilibili_video_download/bilibili_video_download_v1.py -p whatever -o $PWD/collector/video_download -q 80 
