\version "2.24.4"
\language "english"
\header { title = "C maggiore: 5 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 5 10)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 9)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                       (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                        (place-fret 6 8)
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

diagG   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 9)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

diagH   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 10)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #8
  <c g' c e g>1^\diagA
  <c b' e g>1^\diagB
    \set TabStaff.minimumFret = #7
  <c a' e' g>1^\diagC 
  <c a' d g>1^\diagD 
  <c e a d g>1^\diagE 
  <e a d g>1^\diagF 
  <e b' d g>1^\diagG 
  <e c' d g>1^\diagH 
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
