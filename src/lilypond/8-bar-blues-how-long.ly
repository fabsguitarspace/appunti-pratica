\version "2.24.0"

\paper {
  indent = 0
  system-count = 3
}

\header {
  title = "Blues"
}

\layout {
  \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
  \context {
      \Staff
      \override VerticalAxisGroup.default-staff-staff-spacing =
        #'((basic-distance . 14)
           (minimum-distance . 12)
           (padding . 6)
           (stretchability . 0))
    }
  \context {
    \ChordNames
    chordChanges = ##t
  }
}

functions = {
  % 12 battute, 3 righe da 4
  s1^\markup "I7"
  s1^\markup \bold "I7"
  s1^\markup \bold "I7"
  s1^\markup \bold "I7"
  \break

  s1^\markup \bold "IV7"
  s1^\markup \bold "IV7"
  s1^\markup \bold "I7"
  s1^\markup \bold "I7"
  \break

  s1^\markup \bold "V7"
  s1^\markup \bold "IV7"
  s1^\markup \bold "I7"
  s1^\markup \bold "V7"
}

staff = \relative c' {
  \repeat unfold 12 { s1^\markup \vspace #2  \bar "|" }
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