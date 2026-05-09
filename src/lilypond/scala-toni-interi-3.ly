\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
  
        (place-fret 5 15 "1" red)
        (place-fret 4 12 "2" )
        (place-fret 4 14 "3" )
        (place-fret 4 16 "#4" )
        (place-fret 3 13 "#5" )
        (place-fret 3 15 "b7" )
         (place-fret 2 13 "1" red)
        (place-fret 2 15 "2" )
        (place-fret 2 17 "3" )
        (place-fret 1 14 "#4" )
        (place-fret 1 16 "#5" )
        (place-fret 1 18 "b7" )
         (place-fret 1 20 "1" red)
       )
        
\markup {
  \my-scale #scale
}