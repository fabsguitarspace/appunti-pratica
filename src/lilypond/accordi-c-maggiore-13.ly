\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 10)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 9)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 10)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                       (place-fret 6 8)
                          (mute 5)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )

                      

diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                        (place-fret 5 7)
                          (place-fret 4 9)
                          (place-fret 3 7)
                          (place-fret 2 10)
                        )



music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #9
  <g' c e a>1^\diagA
    \set TabStaff.minimumFret = #7
  <c, b' e a>1^\diagB
    \set TabStaff.minimumFret = #7
  <c a' e' a>1^\diagC 
  <c a' d a'>1^\diagD 
  < e a d a'>1^\diagE 
  <e b' d a'>1^\diagF 
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
