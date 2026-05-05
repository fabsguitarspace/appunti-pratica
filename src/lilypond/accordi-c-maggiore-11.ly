\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


diagA    = \markup \center-column { "R" 
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 1)
                        )
}
diagB    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 1)
                        )
diagBa    = \markup \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 1)
                        )
diagC    = \markup \center-column { "9" 
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (open 3)
                          (place-fret 2 3)
                          ) }
diagD    = \markup  \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          )
diagDa    = \markup  \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 3)
                          )
diagE    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 3)
                          )
diagEa    = \markup \fret-diagram-verbose #'(
                          (place-fret 6 3)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 3)
                          )
diagF    = \markup \center-column { "3" 
                       \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 2)
                          (place-fret 2 5)
                          ) }

diagFa    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 2)
                          (place-fret 3 4)
                          (place-fret 2 5)
                          )


diagFb    = \markup \fret-diagram-verbose #'(
                          (place-fret 5 3)
                          (place-fret 4 5)
                          (place-fret 3 4)
                          (place-fret 2 5)
                          )

diagG    = \markup \center-column { "♯11" 
                       \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 4 7)
                          (place-fret 3 7)
                          (place-fret 2 7)
                          ) }

diagGa    = \markup \fret-diagram-verbose #'(
                          (place-fret 6 8)
                          (place-fret 4 9)
                          (place-fret 3 9)
                          (place-fret 2 7)
                          )

music = \relative c { 
  \set TabStaff.restrainOpenStrings = ##t
  <c e g c>1^\diagA
  <c e a c>1^\diagB 
  <g e' a c>1^\diagBa 
  <c e g d'>1^\diagC
  \break
  <c e a d>1^\diagD
  <g e' a d>1^\diagDa
  <c e b' d>1^\diagE
  <g e' b' d>1^\diagEa
  \break
    \set TabStaff.minimumFret = #2
  <c e a e'>1^\diagF
  <c e b' e>1^\diagFa
  <c g' b e>1^\diagFb
    \set TabStaff.minimumFret = #5
  <c a' d fs>1^\diagG
    \break
  <c b' e fs>1^\diagGa
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
       \omit Staff.TimeSignature
      \remove "Bar_number_engraver"
      \override RehearsalMark.self-alignment-X = #LEFT
    }
  }
 \midi {}
}
