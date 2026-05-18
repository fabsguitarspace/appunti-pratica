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
\key c \minor
c'4 ef g ef c1
\key f \minor
f,4 af c af f1




\key bf \minor
bf4 df f df bf1

\break

\key ef \minor
ef4 gf bf gf ef1



\key gs \minor
gs,4 b ds b gs1

\key cs \minor
cs4 e gs e cs1

\break

\key fs \minor
fs,4 a cs a fs1


\key b \minor
b4 d fs d b1


\key e \minor
e,4 g b g e1

\break

\key a \minor
a4 c e c a1


\key d \minor
d4 f a f   d1


\key g \minor
g,4 bf d bf g1

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