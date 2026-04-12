\version "2.24.0"

\paper {
  indent = 0
  ragged-last = ##f
  ragged-bottom = ##f
  system-count = 3

  % Dimensioni pagina
  paper-width  = 210\mm
  paper-height = 160\mm
  top-margin   = 10\mm
  bottom-margin = 10\mm
  left-margin  = 12\mm
  right-margin = 12\mm
  between-system-space = 8\mm
  system-system-spacing.basic-distance = 18
}

\layout {
  \context {
    \Score
    \remove "Bar_number_engraver"
    defaultBarType = ""
  }
}

music = \relative c' {
  \time 4/4
  \clef treble
  \key a \major

  % 12 battute vuote, distribuite in 3 righe da 4
  \repeat unfold 12 { s1 \bar "|" }
  \bar "|."
}

\score {
  \new Staff {
    \music
  }
}
