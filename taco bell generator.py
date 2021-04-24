import random

word1 = ["crunchy", "soft", "supreme", "beefy", "nacho", "beefy 5-layer", "cheesy", "nacho cheese", "spicy", "mild"]

word2 = [" chicken", " bean", " black bean", " nacho", " doritos locos", " gordita"]

word3 = [ " taco", " burrito"," chalupa", " quesadilla", " bellgrande", " supreme", " crunchwrap", " quesalupa", " nachos", " fries", " quesarito"]

def generate():
    for i in range(30):
        print(word1[random.randint(0,9)] + word2[random.randint(0,5)] + word3[random.randint(0,10)])
    restart()



def restart():
    restart = input("r to run ")
    if restart == "r":
        generate()


print("TACO BELL GENERATOR")
print("=-=-=-=-=-=-=-=-=-=")
restart()
