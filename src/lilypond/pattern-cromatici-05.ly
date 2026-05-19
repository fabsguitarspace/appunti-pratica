\version "2.24.0"

\language "english"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 

    c8 d ef df
    d e f ef
    e fs g f
    fs gs a g
    gs as b a
    as c df b
       
   s1^\markup { "ETC..." }
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}