# five-hundred
500 card game

## Normal game flow:
* game = FiveHundredGame([ Team([ Player(Account(...)), Player(Account(...)) ]), Team([ Player(Account(...)), Player(Account(...)) ]) ])
* loop until game complete:
	* loop until bidding complete:
		* game.hands[-1].accept_bid(Bid(..., playerN_id))
		* game.hands[-1].accept_bid(Bid(..., playerN+1_id))
		* game.hands[-1].accept_bid(Bid(..., playerN+2_id))
		* game.hands[-1].accept_bid(Bid(..., playerN+3_id))
		* game.hands[-1].accept_bid(Bid(..., playerN_id))
		* game.hands[-1].accept_bid(Bid(..., playerN+1_id))
		* ...
	* loop until hand complete:
		* game.hands[-1].accept_card(Card(...), playerM_id)
		* game.hands[-1].accept_card(Card(...), playerM+1_id)
		* game.hands[-1].accept_card(Card(...), playerM+2_id)
		* game.hands[-1].accept_card(Card(...), playerM+3_id)
		* game.hands[-1].accept_card(Card(...), playerM_id)
		* game.hands[-1].accept_card(Card(...), playerM+1_id)
		* ...
	* [Placeholder] calculate hand score and apply to team totals
