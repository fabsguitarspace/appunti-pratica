\version "2.26.0"
\language "english"
\header { tagline = ##f }
\score {
  \new Staff \fixed c' {
    \time 4/4
    \tempo 4 = 72
    c8 d e f g4 r4 | c8-> d e f g4-> r4 | c8 d e f r4 g4 | c4 r4 r2
    \bar "||"
  }
  \layout { indent = 0 }
  \midi { }
}
