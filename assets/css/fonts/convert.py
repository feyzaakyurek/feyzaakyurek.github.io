from fontTools.ttLib import TTFont
import os

for file in os.listdir("."):
    if file.endswith("otf"):
        with TTFont(file) as font:
            font.flavor = "woff"
            font.save(file.split(".")[0] + ".woff")
