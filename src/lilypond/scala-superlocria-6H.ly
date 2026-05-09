\version "2.24.4"

\include "include/my-scales.ly"




scale = #'(
  
        (place-fret 6 9 "1" red)
        (place-fret 6 10 "b2" )
        (place-fret 6 12 "#2")
        (place-fret 6 13 "3")
        (place-fret 5 10 "#4")
        (place-fret 5 12 "b6")
        (place-fret 5 14 "b7")
        (place-fret 4 11 "1" red)
        (place-fret 4 12 "b2" )
        (place-fret 4 14 "#2")
        (place-fret 4 15 "3")
        (place-fret 3 12 "#4")
        (place-fret 3 14 "b6")
        (place-fret 2 12 "b7")
        (place-fret 2 14 "1" red)
        )

\markup {
  \my-scale #scale
}