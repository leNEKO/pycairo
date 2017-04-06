#!/usr/bin/env python
"""Python version of cairo-demo/cairo_snippets/cairo_snippets_png.c
"""
from __future__ import division
from math import pi as M_PI  # used by many snippets
import sys

import cairo

from snippets import snip_list, snippet_normalize, snippet_set_bg_svg

width, height = 256, 256 # used by snippet_normalize()
Verbose_mode = True


def do_snippet (snippet):
    if Verbose_mode:
        print 'processing %s' % snippet,
    
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    cr = cairo.Context(surface)

    cr.save()
    try:
        execfile ('snippets/%s.py' % snippet, globals(), locals())
    except:
        exc_type, exc_value = sys.exc_info()[:2] 
        print >> sys.stderr, exc_type, exc_value
    else:
        cr.restore()
        surface.write_to_png ('snippets/%s.png' % snippet)

    if Verbose_mode:
        print

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-s':
        Verbose_mode=False
        del sys.argv[1]
    
    if len(sys.argv) > 1: # do specified snippets
        snippet_list = sys.argv[1:]
    else:                 # do all snippets
        snippet_list = snip_list

    for s in snippet_list:
        do_snippet (s)
