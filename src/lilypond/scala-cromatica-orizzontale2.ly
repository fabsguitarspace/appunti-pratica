\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  b4\downbow-0 c4\downbow-1 cs4\downbow-2 d4\downbow-3 ds4-4 
  e4-1 f4-2 fs4-3 g4-4 
  gs4-1 a4-2 as4-3 b4-4
  b4-4 bf4-3 a4-2 af4-1 
  g4-4 gf4-3 f4-2 e4-1 
  ef4-4 d4-3 df4-2 c4-1 b4-0
  
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