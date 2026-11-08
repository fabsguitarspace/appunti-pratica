\version "2.26.0"
\language "english"
\header { tagline = ##f }
\score {
  \new Staff \fixed c' {
    \time 4/4
    \tempo 4 = 72
    c8 e d f e g f a | g8 b a c' b d' c' e' | d'4 b g e | c1
    \bar "||"
  }
  \layout { indent = 0 }
  \midi { }
}
