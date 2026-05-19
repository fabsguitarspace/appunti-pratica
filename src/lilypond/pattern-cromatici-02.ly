\version "2.24.0"

\language "english"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 
  
    c'8 b bf a
    b bf a af
    bf a af g
    a af g gf
    af g gf f
    g gf f e
       
   s1^\markup { "ETC..." }
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}