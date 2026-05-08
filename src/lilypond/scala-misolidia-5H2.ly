\version "2.24.4"

\include "include/my-scales.ly"
scale = #'(
        (place-fret 6 3 "1" red)
        (place-fret 6 5 "2")
        (place-fret 5 2 "3" )
        (place-fret 5 3 "4" )
        (place-fret 5 5 "5")
        (place-fret 4 2 "6")
        (place-fret 4 3 "b7")
        (place-fret 4 5 "1")
        (place-fret 4 7 "2")
        (place-fret 3 4 "3")
        (place-fret 3 5 "4" red)
        (place-fret 3 7 "5")
        (place-fret 2 5 "6")
        (place-fret 2 6 "b7")
        (place-fret 2 8 "1" red)
        )
        
\markup {
  \my-scale #scale
}