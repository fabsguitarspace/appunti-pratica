\version "2.24.0"

\paper {
  indent = 0
  system-count = 4
}

\header {
  title = "My Babe"
}

\include "include/my-chart.ly"

functions = {
  s1^\markup "I7"
  s1
  s1
  s1
  \break

  s1
  s1
  s1^\markup "V7"
  s1
  \break

  s1^\markup "I7"
  s1
  s1^\markup "IV7"
  s1
  \break

  s1^\markup "I7"
  s1^\markup "(V7)"
  s1^\markup "I7"
  s1
}

staff = \relative c' {
  \repeat unfold 16 { s1^\markup \vspace #2  \bar "|" }
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