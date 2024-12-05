class Pet:
     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
     all = [] 

     def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are {', '.join(Pet.PET_TYPES)}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    
        Pet.all.append(self)

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            owner.add_pet(self)
    
     def __repr__(self):
        return f"{self.name} ({self.pet_type})"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = [] 

    def pets(self):
        return self.pets_list
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        self.pets_list.append(pet)
        pet.owner = self 

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
