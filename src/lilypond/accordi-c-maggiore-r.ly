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
                          (open 3)
                          (place-fret 2 1)
                        )


diagB    = \markup \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                         (open 5)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 1)
                        )


diagC    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 1)
                        )

diagD    = \markup \scale #'(1.5 . 1.5) 
        \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (mute 5)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 1)
                        )

diagE    = \markup \scale #'(1.5 . 1.5) 
      \fret-diagram-verbose #'(
                          (place-fret 6 3)
                           (mute 5)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 1)
                        )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
  <c e g c>1^\diagA
  <a e' g c>1^\diagB
  <c e a c>1^\diagC 
  <g e' a c>1^\diagD 
  <g e' b' c>1^\diagE
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
       \override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1/25)
       \omit Staff.TimeSignature
      \remove "Bar_number_engraver"
    }
  }
 \midi {}
}
