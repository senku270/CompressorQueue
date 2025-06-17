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
    BOT_TOKEN = config("BOT_TOKEN", "6778992913:AAFpUEeJo7kfEfDZhxAdhvK9-9s3xqD31DE")
    DEV = 5385471287
    OWNER = config("OWNER", "5385471287")
    FFMPEG = config("FFMPEG", 'ffmpeg -i "{}" -vf "subtitles=subtitles.srt" -map 0:v:0 -map 0:a:0 -map 0:a:1 -c:v hevc_nvenc -preset p7 -tune hq -rc constqp -qp 28 -c:a copy -metadata:s:s:0 title="Subtitles by @Anime_Stein" -metadata:s:v title="Encoded by [Anime Stein] Telegram Channel" -metadata:s:a:0 title="[Telegram: @AnimeStein]" -metadata:s:a:1 title="[Telegram: @Anime_Stein]" -metadata title="Fileinfo - Steins Gate is Goat" -movflags +faststart "{}" -y')
    TELEGRAPH_API = config("TELEGRAPH_API", default="https://api.telegra.ph")
    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/75ee20ec8d8c8bba84f02"
    )
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
