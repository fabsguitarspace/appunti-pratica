\version "2.24.4"

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
       (dot-radius . 0.35)
       (string-label-font-mag . 0.3)
     ))
     #:override '(size . 2)
     #:center-column (
       #:fret-diagram-verbose scaleLst
      )
     )
   )
  )




scale = #'(
        (place-fret 6 3 "1" red)
        (place-fret 6 5 "2")
        (place-fret 5 2 "3")
        (place-fret 5 3 "4")
        (place-fret 5 5 "5")
        (place-fret 4 2 "6")
        (place-fret 4 3 "b7")
        (place-fret 4 5 "1" red)
        (place-fret 3 2 "2")
        (place-fret 3 4 "3")
        (place-fret 3 5 "4" )
        (place-fret 2 3 "5")
        (place-fret 2 5 "6")
        (place-fret 2 6 "b7")
        (place-fret 1 3 "1" red)

        )

\markup {
  \my-scale #scale
}