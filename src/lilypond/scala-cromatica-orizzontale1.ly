\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  e4\downbow-0 f4\downbow-1 fs4\downbow-2 g4\downbow-3 gs4-4 a4-1 as4-2 b4-3 c4-4 cs4-1 d4-2 ds4-3 e4-4
  e4-4 ef4-3 d4-2 df4-1 c4-4 b4-3 bf4-2 a4-1 af4-4 g4-3 gf4-2 f4-1 e4-0
  
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