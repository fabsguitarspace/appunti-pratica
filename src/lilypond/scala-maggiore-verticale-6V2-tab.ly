\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c {      
    \set TabStaff.restrainOpenStrings = ##t
   \set TabStaff.minimumFret = #7
  c8\downbow d\upbow 
  e\downbow f\upbow g\downbow 
  a\downbow b\upbow c\downbow 
  d\downbow e\upbow f\downbow 
  g\downbow a\upbow 
  b\downbow c\upbow b\downbow 
  a\downbow g\upbow 
  f\downbow e\upbow d\downbow
  c\downbow b\upbow a\downbow 
  g\downbow f\upbow e\downbow 
  d\downbow c2\upbow
  

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
  system-count = 2
  
   \context {
    \Score
    \omit Staff.TimeSignature
    \remove "Bar_number_engraver"
  }
}
  \midi {}
}