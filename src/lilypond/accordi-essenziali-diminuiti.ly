\version "2.24.4"
\language "english"
\header { title = "Accordi essenziali diminuiti" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    =  \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 5)
                           (place-fret 2 4)

                        )
}

diagB    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 6)
                          (place-fret 3 4)
                          (place-fret 2 6)

                        )
                      }

diagC    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 4 5)
                          (place-fret 3 6)
                          (place-fret 2 5)
                          (place-fret 1 6)


                        )
}



music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #4
  <a gf' c ef>1^\diagA
  <d af' b f'>1^\diagB
  <g df' e bf'>1^\diagC


}

accordi = \chordmode {
  a1:dim7
  d1:dim7
  g1:dim7
}

\score {
  <<
    \new ChordNames { \accordi }
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
