\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 5 4 "1" red)
        (place-fret 5 5 "b2" )
        (place-fret 4 2 "#2")
        (place-fret 4 3 "3")
        (place-fret 4 5 "#4")
        (place-fret 3 2 "b6")
        (place-fret 3 4 "b7")
        (place-fret 2 2 "1" red)
        (place-fret 2 3 "b2")
        (place-fret 2 5 "#2")
        (place-fret 2 6 "3")
        (place-fret 1 3 "#4")
        (place-fret 1 5 "b6")
        (place-fret 1 7 "b7")
        (place-fret 1 9 "1" red)
        )

\markup {
  \my-scale #scale
}