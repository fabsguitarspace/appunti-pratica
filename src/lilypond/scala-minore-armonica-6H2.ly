\version "2.24.4"

\include "include/my-scales.ly"




scale = #'(
        (place-fret 5 12 "1" red)
        (place-fret 4 9 "2")
        (place-fret 4 10 "b3" )
        (place-fret 4 12 "4")
        (place-fret 3 9 "5")
        (place-fret 3 10 "b6")
        (place-fret 2 9 "7")
        (place-fret 2 10 "1" red)
        (place-fret 2 12 "2")
        (place-fret 2 13 "b3")
        (place-fret 1 10 "4")
        (place-fret 1 12 "5")
        (place-fret 1 13 "b6")
        (place-fret 1 16 "7")
        (place-fret 1 17 "1" red)
        )



\markup {
  \my-scale #scale
}