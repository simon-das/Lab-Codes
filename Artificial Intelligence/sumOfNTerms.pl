ssum(0, _, _, 0):-!.
ssum(N, I, F, S) :- N1 is N-1, ssum(N1, I, F, S1), S is S1+F+(N-1) * I.
