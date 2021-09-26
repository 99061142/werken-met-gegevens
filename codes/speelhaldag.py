persons = 3
ticketTotal = persons * 7.45 

gameseat_time = 45;

gameseat_price = (gameseat_time / 5) * .37
gameseatTotal = gameseat_price * persons

arcadeTotal = gameseatTotal + ticketTotal


print("Dit geweldige dagje-uit met", persons, "mensen in de Speelhal met", gameseat_time, "minuten VR kost je maar", arcadeTotal, "euro")