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

g' c ef c g1
\key f \minor

f4 af c af f1


\key bf \minor
f4 bf df bf f1

\break

\key ef \minor
gf4 bf ef bf gf1


\key gs \minor
gs4 b ds b gs1

\key cs \minor
e4 gs cs gs e1

\break

\key fs \minor
fs4 a cs a fs1


\key b \minor
fs4 b d b fs1

\key e \minor
e4 g b g e1

\break

\key a \minor
e4 a c a e1


\key d \minor
f4 a d a f1


\key g \minor
g4 bf d bf g1

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