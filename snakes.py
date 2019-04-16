class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
<<<<<<< HEAD
    
    def bites(self, other):
=======
    """KEVINS LOUD EDIT"""
    def bite(self, other):
>>>>>>> miles/master
        """Deliver a dose of venom."""
        pass

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        from bear import hug
        hug(self, other, kill=True)

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
