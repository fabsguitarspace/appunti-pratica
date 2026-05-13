\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 2)
                          (place-fret 2 5)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                         (place-fret 3 4)
                          (place-fret 2 5)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 2)
                          (place-fret 2 5)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 5)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 5)
                          (place-fret 2 5)
                        )

diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 6 5)
                          (mute 5)
                          (place-fret 4 5)
                          (place-fret 3 5)
                          (place-fret 2 5)
                        )
music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <c e a e'>1^\diagA
  <c e b' e>1^\diagB
  <c g' a e'>1^\diagC 
  <c g' b e>1^\diagD 
  <c g' c e>1^\diagE 
  <a g' c e>1^\diagF
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
