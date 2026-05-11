\version "2.26.0"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 7)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 5 7)
                          (place-fret 4 7)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (place-fret 5 7)
                          (place-fret 4 9)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 6 8)
            
                          (place-fret 4 9)
                         (place-fret 3 9)
                          (place-fret 2 7)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 6 8)
            
                          (place-fret 4 7)
                         (place-fret 3 9)
                          (place-fret 2 7)
                        )
            
diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                             (place-fret 5 7)
            
                          (place-fret 4 9)
                         (place-fret 3 7)
                          (place-fret 2 7)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #3
  <c a' d fs>1^\diagA
      \set TabStaff.minimumFret = #7
  <c e a d fs>1^\diagB
  <c e b' d fs>1^\diagC 
  <c b' e fs>1^\diagD 
  <c a' e' fs>1^\diagE 
  <e b' d fs>1^\diagF 
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
