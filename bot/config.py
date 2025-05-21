#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "4018758")
    API_HASH = config("API_HASH", "622bba3cf046315531f71f9d97fa6c2a")
    BOT_TOKEN = config("BOT_TOKEN", "6942815361:AAHwpmE7ThoaKWJJyRIrIZHRXOaxooCXGd8")
    DEV = 1322549723
    OWNER = config("OWNER", "5385471287")
    FFMPEG = config(
        "FFMPEG",
        default='ffmpeg -i "{}" -vf "scale=1920:1080:flags=lanczos,format=gbrpf32le,zscale=rin=limited:r=full,eq=contrast=1.1:saturation=1.2,unsharp=5:5:1.0:5:5:0.0,zimg=param1=1.1:param2=0.98,deband=range=24:blur=false,drawtext=fontfile=font.ttf:fontsize=27:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6',
    )
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f2.jpg"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
