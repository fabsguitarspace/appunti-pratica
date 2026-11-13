\version "2.24.4"
\language "english"
\header { title = "F maggiore: 13 sulla 1a corda" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA = \markup \fret-diagram-verbose #'(
                          (place-fret 4 10)
                          (place-fret 3 10)
                          (place-fret 2 10)
                          (place-fret 1 10)
                        )

diagB = \markup \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 3 9)
                          (place-fret 2 10)
                          (place-fret 1 10)
                        )

diagC = \markup \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 10)
                        )

diagD = \markup \fret-diagram-verbose #'(
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 10)
                        )

diagE = \markup \fret-diagram-verbose #'(
                          (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 8)
                          (place-fret 1 10)
                        )


music = \absolute {
  \set TabStaff.restrainOpenStrings = ##t
  <c'\4 f'\3 a'\2 d''\1>1^\diagA
  <f\5 e'\3 a'\2 d''\1>1^\diagB
  <f\5 a\4 d'\3 g'\2 d''\1>1^\diagC
  <a\4 d'\3 g'\2 d''\1>1^\diagD
  <a\4 e'\3 g'\2 d''\1>1^\diagE
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
  \layout { indent = 0 system-count = #1
    \context { \Voice \override TextScript.staff-padding = #4 }
    \context { \Score \omit StringNumber }
  }
  \midi { }
}
