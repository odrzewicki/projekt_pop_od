from tkinter import *
import tkintermapview
from tkinter import messagebox
from models import Parking, Worker, User
from init_data import parkings_data, workers_data, users_data
from geo_utils import get_coordinates

root = Tk()
root.configure(bg="#e6f2ff")  # np. jasnoniebieski
root.title("System Parkingowy")
root.geometry("1300x900")

frame_top = Frame(root)
frame_top.pack(pady=10)

frame_maps = Frame(root)
frame_maps.pack(pady=20)

frame_parking = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_parking.grid(row=0, column=0, padx=10)

frame_worker = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_worker.grid(row=0, column=1, padx=10)

frame_user = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_user.grid(row=0, column=2, padx=10)

parkings, workers, users = [], [], []

# ============ PARKING FUNKCJE ============

def add_parking():
    name = entry_parking_name.get()
    location = entry_parking_location.get()
    if not name or not location:
        return
    obj = Parking(name, location, map_parking)
    parkings.append(obj)
    listbox_parkings.insert(END, obj.name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)

def show_parking_details():
    selected = listbox_parkings.curselection()
    if not selected:
        return
    obj = parkings[selected[0]]
    label_parking_details.config(text=f"Lokalizacja: {obj.location}")

def edit_parking():
    selected = listbox_parkings.curselection()
    if not selected:
        return
    index = selected[0]
    obj = parkings[index]
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)
    entry_parking_name.insert(0, obj.name)
    entry_parking_location.insert(0, obj.location)
    button_parking_add.config(text="Zapisz", command=lambda: save_parking(index))

def save_parking(index):
    name = entry_parking_name.get()
    location = entry_parking_location.get()
    obj = parkings[index]
    obj.marker.delete()
    obj.name = name
    obj.location = location
    obj.coordinates = get_coordinates(location)
    obj.marker = map_parking.set_marker(*obj.coordinates, text=obj.name)
    listbox_parkings.delete(index)
    listbox_parkings.insert(index, name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)
    button_parking_add.config(text="Dodaj", command=add_parking)

# ============ WORKER FUNKCJE ============

def add_worker():
    name = entry_worker_name.get()
    parking = entry_worker_parking.get()
    location = entry_worker_location.get()
    if not name or not parking or not location:
        return

    # Sprawdzenie czy parking istnieje
    if parking not in [p.name for p in parkings]:
        messagebox.showerror("Błąd", "Nie ma takiego parkingu.")
        return

    obj = Worker(name, parking, location, map_worker)
    workers.append(obj)
    listbox_workers.insert(END, obj.name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)

def show_worker_details():
    selected = listbox_workers.curselection()
    if not selected:
        return
    obj = workers[selected[0]]
    label_worker_details.config(text=f"Parking: {obj.parking}, Lokalizacja: {obj.location}")

def edit_worker():
    selected = listbox_workers.curselection()
    if not selected:
        return
    index = selected[0]
    obj = workers[index]
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)
    entry_worker_name.insert(0, obj.name)
    entry_worker_parking.insert(0, obj.parking)
    entry_worker_location.insert(0, obj.location)
    button_worker_add.config(text="Zapisz", command=lambda: save_worker(index))

def save_worker(index):
    name = entry_worker_name.get()
    parking = entry_worker_parking.get()
    location = entry_worker_location.get()
    obj = workers[index]
    obj.marker.delete()
    obj.name = name
    obj.parking = parking
    obj.location = location
    obj.coordinates = get_coordinates(location)
    obj.marker = map_worker.set_marker(*obj.coordinates, text=obj.name)
    listbox_workers.delete(index)
    listbox_workers.insert(index, name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)
    button_worker_add.config(text="Dodaj", command=add_worker)

# ============ USER FUNKCJE ============

def add_user():
    name = entry_user_name.get()
    parking = entry_user_parking.get()
    location = entry_user_location.get()
    if not name or not parking or not location:
        return

    # Sprawdzenie czy parking istnieje
    if parking not in [p.name for p in parkings]:
        messagebox.showerror("Błąd", "Nie ma takiego parkingu.")
        return

    obj = User(name, parking, location, map_user)
    users.append(obj)
    listbox_users.insert(END, obj.name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)

def show_user_details():
    selected = listbox_users.curselection()
    if not selected:
        return
    obj = users[selected[0]]
    label_user_details.config(text=f"Parking: {obj.parking}, Lokalizacja: {obj.location}")

def edit_user():
    selected = listbox_users.curselection()
    if not selected:
        return
    index = selected[0]
    obj = users[index]
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)
    entry_user_name.insert(0, obj.name)
    entry_user_parking.insert(0, obj.parking)
    entry_user_location.insert(0, obj.location)
    button_user_add.config(text="Zapisz", command=lambda: save_user(index))

def save_user(index):
    name = entry_user_name.get()
    parking = entry_user_parking.get()
    location = entry_user_location.get()
    obj = users[index]
    obj.marker.delete()
    obj.name = name
    obj.parking = parking
    obj.location = location
    obj.coordinates = get_coordinates(location)
    obj.marker = map_user.set_marker(*obj.coordinates, text=obj.name)
    listbox_users.delete(index)
    listbox_users.insert(index, name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)
    button_user_add.config(text="Dodaj", command=add_user)

# ============ FORMULARZE GUI ============

# PARKING
Label(frame_parking, text="Dodaj parking").grid(row=0, column=0, columnspan=2)
Label(frame_parking, text="Nazwa:").grid(row=1, column=0)
entry_parking_name = Entry(frame_parking)
entry_parking_name.grid(row=1, column=1)
Label(frame_parking, text="Lokalizacja:").grid(row=2, column=0)
entry_parking_location = Entry(frame_parking)
entry_parking_location.grid(row=2, column=1)
button_parking_add = Button(frame_parking, text="Dodaj", command=add_parking)
button_parking_add.grid(row=3, column=0, columnspan=2, pady=5)
listbox_parkings = Listbox(frame_parking, width=30, height=5)
listbox_parkings.grid(row=4, column=0, columnspan=2)
Button(frame_parking, text="Szczegóły", command=show_parking_details).grid(row=5, column=0, columnspan=2)
Button(frame_parking, text="Edytuj", command=edit_parking).grid(row=6, column=0, columnspan=2)
label_parking_details = Label(frame_parking, text="...")
label_parking_details.grid(row=7, column=0, columnspan=2)

# Dodaj pusty label dla zachowania proporcji
Label(frame_parking).grid(row=8, column=0, columnspan=2)

# WORKER
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
button_worker_add.grid(row=4, column=0, columnspan=2, pady=5)
listbox_workers = Listbox(frame_worker, width=30, height=5)
listbox_workers.grid(row=5, column=0, columnspan=2)
Button(frame_worker, text="Szczegóły", command=show_worker_details).grid(row=6, column=0, columnspan=2)
Button(frame_worker, text="Edytuj", command=edit_worker).grid(row=7, column=0, columnspan=2)
label_worker_details = Label(frame_worker, text="...")
label_worker_details.grid(row=8, column=0, columnspan=2)

# USER
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
button_user_add.grid(row=4, column=0, columnspan=2, pady=5)
listbox_users = Listbox(frame_user, width=30, height=5)
listbox_users.grid(row=5, column=0, columnspan=2)
Button(frame_user, text="Szczegóły", command=show_user_details).grid(row=6, column=0, columnspan=2)
Button(frame_user, text="Edytuj", command=edit_user).grid(row=7, column=0, columnspan=2)
label_user_details = Label(frame_user, text="...")
label_user_details.grid(row=8, column=0, columnspan=2)

# ============ MAPY ============

Label(frame_maps, text="Mapa parkingów").grid(row=0, column=0)
Label(frame_maps, text="Mapa pracowników").grid(row=0, column=1)
Label(frame_maps, text="Mapa użytkowników").grid(row=0, column=2)

map_parking = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_parking.grid(row=1, column=0, padx=5)
map_parking.set_position(52.23, 21.01)
map_parking.set_zoom(6)

map_worker = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_worker.grid(row=1, column=1, padx=5)
map_worker.set_position(52.23, 21.01)
map_worker.set_zoom(6)

map_user = tkintermapview.TkinterMapView(frame_maps, width=400, height=300)
map_user.grid(row=1, column=2, padx=5)
map_user.set_position(52.23, 21.01)
map_user.set_zoom(6)

# ============ DANE STARTOWE ============

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
