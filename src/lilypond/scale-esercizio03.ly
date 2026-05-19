\version "2.24.0"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 
  
    c8 d e f 
    d e f g
    e f g a
    f g a b
    g a b c
    a b c d
    b c d e
    c2
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}