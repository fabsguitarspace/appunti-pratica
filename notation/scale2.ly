\version "2.24.1"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 6 3 "1" red)
        (place-fret 6 5 "2")
        (place-fret 6 6 "m3")

        (place-fret 5 3 "4")
        (place-fret 5 5 "5")

        (place-fret 4 2 "6")
        (place-fret 4 3 "m7")
        (place-fret 4 5 "1" red)

        (place-fret 3 2 "2")
        (place-fret 3 3 "m3")
        (place-fret 3 5 "4")

        (place-fret 2 3 "5")
        (place-fret 2 5 "6")
        (place-fret 2 6 "m7")

        (place-fret 1 3 "1" red)
        (place-fret 1 5 "2")
        (place-fret 1 6 "m3"))


\markup {
  \my-scale \scale
}