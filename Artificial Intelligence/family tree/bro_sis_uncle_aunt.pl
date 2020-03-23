parent('Hasib', 'Rakib'). parent('Rakib', 'Sohel'). parent('Hasib', 'Sakib').
parent('Rakib', 'Rebeka'). parent('Rashid', 'Hasib'). parent('Hasib', 'Jarin').
male('Hasib'). male('Rakib'). male('Sohel'). male('Sakib'). male('Rashid'). female('Rebeka'). female('Jarin').
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), (X \= Y).
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), (X \= Y).
uncle(X, Y) :- parent(Z, Y), parent(P, Z), parent(P, X), male(X), (Z \= X).
aunty(X, Y) :- parent(Z, Y), parent(P, Z), parent(P, X), female(X), (Z \= X).
findBro :- write('First Person : '), read(Y), write('Brother : '), brother(Bro, Y),
	write(Bro), tab(5), fail.
findBro.
findSis :- write('First Person : '), read(Y), write('Sister : '), sister(Sis, Y),
	write(Sis), tab(5), fail.
findSis.
findUncle :- write('First Person : '), read(Y), write('Uncle : '), uncle(Unc, Y),
	write(Unc), tab(5), fail.
findUncle.
findAunty :- write('First Person : '), read(Y), write('Aunty : '), aunty(Aun, Y),
	write(Aun), tab(5), fail.
findAunty.



