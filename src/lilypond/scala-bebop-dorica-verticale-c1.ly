\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #8
  c8-1 d ef e f g a bf c bf a g f e ef d c2 r
  \break
  \set TabStaff.minimumFret = #7
  c8-2 d ef e f g a bf c bf a g f e ef d c2 r
  \break
  \set TabStaff.minimumFret = #4
  c8-4 d ef e f g a bf c bf a g f e ef d c2 r
  \break
  \set TabStaff.minimumFret = #3
  c8-1 d ef e f g a bf c bf a g f e ef d c2 r
  \break
  \set TabStaff.minimumFret = #2
  c8-2 d ef e f g a bf c bf a g f e ef d c2 r
  \break
  \set TabStaff.minimumFret = #0
  c8-4 d ef e f g a bf c bf a g f e ef d c2 r
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