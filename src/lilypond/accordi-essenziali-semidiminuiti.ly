\version "2.24.4"
\language "english"
\header { title = "Accordi essenziali semidiminuiti" tagline = ##f }
\paper { page-breaking = #ly:one-page-breaking
  line-width = 160\mm ragged-right = ##f }


diagA    =  \markup  {

  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)
                           (place-fret 2 4)

                        )
}

diagB    = \markup  { 

  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 6)
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
                          (place-fret 6 4)
                          (place-fret 4 3)
                          (place-fret 3 5)


                        )
}


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #4
  <a g' c ef>1^\diagA
  <d af' c f>1^\diagB
    \set TabStaff.minimumFret = #4
    \set TabStaff.minimumFret = #5
  <a g' c>1^\diagF
   \set TabStaff.minimumFret = #3
  <af f' c'>1^\diagG

}

accordi = \chordmode {
  a1:m7.5-
  d1:m7.5-
  a1:m7.5-
  d1:m7.5-
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
