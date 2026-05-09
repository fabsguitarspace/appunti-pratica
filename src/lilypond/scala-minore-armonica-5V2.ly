\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
        (place-fret 6 5 "1" red)
        (place-fret 5 2 "2" )
        (place-fret 5 3 "b3" )
        (place-fret 5 5 "4")
        (place-fret 4 2 "5")
        (place-fret 4 3 "b6")
        (place-fret 3 1 "7")
        (place-fret 3 2 "1" red)
        (place-fret 3 4 "2")
        (place-fret 3 5 "b3" )
        (place-fret 2 3 "4")
        (place-fret 2 5 "5")
        (place-fret 2 6 "b6")
        (place-fret 1 4 "7")
        (place-fret 1 5 "1" red)
        )


\markup {
  \my-scale #scale
}