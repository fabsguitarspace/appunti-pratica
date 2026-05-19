\version "2.24.0"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 
  
    c'8 b a g
    b a g f
    a g f e
    g f e d
    f e d c
    e d c b
    d c b a
    c2
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}