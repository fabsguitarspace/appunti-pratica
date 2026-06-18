\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA   = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )

diagB    =  \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 9)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )

diagC   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                             (place-fret 4 7)
            
                          (place-fret 3 9)
                         (place-fret 2 8)
                          (place-fret 1 7)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 8)
                                      (mute 4)

                          (place-fret 3 9)
                         (place-fret 2 10)
                          (place-fret 1 7)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 8)
                                      (mute 4)

                          (place-fret 3 7)
                         (place-fret 2 10)
                          (place-fret 1 7)
                        )
            
diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                             (place-fret 4 5)
            
                          (place-fret 3 5)
                         (place-fret 2 5)
                          (place-fret 1 7)
                        )


            
diagG   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                             (place-fret 4 5)
            
                          (place-fret 3 7)
                         (place-fret 2 5)
                          (place-fret 1 7)
                        )
music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #7
  <f a d g b>1^\diagA
  <f a e' g b>1^\diagB
  <a e' g b>1^\diagC
  <f e' a b>1^\diagD
  <f d' a' b>1^\diagE
    \set TabStaff.minimumFret = #5
  <g c e b'>1^\diagF 
  <g d' e b'>1^\diagG
}

\score {
  <<


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
       \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/40)
       \omit Staff.TimeSignature
      \remove "Bar_number_engraver"
    }
  }
 \midi {}
}
