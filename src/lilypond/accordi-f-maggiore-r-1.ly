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
                          (place-fret 1 1)
                        )


diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                         (place-fret 4 3)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 1)
                        )

diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 5 3)
                          (mute 4)
                          (place-fret 3 2)
                         (place-fret 2 3)
                          (place-fret 1 1)
                        )


diagD   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                       (open 4 )
                          (place-fret 3 2)
                         (place-fret 2 1)
                          (place-fret 1 1)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                       (open 4 )
                         (open 3)
                         (place-fret 2 1)
                          (place-fret 1 1)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #0
  <f a c f>1^\diagA
      \set TabStaff.minimumFret = #1
  <f a d f>1^\diagB
  <c a' d f>1^\diagC 
    \set TabStaff.minimumFret = #0
  <d a' c f>1^\diagD 
    <d g c f>1^\diagE 
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
