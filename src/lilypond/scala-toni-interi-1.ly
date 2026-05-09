\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
  
        (place-fret 5 3 "1" red)
        (place-fret 5 5 "2" )
        (place-fret 4 2 "3" )
        (place-fret 4 4 "#4" )
        (place-fret 4 6 "#5" )
        (place-fret 3 3 "b7" )
         (place-fret 3 5 "1" red)
        (place-fret 2 3 "2" )
        (place-fret 2 5 "3" )
        (place-fret 2 7 "#4" )
        (place-fret 1 4 "#5" )
        (place-fret 1 6 "b7" )
         (place-fret 1 8 "1" red)
       )
        
\markup {
  \my-scale #scale
}