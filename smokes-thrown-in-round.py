from awpy import Demo
from awpy.plot import plot
import matplotlib.pyplot as plt

#EX 2
#show smokes thrown in a specific round

dem = Demo("spirit-vs-faze-m1-nuke.dem")

selected_round = 5
smokes = dem.smokes

# Filtruj tylko dymy z wybranej rundy
smokes_filtered = smokes[smokes["round"] == selected_round]

if smokes_filtered.empty:
    print(f"no smokes found in {selected_round} round!")
else:
    points = []
    point_settings = []

    for _, row in smokes_filtered.iterrows():
        points.append((row['X'], row['Y'], row['Z']))
        point_settings.append({
            'color': 'grey',
            'size': 10,
            'marker': 'o'
        })

    plot("de_nuke", points, point_settings)
    plt.title(f"smokes thrown in {selected_round}", color='white')  # Dodaj tytuł
    plt.show()