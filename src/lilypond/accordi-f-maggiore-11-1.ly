\version "2.24.4"
\language "english"
\header { title = "F maggiore: ♯11 sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA   = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )

diagB    =  \markup  \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 9)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )

diagC   = \markup \fret-diagram-verbose #'(
                             (place-fret 4 7)

                          (place-fret 3 9)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 8)
                                      (mute 4)

                          (place-fret 3 9)
                         (place-fret 2 10)
                          (place-fret 1 7)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 8)
                                      (mute 4)

                          (place-fret 3 7)
                         (place-fret 2 10)
                          (place-fret 1 7)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                             (place-fret 4 5)

                          (place-fret 3 5)
                         (place-fret 2 5)
                          (place-fret 1 7)
                        )



diagG   = \markup \fret-diagram-verbose #'(
                             (place-fret 4 5)

                          (place-fret 3 7)
                         (place-fret 2 5)
                          (place-fret 1 7)
                        )
music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #7
  <f a d g b>1^\diagA
  <f a e' g b>1^\diagB
  <a e' g b>1^\diagC
  <f e' a b>1^\diagD
  <f d' a' b>1^\diagE
    \set TabStaff.minimumFret = #5
  <g c e b'>1^\diagF 
  <g d' e b'>1^\diagG
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
