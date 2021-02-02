from Song import Song

# when playlist gets created there is nothing and when there is a first song that is assigned to the first song variable
class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

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
 

  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    pass


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pass



  # TODO: Create a method called length, which returns the number of songs in the playlist.
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

   

  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  # def print_songs(self):
  #  print(self.__first_song)
  #  print(self.__new_song)

  