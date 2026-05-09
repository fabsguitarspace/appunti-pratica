\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 5 3 "1" red)
        (place-fret 5 5 "2")
        (place-fret 4 2 "3")
        (place-fret 4 3 "4")
        (place-fret 4 5 "5")
        (place-fret 3 2 "6")
        (place-fret 3 4 "7")
        (place-fret 3 5 "1" red)
        (place-fret 2 3 "2")
        (place-fret 2 5 "3")
        (place-fret 2 6 "4")
        (place-fret 1 3 "5")
        (place-fret 1 5 "6")
        (place-fret 1 7 "7")
        (place-fret 1 8 "1" red)
        )

\markup {
  \my-scale #scale
}