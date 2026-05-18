\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
     \key c \minor
       \omit Staff.TimeSignature
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #8   
c,4-1 ef g ef c1
  \set TabStaff.minimumFret = #6   
c4-2 ef g ef c1
  \set TabStaff.minimumFret = #6   
c4-3 ef g ef c1
  \set TabStaff.minimumFret = #5   
c4-4 ef g ef c1
\break
  \set TabStaff.minimumFret = #3   
c4-1 ef g ef c1

  \set TabStaff.minimumFret = #1  
c4-2 ef g ef c1

  \set TabStaff.minimumFret = #1  
c4-3 ef g ef c1


  \set TabStaff.minimumFret = #0  
c4-4 ef g ef c1

\break

  \set TabStaff.minimumFret = #10   
c'4-1 ef g ef c1

  \set TabStaff.minimumFret = #8  
c4-2 ef 
  \set TabStaff.minimumFret = #9 
g 
  \set TabStaff.minimumFret = #8 
ef c1


  \set TabStaff.minimumFret = #8  
c4-3 ef g ef c1

  \set TabStaff.minimumFret = #6  
c4-4 ef g ef c1

\break

  \set TabStaff.minimumFret = #5   
c4-1 ef g ef c1

  \set TabStaff.minimumFret = #4  
c4-2 ef 
  \set TabStaff.minimumFret = #5  
g 
  \set TabStaff.minimumFret = #4  
  ef c1


  \set TabStaff.minimumFret = #3  
c4-3 ef g ef c1

  \set TabStaff.minimumFret = #3  
c4-4 ef g ef c1

\break

  \set TabStaff.minimumFret = #13   
c'4-1 ef g ef c1

  \set TabStaff.minimumFret = #11  
c4-2 ef g ef c1

c4-3 ef g ef c1

c4-4 ef g ef c1

\bar "||"

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
}
  \midi {}
}