\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 3 5)
    (place-fret 4 2)
    (place-fret 1 3)
)

diagAbis    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 2 1)
    (place-fret 4 2)
    (place-fret 1 3)
)


diagB    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 3 9)
    (place-fret 5 10)
    (place-fret 1 8)
)

diagC    = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 3 12)
    (place-fret 4 10)
    (place-fret 1 12)
)


diagD   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 5)
    (place-fret 5 3)
    (place-fret 2 5)
)


diagE   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 10)
    (place-fret 5 7)
    (place-fret 2 8)
)

diagF   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 14)
    (place-fret 3 12)
    (place-fret 2 13)
)

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <c' e, g'>1^\diagA
    \set TabStaff.minimumFret = #1
  <c e, g'>1^\diagAbis
    \set TabStaff.minimumFret = #8
  <e g, c'>1^\diagB
    \set TabStaff.minimumFret = #10
  <g c, e'>1^\diagC 
    \set TabStaff.minimumFret = #3
  <g, c, e'>1^\diagD 
      \set TabStaff.minimumFret = #7
  <c e, g'>1^\diagE 
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
