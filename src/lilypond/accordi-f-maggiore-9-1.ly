\version "2.24.4"
\language "english"
\header { title = "F maggiore: 9 sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 1)                         
                          (place-fret 1 3)
                        )


diagB    = \markup \fret-diagram-verbose #'(
                         (open 4)
                          (place-fret 3 2)
                          (place-fret 2 1)                         
                          (place-fret 1 3)
                        )


diagC    = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          (place-fret 1 3)
                        )

diagD    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (mute 4)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          (place-fret 1 3)
                        )

diagE    = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )

diagF    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                           (mute 4)
                          (place-fret 3 2)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )

diagG    = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
  <f a c g'>1^\diagA
  <d a' c g'>1^\diagB
  <f a d g>1^\diagC 
  <c a' d g>1^\diagD 
  <f a e' g>1^\diagE
  <c a' e' g>1^\diagF
  <f c' e g>1^\diagG
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
