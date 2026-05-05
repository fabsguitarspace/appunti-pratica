\version "2.24.4"

\include "include/my-scales.ly"

scale = #'(
        (place-fret 6 8 "1" red)
        (place-fret 6 10 "2")
        (place-fret 5 7 "3")

        (place-fret 5 8 "4")
        (place-fret 5 10 "5")

        (place-fret 4 7 "6")
        (place-fret 4 9 "7")
        (place-fret 4 10 "1" red)

        (place-fret 3 7 "2")
        (place-fret 3 9 "3")
        (place-fret 3 10 "4")

        (place-fret 2 8 "5")
        (place-fret 2 10 "6")
        (place-fret 1 7 "7")

        (place-fret 1 8 "1" red)
        )

\markup {
  \my-scale #scale
}