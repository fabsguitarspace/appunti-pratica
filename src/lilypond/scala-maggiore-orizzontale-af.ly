\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
   \key af \major
  \set TabStaff.restrainOpenStrings = ##t
  f'4\1 g af bf c df ef f g af
  af g f ef df c bf af g f
  
   c\2 d 
  \set TabStaff.minimumFret = #4
  ef f g 
  \set TabStaff.minimumFret = #8
  af bf 
  \set TabStaff.minimumFret = #12
  c df 
  \set TabStaff.minimumFret = #13
  ef ef df c
   \set TabStaff.minimumFret = #11
  bf 
  \set TabStaff.minimumFret = #8
  af g 
    \set TabStaff.minimumFret = #4
  f ef 
    \set TabStaff.minimumFret = #0
  df c
  
  g\3 af 
    \set TabStaff.minimumFret = #3
  bf c 
    \set TabStaff.minimumFret = #6
  df ef 
      \set TabStaff.minimumFret = #9
  f g 
        
          \set TabStaff.minimumFret = #10
  af 
  \set TabStaff.minimumFret = #14
  bf bf
  \set TabStaff.minimumFret = #10
  af
  
  g 
   
  f 
    \set TabStaff.minimumFret = #5
ef 
  df c 
   \set TabStaff.minimumFret = #2
  bf 
      \set TabStaff.minimumFret = #0
      af 
  g
  
  ef\4 
    \set TabStaff.minimumFret = #3
  f g 
    \set TabStaff.minimumFret = #6
  af bf 
      \set TabStaff.minimumFret = #9
  c df ef 
        \set TabStaff.minimumFret = #14
  f g g f
  
 
  \set TabStaff.minimumFret = #9
   ef
  df 
    \set TabStaff.minimumFret = #7
  c bf 
    \set TabStaff.minimumFret = #5

  af g 
   \set TabStaff.minimumFret = #2
  f 
      \set TabStaff.minimumFret = #0
      ef 



 bf\5 
    \set TabStaff.minimumFret = #3
  c df
    \set TabStaff.minimumFret = #6
  ef f 
      \set TabStaff.minimumFret = #9
  g af 
        \set TabStaff.minimumFret = #12
  bf c 
  \set TabStaff.minimumFret = #14
  df df 
  \set TabStaff.minimumFret = #12
  c
  
  bf
  \set TabStaff.minimumFret = #9
  af 
   
  g  
    \set TabStaff.minimumFret = #5
f
  ef df 
   \set TabStaff.minimumFret = #1
  c bf 
      \set TabStaff.minimumFret = #0
 



   f\6 
    \set TabStaff.minimumFret = #3
  g af 
    \set TabStaff.minimumFret = #6
  bf c 
      \set TabStaff.minimumFret = #9
  df ef 
        \set TabStaff.minimumFret = #12
  f g 
  \set TabStaff.minimumFret = #15
  af af 
  \set TabStaff.minimumFret = #12
  g
  
  f
  \set TabStaff.minimumFret = #9
  ef 
   
  df  
    \set TabStaff.minimumFret = #5
c
\set TabStaff.minimumFret = #3
  bf af 
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