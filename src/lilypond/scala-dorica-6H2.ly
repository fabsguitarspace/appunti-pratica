\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
        (place-fret 6 10 "1" red)
        (place-fret 5 7 "2")
        (place-fret 5 8 "b3")
        (place-fret 5 10 "4")
        (place-fret 5 12 "5")
        (place-fret 4 9 "6")
        (place-fret 4 10 "b7")
        (place-fret 4 12 "1" red)
        (place-fret 3 9 "2")
        (place-fret 3 10 "b3")
        (place-fret 3 12 "4")
        (place-fret 2 10 "5")
        (place-fret 2 12 "6")
        (place-fret 2 13 "b7" )
        (place-fret 1 10 "1" red)

        )


\markup {
  \my-scale #scale
}