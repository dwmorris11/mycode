#!/usr/bin/env python3
import requests

def getPokemonJSON(pokemon):
    try:
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()
        return pokeapi
    except:
        print("Pokemon is not found or available for query.")
        exit(0)

def printImageLink(pokemon):
    return pokemon.get("sprites").get("front_default")

def countGames(pokemon):
    return len(pokemon.get("game_indices"))

def pokeMoves(pokemon):
    result = []
    moves = pokemon.get("moves")
    for move in moves:
        result.append(move.get("move").get("name"))
    return result

poke = input("What pokemon do you want to search?").strip().lower()
pokemon = getPokemonJSON(poke)
image = printImageLink(pokemon)
games = countGames(pokemon)
moves = pokeMoves(pokemon)

print(f"""
{poke}:
image: {image}
appearances in games: {games}
moves: {moves}
""")



