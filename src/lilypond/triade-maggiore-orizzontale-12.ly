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

c'4 e g e c1
\key f \major
f,4 a c a f1




\key bf \major
bf4 d f d bf1

\break

\key ef \major
ef4 g bf g ef1



\key af \major
af,4 c ef c af1

\key df \major
df4 f af f df1

\break

\key fs \major
fs,4 as cs as fs1


\key b \major
b4 ds fs ds b1


\key e \major
e,4 gs b gs e1

\break

\key a \major
a4 cs e cs a1


\key d \major
d4 fs a fs   d1


\key g \major
g,4 b d b g1

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