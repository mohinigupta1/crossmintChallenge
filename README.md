# Crossmint Coding Challenge:

Welcome to our Crossmint coding challenge, in which you will help us mint a new megaverse into existence!

Megaverses are 2D spaces comprised of combinations of different astral objects: 🪐POLYanets with 🌙SOLoons around them and ☄comETHs floating around.

Your job as the master of the megaverse will be to create one with some given parameters and shapes. You will use a megaverse creator API to help you with such legendary quest.

The challenge is composed of 2 phases. In the first one you will learn how to interact with the API and create some 🪐POLYanets and validate them. In the second one you will create a bigger megaverse with some peculiar shape.

# Documentation (APIs)

The Megaverse service allows you to generate different astral objects: Polyanets, Soloons and Comeths!

The megaverse service is a REST API. All API routes below refer to a single route: https://challenge.crossmint.io/api/...

IMPORTANT: All APIs take a required parameter 'candidateId'
Polyanets
POST /api/polyanets with arguments 'row' and 'column' for their position in the map
DELETE /api/polyanets with arguments 'row' and 'column' will delete a Polyanet if you made a mistake
Soloons
POST /api/soloons with arguments 'row' and 'column' for their position in the map.
Additionally you should provide a 'color' argument which can be "blue", "red", "purple" or "white"
DELETE /api/soloons with arguments 'row' and 'column' will delete a Polyanet if you made a mistake
Cometh
POST /api/comeths with arguments 'row' and 'column' for their position in the map.
Additionally you should provide a 'direction' argument which can be "up", "down", "right" or "left"
DELETE /api/comeths with arguments 'row' and 'column' will delete a Polyanet if you made a mistake
Goal Map
There is one extra endpoint you might find helpful! It' the /api/map/[candidateId]/goal, where [candidateId] is your candidate ID.
