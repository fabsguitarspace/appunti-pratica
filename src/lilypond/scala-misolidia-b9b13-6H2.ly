\version "2.24.4"

\include "include/my-scales.ly"





scale = #'(
        (place-fret 6 12 "1" red)
        (place-fret 6 13 "b2")
        (place-fret 5 11 "3" )
        (place-fret 5 12 "4")
        (place-fret 4 9 "5")
        (place-fret 4 10 "b6" )
        (place-fret 4 12 "b7")
        (place-fret 3 9 "1" red)
        (place-fret 3 10 "b2")
        (place-fret 2 9 "3")
        (place-fret 2 10 "4" )
        (place-fret 2 12 "5")
        (place-fret 2 13 "b6")
        (place-fret 1 10 "b7")
        (place-fret 1 12 "1" red)
        )


\markup {
  \my-scale #scale
}