def count_games(file_name):
    with open(file_name,'r') as f:
        return len(f.readlines())


def decide(file_name,year):
    with open(file_name,'r') as f:
        games=f.readlines()
        for i in games:
            if str(year)in i:
                return True
        return False        
    

def get_latest(file_name):
    with open(file_name,'r') as f:
        games=sorted([line.split('\t') for line in f.readlines()], key = lambda  x : x[2])
        return games[-1][0]

print(get_latest('game_stat.txt'))
