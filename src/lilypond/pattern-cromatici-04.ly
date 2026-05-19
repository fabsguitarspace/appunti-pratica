\version "2.24.0"

\language "english"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 

    c'8 bf b a
    bf af a g
    af gf g f
    gf e f ef
    e d ef df
    d c df b
       
   s1^\markup { "ETC..." }
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}