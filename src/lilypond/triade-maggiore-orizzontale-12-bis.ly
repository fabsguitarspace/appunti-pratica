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

e g c g e1
\key f \major

f4 a c a f1


\key bf \major
f4 bf d bf f1

\break

\key ef \major
g4 bf ef bf g1


\key af \major
af4 c ef c af1

\key df \major
f4 af df af f1

\break

\key fs \major
fs4 as cs as fs1


\key b \major
fs4 b ds b fs1

\key e \major
e4 gs b gs e1

\break

\key a \major
e4 a cs a e1


\key d \major
fs4 a d a fs1


\key g \major
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