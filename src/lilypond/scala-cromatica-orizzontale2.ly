\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  b4\downbow c4\downbow cs4\downbow d4\downbow ds4 e4 f4 fs4 g4 gs4 a4 as4 b4
  b4 bf4 a4 af4 g4 gf4 f4 e4 ef4 d4 df4 c4 b4
  
}



\score {
  <<
 
\new Staff {
    \clef "treble_8"
    \musica
  }
  \new TabStaff {
\relative c' {
  b4 c4 cs4 d4 ds4 e4\2 f4\2 fs4\2 g4\2 gs4\2 a4\2 as4\2 b4\2
  b4\2 bf4\2 a4\2 af4\2 g4\2 gf4\2 f4\2 e4\2 ef4\2 d4\2 df4\2 c4\2 b4\2
}
  }
  >>
\layout { }
  \midi {}
}