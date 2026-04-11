\header {
	tagline = ##f
	indent = 0
}

#(define-markup-command (my-scale layout props scaleLst) (scheme?)
  "Draw a scale"
  (interpret-markup layout props
   (markup
     #:override '(fret-diagram-details . (
       (finger-code . in-dot)
       (number-type . arabic)
       (dot-radius . 0.3)
       (string-label-font-mag . 0.3)
     ))
     #:override '(size . 2)
     #:center-column (
       #:fret-diagram-verbose scaleLst
     )
     #:hspace 3)))