\version "2.24.4"

\include "include/my-scales.ly"




scale = #'(
        (place-fret 5 7 "1" red)
        (place-fret 5 8 "b9")
        (place-fret 4 6 "3")
        (place-fret 4 7 "4" )
        (place-fret 3 4 "5")
        (place-fret 3 5 "b6" )
        (place-fret 3 7 "b7")
        (place-fret 2 5 "1" red)
        (place-fret 2 6 "b2")
        (place-fret 1 4 "3")
        (place-fret 1 5 "4" )
        (place-fret 1 7 "5")
        (place-fret 1 8 "b6")
        (place-fret 1 10 "b7")
        (place-fret 1 12 "1" red)
        )

\markup {
  \my-scale #scale
}