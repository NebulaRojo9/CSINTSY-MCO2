% to check adjacent
adjacent((X1, Y1), (X2, Y2)) :-
    (X2 is X1 + 1, Y2 is Y1);
    (X2 is X1 - 1, Y2 is Y1);
    (X2 is X1, Y2 is Y1 + 1);
    (X2 is X1, Y2 is Y1 - 1).

% breeze, glitter, and fall
breeze((X, Y)) :- adjacent((X, Y), Pit), pit(Pit).
glitter((X, Y)) :- gold((X, Y)).
fall((X, Y)) :- pit((X, Y)).

% Breeze checker by using adjacent on all pits
findBreeze((X, Y)) :- adjacent((X, Y), Pit), pit(Pit).

% Compares all breezes found so far
findPit((X, Y)) :-
    % format (element, condition, list)
    % looking for coordinates, from (adjacent to given x and y) and is a breeze spot, from the BreezeSpots
                                        % NOTE B reezeSpots and not b reezeSpots, capital means variable
    findall((AdjX, AdjY), (adjacent((X, Y), (AdjX, AdjY)), breezeSpot((AdjX, AdjY))), BreezeSpots),
    length(BreezeSpots, Count),
    Count >= 3.