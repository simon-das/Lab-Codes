parent('Hasib', 'Rakib'). parent('Rakib', 'Sohel'). parent('Rakib', 'Rebeka'). parent('Rashid', 'Hasib'). grandparent(X,Z) :- parent(X, Y), parent(Y, Z).
findGp :- write('Grandchildren : '), read(X), write('Grandparent : '),
	grandparent(Gp, X), write(Gp), tab(5), fail.
findGp.
