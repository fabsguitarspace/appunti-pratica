\version "2.24.0"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 
  
    c'8 b a g f e d c b
    c d e f g a b c1
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}