from Song import Song

# when playlist gets created there is nothing and when there is a first song that is assigned to the first song variable
class Playlist:
  def __init__(self):
    self.__first_song = None


  # Done: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)

  #  If there is no first song, the "new_song" becomes the new first song on the list.   
    if self.__first_song == None:
      self.__first_song = new_song
      return

    # set new song's pointer to where head is pointing
    new_song.set_next_song(self.__first_song)
    # set pointer to point at new song
    self.__first_song = new_song

  # DONE: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    if self.__first_song == None:
      return -1

    #  If there is no first song, the "new_song" becomes the new first song on the list.   
    count = 0
    curr = self.__first_song
    while curr != None:
      if(title.lower() == curr.get_title().lower()):
        return count
      count += 1  
      curr = curr.get_next_song() 
    return -1

  # DONE: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 
  # If the title of the first song is the title we're looking for then remove it by making first song NONE.

  def remove_song(self, title):

# checking that the first song matches the song that we want to remove
# create variable cur_song and set it to the first_song 
    cur_song = self.__first_song
    if cur_song != None and cur_song.get_title().lower() == title.lower():
      self.__first_song = cur_song.get_next_song()

    prev_song = None
    while cur_song != None: 
      # if the title I'm searching for matchees the name of the song
      if cur_song.get_title().lower() == title.lower() and prev_song != None:
        prev_song.set_next_song(cur_song.get_next_song())  
      prev_song = cur_song  
      # change the pointer to the next song
      cur_song = cur_song.get_next_song()

  # DONE: Create a method called length, which returns the number of songs in the playlist.
  # if there are no songs will print zero.  
  def length(self):
    if self.__first_song == None:
      return 0
    #  while loop counter for songs using getter method
    count = 0
    curr = self.__first_song
    while curr != None:
      count += 1
      curr = curr.get_next_song() 
    return count

  # DONE TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  # def print_songs(self):
  #  print(self.__first_song)
  #  print(self.__new_song)
  # print(f'{variable} {song}')

  def print_songs(self): 
    if self.__first_song == None:
      return
    #  while loop counter for songs using getter method
    count = 0
    curr = self.__first_song
    while curr != None:
      count += 1
      print(f'{count} {curr.get_title()}')
      curr = curr.get_next_song() 
    return count