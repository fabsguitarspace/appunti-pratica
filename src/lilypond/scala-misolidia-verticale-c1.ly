\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {    
    \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #8
  c4-1 d e f g a bf c c bf a g f e d c
  \break
  \set TabStaff.minimumFret = #7
  c4-2 d e f g a bf c c bf a g f e d c
    \break
  \set TabStaff.minimumFret = #4
  c4-4 d e f g a bf c c bf a g f e d c
    \break
  \set TabStaff.minimumFret = #3
  c4-1 d e f g a bf c c bf a g f e d c
    \break
  \set TabStaff.minimumFret = #2
  c4-2 d e f g a bf c c bf a g f e d c
    \break
  \set TabStaff.minimumFret = #0
  c4-4 d e f g a bf c c bf a g f e d c
  

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