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
                          (place-fret 2 1)                         
                          (place-fret 1 3)
                        )


diagB    = \markup \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                         (open 4)
                          (place-fret 3 2)
                          (place-fret 2 1)                         
                          (place-fret 1 3)
                        )


diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          (place-fret 1 3)
                        )

diagD    = \markup \scale #'(1.5 . 1.5) 
        \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (mute 4)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          (place-fret 1 3)
                        )

diagE    = \markup \scale #'(1.5 . 1.5) 
      \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 2)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )

diagF    = \markup \scale #'(1.5 . 1.5) 
      \fret-diagram-verbose #'(
                          (place-fret 5 3)
                           (mute 4)
                          (place-fret 3 2)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )
      
diagG    = \markup \scale #'(1.5 . 1.5) 
      \fret-diagram-verbose #'(
                          (place-fret 4 3)
                          (place-fret 3 5)
                          (place-fret 2 5)
                          (place-fret 1 3)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
  <f a c g'>1^\diagA
  <d a' c g'>1^\diagB
  <f a d g>1^\diagC 
  <c a' d g>1^\diagD 
  <f a e' g>1^\diagE
  <c a' e' g>1^\diagF
  <f c' e g>1^\diagG
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
