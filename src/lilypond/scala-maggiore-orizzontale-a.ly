\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
     \key a \major
  e'4\1 fs gs a b cs d e fs gs
  gs fs e d cs b a gs fs e
  
  b\2 cs d 
  \set TabStaff.minimumFret = #5
  \set TabStaff.restrainOpenStrings = ##t
  e fs gs 
  \set TabStaff.minimumFret = #8
  a b 
  \set TabStaff.minimumFret = #12
  cs d d cs b 
  \set TabStaff.minimumFret = #8
  a gs 
    \set TabStaff.minimumFret = #5

  fs e 
    \set TabStaff.minimumFret = #0
  d cs b
  
  gs\3 a 
    \set TabStaff.minimumFret = #3
  b cs 
    \set TabStaff.minimumFret = #6
  d e 
      \set TabStaff.minimumFret = #8
  fs 
        \set TabStaff.minimumFret = #10
  gs 
        \set TabStaff.minimumFret = #14
  a b b
  
  a
  \set TabStaff.minimumFret = #10
  gs 
   
  fs  
    \set TabStaff.minimumFret = #6
e
  d cs 
   \set TabStaff.minimumFret = #2
  b a 
      \set TabStaff.minimumFret = #0
  gs
  
  d\4 e 
    \set TabStaff.minimumFret = #3
  fs gs 
    \set TabStaff.minimumFret = #6
  a b 
      \set TabStaff.minimumFret = #9
  cs d 
        \set TabStaff.minimumFret = #14
  e fs fs
  
  e
  \set TabStaff.minimumFret = #9
  d 
   
  cs b 
    \set TabStaff.minimumFret = #5

  a gs 
   \set TabStaff.minimumFret = #2
  fs e 
      \set TabStaff.minimumFret = #0
  d


  a\5 b 
    \set TabStaff.minimumFret = #3
  cs d 
    \set TabStaff.minimumFret = #6
  e fs 
      \set TabStaff.minimumFret = #9
  gs a 
        \set TabStaff.minimumFret = #14
  b cs cs
  
  b
  \set TabStaff.minimumFret = #9
  a 
   
  gs  
    \set TabStaff.minimumFret = #5
fs
  e d 
   \set TabStaff.minimumFret = #2
  cs b 
      \set TabStaff.minimumFret = #0
  a



  e\6 fs 
    \set TabStaff.minimumFret = #3
  gs a 
    \set TabStaff.minimumFret = #6
  b cs 
      \set TabStaff.minimumFret = #9
  d e 
        \set TabStaff.minimumFret = #12
  fs gs gs
  
  fs
  \set TabStaff.minimumFret = #9
  e 
   
  d  
    \set TabStaff.minimumFret = #5
cs
  b a 
   \set TabStaff.minimumFret = #1
  gs fs 
      \set TabStaff.minimumFret = #0
  e



  \bar "|."
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
  system-count = 6
  
   \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
}
  \midi {}
}