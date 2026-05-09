\version "2.24.4"

\include "include/my-scales.ly"



scale = #'(
  
        (place-fret 6 8 "1" red)
        (place-fret 5 5 "2" )
        (place-fret 5 7 "3" )
        (place-fret 5 9 "#4" )
        (place-fret 4 6 "#5" )
        (place-fret 4 8 "b7" )
         (place-fret 3 5 "1" red)
        (place-fret 3 7 "2" )
        (place-fret 2 5 "3" )
        (place-fret 2 7 "#4" )
        (place-fret 2 9 "#5" )
        (place-fret 1 6 "b7" )
         (place-fret 1 8 "1" red)
       )
        
\markup {
  \my-scale #scale
}