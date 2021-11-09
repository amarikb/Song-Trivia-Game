from states.state import State
import states.titleMenu
from states.song_trivia import Song_Game
import pygame,os,threading,random,json,time
from better_profanity import profanity
import lyricsgenius,socket
from dotenv import load_dotenv

class Loading(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game.state = "Loading Menu"
        load_dotenv()
        self.lyrics = ""
        self.song_title = ""
        self.artist = ""
        self.img = ""
        self.error = False

      
        game_info_thread = threading.Thread(name='game_info', target=self.get_guessing_game_info)
        game_info_thread.daemon = True
        game_info_thread.start()
              
  
       

    def update(self, actions):
        if(self.lyrics != "" and self.lyrics != None):
             new_state = Song_Game(self.game,self.lyrics,self.artist,self.song_title,self.img)
             new_state.enter_state()

        if(self.lyrics == None):
            print("this is true in update")

            """TODO: DELETE BELOW LATER ADD ANOTHER STATE 'ERRORMENU'"""
            #self.game.songs_done.clear()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()
            """
            TODO: ADD ERROR MESSAGE HERE (FOR WHEN WE CANT FIND LYRICS) AND GET SCORE AND CALCULATE HIGH SCORE
            display score 
            Add button "ok" that will go to main screen 
            """ 

        self.game.reset_keys()

    def render(self, display):
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky2.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))

        
        display.blit(background, (0, 0)) 
       
        self.game.draw_text(display, "Loading Game....", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2, 30,"NicoClean-Regular.ttf")
        


    def get_artist_name(self):
        """
        ADD METHOD DESCRIPTION HERE
        """
        with open("./data/artist_names.json") as names:
            artist_names = json.load(names)
        names.close()

        random.seed(time.time())
        random_key_num = str(random.randint(0,len(artist_names) - 1))
        artist_name = artist_names[random_key_num]
  
        return artist_name

    
    def get_guessing_game_info(self):
        """
        ADD METHOD DESCRIPTION HERE
        """
        lyrics_tries = 0
        song_lyrics = ""
        song = ""
        artist = None 
        genius = lyricsgenius.Genius(retries=3)
        genius.skip_non_songs = True
    
        while artist == None:
            artist_name = self.get_artist_name() 
            genius.excluded_terms = [artist_name,"(Remix)", "(Live)","(Demo)", "(Version)","(Edit)","(Bonus)", "(Intro)", "(Cover)", 
        "(Cut)", "tour","(Black Magic*)","(Extended)","(Clean)","Import","(Booklet)", "(Broadway)"]
        #,"liner notes", "credits", "interview", "skit", "instrumental", "setlist"] TODO: ADD IF NEEDED
        
            artist = genius.search_artist(artist_name, max_songs=28, sort="title")
                
        
        while song_lyrics  == "":
            if(lyrics_tries == len(artist) or self.error):
                    break
            try:
                self.song = genius.search_song(artist.songs[lyrics_tries].title, artist_name)
            except socket.timeout as e: #TODO : FIX IF STILL NOT WORKING
                self.error = True
                #print('this is true 1',e) #TODO DELETE PRINT STATEMENT
                continue
                

            while self.song.title in self.game.songs_done:
                if self.error:
                    break
                try:
                    self.song = genius.search_song(artist.songs[lyrics_tries].title, artist_name)
                    lyrics_tries += 1
                
                except (socket.timeout,IndexError) as e: #TODO : FIX IF STILL NOT WORKING 
                  self.error = True
                  #print('this is true 2', e) #TODO DELETE PRINT STATEMENT
                  continue
                    
            left_lyrics = self.song.lyrics.find("]",self.song.lyrics.find("[Chorus:")) + 1
            song_lyrics = profanity.censor(self.song.lyrics[left_lyrics: self.song.lyrics.find("[",left_lyrics)],"-")

            if ("Lyrics from Snippet:" in song_lyrics):
                    song_lyrics = ""

            lyrics_tries += 1

        if(song_lyrics == "" or self.error == True):
            self.lyrics = None   # "no lyrics available"
        else:
             self.game.songs_done.append(self.song.title)
             #print(self.game.songs_done) #TODO : DELETE PRINT STATEMENT
             print(self.song.song_art_image_url) #TODO : DELETE PRINT STATEMENT
             self.lyrics = song_lyrics
             self.artist = artist_name
             self.img = self.song.song_art_image_url
             self.song_title = self.song.title.encode('ascii', 'ignore').decode("utf-8")

   