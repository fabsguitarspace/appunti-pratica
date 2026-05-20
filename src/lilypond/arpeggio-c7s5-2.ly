\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {    
    \set TabStaff.restrainOpenStrings = ##t
   \set TabStaff.minimumFret = #10
 c'4-1 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #9
  c4-2 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #7
  c4-4 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #5
  c4-1 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #3
  c4-3 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #1
  c4-1 e gs bf c bf gs e c1
  \break
  \set TabStaff.minimumFret = #0
  c4-2 e gs bf c bf gs e c1
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