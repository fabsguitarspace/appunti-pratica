\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
  e,4\6-0 f4-1 fs4-2 g4-3 gs4-4 
  a4\5-0 as4-1 b4-2 c4-3 cs4-4 
  d4\4-0 ds4-1 e4-2 f4-3 fs4-4
  g4\3-0 gs4-1 a4-2 as4-3
  b4\2-0 c4-1 cs4-2 d4-3 ds4-4
  e4\1-0 f4-1 fs4-2 g4-3 gs4-4
  g4-3 gf4-2 f4-1 e4-0
  ef4\2-4 d4-3 df4-2 c4-1 b4-0
  bf4\3-3 a4-2 af4-1 g4-0
  gf4\4-4 f4-3 e4-2 ef4-1 d4-0
  df4\5-4 c4-3 b4-2 bf4-1 a4-0
  af4\6-4 g4-3 gf4-2 f4-1 e1-0
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