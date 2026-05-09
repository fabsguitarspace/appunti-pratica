\version "2.24.4"

\include "include/my-scales.ly"




scale = #'(
  
        (place-fret 6 10 "1" red)
        (place-fret 6 12 "2")
        (place-fret 6 13 "b3")
        (place-fret 5 10 "4")
        (place-fret 5 12 "5")
        (place-fret 5 14 "6")
        (place-fret 4 13 "7")
        (place-fret 4 12 "1" red)
        (place-fret 4 14 "2")
        (place-fret 4 15 "b3")
        (place-fret 3 12 "4")
        (place-fret 3 14 "5")
        (place-fret 2 12 "6")
        (place-fret 2 14 "7")
        (place-fret 2 15 "1" red)
        )

\markup {
  \my-scale #scale
}