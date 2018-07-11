def enter_num():
    return input("Please enter a number!\n")

def odd_even(number):
      if int(number)%2 == 0:
          print("Even")
      else:
          print("Odd")

def main():
    num_enter=enter_num()
    odd_even(number=num_enter)


if __name__ == '__main__':
    main()
