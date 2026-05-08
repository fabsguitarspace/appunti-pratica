\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
        (place-fret 6 15 "1" red)
        (place-fret 5 12 "2")
        (place-fret 5 13 "3")
        (place-fret 5 15 "4")
        (place-fret 4 12 "5")
        (place-fret 4 14 "6")
        (place-fret 4 15 "b7")
        (place-fret 3 12 "1" red)
        (place-fret 3 14 "2")
        (place-fret 2 12 "3")
        (place-fret 2 13 "4" )
        (place-fret 2 15 "5")
        (place-fret 1 12 "6")
        (place-fret 1 13 "b7")
        (place-fret 1 15 "1" red)
        )
\markup {
  \my-scale #scale
}