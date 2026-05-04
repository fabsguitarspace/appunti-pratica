\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {    
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #5   
  a8\6-1\downbow as8-2\upbow b8-3\downbow c8-4\upbow
  \set TabStaff.minimumFret = #4   
  cs8\5-1 d8-2 ds8-3 e8-4
    \set TabStaff.minimumFret = #3
  f8\4-1 fs8-2 g8-3 gs8-4
  \set TabStaff.minimumFret = #2
  a8-1\3 as8-2 b8-3 c8-4
  \set TabStaff.minimumFret = #2
  cs8-1\2 d8-2 ds8-3 e8-4
  \set TabStaff.minimumFret = #1
  f8-1\1 fs8-2 g8-3 gs8-4
  \set TabStaff.minimumFret = #2
  a8-4\1 af8-3 g8-2 gf8-1
  \set TabStaff.minimumFret = #3
  f8-4\2 e8-3 ef8-2 d8-1
  \set TabStaff.minimumFret = #3
  df8-4\3 c8-3 b8-2 bf8-1
  \set TabStaff.minimumFret = #4
  a8-4\4 af8-3 g8-2 gf8-1
  \set TabStaff.minimumFret = #5
  f8-4\5 e8-3 ef8-2 d8-1
  \set TabStaff.minimumFret = #6
  df8-4\6 c8-3 b8-2 bf8-1
  
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