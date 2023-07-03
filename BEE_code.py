import random
import math
import matplotlib.pyplot as plt

# Data utiliser
cities = {

        "Casablanca":(33.53333,7.58333),
        "Rabat":(34.02083,6.84167),
        "Marrakech":(31.63000,8.00889),
       "Tanger":(35.76611,5.80000),
       "Agadir":(30.43278,9.60000),
       "Safi":(32.28333,9.23333),
        "Tan–Tan":(28.43333,11.10000),
        "Tiznit":(29.70722,9.73333),
        "Tarfaya":(27.93583,12.91861),
        "Ait Baha":(31.58333,5.58333),
        "Saidia":(35.08500,2.23917),
        "Guelmim":(28.98333,10.06667),
        "Ben Slimane":(33.61667,7.11667)
    
}
# minimiser le nomber de villes a pour but d'avoire un graphe bien lisibles
# cities = {
    
#             "Casablanca"(33.53333,7.58333),
#             "Rabat"(34.02083,6.84167),
#             "Oujda"(34.68667,1.91139),
#             "Marrakech"(31.63000,8.00889),
#             "Fès"(34.03333,50.0000),0
#             "Tanger"(35.76611,5.80000),
#             "Salé"(34.03333,6.80000),
#             "Meknès"(33.89500,5.55472),
#             "Agadir"(30.43278,9.60000),
#             "Kénitra"(34.26528,6.57806),
#             "Tétouan"(35.56667,5.36667),
#             "Safi"(32.28333,9.23333),
#             "Témara"(33.92611,6.91222),
#             "Béni Mellal"(32.33944,6.36083),
#             "Mohammédia"(33.68333,7.38333),
#             "Khouribga"(32.88972,6.90694),
#             "Nador"(35.16667,2.93333),
#             "El Jadida"(33.23333,8.50000),
#             "Taza"(34.22417,4.00667),
#             "Aït Melloul"(30.33444,9.49722),
#             "Larache"(35.18389,6.15000),
#             "Settat"(30.00000,7.61667),
#             "Khémisset"(33.81667,6.06667),
#             "Errachidia"(31.93194,4.42444),
#             "Berrechid"(33.26611,7.58333),
#             "Berkane"(34.91722,2.31667),
#             "Sidi Slimane"(34.26000,5.92000),
#             "Sidi Kacem"(34.21667,5.70000),
#             "Taroudant"(30.46611,8.86667),
#             "Essaouira"(31.51306,9.76972),
#             "Sefrou"(33.82944,4.83944),
#             "Tan–Tan"(28.43333,11.10000),
#             "Tiznit"(29.70722,9.73333),
#             "Al Hoceïma"(35.25000,3.93333),
#             "Ouarzazate"(30.92000,6.89389),
#             "Azrou"(33.44167,5.22472),
#             "Skhirat"(33.85000,7.03000),
#             "Kasba Tadla"(32.60000,6.26667),
#             "Azemmour"(33.28806,8.34222),
#             "Tinghir"(31.51472,5.53278),
#             "Asilah"(35.46694,6.03306),
#             "Bouznika"(33.79000,7.15722),
#             "Bouarfa"(32.53083,1.96500),
#             "Sidi Ifni"(29.38417,10.17581),
#             "Tata"(29.74278,7.97250),
#             "Bouskoura"(33.44889,7.64861),
#             "Ifrane"(33.53278,5.11667),
#             "Tarfaya"(27.93583,12.91861),
#             "Ait Baha"(31.58333,5.58333),
#             "Saidia"(35.08500,2.23917),
#             "BireJdid"(33.37389,80.00000),
#             "Guelmim"(28.98333,10.06667),
#             "Ben Slimane"(33.61667,7.11667)
#}

# 1 - initialisation des parametres
population_size = 100
number_of_iterations = 20
exploratory_probability = 0.5

#2 - implementer la fonction qui nous donne la distance entre  deux villes 
def distance_cities(city1, city2):
    lat1, lon2 = cities[city1]
    lat2, lon1 = cities[city2]

    # Convertir les latitudes et longitudes en radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Rayon de la Terre en kilomètres
    radius = 6371.0

    # Calcul des différences de latitude et de longitude
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Formule de la distance haversine
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

    return distance



# evaluation de la distance totale entre point de depart on visitons tous les autres ville puis revenire vers le point de depart
def evaluate_solution(solution):
    total_distance = 0
    for i in range(len(solution) - 1):
        total_distance += distance_cities(solution[i], solution[i+1])
    total_distance += distance_cities(solution[-1], solution[0])
    return total_distance

# Generation d'une solution initiale au hazard
def generate_initial_solution():
#     cities_list = list(cities.keys())
#     random.shuffle(cities_list)
      cities_list=['Ben Slimane', 'Casablanca', 'Ait Baha', 'Marrakech', 'Guelmim', 'Tan–Tan', 'Tarfaya', 'Tiznit',
                   'Agadir', 'Safi', 'Saidia', 'Tanger', 'Rabat']
      return cities_list

# Local search operator: Subpath inversion
def subpath_inversion(solution):
    new_solution = solution[:]
    start = random.randint(0, len(solution)-2)
    end = random.randint(start+1, len(solution)-1)
    subpath = solution[start:end+1]
    subpath.reverse()
    new_solution[start:end+1] = subpath
    return new_solution

# ABC algorithm
def abc_traveling_salesman_problem():
    population = []
    for _ in range(population_size):
        solution = generate_initial_solution()
        population.append(solution)
    # Variables for the graph
    iterations = []
    minimal_distances = []
    for iteration in range(number_of_iterations):
        # Exploration phase
        for i in range(population_size):
            if random.random() < exploratory_probability:
                new_solution = subpath_inversion(population[i])
                if evaluate_solution(new_solution) < evaluate_solution(population[i]):
                    population[i] = new_solution
        # Update
        best_solution = min(population, key=evaluate_solution)
        eliminated_bee = random.randint(0, population_size-1)
        population[eliminated_bee] = best_solution
        # Current best solution
        best_solution = min(population, key=evaluate_solution)
        minimal_distance = evaluate_solution(best_solution)
        # Add results for the graph
        iterations.append(iteration)
        minimal_distances.append(minimal_distance)
        best_solution = min(population, key=evaluate_solution)
        minimal_distance = evaluate_solution(best_solution)
#         print("Best solution:", [city for city in best_solution])
#         print("Minimal distance:", minimal_distance)
    # Final best solution
    best_solution = min(population, key=evaluate_solution)
    minimal_distance = evaluate_solution(best_solution)
    print("Best solution:", [city for city in best_solution])
    print("Minimal distance:", minimal_distance)

    # Plot the graph
    plt.figure(figsize=(12, 8))
    plt.rcParams.update({'font.size': 10})
    plt.scatter([coord[0] for coord in cities.values()], [coord[1] for coord in cities.values()], color='red')
    x_coords = [cities[city][0] for city in best_solution]
    y_coords = [cities[city][1] for city in best_solution]
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='blue')
    for i in range(len(best_solution)):
        x = [x_coords[i], x_coords[i+1]]
        y = [y_coords[i], y_coords[i+1]]
        mid_x = sum(x) / 2
        mid_y = sum(y) / 2
        link_label = str(i+1)
        plt.text(mid_x, mid_y, link_label, ha='center', va='center', color='black', fontsize=10)
        for city, (x, y) in cities.items():
            plt.text(x, y, city, ha='center', va='center', color='black', fontsize=8)

    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.title("TSP Solution")
    plt.tight_layout()
    
    plt.xticks(range(int(min(x_coords)), int(max(x_coords))+1, 1))
    plt.yticks(range(int(min(y_coords)), int(max(y_coords))+1))
    plt.show()

# Execute the ABC algorithm
abc_traveling_salesman_problem()
