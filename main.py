from tkinter import *
import tkintermapview
from models import Parking, Worker, User
from init_data import parkings_data, workers_data, users_data

root = Tk()
root.title("System Mapa MJ")
root.geometry("1200x600")

frame_maps = Frame(root)
frame_maps.pack(pady=20)

# Mapa parkingów
Label(frame_maps, text="Mapa parkingów").grid(row=0, column=0)
map_parking = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_parking.grid(row=1, column=0, padx=5)
map_parking.set_position(52.23, 21.01)
map_parking.set_zoom(6)

# Mapa pracowników
Label(frame_maps, text="Mapa pracowników").grid(row=0, column=1)
map_worker = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_worker.grid(row=1, column=1, padx=5)
map_worker.set_position(52.23, 21.01)
map_worker.set_zoom(6)

# Mapa użytkowników
Label(frame_maps, text="Mapa użytkowników").grid(row=0, column=2)
map_user = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_user.grid(row=1, column=2, padx=5)
map_user.set_position(52.23, 21.01)
map_user.set_zoom(6)

# Tworzenie obiektów
parkings = [Parking(p["parking_name"], p["parking_location"], map_parking) for p in parkings_data]
workers = [Worker(w["worker_name"], w["worker_parking"], w["worker_location"], map_worker) for w in workers_data]
users = [User(u["user_name"], u["user_parking"], u["user_location"], map_user) for u in users_data]

root.mainloop()
