import sys
import reports

def export(filename,export_filename):
    year = sys.argv[3]
    genre = sys.argv[4]
    title = sys.argv[5]
    with open(export_filename,"w") as file:
        file.write(f"How many games are in the file?\n{reports.count_games(filename)}\n")
        file.write(f"Is there a game from a given year?\n{reports.decide(filename,year)}\n")
        file.write(f"Which is the latest game?\n{reports.get_latest(filename)}\n")
        file.write(f"How many games are in the file by genre?\n{reports.count_by_genre(filename,genre)}\n")
        try:
            file.write(f"What is the line number of a given title?\n{reports.get_line_number_by_title(filename,title)}\n")
        except ValueError:
            file.write(f"What is the line number of a given title?\nThis title is not in the list!\n")
        file.write(f"Can you give me the alphabetically ordered list of the titles?\n{reports.sort_abc(filename)}\n")
        file.write(f"Which genres occur in the data file?\n{reports.get_genres(filename)}\n")
        try:
            file.write(f"What is the release year of the top sold first-person shooter game?\n{reports.when_was_top_sold_fps(filename)}\n")
        except ValueError:
            file.write(f"What is the release year of the top sold first-person shooter game?\nThere is no FPS game in the list!\n")
    file.close()

def main():
    filename = sys.argv[1]
    export_filename = sys.argv[2]
    export(filename, export_filename)

if __name__ == "__main__":
    main()    