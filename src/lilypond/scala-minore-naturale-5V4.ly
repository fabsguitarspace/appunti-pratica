\version "2.24.4"

\include "include/my-scales.ly"

scale = #'(
        (place-fret 5 12 "1" red)
        (place-fret 5 14 "2")
        (place-fret 5 15 "b3")
        (place-fret 4 12 "4")
        (place-fret 4 14 "5")
        (place-fret 4 15 "b6")
        (place-fret 3 12 "b7")
        (place-fret 3 14 "1" red)
        (place-fret 2 12 "2")
        (place-fret 2 13 "b3" )
        (place-fret 2 15 "4")
        (place-fret 1 12 "5")
        (place-fret 1 13 "b6")
        (place-fret 1 15 "b7")
        (place-fret 1 17 "1" red)
        )
\markup {
  \my-scale #scale
}