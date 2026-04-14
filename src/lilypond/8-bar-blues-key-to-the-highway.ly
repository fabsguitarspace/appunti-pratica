\version "2.24.0"

\paper {
  indent = 0
  system-count = 2
}

\header {
  title = "Key to the Highway"
  composer = " "
  tagline = ##f
}

\include "include/my-chart.ly"

functions = {
  % 12 battute, 3 righe da 4
  s1^\markup "I7"
  s1^\markup "V7"
  s1^\markup "IV7"
  s1
  \break

  s1^\markup "I7"
  s1^\markup "V7"
  s2^\markup "I7"
  s2^\markup "IV7"
  s2^\markup "I7"
  s2^\markup "V7"
}

staff = \relative c' {
  \repeat unfold 8 { s1 \bar "|" }
  \bar "|."
}

\score {
  <<
    \new Staff {
      <<
        \new Voice { \functions }
        \new Voice { \staff }
      >>
    }
  >>
}