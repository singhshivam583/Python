pet_species = "Cat"
pet_age = 4

if pet_species == "Dog":
    if pet_age <= 2:
        print("Puppy Food")
    elif pet_age <=5:
        print("Adult Dog Food")
    else:
        print("Senior Dog Food")

elif pet_species == "Cat":
    if pet_age <= 2:
        print("Kitten Food")
    elif pet_age <=5:
        print("Adult Cat Food")
    else:
        print("Senior Cat Food")