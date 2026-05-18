\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 3 5)
    (place-fret 2 4)
    (place-fret 1 3)
)


diagB    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 3 8)
    (place-fret 2 8)
    (place-fret 1 8)
)

diagC    = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 3 11)
    (place-fret 2 13)
    (place-fret 1 12)
)


diagD   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 5)
    (place-fret 3 5)
    (place-fret 2 4)
)


diagE   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 10)
    (place-fret 3 8)
    (place-fret 2 8)
)

diagF   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 4 13)
    (place-fret 3 12)
    (place-fret 2 13)
)

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <c' ef g>1^\diagA
  <ef g c>1^\diagB
  <g c ef>1^\diagC 
  <g, c ef>1^\diagD 
      \set TabStaff.minimumFret = #8
  <c ef g>1^\diagE 
       \set TabStaff.minimumFret = #12
  <ef g c>1^\diagF
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
