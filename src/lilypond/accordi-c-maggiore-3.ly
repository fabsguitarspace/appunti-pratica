\version "2.24.4"
\language "english"
\header { title = "C maggiore: 3 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 2)
                          (place-fret 2 5)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 4)
                          (place-fret 2 5)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 2)
                          (place-fret 2 5)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 5)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 5)
                          (place-fret 2 5)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                          (place-fret 6 5)
                          (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)
                          (place-fret 2 5)
                        )

diagG   = \markup \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 7)
                          (place-fret 2 5)
                        )

diagH   = \markup \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 5)
                          (place-fret 2 5)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <c e a e'>1^\diagA
  <c e b' e>1^\diagB
  <c g' a e'>1^\diagC 
  <c g' b e>1^\diagD 
  <c g' c e>1^\diagE 
  <a g' c e>1^\diagF
    \set TabStaff.minimumFret = #5
  <c g' d' e>1^\diagG
  <c a' c e>1^\diagH
}

\score {
  <<
    \new StaffGroup <<
      \new Staff {
        \clef "treble_8" \tempo 4 = 60
        \key c \major \time 4/4 \music
      }
      \new TabStaff {
        \set TabStaff.stringTunings = #guitar-tuning
        \omit TextScript \music
      }
    >>
  >>
  \layout { indent = 0 system-count = #2
    \context { \Voice \override TextScript.staff-padding = #4 }
    \context { \Score \omit StringNumber }
  }
  \midi { }
}
