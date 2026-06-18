\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 4 10)
                          (place-fret 3 9)
                          (place-fret 2 10)
                          (place-fret 1 8)
                        )

diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 5 8)
                          (place-fret 3 9)
                          (place-fret 2 10)
                          (place-fret 1 8)
                        )

diagC    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                         (place-fret 5 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )

diagD    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )


diagE   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 6)
                          (place-fret 1 8)
                        )
            
diagF   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 6)
                          (place-fret 1 8)
                        )

diagG   = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 4 7)
                          (place-fret 3 9)
                          (place-fret 2 8)
                          (place-fret 1 8)
                        )


music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #8
  <f c' e a c>1^\diagA
  <f e' a c>1^\diagB
    \set TabStaff.minimumFret = #7
  <f a d g c>1^\diagC 
  <a d g c>1^\diagD 
    \set TabStaff.minimumFret = #6
  <a d f c'>1^\diagE 
  <a e' f c'>1^\diagF 
  <a e' g c>1^\diagG 
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
