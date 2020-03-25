bangladeshi('Rahim'). bangladeshi('Karim'). bangladeshi('Rakib'). bangladeshi('Hasib'). bangladeshi('Sohel'). bangladeshi('Rashid').
weapon('Missile'). weapon('Gun'). weapon('Swords'). weapon('Fighting knife'). weapon('Bomb'). weapon('Grenade').
enemy('Jack', 'Bangladesh'). enemy('Sparrow', 'Bangladesh'). enemy('John', 'India'). enemy('Hobs', 'Bangladesh'). enemy('Shaw', 'Bangladesh'). enemy('Ron', 'Canada'). enemy('Mack', 'Bangladesh').
sell('Karim', 'Cold drink', 'Shaw'). sell('Rakib', 'Grenade', 'Sparrow'). sell('Sohel', 'Bomb', 'Jack'). sell('Rahim', 'Paper', 'John'). sell('Rashid', 'Gun', 'Mack'). sell('Karim', 'Water', 'Hobs'). sell('Hasib', 'Swords', 'Ron').

criminal(X) :- bangladeshi(X), weapon(Y), enemy(Z, 'Bangladesh'), sell(X, Y, Z).
