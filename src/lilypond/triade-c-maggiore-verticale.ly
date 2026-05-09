\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
       \omit Staff.TimeSignature
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #8   
c,4-1 e g e c1
  \set TabStaff.minimumFret = #7   
c4-2 e g e c1
  \set TabStaff.minimumFret = #5   
c4-3 e g e c1
  \set TabStaff.minimumFret = #5   
c4-4 e g e c1
\break
  \set TabStaff.minimumFret = #3   
c4-1 e g e c1

  \set TabStaff.minimumFret = #2  
c4-2 e g e c1

  \set TabStaff.minimumFret = #0  
c4-3 e g e c1


  \set TabStaff.minimumFret = #0  
c4-4 e g e c1

\break

  \set TabStaff.minimumFret = #10   
c'4-1 e g e c1

  \set TabStaff.minimumFret = #9  
c4-2 e g e c1


  \set TabStaff.minimumFret = #8  
c4-3 e g e c1

  \set TabStaff.minimumFret = #8  
c4-4 e g e c1

\break

  \set TabStaff.minimumFret = #5   
c4-1 e g e c1

  \set TabStaff.minimumFret = #3  
c4-2 e g e c1


  \set TabStaff.minimumFret = #3  
c4-3 e g e c1

  \set TabStaff.minimumFret = #3  
c4-4 e g e c1

\break

  \set TabStaff.minimumFret = #13   
c'4-1 e g e c1

  \set TabStaff.minimumFret = #12  
c4-2 e g e c1

c4-3 e g e c1

c4-4 e g e c1

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