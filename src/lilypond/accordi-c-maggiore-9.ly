\version "2.24.4"
\language "english"
\header { title = "C maggiore: 9 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 3)
                        )


diagB    = \markup \fret-diagram-verbose #'(
                         (open 5)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 3)
                        )


diagC    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 3)
                        )

diagD    = \markup \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (mute 5)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 3)
                        )

diagE    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 3)
                        )

diagF    = \markup \fret-diagram-verbose #'(
                          (place-fret 6 3)
                           (mute 5)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 3)
                        )

diagG    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 3)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
  <c e g d'>1^\diagA
  <a e' g d'>1^\diagB
  <c e a d>1^\diagC 
  <g e' a d>1^\diagD 
  <c e b' d>1^\diagE
  <g e' b' d>1^\diagF
  <c g' b d>1^\diagG
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
