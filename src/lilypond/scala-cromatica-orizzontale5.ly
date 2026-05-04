\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {
       \omit Staff.TimeSignature
       \cadenzaOn
       
  a4\downbow as4\downbow b4\downbow c4\downbow cs4 d4 ds4 e4 f4 fs4 g4 gs4 a4
  a4 af4 g4 gf4 f4 e4 ef4 d4 df4 c4 b4 bf4 a4
  
}



\score {
  <<
 
\new Staff {
    \clef "treble_8"
    \musica
  }
  \new TabStaff {
    \relative c {
      a4\5 as4\5 b4\5 c4\5 cs4\5 d4\5 ds4\5 e4\5 f4\5 fs4\5 g4\5 gs4\5 a4\5
      a4\5 af4\5 g4\5 gf4\5 f4\5 e4\5 ef4\5 d4\5 df4\5 c4\5 b4\5 bf4\5 a4\5
    }
  }
  
  >>
\layout { }
  \midi {}
}