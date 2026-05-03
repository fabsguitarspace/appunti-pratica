\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  g4\downbow gs4\downbow a4\downbow as4\downbow b4 c4 cs4 d4 ds4 e4 f4 fs4 g4
  g4 gf4 f4 e4 ef4 d4 df4 c4 b4 bf4 a4 af4 g4
  
}



\score {
  <<
 
\new Staff {
    \clef "treble_8"
    \musica
  }
  \new TabStaff {
\relative c' {
  g4 gs4 a4 as4 b4\3 c4\3 cs4\3 d4\3 ds4\3 e4\3 f4\3 fs4\3 g4\3
  g4\3 gf4\3 f4\3 e4\3 ef4\3 d4\3 df4\3 c4\3 b4\3 bf4\3 a4\3 af4\3 g4\3
}
  }
  >>
\layout { }
  \midi {}
}