\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
        (place-fret 6 5 "1" red)
        (place-fret 6 7 "2")
        (place-fret 6 8 "b3")
        (place-fret 5 5 "4")
        (place-fret 5 7 "5")
        (place-fret 5 8 "b6")
        (place-fret 4 6 "7")
        (place-fret 4 7 "1" red)
        (place-fret 3 4 "2")
        (place-fret 3 5 "b3" )
        (place-fret 3 7 "4")
        (place-fret 2 5 "5")
        (place-fret 2 6 "b6")
        (place-fret 1 4 "7")
        (place-fret 1 5 "1" red)
        )


\markup {
  \my-scale #scale
}