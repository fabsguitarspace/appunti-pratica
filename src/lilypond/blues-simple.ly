\version "2.24.4"

\include "include/my-scales.ly"

\score {
  <<
    \new ChordNames {
      \chordmode {
        c1:7 f1:7 c1:7 c1:7
        f1:7 f1:7 c1:7 a1:7
        d1:m7 g1:7 c1:7 g1:7
      }
    }


  >>
  \layout { }
}