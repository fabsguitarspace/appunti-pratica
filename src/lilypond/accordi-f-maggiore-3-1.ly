\version "2.24.4"
\language "english"
\header { title = "F maggiore: 3 sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 5)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 5)
                          (place-fret 1 5)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 3)
                          (place-fret 1 5)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 5)
                          (place-fret 1 5)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (mute 4)
                          (place-fret 3 5)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )

diagG   = \markup \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (mute 4)
                          (place-fret 3 5)
                          (place-fret 2 8)
                          (place-fret 1 5)
                        )

diagH   = \markup \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (mute 4)
                          (place-fret 3 7)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <f a d a'>1^\diagA
  <f a e' a>1^\diagB
  <f c' d a'>1^\diagC 
  <f c' e a>1^\diagD 
  <f c' f a>1^\diagE 
  <d c' f a>1^\diagF
    \set TabStaff.minimumFret = #5
  <f c' g' a>1^\diagG
  <f d' f a>1^\diagH
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
