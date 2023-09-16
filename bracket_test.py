import re

test_text = "<blockquote class=\"npf_indented\"><p><About an hour later…> </p></blockquote>"

p = re.compile("< ?([A-Z][^>]*) ?>")
open_cleaned = p.sub(r"=== \1 ===", test_text)

print(open_cleaned)