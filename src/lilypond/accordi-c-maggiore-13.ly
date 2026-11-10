\version "2.24.4"
\language "english"
\header { title = "C maggiore: 13 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 10)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )


diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 9)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )

diagC    = \markup \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )


diagD   = \markup \fret-diagram-verbose #'(
                       (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )



diagF   = \markup \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 9)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )

diagG   = \markup \fret-diagram-verbose #'(
                        (place-fret 6 12)
                          (place-fret 4 10)
                          (place-fret 3 12)
                          (place-fret 2 10)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #9
  <g' c e a>1^\diagA
    \set TabStaff.minimumFret = #7
  <c, b' e a>1^\diagB
    \set TabStaff.minimumFret = #7
  <c a' e' a>1^\diagC 
  <c a' d a'>1^\diagD 
  < e a d a'>1^\diagE 
  <e b' d a'>1^\diagF 
    \set TabStaff.minimumFret = #10
  <e c' g' a>1^\diagG
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
