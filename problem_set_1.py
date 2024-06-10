"""
Your job is to complete the definitions of each function so that it achieves its indicated behavior.

Do not run this file directly... 
Rather, call whichever functions defined in this file that you want to run from within the file named main.py and run that file directly.
"""

def bark():
    """
    Asks the user to enter the name, age, and breed of a dog, as three separate inputs.  
    Then prints out a bark message on behalf of the dog, in the following format:
      'Spot, the 4 year old Schnauzer, says, "Woof!"'

    Requirements: 
      1. The proper nouns (name and breed) must be capitalized in the output, as is standard in English writing, regardless of how the user entered them.
    """
    name = input("Enter your dog's name here: ").strip().capitalize()
    
    age = input("Enter your dog's age here: ").strip()
    breed = input("Enter your dog's breed here: ").strip().capitalize()

    #print( name + ', the ' + age + ' year old ' + breed + ', says, "Woof!"')
    print(name + ', the ' + age + ' year old ' + breed + ', says, "Woof!"')
  
    

def bark_with_validation():
    """
    Do everything the same as in the previous bark() function, with the following additional validation requirements:

    Requirements: 
      2. If the user enters an invalid name, the string, "Name error!", must be printed and nothing else.  An invalid name is any input that is not 2 or more alphabetic characters.
      3. If the user enters an invalid age, the string, "Age error!", must be printed and nothing else.  An invalid age is any input that is not an integer between 0 and 15, inclusive.
      4. If the user enters an invalid breed, the string, "Breed error!", must be printed and nothing else.  An invalid breed is any breed that is not in the list, ["Schnauzer", "Terrier", "Poodle", "Mastiff"]
    """
    name = input("Enter your dog's name here: ").strip().capitalize()
    
    age = input("Enter your dog's age here: ").strip()
    breed = input("Enter your dog's breed here: ").strip().capitalize()

    if name.isalpha() and len(name) >=2:
      if age.isnumeric() and int(age) >=0 and int(age)<=15:
        if breed in ["Schnauzer", "Terrier", "Poodle", "Mastiff"]:
          print( name + ', the ' + age + ' year old ' + breed + ', says, "Woof!"')
        else:
          print("Breed error!") 
      else:
        print("Age error!") 
    else:
      print("Name error!")

  



def respond_to_anything():
    """
    Ask the user to input a sentence.  Print a response based on the input according to the requirements below.

    Requirements: 
      1. If the user enters text ending in the "." character, print the response, "That's true."
      2. If the user enters text ending in the "?" character, print the response, "I'm sorry, I don't know."
      3. If the user enters text ending in the "!" character, print the response, "Exciting!"
      4. If the user enters text that does not include a punctuation mark at the end (punctuation marks include ".", "?", and "!"), print the response, "Please include a punctuation mark at the end of your sentence!"
    """
    sentence = input("Say some thing in a full sentence: ").strip()
    mark = sentence[-1]#determine the punctuation mark
    if mark == ".":
       print("That's true.")
    elif mark == "?":
       print("I'm sorry, I don't know.")
    elif mark == "!":
       print("Exciting!")
    else:
       print("Please include a punctuation mark at the end of your sentence!")



def respond_to_anything_but_nonsense():
    """
    Do everything the same as in the previous respond_to_anything() function, with the following additional validation requirements:

    Requirements:
      5. If the user includes the word, 'nonsense', anywhere in the response, regardless of capitalization, do not print any output.
    """
    sentence = input("Say some thing in a full sentence: ").strip()
    non = "nonsense"#determine the punctuation mark
    if non in sentence.lower():
      return
    
    mark = sentence[-1]
    if mark == ".":
      print("That's true.")
    elif mark == "?":
      print("I'm sorry, I don't know.")
    elif mark == "!":
      print("Exciting!")
    else:
      print("Please include a punctuation mark at the end of your sentence!")
        
       

 

  
