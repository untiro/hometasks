class PokeScan:
    # your awesome code goes here!
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        if self.level <= 20:
            pktype = 'weak'
        elif (self.level > 20) & (self.level <= 50):
            pktype = 'fair'
        else:
            pktype = 'strong'

        if self.pkmntype in 'water':
            observ = 'wet'
        elif self.pkmntype in 'fire':
            observ = 'fiery'
        else:
            observ = 'grassy'
        return '{}, a {} and {} Pokemon.'.format(self.name, observ, pktype)

print(PokeScan('Squirtle', 0, 'water').info())