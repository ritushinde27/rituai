male(omprakash).
male(rakesh).
male(subodh).
male(sanjeev).
male(alok).
male(kairav).

female(omvati).
female(savita).
female(dipti).
female(nishi).
female(shobhna).
female(parul).
female(anu).
female(rekha).

parent(omprakash,omvati,rakesh).
parent(omprakash,omvati,subodh).
parent(rakesh,savita,alok).
parent(rakesh,savita,anu).
parent(alok,parul,kairav).
parent(subodh,dipti,harshit).

brother(rakesh,subodh).
brother(subodh,rakesh).
brother(alok,harshit).
brother(harshit,alok).
brother(sanjeev,savita).

sister(shobhna,rakesh).
sister(anu,alok).
sister(anu,harshit).
sister(savita,rekha).
sister(rekha,savita).
sister(savita,sanjeev).

father(X,Y) :- parent(X,Z,Y).
mother(X,Y) :- parent(Z,X,Y).

son(X,Y,Z) :- male(X),father(Y,X),mother(Z,X).
daughter(X,Y,Z) :- female(X),father(Y,X),mother(Z,X).

wife(X,Y) :- female(X),parent(Y,X,Z).

uncle(X,Y) :- male(X),brother(X,Z),father(Z,Y).

aunt(X,Y) :- wife(X,Z),uncle(Z,Y).

chacha(X,Y) :- male(X),brother(X,Z),father(Z,Y).

mama(X,Y) :- male(X),brother(X,Z),mother(Z,Y).

fufi(X,Y) :- female(X),sister(X,Z),father(Z,Y).

maasi(X,Y) :- female(X),sister(X,Z),mother(Z,Y).