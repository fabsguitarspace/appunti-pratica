\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
   \key bf \major
  \set TabStaff.restrainOpenStrings = ##t
  f'4\1 g a bf c d ef f g a
  a g f ef d c bf a g f
  
   c\2 d 
  \set TabStaff.minimumFret = #4
  ef f g 
  \set TabStaff.minimumFret = #8
  a bf 
  \set TabStaff.minimumFret = #12
  c d 
  \set TabStaff.minimumFret = #13
  ef ef d c
   \set TabStaff.minimumFret = #11
  bf 
  \set TabStaff.minimumFret = #8
  a g 
    \set TabStaff.minimumFret = #4
  f ef 
    \set TabStaff.minimumFret = #0
  d c
  
  g\3 a 
    \set TabStaff.minimumFret = #3
  bf c 
    \set TabStaff.minimumFret = #6
  d ef 
      \set TabStaff.minimumFret = #9
  f g 
        \set TabStaff.minimumFret = #14
  a bf bf
  
  a
  \set TabStaff.minimumFret = #10
  g 
   
  f 
    \set TabStaff.minimumFret = #5
ef 
  d c 
   \set TabStaff.minimumFret = #2
  bf a 
      \set TabStaff.minimumFret = #0
  g
  
  d\4 ef 
    \set TabStaff.minimumFret = #3
  f g 
    \set TabStaff.minimumFret = #6
  a bf 
      \set TabStaff.minimumFret = #9
  c d ef 
        \set TabStaff.minimumFret = #14
  f f
  
 
  \set TabStaff.minimumFret = #9
   ef
  d 
    \set TabStaff.minimumFret = #7
  c bf 
    \set TabStaff.minimumFret = #5

  a g 
   \set TabStaff.minimumFret = #2
  f 
      \set TabStaff.minimumFret = #0
      ef 
  d


  a\5 bf 
    \set TabStaff.minimumFret = #3
  c d 
    \set TabStaff.minimumFret = #6
  ef f 
      \set TabStaff.minimumFret = #9
  g a 
        \set TabStaff.minimumFret = #12
  bf c c
  
  bf
  \set TabStaff.minimumFret = #9
  a 
   
  g  
    \set TabStaff.minimumFret = #5
f
  ef d 
   \set TabStaff.minimumFret = #1
  c bf 
      \set TabStaff.minimumFret = #0
  a



   f\6 
    \set TabStaff.minimumFret = #3
  g a 
    \set TabStaff.minimumFret = #6
  bf c 
      \set TabStaff.minimumFret = #9
  d ef 
        \set TabStaff.minimumFret = #12
  f g 
  \set TabStaff.minimumFret = #15
  a a 
  \set TabStaff.minimumFret = #12
  g
  
  f
  \set TabStaff.minimumFret = #9
  ef 
   
  d  
    \set TabStaff.minimumFret = #5
c
  bf a 
   \set TabStaff.minimumFret = #1
  g f 
  



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