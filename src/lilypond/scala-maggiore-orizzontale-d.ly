\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {       
     \key d \major
  e'4\1 fs g a b cs d e fs g
  g fs e d cs b a g fs e
  
  b\2 cs d 
  \set TabStaff.minimumFret = #5
  \set TabStaff.restrainOpenStrings = ##t
  e fs g 
  \set TabStaff.minimumFret = #8
  a b 
  \set TabStaff.minimumFret = #12
  cs d d cs b 
  \set TabStaff.minimumFret = #8
  a g 
    \set TabStaff.minimumFret = #5

  fs e 
    \set TabStaff.minimumFret = #0
  d cs b
  
  g\3 a 
    \set TabStaff.minimumFret = #3
  b cs 
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

  d cs 
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
  cs d 
        \set TabStaff.minimumFret = #14
  e fs fs
  
  e
  \set TabStaff.minimumFret = #9
  d 
   
  cs b 
    \set TabStaff.minimumFret = #5

  a g 
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
  g a 
        \set TabStaff.minimumFret = #14
  b cs cs
  
  b
  \set TabStaff.minimumFret = #9
  a 
   
  g  
    \set TabStaff.minimumFret = #5
fs
  e d 
   \set TabStaff.minimumFret = #2
  cs b 
      \set TabStaff.minimumFret = #0
  a



  e\6 fs 
    \set TabStaff.minimumFret = #3
  g a 
    \set TabStaff.minimumFret = #6
  b cs 
      \set TabStaff.minimumFret = #9
  d e 
        \set TabStaff.minimumFret = #12
  fs g g
  
  fs
  \set TabStaff.minimumFret = #9
  e 
   
  d  
    \set TabStaff.minimumFret = #5
cs
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