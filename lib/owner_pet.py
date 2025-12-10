class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def pets(self):
        """Return a list of all Pet instances that belong to this owner."""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign this owner to the pet if valid."""
        if not isinstance(pet, Pet):
            raise Exception("add_pet requires a Pet instance")

        pet.owner = self

    def get_sorted_pets(self):
        """Return owner's pets sorted alphabetically by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)