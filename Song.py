class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # DONE TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # DONE BUT todo title case TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    self.__title = str(title)


  # DONE TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # DONE TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    self.__next_song = next_title


  # DONE TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return self.get_title()


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    return f"{self.get_title()} -> {self.get_next_song()}"

