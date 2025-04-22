
# Liskov Substitution Principle (LSP):

class Bird:
    def make_sound(self):
        return 'Some bird sound'

class Sparrow(Bird):
    def make_sound(self):
        return 'Chirp chirp'

class Duck(Bird):
    def make_sound(self):
        return 'Quack quack'

def play_bird_sound(bird: Bird):
    print(bird.make_sound())

if __name__ == '__main__':
    birds = [Sparrow(), Duck()]
    for bird in birds:
        play_bird_sound(bird)
# This example demonstrates the Liskov Substitution Principle. The play_bird_sound function works with the Bird superclass, and both Sparrow and Duck subclasses can replace Bird without causing any issues. The behavior remains consistent, which follows the core idea of LSP.