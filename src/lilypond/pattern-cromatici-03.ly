\version "2.24.0"

\language "english"

\header {
	tagline = ##f
	indent = 0
}

\score {
  \relative c' { 

    c8 d cs ds
    d e ds f
    e fs f g
    fs gs g a
    gs as a b
    as c b cs
       
   s1^\markup { "ETC..." }
  \bar "||"
  }
  \layout { 
      \omit Staff.TimeSignature

      indent = 0
  }
  \midi { }
}