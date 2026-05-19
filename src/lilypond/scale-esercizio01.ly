\version "2.24.0"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 
  
    c8 d e f g a b c
   d c b a g f e d c1
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}