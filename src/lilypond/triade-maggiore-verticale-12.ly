\version "2.24.4"
\language "english"
\header {
	tagline = ##f
	indent = 0
}


musica = \relative c' {
\omit Staff.TimeSignature
\set Staff.printKeyCancellation = ##f
\set Staff.explicitKeySignatureVisibility = #end-of-line-invisible
  \set TabStaff.restrainOpenStrings = ##t
  \set TabStaff.minimumFret = #2   
c,4 e g e 
c4 e g e c1
\key f \major
f4 a c a 
f4 a c a f1

\break


\key bf \major
bf4 d f d 
bf4 d f d bf1

\key ef \major
ef4 g bf g 
ef4 g bf g ef1

\break

\key af \major
af,4 c ef c 
af4 c ef c af1

\key df \major
df,4 f af f 
df4 f af f df1

\break

\key fs \major
fs4 as cs as 
fs4 as cs as fs1



\key b \major
b4 ds fs ds 
b4 ds fs ds b1

\break

\key e \major
e4 gs b gs 
e4 gs b gs e1

\key a \major
a,4 cs e cs 
a4 cs e cs a1

\break

\key d \major
d,4 fs a fs 
d4 fs a fs d1


\key g \major
g4 b d b 
g4 b d b g1

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