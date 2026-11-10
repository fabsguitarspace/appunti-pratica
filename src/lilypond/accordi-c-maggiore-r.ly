\version "2.24.4"
\language "english"
\header { title = "C maggiore: R sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 1)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                         (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 2)
                          (place-fret 2 1)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                         (place-fret 6 3)
                          (mute 5)
                          (place-fret 4 2)
                         (place-fret 3 2)
                          (place-fret 2 1)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                       (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 4)
                          (place-fret 2 1)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                           (place-fret 6 3)
                          (mute 5)
                          (place-fret 4 2)
                         (place-fret 3 4)
                          (place-fret 2 1)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #0
  <c e g c>1^\diagA
      \set TabStaff.minimumFret = #1
  <c e a c>1^\diagB
 <g e' a c>1^\diagC 
  <c e b' c>1^\diagD 
  <g e' b' c>1^\diagE 
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
