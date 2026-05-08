\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
   \key df \major
  \set TabStaff.restrainOpenStrings = ##t
  f'4\1 gf af bf c df ef f gf af
  af gf f ef df c bf af gf f
  
   c\2 df 
  \set TabStaff.minimumFret = #4
  ef f gf 
  \set TabStaff.minimumFret = #8
  af bf 
  \set TabStaff.minimumFret = #12
  c df 
  \set TabStaff.minimumFret = #13
  ef ef df c
   \set TabStaff.minimumFret = #11
  bf 
  \set TabStaff.minimumFret = #8
  af 
    \set TabStaff.minimumFret = #4
    gf 
  f ef 
    \set TabStaff.minimumFret = #0
  df c
  
  af\3 
    \set TabStaff.minimumFret = #3
  bf c 
    \set TabStaff.minimumFret = #6
  df ef 
      \set TabStaff.minimumFret = #9
  f gf 
        
          \set TabStaff.minimumFret = #10
  af 
  \set TabStaff.minimumFret = #14
  bf 
  c c
  bf
  \set TabStaff.minimumFret = #10
  af
  
  gf 
   
  f 
    \set TabStaff.minimumFret = #5
ef 
  df c 
   \set TabStaff.minimumFret = #2
  bf 
      \set TabStaff.minimumFret = #0
      af 
  
  
  ef\4 
    \set TabStaff.minimumFret = #3
  f gf 
    \set TabStaff.minimumFret = #6
  af bf 
      \set TabStaff.minimumFret = #9
  c df ef 
        \set TabStaff.minimumFret = #14
  f gf gf f
  
 
  \set TabStaff.minimumFret = #9
   ef
  df 
    \set TabStaff.minimumFret = #7
  c bf 
    \set TabStaff.minimumFret = #5

  af 
   \set TabStaff.minimumFret = #2
   gf 
  f 
      \set TabStaff.minimumFret = #0
      ef 



 bf\5 
    \set TabStaff.minimumFret = #3
  c df
    \set TabStaff.minimumFret = #6
  ef f 
      \set TabStaff.minimumFret = #9
  gf af 
        \set TabStaff.minimumFret = #12
  bf c 
  \set TabStaff.minimumFret = #14
  df df 
  \set TabStaff.minimumFret = #12
  c
  
  bf
  \set TabStaff.minimumFret = #9
  af 
   
  gf  
    \set TabStaff.minimumFret = #5
f
  ef 
   \set TabStaff.minimumFret = #1
   df 
  c bf 
      \set TabStaff.minimumFret = #0
 



   f\6 
   
  gf 
   \set TabStaff.minimumFret = #3
   af 
    \set TabStaff.minimumFret = #6
  bf c 
      \set TabStaff.minimumFret = #9
  df ef 
        \set TabStaff.minimumFret = #12
  f gf 
  \set TabStaff.minimumFret = #15
  af af 
  \set TabStaff.minimumFret = #12
  gf
  
  f
  \set TabStaff.minimumFret = #9
  ef 
   
  df  
    \set TabStaff.minimumFret = #5
c
\set TabStaff.minimumFret = #3
  bf af 
   \set TabStaff.minimumFret = #1
  gf f 
  



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