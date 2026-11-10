\version "2.24.4"
\language "english"
\header { title = "C maggiore: Δ7 sulla 2a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 10)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 12)
                        )

diagB    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 12)
                          (mute 5)
                          (place-fret 4 10)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )


diagC    = \markup  \fret-diagram-verbose #'(
                         (place-fret 6 12)
                          (mute 5)
                          (place-fret 4 12)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )

diagD    = \markup  \fret-diagram-verbose #'(
                         (place-fret 6 12)
                          (place-fret 5 15)
                          (place-fret 4 12)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )

diagE    = \markup \fret-diagram-verbose #'(
                         (place-fret 5 15)
                          (place-fret 4 14)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )

diagG    = \markup \fret-diagram-verbose #'(
                         (place-fret 5 15)
                          (place-fret 4 14)
                          (place-fret 3 14)
                          (place-fret 2 12)
                        )



music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #9
  <g' c e b'>1^\diagA
    \set TabStaff.minimumFret = #10
  <e c' g' b>1^\diagB
    \set TabStaff.minimumFret = #10
  <e d' g b>1^\diagC 
    \set TabStaff.minimumFret = #11
  <e c' d g b>1^\diagD 
  <c' e g b>1^\diagE 
  <c e a b>1^\diagG
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
