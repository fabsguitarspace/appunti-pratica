\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #10
  c'8-1 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #9
  c8-2 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #7
  c8-4 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #5
  c8-1 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #3
  c8-3 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #1
  c8-1 d e f g a bf b c b bf a g f e d c2 r
  \break
  \set TabStaff.minimumFret = #0
  c8-2 d e f g a bf b c b bf a g f e d c2 r
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