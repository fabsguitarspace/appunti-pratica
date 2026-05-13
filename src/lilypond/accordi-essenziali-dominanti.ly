\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  { 
 
                       \scale #'(1.5 . 1.5)
                     
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

  \scale #'(1.5 . 1.5) 
  
  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 6)
                           (place-fret 2 5)
                    
                        )
}

diagC    =\markup { 

  \scale #'(1.5 . 1.5) 
   
  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 4)
                          (place-fret 3 5)
                          (place-fret 2 3)
                        
                        )
                      
}

diagD    = \markup { 

  \scale #'(1.5 . 1.5) 
   
  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 5)
                          (place-fret 2 7)
                        
                        )
                      }
                      


diagE    = \markup  {

  \scale #'(1.5 . 1.5) 
  
  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 6)
                
                    
                        )
}

diagF    = \markup  { 

  \scale #'(1.5 . 1.5) 
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
      
       \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/30)
\omit Staff.TimeSignature
      \remove "Bar_number_engraver"
    }
  }
 \midi {}
}
