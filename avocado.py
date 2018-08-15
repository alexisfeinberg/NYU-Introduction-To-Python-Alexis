
class a_toast:
    def __init__(self, base='toast', first_item='avocado',
                 second_item='spices', third_item='olive oil',
                 sprinkle=True, smash=True, drizzle=True):
        self.base = base
        self.first_item = first_item
        self.second_item = second_item
        self.third_item = third_item
        self.sprinkle = sprinkle
        self.smash = smash
        self.drizzle = drizzle


def main():
    avocado = a_toast()
    print('You will need {}, {}, {}, and {} to make avocado toast'.
          format(avocado.base, avocado.first_item, avocado.second_item,
          avocado.third_item))
    print('Do I need to smash {}?'.format(avocado.first_item))
    print(avocado.smash)
    print('Do I need to sprinkle {}?'.format(avocado.second_item))
    print(avocado.sprinkle)
    print('Do I need to drizzle {}?'.format(avocado.third_item))
    print(avocado.drizzle)



if __name__ == "__main__":
    main()
