\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 5 15 "1" red)
        (place-fret 4 12 "2")
        (place-fret 4 14 "3")

        (place-fret 4 15 "4")
        (place-fret 3 12 "5")

        (place-fret 3 14 "6")
        (place-fret 2 12 "7")
        (place-fret 2 13 "1" red)

        (place-fret 2 15 "2")
        (place-fret 1 12 "3")
        (place-fret 1 13 "4")

        (place-fret 1 15 "5")
        (place-fret 1 17 "6")
        (place-fret 1 19 "7")

        (place-fret 1 20 "1" red)
        )

\markup {
  \my-scale #scale
}