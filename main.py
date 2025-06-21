from tkinter import *
import tkintermapview

from init_data import parkings_data, workers_data, users_data
from models import Parking, Worker, User
from geo_utils import get_coordinates

# ==================== LISTY ====================
parkings = []
workers = []
users = []

# ==================== FUNKCJE ====================

def add_parking():
    name = entry_parking_name.get()
    location = entry_parking_location.get()
    coordinates = get_coordinates(location)
    obj = Parking(name, location, coordinates, map_parking)
    parkings.append(obj)
    listbox_parkings.insert(END, obj.name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)

def show_parking_details():
    idx = listbox_parkings.curselection()
    if idx:
        obj = parkings[idx[0]]
        label_parking_details.config(text=f"Lokalizacja: {obj.location}")

def edit_parking():
    idx = listbox_parkings.curselection()
    if idx:
        obj = parkings[idx[0]]
        entry_parking_name.delete(0, END)
        entry_parking_location.delete(0, END)
        entry_parking_name.insert(0, obj.name)
        entry_parking_location.insert(0, obj.location)
        button_parking_add.config(text="Zapisz", command=lambda: save_parking(idx[0]))

def save_parking(index):
    name = entry_parking_name.get()
    location = entry_parking_location.get()
    coordinates = get_coordinates(location)
    parkings[index].marker.delete()
    parkings[index].name = name
    parkings[index].location = location
    parkings[index].coordinates = coordinates
    parkings[index].marker = map_parking.set_marker(*coordinates, text=name)
    listbox_parkings.delete(index)
    listbox_parkings.insert(index, name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)
    button_parking_add.config(text="Dodaj", command=add_parking)

# === WORKERS ===

def add_worker():
    name = entry_worker_name.get()
    parking = entry_worker_parking.get()
    location = entry_worker_location.get()
    coordinates = get_coordinates(location)
    obj = Worker(name, parking, location, coordinates, map_worker)
    workers.append(obj)
    listbox_workers.insert(END, obj.name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)

def show_worker_details():
    idx = listbox_workers.curselection()
    if idx:
        obj = workers[idx[0]]
        label_worker_details.config(text=f"Parking: {obj.parking}, Lokalizacja: {obj.location}")

def edit_worker():
    idx = listbox_workers.curselection()
    if idx:
        obj = workers[idx[0]]
        entry_worker_name.delete(0, END)
        entry_worker_parking.delete(0, END)
        entry_worker_location.delete(0, END)
        entry_worker_name.insert(0, obj.name)
        entry_worker_parking.insert(0, obj.parking)
        entry_worker_location.insert(0, obj.location)
        button_worker_add.config(text="Zapisz", command=lambda: save_worker(idx[0]))

def save_worker(index):
    name = entry_worker_name.get()
    parking = entry_worker_parking.get()
    location = entry_worker_location.get()
    coordinates = get_coordinates(location)
    workers[index].marker.delete()
    workers[index].name = name
    workers[index].parking = parking
    workers[index].location = location
    workers[index].coordinates = coordinates
    workers[index].marker = map_worker.set_marker(*coordinates, text=name)
    listbox_workers.delete(index)
    listbox_workers.insert(index, name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)
    button_worker_add.config(text="Dodaj", command=add_worker)

# === USERS ===

def add_user():
    name = entry_user_name.get()
    parking = entry_user_parking.get()
    location = entry_user_location.get()
    coordinates = get_coordinates(location)
    obj = User(name, parking, location, coordinates, map_user)
    users.append(obj)
    listbox_users.insert(END, obj.name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)

def show_user_details():
    idx = listbox_users.curselection()
    if idx:
        obj = users[idx[0]]
        label_user_details.config(text=f"Parking: {obj.parking}, Lokalizacja: {obj.location}")

def edit_user():
    idx = listbox_users.curselection()
    if idx:
        obj = users[idx[0]]
        entry_user_name.delete(0, END)
        entry_user_parking.delete(0, END)
        entry_user_location.delete(0, END)
        entry_user_name.insert(0, obj.name)
        entry_user_parking.insert(0, obj.parking)
        entry_user_location.insert(0, obj.location)
        button_user_add.config(text="Zapisz", command=lambda: save_user(idx[0]))

def save_user(index):
    name = entry_user_name.get()
    parking = entry_user_parking.get()
    location = entry_user_location.get()
    coordinates = get_coordinates(location)
    users[index].marker.delete()
    users[index].name = name
    users[index].parking = parking
    users[index].location = location
    users[index].coordinates = coordinates
    users[index].marker = map_user.set_marker(*coordinates, text=name)
    listbox_users.delete(index)
    listbox_users.insert(index, name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)
    button_user_add.config(text="Dodaj", command=add_user)

# ==================== GUI ====================

root = Tk()
root.title("System Parkingowy")
root.geometry("1300x900")

frame_top = Frame(root)
frame_top.pack(pady=10)

frame_maps = Frame(root)
frame_maps.pack(pady=10)

# === Parkingi ===
frame_parking = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_parking.grid(row=0, column=0, padx=10)

Label(frame_parking, text="Dodaj parking").grid(row=0, column=0, columnspan=2)
Label(frame_parking, text="Nazwa:").grid(row=1, column=0)
entry_parking_name = Entry(frame_parking)
entry_parking_name.grid(row=1, column=1)
Label(frame_parking, text="Lokalizacja:").grid(row=2, column=0)
entry_parking_location = Entry(frame_parking)
entry_parking_location.grid(row=2, column=1)
button_parking_add = Button(frame_parking, text="Dodaj", command=add_parking)
button_parking_add.grid(row=3, column=0, columnspan=2)
listbox_parkings = Listbox(frame_parking, width=30)
listbox_parkings.grid(row=4, column=0, columnspan=2)
Button(frame_parking, text="Szczegóły", command=show_parking_details).grid(row=5, column=0)
Button(frame_parking, text="Edytuj", command=edit_parking).grid(row=5, column=1)
label_parking_details = Label(frame_parking, text="...")
label_parking_details.grid(row=6, column=0, columnspan=2)

# === Pracownicy ===
frame_worker = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_worker.grid(row=0, column=1, padx=10)

Label(frame_worker, text="Dodaj pracownika").grid(row=0, column=0, columnspan=2)
Label(frame_worker, text="Imię i nazwisko:").grid(row=1, column=0)
entry_worker_name = Entry(frame_worker)
entry_worker_name.grid(row=1, column=1)
Label(frame_worker, text="Parking:").grid(row=2, column=0)
entry_worker_parking = Entry(frame_worker)
entry_worker_parking.grid(row=2, column=1)
Label(frame_worker, text="Lokalizacja:").grid(row=3, column=0)
entry_worker_location = Entry(frame_worker)
entry_worker_location.grid(row=3, column=1)
button_worker_add = Button(frame_worker, text="Dodaj", command=add_worker)
button_worker_add.grid(row=4, column=0, columnspan=2)
listbox_workers = Listbox(frame_worker, width=30)
listbox_workers.grid(row=5, column=0, columnspan=2)
Button(frame_worker, text="Szczegóły", command=show_worker_details).grid(row=6, column=0)
Button(frame_worker, text="Edytuj", command=edit_worker).grid(row=6, column=1)
label_worker_details = Label(frame_worker, text="...")
label_worker_details.grid(row=7, column=0, columnspan=2)

# === Użytkownicy ===
frame_user = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_user.grid(row=0, column=2, padx=10)

Label(frame_user, text="Dodaj użytkownika").grid(row=0, column=0, columnspan=2)
Label(frame_user, text="Imię i nazwisko:").grid(row=1, column=0)
entry_user_name = Entry(frame_user)
entry_user_name.grid(row=1, column=1)
Label(frame_user, text="Parking:").grid(row=2, column=0)
entry_user_parking = Entry(frame_user)
entry_user_parking.grid(row=2, column=1)
Label(frame_user, text="Lokalizacja:").grid(row=3, column=0)
entry_user_location = Entry(frame_user)
entry_user_location.grid(row=3, column=1)
button_user_add = Button(frame_user, text="Dodaj", command=add_user)
button_user_add.grid(row=4, column=0, columnspan=2)
listbox_users = Listbox(frame_user, width=30)
listbox_users.grid(row=5, column=0, columnspan=2)
Button(frame_user, text="Szczegóły", command=show_user_details).grid(row=6, column=0)
Button(frame_user, text="Edytuj", command=edit_user).grid(row=6, column=1)
label_user_details = Label(frame_user, text="...")
label_user_details.grid(row=7, column=0, columnspan=2)

# === MAPY ===
Label(frame_maps, text="Mapa parkingów").grid(row=0, column=0)
Label(frame_maps, text="Mapa pracowników").grid(row=0, column=1)
Label(frame_maps, text="Mapa użytkowników").grid(row=0, column=2)

map_parking = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_parking.grid(row=1, column=0, padx=10)
map_parking.set_position(52.23, 21.01)
map_parking.set_zoom(6)

map_worker = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_worker.grid(row=1, column=1, padx=10)
map_worker.set_position(52.23, 21.01)
map_worker.set_zoom(6)

map_user = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_user.grid(row=1, column=2, padx=10)
map_user.set_position(52.23, 21.01)
map_user.set_zoom(6)

# ========== LOAD START DATA ==========

for p in parkings_data:
    obj = Parking(p["parking_name"], p["parking_location"], map_parking)
    parkings.append(obj)
    listbox_parkings.insert(END, obj.name)

for w in workers_data:
    obj = Worker(w["worker_name"], w["worker_parking"], w["worker_location"], map_worker)
    workers.append(obj)
    listbox_workers.insert(END, obj.name)

for u in users_data:
    obj = User(u["user_name"], u["user_parking"], u["user_location"], map_user)
    users.append(obj)
    listbox_users.insert(END, obj.name)


root.mainloop()
