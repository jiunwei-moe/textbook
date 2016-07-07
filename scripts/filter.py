#!/usr/bin/env python

"""
Pandoc filter to process code blocks.
"""

import hashlib
import html
import re
import sys

from pandocfilters import toJSONFilter, walk, Image, Div, RawBlock, RawInline, Header, HorizontalRule, Null


def sha1(x):
    return hashlib.sha1(x.encode(sys.getfilesystemencoding())).hexdigest()

def process_html(code):
    code = html.escape(code)
    code = code.replace("[[", "<span class=\"placeholder\">")
    code = code.replace("]]", "</span>")
    code = re.sub(r"^(C:[^&]+&gt; )(.+)$", r"\1<b>\2</b>", code, flags=re.MULTILINE)
    code = re.sub(r"^(&gt;&gt;&gt; )(.+)$", r"\1<b>\2</b>", code, flags=re.MULTILINE)
    code = re.sub(r"^(\.\.\. )(.+)$", r"\1<b>\2</b>", code, flags=re.MULTILINE)
    code = re.sub(r"^(Enter [^:]+: )(.+)$", r"\1<b>\2</b>", code, flags=re.MULTILINE)
    return code

def textbook(key, value, format, meta):
    if key == "Header":
        [level, [ident, classes, keyvals], inlines] = value
        if (level == 5 or level == 1) and not "unnumbered" in classes:
            return Header(level, [ident, classes + ["unnumbered"], keyvals], inlines)
    if key == "CodeBlock":
        [[ident, classes, keyvals], code] = value
        if format == "html":
            return RawBlock("html", "<pre>" + process_html(code) + "</pre>")
    if key == "Code":
        [[ident, classes, keyvals], code] = value
        if format == "html":
            return RawInline("html", "<code>" + process_html(code) + "</code>")
    if key == "Image":
        [attr, inlines, [src, tit]] = value
        if format != "icml":
            return Image(attr, inlines, [src.replace(".pdf", ".png"), tit])
    if key == "Div":
        [[ident, classes, keyvals], blocks] = value
        if format == "docx":
            if "numbers" in classes:
                return Null()
            if any(cls in classes for cls in ["keyterm", "keyterms", "didyouknow", "syntax", "quickcheck", "program"]):
                return Div([ident, classes, keyvals],
                           [HorizontalRule()] + walk(blocks, textbook, format, meta) + [HorizontalRule()])

if __name__ == "__main__":
    toJSONFilter(textbook)
