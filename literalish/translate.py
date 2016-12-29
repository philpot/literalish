#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cgi
# enable debugging
import cgitb

from literalish import translate
cgitb.enable()

# program written by Andrew Philpot

print "Content-Type: text/html;charset=utf-8"
print

form = cgi.FieldStorage()
if "word" not in form:
    print "<h1>Error</h1>"
    print "Please supply word"
else:
    word = form["word"].value or ""
    print >> sys.stderr, "Word [%s]" % word
    xlat = translate(word)
    print """<h2>%s: <font color="red">%s</font></h2>""" % (word, xlat)
    print """<a href="http://thaddeus.philpot.info/literalish/literalish/index.html">Translate another</a>"""
