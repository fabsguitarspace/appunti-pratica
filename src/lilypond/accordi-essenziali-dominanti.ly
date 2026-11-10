\version "2.24.4"
\language "english"
\header { title = "Accordi essenziali dominanti" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  { 

                       \fret-diagram-verbose #'(
                          (place-fret 6 5)
                          (place-fret 5 7)
                          (place-fret 4 5)
                          (place-fret 3 6)
                           (mute 2)
                            (mute 1)
                        )
}

diagB    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 6)
                           (place-fret 2 5)

                        )
}

diagC    =\markup { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 4)
                          (place-fret 3 5)
                          (place-fret 2 3)

                        )

}

diagD    = \markup { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 5)
                          (place-fret 2 7)

                        )
                      }



diagE    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 6)


                        )
}

diagF    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 4)
                          (place-fret 3 5)

                        )
                      }



music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #5
  <a e' g cs>1^\diagA
  <a g' cs e>1^\diagB
    \set TabStaff.minimumFret = #4
  <d fs c' d>1^\diagC
    \set TabStaff.minimumFret = #5
  <d a' c fs>1^\diagD
  <a g' cs>1^\diagE
    \set TabStaff.minimumFret = #3
  <d fs c'>1^\diagF

}

accordi = \chordmode {

  a1:7
  a1:7
  d1:7
  d1:7
  a1:7
  d1:7
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
