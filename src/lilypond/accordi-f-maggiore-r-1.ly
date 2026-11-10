\version "2.24.4"
\language "english"
\header { title = "F maggiore: R sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 1)
                          (place-fret 1 1)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                         (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 1)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                         (place-fret 5 3)
                          (mute 4)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 1)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                       (open 4 )
                          (place-fret 3 2)
                         (place-fret 2 1)
                          (place-fret 1 1)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                       (open 4 )
                         (open 3)
                         (place-fret 2 1)
                          (place-fret 1 1)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #0
  <f a c f>1^\diagA
      \set TabStaff.minimumFret = #1
  <f a d f>1^\diagB
  <c a' d f>1^\diagC 
    \set TabStaff.minimumFret = #0
  <d a' c f>1^\diagD 
    <d g c f>1^\diagE 
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
