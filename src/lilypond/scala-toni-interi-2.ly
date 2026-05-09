\version "2.24.4"

\include "include/my-scales.ly"





scale = #'(
  
        (place-fret 6 8 "1" red)
        (place-fret 6 10 "2" )
        (place-fret 5 7 "3" )
        (place-fret 5 9 "#4" )
        (place-fret 5 11 "#5" )
        (place-fret 4 8 "b7" )
         (place-fret 4 10 "1" red)
        (place-fret 3 7 "2" )
        (place-fret 3 9 "3" )
        (place-fret 2 7 "#4" )
        (place-fret 2 9 "#5" )
        (place-fret 2 11 "b7" )
         (place-fret 2 13 "1" red)
       )
        
\markup {
  \my-scale #scale
}