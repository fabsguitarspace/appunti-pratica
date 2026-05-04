\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
  a8\6-1\downbow as8-2\6\upbow b8-3\6\downbow c8-4\6\upbow
  cs8\5-1 d8-2\5 ds8-3\5 e8-4\5
  f8\4-1 fs8-2\4 g8-3\4 gs8-4\4
  a8-1\3 as8-2\3 b8-3\3 c8-4\3
  cs8-1\2 d8-2\2 ds8-3\2 e8-4\2
  f8-1\1 fs8-2 g8-3 gs8-4
  a8-4\1 af8-3 g8-2 gf8-1
  f8-4\2 e8-3\2 ef8-2 d8-1
  df8-4\3 c8-3\3 b8-2\3 bf8-1
  a8-4\4 af8-3\4 g8-2\4 gf8-1
  f8-4\5 e8-3\5 ef8-2\5 d8-1\5
  df8-4\6 c8-3\6 b8-2\6 bf8-1\6
  
  \bar ":|."
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
  system-count = 3
  
   \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
}
  \midi {}
}