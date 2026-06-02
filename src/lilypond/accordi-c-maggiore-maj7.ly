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
                          (place-fret 2 12)
                        )

diagB    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                          (place-fret 6 12)
                          (place-fret 4 10)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )


diagC    = \markup  \scale #'(1.5 . 1.5)
                       \fret-diagram-verbose #'(
                         (place-fret 6 12)
                          (place-fret 4 12)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )

diagD    = \markup \scale #'(1.5 . 1.5) 
            \fret-diagram-verbose #'(
                         (place-fret 5 15)
                          (place-fret 4 14)
                          (place-fret 3 12)
                          (place-fret 2 12)
                        )




music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #9
  <g' c e b'>1^\diagA
    \set TabStaff.minimumFret = #10
  <e c' g' b>1^\diagB
    \set TabStaff.minimumFret = #10
  <e d' g b>1^\diagC 
    \set TabStaff.minimumFret = #11
  <c' e g b>1^\diagD 
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
