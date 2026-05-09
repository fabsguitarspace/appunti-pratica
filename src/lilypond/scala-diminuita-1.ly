\version "2.24.4"

\include "include/my-scales.ly"


scale = #'(
  
        (place-fret 6 2  blue)
        (place-fret 6 4 )
        (place-fret 6 5 blue)
        (place-fret 5 2 )
        (place-fret 5 3  blue)
        (place-fret 5 5 )
        (place-fret 5 6 blue)
        (place-fret 4 3  )
        (place-fret 4 4 blue)
        (place-fret 4 6 )
        (place-fret 4 7 blue)
        (place-fret 3 4 )
        (place-fret 3 5  blue)
        (place-fret 3 7 )
        (place-fret 2 4 blue)
        (place-fret 2 6 )
        (place-fret 2 7 blue)
        (place-fret 1 4 )
        (place-fret 1 5 blue)
        (place-fret 1 7)
       )
        
\markup {
  \my-scale #scale
}