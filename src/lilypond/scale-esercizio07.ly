\version "2.26.0"
\language "english"
\header { tagline = ##f }
\score {
  \new Staff \fixed c' {
    \time 4/4
    \tempo 4 = 72
    c8 d e f g a b c' | r4 e'8 d' c'4 r4 | g8 a b c' d' b a g | e4 d c2
    \bar "||"
  }
  \layout { indent = 0 }
  \midi { }
}
