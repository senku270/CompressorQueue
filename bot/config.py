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
    BOT_TOKEN = config("BOT_TOKEN", "6778992913:AAGKtoktjnXZI9adTcBjTMD1uhrNie9mDCs")
    DEV = 5385471287
    OWNER = config("OWNER", "5385471287")
    FFMPEG = config("FFMPEG",'ffmpeg -i "{}" -preset fast -crf 26 -tune animation -c:v libx265 -pix_fmt yuv420p -s 1920x1080 -x265-params "info=0" -color_primaries bt2020 -color_trc bt709 -colorspace bt2020nc -c:a libopus -b:a 24k -vbr on -compression_level 8 -ac 2 -vf "format=yuv420p,scale=1920:1080:flags=lanczos" -threads 4 "{}" -y')
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
