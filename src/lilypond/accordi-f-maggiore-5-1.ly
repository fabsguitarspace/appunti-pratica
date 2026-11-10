\version "2.24.4"
\language "english"
\header { title = "F maggiore: 5 sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 10)
                          (place-fret 1 8)
                        )

diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 3 9)
                          (place-fret 2 10)
                          (place-fret 1 8)
                        )

diagC    = \markup  \fret-diagram-verbose #'(
                         (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )

diagD    = \markup \fret-diagram-verbose #'(
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )


diagE   = \markup \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 6)
                          (place-fret 1 8)
                        )

diagF   = \markup \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 6)
                          (place-fret 1 8)
                        )

diagG   = \markup \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #8
  <f c' e a c>1^\diagA
  <f e' a c>1^\diagB
    \set TabStaff.minimumFret = #7
  <f a d g c>1^\diagC 
  <a d g c>1^\diagD 
    \set TabStaff.minimumFret = #6
  <a d f c'>1^\diagE 
  <a e' f c'>1^\diagF 
  <a e' g c>1^\diagG 
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
