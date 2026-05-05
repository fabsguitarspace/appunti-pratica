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
                          (place-fret 4 7)
                          (place-fret 3 5)
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
                          (place-fret 3 5)
                           (place-fret 2 5)
                    
                        )
}

diagC    = \markup  {

  \scale #'(1.5 . 1.5) 
  
  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 4)
                          (place-fret 3 5)
                           (place-fret 2 5)
                    
                        )
}
diagD    = \markup { 

  \scale #'(1.5 . 1.5) 
   
  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 6)
                        
                        )
                      }
                      
diagE    = \markup  { 

  \scale #'(1.5 . 1.5) 
  \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (place-fret 4 7)
                          (place-fret 3 5)
                          (place-fret 2 6)
                        
                        )
                      }

diagF    = \markup  {

  \scale #'(1.5 . 1.5) 
  
  \fret-diagram-verbose #'(
                          (place-fret 6 5)
                      (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)
                
                    
                        )
}

diagG    = \markup  {

  \scale #'(1.5 . 1.5) 
  
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
