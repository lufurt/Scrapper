import scrapy
from mpi4py import MPI
import re

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginPlayersSpider(scrapy.Spider):
    name = 'login_doplayers2'
    start_urls = ['https://www.dugout-online.com/']
    custom_settings = {
        'CONCURRENT_REQUESTS': 100,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
    }

    def parse(self, response):
        yield scrapy.FormRequest(
            url='https://www.dugout-online.com/home/none/Free-online-football-manager-game',
            formdata={
                'attemptLogin' : '1',
                'do_user': '',
                'do_pass': ''
            },
            callback=self.after_login,
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        self.log("Logado")
        for i in range (10790000, 10800000):
            yield scrapy.Request(url = "https://www.dugout-online.com/players/details/youth/0/playerID/" + str(i), callback=self.club_info)

    def club_info(self, response):
        error = response.css(".window1_header_text")
        if (error):
            return
        #Auxiliares
        club_aux = response.css(".tabbed_pane div")[7]
        club_aux1 = club_aux.css("table tr td")[1]
        club_aux2 = club_aux.css("table tr")[1]
        club_aux22 = club_aux2.css("td")[1]
        club_aux3 = club_aux.css("table tr")[2]
        club_aux33 = club_aux3.css("td")[1]
        player = response.css(".player_name")[0]
        player_firstname = response.css(".player_name::text")[0].get()
        player_lastname = player.css("b::text").get()
        dados1 = response.css(".row1")[1]
        dados2 = response.css(".row2")[1]
        dados3 = response.css(".row1")[2]
        dados4 = response.css(".row2")[2]
        dados5 = response.css(".row1")[3]
        exp_aux = response.css(".row2 td")[5]
        aux = response.xpath("//*[@id='main-1']/div[5]/table[1]/tr[3]/td[2]/text()").get().strip()
        #Info Final
        Club_name = club_aux1.css("a::text").get().strip(',')
        Player_name = player_firstname + player_lastname
        Position = club_aux33.css("td::text").get()
        Country = response.xpath("//*[@id='content_main']/div[1]/div/div/div[1]/div[3]/img/@title").get()
        Age = club_aux22.css("td::text").get().strip(' years old')
        Reflexes = dados1.css("td::text")[1].get()
        Tackling = dados1.css("td::text")[3].get()
        Creativity = dados1.css("td::text")[5].get()
        Shooting = dados1.css("td::text")[7].get()
        TeamWork = dados1.css("td::text")[9].get()
        OneonOne = dados2.css("td::text")[1].get()
        Marking = dados2.css("td::text")[3].get()
        Passing = dados2.css("td::text")[5].get()
        Dribbling = dados2.css("td::text")[7].get()
        Speed = dados2.css("td::text")[9].get()
        Handling = dados3.css("td::text")[1].get()
        Heading = dados3.css("td::text")[3].get()
        LongShots = dados3.css("td::text")[5].get()
        Positioning = dados3.css("td::text")[7].get()
        Strength = dados3.css("td::text")[9].get()
        Communication = dados4.css("td::text")[1].get()
        Crossing = dados4.css("td::text")[3].get()
        FirstTouch = dados4.css("td::text")[5].get()
        Aggression = dados4.css("td::text")[7].get()
        Influence = dados4.css("td::text")[9].get()
        Eccentricity = dados5.css("td::text")[1].get()
        Experience = exp_aux.css("div::attr(title)").get().strip(' XP')
        Personality1 = response.xpath("//*[@id='main-1']/div[2]/table/tr[2]/td/text()").get().strip()
        Personality2 = response.xpath("//*[@id='main-1']/div[2]/table/tr[3]/td/text()").get()
        Personality3 = response.xpath("//*[@id='main-1']/div[2]/table/tr[4]/td/text()").get()
        Wage = aux.strip(' $/week')
        #logs
        #self.log(Club_name)
        #self.log(Player_name)
        #self.log(Position)
        #self.log(Country)
        #self.log(Age)
        #self.log(Reflexes)
        #self.log(Tackling)
        #self.log(Creativity)
        #self.log(Shooting)
        #self.log(TeamWork)
        #self.log(OneonOne)
        #self.log(Marking)
        #self.log(Passing)
        #self.log(Dribbling)
        #self.log(Speed)
        #self.log(Handling)
        #self.log(Heading)
        #self.log(LongShots)
        #self.log(Positioning)
        #self.log(Strength)
        #self.log(Communication)
        #self.log(Crossing)
        #self.log(FirstTouch)
        #self.log(Aggression)
        #self.log(Influence)
        #self.log(Eccentricity)
        #self.log(Experience)
        #self.log(Personality1)
        #self.log(Personality2)
        #self.log(Personality3)
        #self.log(Wage)
        yield {
            'Club_name':Club_name,
            'Player_name':Player_name,
            'Position':Position,
            'Country':Country,
            'Age':Age,
            'Reflexes':Reflexes,
            'Tackling':Tackling,
            'Creativity':Creativity,
            'Shooting':Shooting,
            'TeamWork':TeamWork,
            'OneonOne':OneonOne,
            'Marking':Marking,
            'Passing':Passing,
            'Dribbling':Dribbling,
            'Speed':Speed,
            'Handling':Handling,
            'Heading':Heading,
            'LongShots':LongShots,
            'Positioning':Positioning,
            'Strength':Strength,
            'Communication':Communication,
            'Crossing':Crossing,
            'FirstTouch':FirstTouch,
            'Aggression':Aggression,
            'Influence':Influence,
            'Eccentricity':Eccentricity,
            'Experience':Experience,
            'Personality1':Personality1,
            'Personality2':Personality2,
            'Personality3':Personality3,
            'Wage':Wage,
        }