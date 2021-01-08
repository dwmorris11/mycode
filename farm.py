farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
# Not to rough
def rough(i=0, animalsOnly=False):
    if(animalsOnly):
      approvedAnimals = ["sheep", "cows", "pigs", "chickens", "llams", "cats", "pigs"]
      for animal in farms[i]["agriculture"]:
        if animal in approvedAnimals:
          print(animal)
    else:
      for animal in farms[i]["agriculture"]:
        print(animal)
# Hurt me plenty
def hurtMe(animalsOnly=False):
    farm = input("Choose a farm (NE, W, SE): ").strip().upper()
    if farm == "NE":
      rough(0, animalsOnly)
    elif farm == "W":
      rough(1)
    elif farm == "SE":
      rough(2, animalsOnly)
    else:
      print("Try again!")
      hurtMe(animalsOnly)
# Nightmare
def nightmare():
  hurtMe(True)

rough()
hurtMe()
nightmare()
