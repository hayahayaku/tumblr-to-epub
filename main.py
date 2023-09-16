# hi

import urllib.request as request
import pypub
from html import unescape
import re

# url = "https://leaderoffestivals.tumblr.com/post/677805377142784000/myriad-of-colours-and-flowers-ch-1"
url = "https://leaderoffestivals.tumblr.com/post/728527964399173632/poltergeist-chapter-4"

raw_html = request.urlopen(url).read().decode("utf-8")
post_body = raw_html.split("<li class=\"caption ogcap text-cap\">")[1].split("    </li>")[0]
post_body = unescape(post_body)
title = raw_html.split("<title>")[1].split("</title>")[0]
# post_body = "<html>"+post_body+"</html>"
post_body = f"""<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {post_body}
    </body>
</html>
"""
#         <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Calibre_logo_3.png/240px-Calibre_logo_3.png" />

# [^>]* matches everything before the next >
bracket_cleaner = re.compile("< ?([A-Z0-9][^>]*) ?>")
post_body = bracket_cleaner.sub(r"=== \1 ===", post_body)

# file = open("full_resp.html", "w")
# file.write(raw_html)
# file.close()

file = open("temp.html", "w")
file.write(post_body)
file.close()

test = pypub.Epub("test")
test_chap = pypub.create_chapter_from_file("temp.html")
test.add_chapter(test_chap)
test.create("./test.epub")