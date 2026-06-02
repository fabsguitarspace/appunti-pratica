\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 5 10)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 9)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 8)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                       (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 6 8)
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )
            
diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

diagG   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 9)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

diagH   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 10)
                          (place-fret 3 7)
                          (place-fret 2 8)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #8
  <c g' c e g>1^\diagA
  <c b' e g>1^\diagB
    \set TabStaff.minimumFret = #7
  <c a' e' g>1^\diagC 
  <c a' d g>1^\diagD 
  <c e a d g>1^\diagE 
  <e a d g>1^\diagF 
  <e b' d g>1^\diagG 
  <e c' d g>1^\diagH 
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
