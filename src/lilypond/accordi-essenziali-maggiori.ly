\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  { 
 
                       \scale #'(1.5 . 1.5)
                     
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

  \scale #'(1.5 . 1.5) 
  
  \fret-diagram-verbose #'(
                          (place-fret 6 3)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 4)
                           (place-fret 2 3)
                    
                        )
}
diagC    = \markup  { 

  \scale #'(1.5 . 1.5) \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 5)
                        )
}
diagD    = \markup { 

  \scale #'(1.5 . 1.5) 
   
  \fret-diagram-verbose #'(
                          (place-fret 6 3)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 4)
                        
                        )
                      }
                      
diagE    = \markup  { 

  \scale #'(1.5 . 1.5) 
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

   \new ChordNames {
      \accordi
    }

    % ── Notazione standard ───────────────────────────────────────────
    \new Staff {
    \clef "treble_8"
      \key c \major
      \time 4/4
      \music
    }

    % ── Tablatura ────────────────────────────────────────────────────
    \new TabStaff {
      \set TabStaff.stringTunings = #guitar-tuning
      \music
    }
  >>

  \layout {
    indent = 0

    \context {
      \Score
      
       \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/25)
\omit Staff.TimeSignature
      \remove "Bar_number_engraver"
    }
  }
 \midi {}
}
