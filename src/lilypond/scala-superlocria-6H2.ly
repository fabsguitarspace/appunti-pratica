\version "2.24.4"

\include "include/my-scales.ly"




scale = #'(
        (place-fret 6 9 "1" red)
        (place-fret 6 10 "b2" )
        (place-fret 6 12 "#2")
        (place-fret 5 8 "b3")
        (place-fret 5 10 "#4")
        (place-fret 5 12 "b6")
        (place-fret 4 9 "b7")
        (place-fret 4 11 "1" red)
        (place-fret 4 12 "b2" )
        (place-fret 3 9 "#2")
        (place-fret 3 10 "3")
        (place-fret 3 12 "#4")
        (place-fret 2 10 "b6")
        (place-fret 2 12 "b7")
        (place-fret 1 9 "1" red)

        )


\markup {
  \my-scale #scale
}