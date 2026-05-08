\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
     \key g \major
  e'4\1 fs g a b c d e fs g
  g fs e d c b a g fs e
  
  b\2 c d 
  \set TabStaff.minimumFret = #5
  \set TabStaff.restrainOpenStrings = ##t
  e fs g 
  \set TabStaff.minimumFret = #8
  a b 
  \set TabStaff.minimumFret = #12
  c d d c b 
  \set TabStaff.minimumFret = #8
  a g 
    \set TabStaff.minimumFret = #5

  fs e 
    \set TabStaff.minimumFret = #0
  d c b
  
  g\3 a 
    \set TabStaff.minimumFret = #3
  b c 
    \set TabStaff.minimumFret = #6
  d e 
      \set TabStaff.minimumFret = #9
  fs g 
        \set TabStaff.minimumFret = #14
  a b b
  
  a
  \set TabStaff.minimumFret = #9
  g 
   
  fs e 
    \set TabStaff.minimumFret = #5

  d c 
   \set TabStaff.minimumFret = #2
  b a 
      \set TabStaff.minimumFret = #0
  g
  
  d\4 e 
    \set TabStaff.minimumFret = #3
  fs g 
    \set TabStaff.minimumFret = #6
  a b 
      \set TabStaff.minimumFret = #9
  c d 
        \set TabStaff.minimumFret = #14
  e fs fs
  
  e
  \set TabStaff.minimumFret = #9
  d 
   
  c b 
    \set TabStaff.minimumFret = #5

  a g 
   \set TabStaff.minimumFret = #2
  fs e 
      \set TabStaff.minimumFret = #0
  d


  a\5 b 
    \set TabStaff.minimumFret = #3
  c d 
    \set TabStaff.minimumFret = #6
  e fs 
      \set TabStaff.minimumFret = #9
  g a 
        \set TabStaff.minimumFret = #14
  b c c
  
  b
  \set TabStaff.minimumFret = #9
  a 
   
  g  
    \set TabStaff.minimumFret = #5
fs
  e d 
   \set TabStaff.minimumFret = #2
  c b 
      \set TabStaff.minimumFret = #0
  a



  e\6 fs 
    \set TabStaff.minimumFret = #3
  g a 
    \set TabStaff.minimumFret = #6
  b c 
      \set TabStaff.minimumFret = #9
  d e 
        \set TabStaff.minimumFret = #12
  fs g g
  
  fs
  \set TabStaff.minimumFret = #9
  e 
   
  d  
    \set TabStaff.minimumFret = #5
c
  b a 
   \set TabStaff.minimumFret = #1
  g fs 
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