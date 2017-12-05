# five-hundred
500 card game

## Task tracking

[Trello Board](https://trello.com/b/Ox0k6rDp/five-hundred)

## Normal game flow:
* game = FiveHundredGame([ Player(player1_id, player1_name), Player(player2_id, player2_name), Player(player3_id, player3_name), Player(player4_id, player4_name) ])
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
