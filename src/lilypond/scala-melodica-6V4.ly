\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
  
        (place-fret 5 5 "1" red)
        (place-fret 5 7 "2")
        (place-fret 5 8 "b3")
        (place-fret 4 5 "4")
        (place-fret 4 7 "5")
        (place-fret 3 4 "6")
        (place-fret 3 6 "7")
        (place-fret 3 7 "1" red)
        (place-fret 2 5 "2")
        (place-fret 2 6 "b3")
        (place-fret 2 8 "4")
        (place-fret 1 5 "5")
        (place-fret 1 7 "6")
        (place-fret 1 9 "7")
        (place-fret 1 10 "1" red)
        )

\markup {
  \my-scale #scale
}