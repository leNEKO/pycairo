snippet_normalize (cr, width, height)

snippet_set_bg_svg (cr, "data/freedesktop.svg")
cr.set_operator (cairo.OPERATOR_ADD)
cr.set_source_rgba (1,0,0,0.5)
cr.rectangle (0.2,0.2, 0.5,0.5)
cr.fill ()
cr.set_source_rgb (0,1,0)
cr.rectangle (0.4,0.4, 0.4,0.4)
cr.fill ()
cr.set_source_rgb (0,0,1)
cr.rectangle (0.6,0.6, 0.3,0.3)
cr.fill ()

