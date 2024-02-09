# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format

# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

from datetime import date, datetime

class journal:
    def __init__(self, news_type):
        self.news_type = news_type
        self.text = ""

    def get_text(self):
        self.text = input(f"Enter {self.news_type} text please ")

    def display_news(self):
        print(self.text)

    def display_type(self):
        print(self.news_type, '-----------')

class news(journal):
    def __init__(self):
        super().__init__("News")
        self.city = ""
        self.date = date.today()

    def get_text(self):
        super().get_text()
        self.city = input("Please enter city ")

    def display_news(self):
        super().display_news()
        print(self.city,',',self.date)


class privatead(journal):
    def __init__(self):
        super().__init__("Private ad")

    def get_text(self):
        super().get_text()
        self.date = datetime.strptime(input("Please enter expiration date of news: "), '%m-%d-%Y').date()     

    def display_news(self):
        super().display_news()
        print(f"{(self.date - date.today()).days} days left")

class weather(journal):
    def __init__(self):
        super().__init__("Weather")
        
    
    def get_text(self):
        self.temp = int(input("Please enter temperature: "))
        if self.temp < 20:
            self.comment = "It is chill outside"
        else: 
            self.comment = "It is warm outside" 

    def display_news(self):
        print(f"it is {self.temp}\n",self.comment)


def main():
    choice = input("What kind of news do you want to get? ")

    if choice == "News":
        news_journal = news()
        news_journal.get_text()
        news_journal.display_type()
        news_journal.display_news()
        

    elif choice == "Private ad":
        privatead_journal = privatead()
        privatead_journal.get_text()
        privatead_journal.display_type()
        privatead_journal.display_news()

    elif choice == "Weather":
        weather_journal = weather()
        weather_journal.get_text()
        weather_journal.display_type()
        weather_journal.display_news()

    else:
        print("Sorry, we don't have that kind of news")



if __name__ == "__main__":
    main()


