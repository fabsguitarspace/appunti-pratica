\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {    
    \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #8
  c4-1 d ef f gf af a b c b a af gf f ef d
  \break
  \set TabStaff.minimumFret = #4
  c4-4 d ef f gf af a b c b a af gf f ef d
    \break
  \set TabStaff.minimumFret = #3
  c4-1 d ef f gf af a b c b a af gf f ef d
    \break
  \set TabStaff.minimumFret = #0
  c4-4 d ef f gf af a b c b a af gf f ef d
  

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
  
   \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
}
  \midi {}
}