\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c, {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  e4\downbow f4\downbow fs4\downbow g4\downbow gs4 a4 as4 b4 c4 cs4 d4 ds4 e4
  e4 ef4 d4 df4 c4 b4 bf4 a4 af4 g4 gf4 f4 e4
  
}



\score {
  <<
 
\new Staff {
    \clef "treble_8"
    \musica
  }
  \new TabStaff {
\relative c, {
  e4\6 f4\6 fs4\6 g4\6 gs4\6 a4\6 as4\6 b4\6 c4\6 cs4\6 d4\6 ds4\6 e4\6
  e4\6 ef4\6 d4\6 df4\6 c4\6 b4\6 bf4\6 a4\6 af4\6 g4\6 gf4\6 f4\6 e4\6
}
  }
  >>
\layout { }
  \midi {}
}