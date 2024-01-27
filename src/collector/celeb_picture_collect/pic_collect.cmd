@echo off
mkdir celeb_pictures
REM flrst let's collect info of celebrities.
REM and we've got pictures.
REM make sure pictures are 1000x and more. <- this one is not ramdisked.
REM make ramdisk if you wish? but it might not be good at all.
REM generate information then.
unix2dos celeb_list.txt
python36 collect_pics.py celeb_list.txt
REM detect the face then. just put all pics to faceswap.py.