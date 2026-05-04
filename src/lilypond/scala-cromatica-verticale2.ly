\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
    \set TabStaff.restrainOpenStrings = ##t

  f,4\6-1 fs4-2 g4-3 gs4-4 
   \set TabStaff.minimumFret = #3
  a4-4 
   \set TabStaff.minimumFret = #1
  as4\5-1 b4-2 c4-3 cs4-4 
  \set TabStaff.minimumFret = #3

  d4-4 
  \set TabStaff.minimumFret = #1
  ds4\4-1 e4-2 f4-3 fs4-4 
  \set TabStaff.minimumFret = #3
  g4-4 
  \set TabStaff.minimumFret = #1
  gs4\3-1 a4-2 as4-3 b4-4 
  c4\2-1 cs4-2 d4-3 ds4-4 e4-4 
  f4\1-1 fs4-2 g4-3 gs4-4 a4-4
  af4-4 g4-3 gf4-2 f4-1 
  e4\2-4 ef4-4 d4-3 df4-2 c4-1 
  b4\3-4 bf4-3 a4-2 af4-1 
  g4\4-4 gf4-4 f4-3 e4-2 ef4-1 
  d4\5-4 df4-4 c4-3 b4-2 bf4-1 
  a4\6-4 af4-4 g4-3 gf4-2 f1-1
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