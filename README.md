# battleship-algorithm

## to use
Just enter `python3 bsMain.py` into the terminal at directory.
It'll give you coordinates of its attacks and ask if they hit or if a ship has been sunk.

## assumptions
* Uses a 10x10 grid. This can be changed, but you'll have to change it every time it's written as 9x9.
* Has 5 ships of sizes 2, 3, 3, 4, 5. This can also be changed but you'll have to change it everywhere again.
* Algorithm assumes that ship generation is random.

## to do
* On hits, sets probability of that point to 0 instead of treating it like an obstacle/miss. This was necessary so that any "accidental"
hits during hunting wouldn't disturb the probaibility of other ship placements. (like if ships were placed right next to each other). 
Issue is that this does not provide accurate ship placement probabilities and causes a high frequency of attacks near sunk ships.
  * A solution would be to ask the user for positions of the ship that has been sunk and treat those as obstacles/misses. Accidental
  hits will just be set to 0. This way, accidental hits won't disturb probability and more accurate ship probabilities will be ensured.
    * Downside is that it is a little lame to ask the user where their sunk ships are.
    * This fix might be necessary as no other way to do this while avoiding ambiguity. For example, ships that are placed consecutively
    with the same orientation. Even if given the size of the ship, if there is an accidental hit, can't know where the ship starts
    unless told explicitly. 
