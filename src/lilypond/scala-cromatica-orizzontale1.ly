\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
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
    \musica
  }
  >>
\layout { }
  \midi {}
}