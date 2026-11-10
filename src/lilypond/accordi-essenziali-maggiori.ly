\version "2.24.4"
\language "english"
\header { title = "Accordi essenziali maggiori" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  { 

                       \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (place-fret 5 5)
                          (place-fret 4 5)
                          (place-fret 3 4)
                           (mute 2)
                            (mute 1)
                        )
}

diagB    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 3)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 4)
                           (place-fret 2 3)

                        )
}
diagC    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 5)
                        )
}
diagD    = \markup { 

  \fret-diagram-verbose #'(
                          (place-fret 6 3)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 4)

                        )
                      }

diagE    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 4)

                        )
}
music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #3
  <g d' g b>1^\diagA
  <g fs' b d>1^\diagB
  <c g' b e>1^\diagC 
  <g fs' b >1^\diagD
      \set TabStaff.minimumFret = #2
  <c e b'>1^\diagE

}

accordi = \chordmode {

  g1
  g1:maj7
  c1:maj7
  g1:maj7
  c1:maj7
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
  \layout { indent = 0 system-count = #2
    \context { \Voice \override TextScript.staff-padding = #4 }
    \context { \Score \omit StringNumber }
  }
  \midi { }
}
