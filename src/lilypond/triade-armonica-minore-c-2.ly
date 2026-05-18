\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 5 6)
    (place-fret 4 5)
    (place-fret 3 5)
)


diagB    = \markup  \scale #'(1.5 . 1.5)
\fret-diagram-verbose #'(
    (place-fret 5 10)
    (place-fret 4 10)
    (place-fret 3 8)
)

diagC    = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 5 15)
    (place-fret 4 13)
    (place-fret 3 12)
)


diagD   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 6 3)
    (place-fret 5 3)
    (place-fret 4 1)
)


diagE   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 6 8)
    (place-fret 5 6)
    (place-fret 4 5)
)

diagF   = \markup \scale #'(1.5 . 1.5) 
\fret-diagram-verbose #'(
    (place-fret 6 11)
    (place-fret 5 10)
    (place-fret 4 10)
)

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
    \set TabStaff.minimumFret = #2
  <ef g c>1^\diagA
        \set TabStaff.minimumFret = #8
  <g c ef>1^\diagB
         \set TabStaff.minimumFret = #12
  <c ef g>1^\diagC 
          \set TabStaff.minimumFret = #1
  <g, c ef>1^\diagD 

  <c ef g>1^\diagE 
      \set TabStaff.minimumFret = #10
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
