\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 6 12 "1" red)
        (place-fret 6 13 "b2")
        (place-fret 5 11 "3" )
        (place-fret 5 12 "4" )
        (place-fret 5 14 "5")
        (place-fret 5 15 "b6")
        (place-fret 4 12 "b7")
        (place-fret 4 14 "1" red)
        (place-fret 4 15 "b2")
        (place-fret 3 13 "3")
        (place-fret 3 14 "4" )
        (place-fret 2 12 "5")
        (place-fret 2 13 "b6" )
        (place-fret 2 15 "b7")
        (place-fret 1 12 "1" red)
        )

\markup {
  \my-scale #scale
}