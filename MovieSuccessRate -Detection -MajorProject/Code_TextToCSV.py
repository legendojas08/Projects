import csv

# Data to be written into the CSV file
data = [
    ["title", "budget", "runtime", "genre", "director", "release_date", "success"],
    ["Inception", 160000000, 148, "Sci-Fi", "Christopher Nolan", "2010-07-16", 1],
    ["The Dark Knight", 185000000, 152, "Action", "Christopher Nolan", "2008-07-18", 1],
    ["Avatar", 237000000, 162, "Action", "James Cameron", "2009-12-18", 1],
    ["Titanic", 200000000, 195, "Drama", "James Cameron", "1997-12-19", 1],
    ["Interstellar", 165000000, 169, "Sci-Fi", "Christopher Nolan", "2014-11-07", 1],
    ["Jurassic Park", 63000000, 127, "Action", "Steven Spielberg", "1993-06-11", 1],
    ["Jaws", 7000000, 124, "Thriller", "Steven Spielberg", "1975-06-20", 1],
    ["Saving Private Ryan", 70000000, 169, "War", "Steven Spielberg", "1998-07-24", 1],
    ["The Avengers", 220000000, 143, "Action", "Joss Whedon", "2012-05-04", 1],
    ["Deadpool", 58000000, 108, "Action", "Tim Miller", "2016-02-12", 1],
    ["Logan", 97000000, 137, "Action", "James Mangold", "2017-03-03", 1],
    ["La La Land", 30000000, 128, "Musical", "Damien Chazelle", "2016-12-09", 1],
    ["Gravity", 100000000, 91, "Sci-Fi", "Alfonso Cuarón", "2013-10-04", 1],
    ["Blade Runner 2049", 150000000, 164, "Sci-Fi", "Denis Villeneuve", "2017-10-06", 1],
    ["Black Panther", 200000000, 134, "Action", "Ryan Coogler", "2018-02-16", 1],
    ["The Revenant", 135000000, 156, "Drama", "Alejandro González Iñárritu", "2015-12-25", 1],
    ["Mad Max: Fury Road", 150000000, 120, "Action", "George Miller", "2015-05-15", 1],
    ["The Social Network", 40000000, 120, "Drama", "David Fincher", "2010-10-01", 1],
    ["The Martian", 108000000, 144, "Sci-Fi", "Ridley Scott", "2015-10-02", 1],
    ["Shutter Island", 80000000, 138, "Mystery", "Martin Scorsese", "2010-02-19", 1],
    ["Goodfellas", 25000000, 146, "Crime", "Martin Scorsese", "1990-09-19", 1],
    ["The Godfather", 6000000, 175, "Crime", "Francis Ford Coppola", "1972-03-24", 1],
    ["Fight Club", 63000000, 139, "Drama", "David Fincher", "1999-10-15", 1],
    ["American Beauty", 15000000, 122, "Drama", "Sam Mendes", "1999-10-01", 1],
    ["The Departed", 90000000, 151, "Crime", "Martin Scorsese", "2006-10-06", 1],
    ["Pulp Fiction", 8000000, 154, "Crime", "Quentin Tarantino", "1994-10-14", 1],
    ["Forrest Gump", 55000000, 142, "Drama", "Robert Zemeckis", "1994-07-06", 1],
    ["The Shawshank Redemption", 25000000, 142, "Drama", "Frank Darabont", "1994-10-14", 1],
    ["The Matrix", 63000000, 136, "Action", "Lana Wachowski", "1999-03-31", 1],
    ["Inglourious Basterds", 70000000, 153, "War", "Quentin Tarantino", "2009-08-21", 1],
    ["Django Unchained", 100000000, 165, "Western", "Quentin Tarantino", "2012-12-25", 1],
    ["Back to the Future", 19000000, 116, "Adventure", "Robert Zemeckis", "1985-07-03", 1],
    ["Avatar 2", 250000000, 0, "Action", "James Cameron", "2022-12-16", 0],
    ["The Croods", 135000000, 95, "Animation", "Chris Sanders", "2013-03-22", 0],
    ["The Emoji Movie", 50000000, 86, "Animation", "Tony Leondis", "2017-07-28", 0],
    ["Cats", 95000000, 110, "Drama", "Tom Hooper", "2019-12-20", 0],
    ["Dolittle", 175000000, 101, "Adventure", "Stephen Gaghan", "2020-01-17", 0],
    ["Fantasy Island", 7000000, 109, "Adventure", "Jeff Wadlow", "2020-02-14", 0],
    ["Birds of Prey", 84500000, 109, "Action", "Cathy Yan", "2020-02-07", 0],
    ["The Grudge", 10000000, 93, "Horror", "Nicolas Pesce", "2020-01-03", 0],
    ["Sonic the Hedgehog", 85000000, 99, "Action", "Jeff Fowler", "2020-02-14", 0],
    ["Bloodshot", 45000000, 110, "Action", "Dave Wilson", "2020-03-13", 0],
    ["Artemis Fowl", 125000000, 95, "Adventure", "Kenneth Branagh", "2020-06-12", 0],
    ["Tenet", 200000000, 150, "Action", "Christopher Nolan", "2020-09-03", 0],
    ["Top Gun: Maverick", 152000000, 0, "Action", "Joseph Kosinski", "2022-05-27", 0],
    ["Minions: The Rise of Gru", 80000000, 0, "Animation", "Kyle Balda", "2022-07-01", 0],
    ["The Batman", 180000000, 0, "Action", "Matt Reeves", "2022-03-04", 0],
    ["The Flash", 150000000, 0, "Action", "Andy Muschietti", "2022-11-04", 0],
    ["Avatar 3", 250000000, 0, "Action", "James Cameron", "2024-12-20", 0],
    ["Guardians of the Galaxy Vol. 3", 0, 0, "Action", "James Gunn", "2023-05-05", 0],
    ["Indiana Jones 5", 0, 0, "Adventure", "James Mangold", "2023-07-28", 0],
    ["Black Panther: Wakanda Forever", 0, 0, "Action", "Ryan Coogler", "2022-11-11", 0],
    ["Avatar 4", 0, 0, "Action", "James Cameron", "2026-12-18", 0],
    ["Avatar 5", 0, 0, "Action", "James Cameron", "2028-12-22", 0]
]

# Specify the file path
file_path = 'movies_dataset.csv'

# Write data to CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_path}' has been created successfully.")
