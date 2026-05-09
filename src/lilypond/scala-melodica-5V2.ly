\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 5 5 "1" red)
        (place-fret 4 2 "2")
        (place-fret 4 3 "b3")
        (place-fret 4 5 "4")
        (place-fret 3 2 "5")
        (place-fret 3 4 "6")
        (place-fret 2 2 "7" )
        (place-fret 2 3 "1"red)
        (place-fret 2 5 "2")
        (place-fret 2 6 "b3")
        (place-fret 1 3 "4")
        (place-fret 1 5 "5")
        (place-fret 1 7 "6")
        (place-fret 1 9 "7" )
        (place-fret 1 10 "1" red)
        )
\markup {
  \my-scale #scale
}