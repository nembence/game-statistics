def count_games(file_name):
    with open(file_name,'r') as file:
        return len(file.readlines())


def decide(file_name,year):
    with open(file_name,'r') as file:
        games=file.readlines()
        for i in games:
            if str(year)in i:
                return True
        return False        
    

def get_latest(file_name):
    with open(file_name,'r') as file:
        games=sorted([line.split('\t') for line in file.readlines()], key = lambda  x : x[2])
        return games[-1][0]


def count_by_genre(file_name, genre):
    with open(file_name,'r') as file:
        games=[line.split('\t') for line in file.readlines()]
        count=0
        for game in games:
            if game[3] == genre:
                count += 1
        return count        
       

def get_line_number_by_title(file_name,title):
    with open(file_name,'r') as file:
        games=[line.split('\t') for line in file.readlines()]
        for game in range(len(games)):
            if games[game][0] == title:
                return game+1
        raise ValueError()        

def sort_abc(file_name):
    with open(file_name,'r') as file:
        titles=[line.split('\t')[0] for line in file.readlines()]
        for title in range(len(titles)-1,0,-1):
            for j in range(title):
                if titles[j] > titles[j+1]:
                    temp = titles[j+1]
                    titles[j+1] = titles[j]
                    titles[j] = temp
        return titles

def get_genres(file_name):
    with open(file_name,'r') as file:
        genres=[line.split('\t')[3] for line in file.readlines()]
        genres=list(set(genres))
        for genre in range(len(genres)-1,0,-1):
            for j in range(genre):
                if genres[j] > genres[j+1]:
                    temp = genres[j+1]
                    genres[j+1] = genres[j]
                    genres[j] = temp
    return genres

def when_was_top_sold_fps(file_name):
    with open(file_name,'r') as file:
        fps = sorted([line.split('\t') for line in file.readlines() if line.split('\t')[3] == 'First-person shooter'], key = lambda x:float(x[1]))
        if len(fps) == 0:
            raise ValueError()
        else:
            return int(fps[-1][2])


