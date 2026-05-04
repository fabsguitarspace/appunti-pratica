\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
  f,4\6-1 fs4-1 g4-2 gs4-3 a4\6-4 
  as4\5-1 b4-1 c4-2 cs4-3 d4\5-4 
  ds4\4-1 e4-1 f4-2 fs4-3 g4\4-4 
  gs4\3-1 a4-2 as4-3 b4\3-4 
  c4\2-1 cs4-1 d4-2 ds4-3 e4\2-4 
  f4\1-1 fs4-1 g4-2 gs4-3 a4-4
  af4-3 g4-1 gf4-1 f4-1 
  e4\2-4 ef4-3 d4-2 df4-1 c4-1 
  b4\3-4 bf4-3 a4-2 af4-1 
  g4\4-4 gf4-3 f4-2 e4-1 ef4-1 
  d4\5-4 df4-3 c4-2 b4-1 bf4-1 
  a4\6-4 af4-3 g4-2 gf4-1 f1-1
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
\layout { 
  indent = 0
  system-count = 4
  
   \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
}
  \midi {}
}