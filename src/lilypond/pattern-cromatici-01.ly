\version "2.24.0"

\language "english"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 

    c8 cs d ds
    cs d ds e
    d ds e f
    ds e f fs
    e f fs g
    f fs g gs
       
   s1^\markup { "ETC..." }
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}