\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 5)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 5)
                          (place-fret 1 5)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 3)
                          (place-fret 1 5)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 5)
                          (place-fret 1 5)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )

diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 5)
                          (mute 4)
                          (place-fret 3 5)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )
            
diagG   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (mute 4)
                          (place-fret 3 5)
                          (place-fret 2 8)
                          (place-fret 1 5)
                        )

diagH   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (mute 4)
                          (place-fret 3 7)
                          (place-fret 2 6)
                          (place-fret 1 5)
                        )
     
music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <f a d a'>1^\diagA
  <f a e' a>1^\diagB
  <f c' d a'>1^\diagC 
  <f c' e a>1^\diagD 
  <f c' f a>1^\diagE 
  <d c' f a>1^\diagF
    \set TabStaff.minimumFret = #5
  <f c' g' a>1^\diagG
  <f d' f a>1^\diagH
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
       \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/30)
       \omit Staff.TimeSignature
      \remove "Bar_number_engraver"
    }
  }
 \midi {}
}
