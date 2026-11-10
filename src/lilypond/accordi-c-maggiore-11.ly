\version "2.24.4"
\language "english"
\header { title = "C maggiore: ♯11 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 7)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 5 7)
                          (place-fret 4 7)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (place-fret 5 7)
                          (place-fret 4 9)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                        (place-fret 6 8)
                                      (mute 5)

                          (place-fret 4 9)
                         (place-fret 3 9)
                          (place-fret 2 7)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                        (place-fret 6 8)
                                      (mute 5)

                          (place-fret 4 7)
                         (place-fret 3 9)
                          (place-fret 2 7)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                             (place-fret 5 7)

                          (place-fret 4 9)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #3
  <c a' d fs>1^\diagA
      \set TabStaff.minimumFret = #7
  <c e a d fs>1^\diagB
  <c e b' d fs>1^\diagC 
  <c b' e fs>1^\diagD 
  <c a' e' fs>1^\diagE 
  <e b' d fs>1^\diagF 
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
