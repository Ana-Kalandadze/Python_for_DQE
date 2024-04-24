# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format

# You need to implement:
# 1.News – text and city as input. Date is calculated during publishing.
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

from datetime import date, datetime
from task_6 import ExportToFile
from task_7 import WordCounter, LetterCounter
from task_8 import ExportToJsonFile
from task_9 import create_xml

class journal:
    def __init__(self, news_type):
        self.news_type = news_type
        self.text = ""

    def get_text(self):
        self.text = input(f"Enter {self.news_type} text please ")

    def display_news(self):
        return(self.text)

    def display_type(self):
        return(self.news_type)

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
        return(self.city,',',self.date)


class privatead(journal):
    def __init__(self):
        super().__init__("Private ad")

    def get_text(self):
        super().get_text()
        self.date = datetime.strptime(input("Please enter expiration date of news: "), '%m-%d-%Y').date()     

    def display_news(self):
        super().display_news()
        return(f"{(self.date - date.today()).days} days left")

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
        return(f"it is {self.temp}\n",self.comment)


def output_news():
    results = ''
    while True: 
        choice = input("What kind of news do you want to get? ")

        if choice == "News":
            news_journal = news()
            news_journal.get_text()
            results += (news_journal.display_type()) + '----------' + '\n'
            results += ' '.join(map(str, news_journal.display_news())) + '\n'

        elif choice == "Private ad":
            privatead_journal = privatead()
            privatead_journal.get_text()
            results += ' '.join(privatead_journal.display_type() ()) + '\n'
            results += ' '.join(privatead_journal.display_news() ()) + '\n'

        elif choice == "Weather":
            weather_journal = weather()
            weather_journal.get_text()
            results += ' '.join(weather_journal.display_type() ()) + '\n'
            results += ' '.join(weather_journal.display_news() ()) + '\n'

        else:
            results += "Sorry, we don't have that kind of news" + '\n'

        again = input("Do you want to get another news? (yes/no): ")
        
        if again.lower() != 'yes':
            break

    file = ExportToFile().to_txt(results)
    json_file = ExportToJsonFile().to_json(results)
    counter = WordCounter('news.txt')
    counts = counter.compute_counts()
    counter.write_to_csv(counts)
    letter_counter = LetterCounter('news.txt')


    letter_counter = LetterCounter('news.txt')
    all_counts, uppercase_counts = letter_counter.compute_counts()
    letter_counter.write_to_csv(all_counts, uppercase_counts)
    create_xml(results)
    # Print the results at the end
    print(results)



if __name__ == "__main__":
    output_news()


