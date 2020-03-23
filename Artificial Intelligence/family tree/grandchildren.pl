parent('Hasib', 'Rakib'). parent('Rakib', 'Sohel'). parent('Rakib', 'Rebeka'). parent('Rashid', 'Hasib'). grandparent(X,Z) :- parent(X, Y), parent(Y, Z).
findGc :- write('Grandparent : '), read(X), write('GrandChildren : '),
	grandparent(X, Gc), write(Gc), tab(5), fail.
findGc.
