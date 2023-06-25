from sko.PSO import PSO

import csv
import datetime

user = {'user': (6, 'John', 232.0),
	'albums': [(1, 'Doolittle', 'Pixies', 29.0, 1),
				(9, 'The Immaculate Collection', 'Madonna', 46.0, 5),
				(15, 'Aftermath', 'The Rolling Stones', 35.0, 5),
				(19, 'Black Sabbath', 'Black Sabbath', 26.0, 4),
				(21, 'Let It Bleed', 'The Rolling Stones', 35.0, 3),
				(23, 'At Fillmore East', 'The Allman Brothers Band', 21.0, 3),
				(28, 'Sweet Baby James', 'James Taylor', 47.0, 4),
				(37, 'Goodbye Yellow Brick Road', 'Elton John', 38.0, 4),
				(56, 'The Anthology', 'Muddy Waters', 34.0, 4),
				(66, 'My Generation', 'The Who', 32.0, 1),
				(75, 'Darkness on the Edge of Town', 'Bruce Springsteen', 15.0, 1),
				(82, 'Music From Big Pink', 'The Band', 18.0, 2),
				(83, 'American Idiot', 'Green Day', 36.0, 4),
				(86, 'Moondance', 'Van Morrison', 37.0, 3),
				(97, 'Live at Leeds', 'The Who', 43.0, 3),
				(99, 'Rejuvenation', 'The Meters', 27.0, 2),
				(102, '[Led Zeppelin IV]', 'Led Zeppelin', 40.0, 1),
				(113, 'Bo Diddley / Go Bo Diddley', 'Bo Diddley', 32.0, 5),
				(117, '40 Greatest Hits', 'Hank Williams', 2.0, 4),
				(121, 'At Last!', 'Etta James', 35.0, 4),
				(124, 'The Queen Is Dead', 'The Smiths', 17.0, 1),
				(143, 'Raising Hell', 'Run D.M.C.', 22.0, 5),
				(144, 'A Love Supreme', 'John Coltrane', 13.0, 5),
				(145, 'In the Wee Small Hours', 'Frank Sinatra', 20.0, 1),
				(146, 'The Dock of the Bay', 'Otis Redding', 43.0, 5),
				(147, "Never Mind the Bollocks Here's the Sex Pistols",'Sex Pistols', 23.0, 1),
				(148, 'NULL', "The B 52's", 32.0, 5),
				(149, 'The Chronic', 'Dr. Dre', 48.0, 1),
				(150, 'Aja', 'Steely Dan', 27.0, 3),
				(151, 'Look-Ka Py Py', 'The Meters', 6.0, 2),
				(152, 'Physical Graffiti', 'Led Zeppelin', 20.0, 5),
				(153, 'Chronicle: The 20 Greatest Hits', 'Creedence Clearwater Revival', 38.0, 2),
				(154, 'Funeral', 'Arcade Fire', 20.0, 4),
				(155, 'Freak Out!', 'The Mothers of Invention', 36.0, 4),
				(156, 'NULL', 'Chuck Berry', 49.0, 2),
				(157, 'Paranoid', 'Black Sabbath', 43.0, 3),
				(158, 'Meet the Beatles!', 'The Beatles', 12.0, 1),
				(159, "This Year's Model", 'Elvis Costello', 16.0, 4),
				(160, 'Led Zeppelin', 'Led Zeppelin', 48.0, 2),
				(161, 'Revolver', 'The Beatles', 26.0, 2),
				(162, 'The Notorious Byrd Brothers', 'The Byrds', 28.0, 4)]
                    }

albums = [x for x in user['albums']]
user_funds = user['user'][2]

def make_selections_PSO(funds, wanted_albums, population, max_iter):
    album_costs = [x[3] for x in wanted_albums]
    preferences = [x[4] for x in wanted_albums]

    def fitness(candidate):
        binary = '{0:b}'.format(round(candidate[0]))
        while len(binary) < len(wanted_albums):
            binary = '0'+binary

        satisfaction = 0
        cost = 0
        for i in range(len(binary)):
            digit = int(binary[i])
            satisfaction += digit * preferences[i]
            cost += digit * album_costs[i]

        if cost >= funds:
            return 0

        return -satisfaction

    pso = PSO(func=fitness, n_dim=1, pop=population, max_iter=max_iter, lb=0, ub=(2**len(wanted_albums))-1, w=0.8, c1=0.5, c2=0.5)
    best_x, best_y = pso.run()

    best_x_binary = '{0:b}'.format(round(best_x[0]))
    while len(best_x_binary) < len(wanted_albums):
        best_x_binary = '0'+best_x_binary

    selections = []
    total = 0  
    if best_y[0] != 0:
        for i in range(len(wanted_albums)):
            if best_x_binary[i] == '1':
                selections.append(wanted_albums[i])
        
        for album in selections:
            total += album[3]

    return best_x, -best_y[0], selections, Y_history, total

header = ['population', 'max_iteration', 'satisfaction', 'cost', 'selected_albums', 'repetition']
with open("/home/mike/results_PSO.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    
iteration = 50
while iteration < 1050:
    population = 50
    while population < 1050:
        for j in range(10):
            best_x, best_y, selections, Y_history, total = make_selections_PSO(user_funds, albums, population, iteration) 
            now = datetime.datetime.now()
            with open("/home/mike/results_PSO.csv", 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([population, iteration, best_y, total, len(selections), j, now.time()])
        
        population += 50
    iteration += 50