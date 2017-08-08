## Game start

```
FiveHundredGame:
	Teams:
		Team:
			Player:
				Account: <user account>
			Player:
				Account: <user account>
			Score: 0
		Team:
			Player:
				Account: <user account>
			Player:
				Account: <user account>
			Score: 0
	Hands: []
```

## Beginning of Hand n

```
FiveHundredGame:
	Teams:
		Team:
			Player: ...
			Player: ...
			Score: <integer>
		Team: ...
	Hands: [
		Hand: ... # Hand 1 .. n-1
		Hand: # Hand n
			Dealer: <player>
			Hands:
				Hand:
					Player: <player>
					Cards: [ array of 10 cards ]
				Hand: ... # one hand per player
			Kitty:
				Collected: False
				Cards: [ array of 3 cards ]
			Bids: []
			Tricks: []
	]
```

## End of bidding phase of Hand n

```
FiveHundredGame:
	...
		Hand: # Hand n
			Dealer: <player>
			Hands: ...
			Kitty: ...
			Bids: [
				Bid:
					Player: <player>
					Suit: <bid suit>
					Value: <bid value>
				Bid:
					Player: <player>
					Suit: <bid suit>
					Value: <bid value>
				...
				Bid: # winning bid
					Player: <player>
					Suit: <bid suit>
					Value: <bid value>
				Bid: <pass>
				Bid: <pass>
				Bid: <pass>
			]
			Tricks: []
```

## After Kitty distributed:

```
FiveHundredGame:
	...
		Hand: # Hand n
			Hands:
				...
				Hand: # Bid winner's hand
					...
					Cards: [ array of 13 cards ]
			Kitty:
				Collected: True
				Cards: [ array of 3 cards ] # probably not emptied, for later reference
			...
```

## After 3 cards discarded by bid winner

```
FiveHundredGame:
	...
		Hand: # Hand n
			Hands:
				...
				Hand: # Bid winner's hand
					...
					Cards: [ array of 10 cards ]
			...
```

## After card played by each player

```
FiveHundredGame:
	...
	Hand: # Hand n
		Hands:
			...
			Hand: # Each player's hand
				...
				Cards: [ array of 9 cards ]
				...
				Tricks: [
					Trick:
						Leader: <player>
						Cards: [ array of 4 cards ]
				]
		...
```
