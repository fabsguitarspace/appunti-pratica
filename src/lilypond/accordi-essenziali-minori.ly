\version "2.24.4"
\language "english"
\header { title = "Accordi essenziali minori" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    = \markup  { 

                       \fret-diagram-verbose #'(
                          (place-fret 6 5)
                          (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 5)
                           (mute 2)
                            (mute 1)
                        )
}

diagB    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)
                           (place-fret 2 5)

                        )
}

diagC    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 5)
                           (place-fret 2 5)

                        )
}
diagD    = \markup { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 6)

                        )
                      }

diagE    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 5)
                          (place-fret 2 6)

                        )
                      }

diagF    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)


                        )
}

diagG    = \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 3)
                          (place-fret 3 5)


                        )
}


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #5
  <a e' a c>1^\diagA
  <a g' c e>1^\diagB
    \set TabStaff.minimumFret = #4
  <a fs' c' e>1^\diagC
    \set TabStaff.minimumFret = #5
  <d a' d f>1^\diagD
  <d a' c f>1^\diagE
  <a g' c>1^\diagF
   \set TabStaff.minimumFret = #3
  <d f c'>1^\diagG

}

accordi = \chordmode {

  a1:m
  a1:m7
  a1:m6
  d1:m
  d1:m7
  a1:m7
  d1:m7
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
