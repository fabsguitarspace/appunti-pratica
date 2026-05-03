\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  d4\downbow ds4\downbow e4\downbow f4\downbow fs4 g4 gs4 a4 as4 b4 c4 cs4 d4
  d4 df4 c4 b4 bf4 a4 af4 g4 gf4 f4 e4 ef4 d4
  
}



\score {
  <<
 
\new Staff {
    \clef "treble_8"
    \musica
  }
  \new TabStaff {
\relative c {
  d4\4 ds4\4 e4\4 f4\4 fs4\4 g4\4 gs4\4 a4\4 as4\4 b4\4 c4\4 cs4\4 d4\4
  d4\4 df4\4 c4\4 b4\4 bf4\4 a4\4 af4\4 g4\4 gf4\4 f4\4 e4\4 ef4\4 d4\4
}
  }
  >>
\layout { }
  \midi {}
}