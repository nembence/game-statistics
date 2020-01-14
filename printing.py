import reports
import os 


def questions():
    print("1. How many games are in the file?")
    print("2. Is there a game from a given year?")
    print("3. Which is the latest game?")
    print("4. How many games are in the file by genre?")
    print("5. What is the line number of a given title?")
    print("6. Can you give me the alphabetically ordered list of the titles?")
    print("7. Which genres occur in the data file?")
    print("8. What is the release year of the top sold first-person shooter game?")
    question = int(input("Which question do you want to pick: "))
    return question

def functions(question,filename):
    if question == 1:
        print(reports.count_games(filename))    
    elif question == 2:
        year=int(input("What is the given year: "))
        print(reports.decide(filename,year))
    elif question == 3:
        print(reports.get_latest(filename))
    elif question == 4:
        genre=input("Which genre do you want to check: ")
        print(reports.count_by_genre(filename,genre))
    elif question == 5:
        title=input("What title do you want to check: ")
        print(reports.get_line_number_by_title(filename,title))
    elif question == 6:
        print(reports.sort_abc(filename))
    elif question == 7:
        print(reports.get_genres(filename))
    elif question == 8:
        print(reports.when_was_top_sold_fps(filename))
    
def ask():
    back = input("Do you want to ask again (y/n): ")
    if back == "y":
        return True
    else:
        return False 

def main():
    filename=input("What is your file name: ")
    os.system("clear")
    asking = True
    while asking is True:
        os.system("clear")
        question = questions()
        functions(question,filename)
        asking = ask()

if __name__ == '__main__':
    main()