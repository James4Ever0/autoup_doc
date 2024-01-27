#!/bin/bash
apt install ffmpeg espeak
sudo apt install --reinstall python*-decorator
alocation=$(which ffmpeg)
mkdir -p ~/.imageio/ffmpeg
ln -s $alocation ~/.imageio/ffmpeg/ffmpeg.linux64
pip3 install -r requirements.txt
pip3 install -r poster/bilibiliupload/requirements.txt
cat nodejs_require | xargs -iabc npm i -g abc
pip3 install -r collector/Bilibili_video_download/requirements.txt
pip3 install webrtcvad==2.0.10 wave pydub simpleaudio numpy matplotlib
# use virtualenv? what do you think?
# also some basic audio library? such as TTS.
# when advanced, use sclang, scide, scsynth to generate music, or deeplearning.
