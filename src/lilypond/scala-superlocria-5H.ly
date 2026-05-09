\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 5 4 "1" red)
        (place-fret 5 5 "b2" )
        (place-fret 5 7 "#2")
        (place-fret 5 8 "3")
        (place-fret 4 5 "#4")
        (place-fret 4 7 "b6")
        (place-fret 4 9 "b7")
        (place-fret 3 6 "1" red)
        (place-fret 3 7 "b2" )
        (place-fret 3 9 "#2")
        (place-fret 3 10 "3")
        (place-fret 2 8 "#4")
        (place-fret 2 10 "b6")
        (place-fret 1 7 "b7")
        (place-fret 1 9 "1" red)
        )

\markup {
  \my-scale #scale
}