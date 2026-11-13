\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #10
  c'4-1 ef f gf g bf c bf g gf f ef c r r r
  \break
  \set TabStaff.minimumFret = #7
  c4-4 ef f gf g bf c bf g gf f ef c r r r
  \break
  \set TabStaff.minimumFret = #5
  c4-1 ef f gf g bf c bf g gf f ef c r r r
  \break
  \set TabStaff.minimumFret = #3
  c4-3 ef f gf g bf c bf g gf f ef c r r r
  \break
  \set TabStaff.minimumFret = #1
  c4-1 ef f gf g bf c bf g gf f ef c r r r
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