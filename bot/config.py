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
        default='ffmpeg -y -i "{}" -preset slower -crf 24 -tune animation -c:v libx265 -pix_fmt yuv420p10le -x265-params "profile=main10:aq-mode=3:psy-rd=2.0:no-sao=1:deblock=-1 -1" -s 1920x1080 -colorspace bt2020nc -color_trc smpte2084 -color_primaries bt2020 -master-display "G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)" -max-cll "1000,400" -c:a libopus -b:a 32k -vbr on -compression_level 10 -ac 2 -vf "drawtext=fontfile=font.ttf:fontsize=27:fontcolor=white:bordercolor=black@0.50:x=w-tw-10:y=10:box=1:boxcolor=black@0.5:boxborderw=6:text='Nikhil_Sequeira'" "{}"',
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
