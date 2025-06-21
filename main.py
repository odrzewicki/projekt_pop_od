from tkinter import *
import tkintermapview
from models import Parking, Worker, User
from init_data import parkings_data, workers_data, users_data

root = Tk()
root.title("System Parkingowy")
root.geometry("1300x900")

frame_top = Frame(root)
frame_top.pack(pady=10)

frame_parking = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_parking.grid(row=0, column=0, padx=10)

frame_worker = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_worker.grid(row=0, column=1, padx=10)

frame_user = Frame(frame_top, bd=2, relief=GROOVE, padx=10, pady=10)
frame_user.grid(row=0, column=2, padx=10)

frame_maps = Frame(root)
frame_maps.pack(pady=20)

parkings, workers, users = [], [], []

# ============ PARKING ============

def add_parking():
    name = entry_parking_name.get()
    location = entry_parking_location.get()
    p = Parking(name, location, map_parking)
    parkings.append(p)
    listbox_parkings.insert(END, p.name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)

def show_parking_details():
    i = listbox_parkings.curselection()
    if i:
        selected = parkings[i[0]]
        label_parking_details.config(text=f"Lokalizacja: {selected.location}")

def edit_parking():
    i = listbox_parkings.curselection()
    if not i:
        return
    index = i[0]
    selected = parkings[index]
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)
    entry_parking_name.insert(0, selected.name)
    entry_parking_location.insert(0, selected.location)
    button_parking_add.config(text="Zapisz", command=lambda: save_parking(index))

def save_parking(index):
    new_name = entry_parking_name.get()
    new_location = entry_parking_location.get()
    parkings[index].marker.delete()
    parkings[index] = Parking(new_name, new_location, map_parking)
    listbox_parkings.delete(index)
    listbox_parkings.insert(index, new_name)
    entry_parking_name.delete(0, END)
    entry_parking_location.delete(0, END)
    button_parking_add.config(text="Dodaj", command=add_parking)

# ============ WORKER ============

def add_worker():
    name = entry_worker_name.get()
    parking = entry_worker_parking.get()
    location = entry_worker_location.get()
    w = Worker(name, parking, location, map_worker)
    workers.append(w)
    listbox_workers.insert(END, w.name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)

def show_worker_details():
    i = listbox_workers.curselection()
    if i:
        selected = workers[i[0]]
        label_worker_details.config(text=f"Parking: {selected.parking}, Lokalizacja: {selected.location}")

def edit_worker():
    i = listbox_workers.curselection()
    if not i:
        return
    index = i[0]
    selected = workers[index]
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)
    entry_worker_name.insert(0, selected.name)
    entry_worker_parking.insert(0, selected.parking)
    entry_worker_location.insert(0, selected.location)
    button_worker_add.config(text="Zapisz", command=lambda: save_worker(index))

def save_worker(index):
    new_name = entry_worker_name.get()
    new_parking = entry_worker_parking.get()
    new_location = entry_worker_location.get()
    workers[index].marker.delete()
    workers[index] = Worker(new_name, new_parking, new_location, map_worker)
    listbox_workers.delete(index)
    listbox_workers.insert(index, new_name)
    entry_worker_name.delete(0, END)
    entry_worker_parking.delete(0, END)
    entry_worker_location.delete(0, END)
    button_worker_add.config(text="Dodaj", command=add_worker)

# ============ USER ============

def add_user():
    name = entry_user_name.get()
    parking = entry_user_parking.get()
    location = entry_user_location.get()
    u = User(name, parking, location, map_user)
    users.append(u)
    listbox_users.insert(END, u.name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)

def show_user_details():
    i = listbox_users.curselection()
    if i:
        selected = users[i[0]]
        label_user_details.config(text=f"Parking: {selected.parking}, Lokalizacja: {selected.location}")

def edit_user():
    i = listbox_users.curselection()
    if not i:
        return
    index = i[0]
    selected = users[index]
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)
    entry_user_name.insert(0, selected.name)
    entry_user_parking.insert(0, selected.parking)
    entry_user_location.insert(0, selected.location)
    button_user_add.config(text="Zapisz", command=lambda: save_user(index))

def save_user(index):
    new_name = entry_user_name.get()
    new_parking = entry_user_parking.get()
    new_location = entry_user_location.get()
    users[index].marker.delete()
    users[index] = User(new_name, new_parking, new_location, map_user)
    listbox_users.delete(index)
    listbox_users.insert(index, new_name)
    entry_user_name.delete(0, END)
    entry_user_parking.delete(0, END)
    entry_user_location.delete(0, END)
    button_user_add.config(text="Dodaj", command=add_user)

# ============ FORMULARZE ============

# Parking
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
Button(frame_parking, text="Szczegóły", command=show_parking_details).grid(row=5, column=0)
Button(frame_parking, text="Edytuj", command=edit_parking).grid(row=5, column=1)
label_parking_details = Label(frame_parking, text="...")
label_parking_details.grid(row=6, column=0, columnspan=2)

# Worker
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
Button(frame_worker, text="Szczegóły", command=show_worker_details).grid(row=6, column=0)
Button(frame_worker, text="Edytuj", command=edit_worker).grid(row=6, column=1)
label_worker_details = Label(frame_worker, text="...")
label_worker_details.grid(row=7, column=0, columnspan=2)

# User
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
Button(frame_user, text="Szczegóły", command=show_user_details).grid(row=6, column=0)
Button(frame_user, text="Edytuj", command=edit_user).grid(row=6, column=1)
label_user_details = Label(frame_user, text="...")
label_user_details.grid(row=7, column=0, columnspan=2)

# ============ MAPS ============

Label(frame_maps, text="Mapa parkingów").grid(row=0, column=0)
Label(frame_maps, text="Mapa pracowników").grid(row=0, column=1)
Label(frame_maps, text="Mapa użytkowników").grid(row=0, column=2)

map_parking = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_parking.grid(row=1, column=0)
map_parking.set_position(52.23, 21.01)
map_parking.set_zoom(6)

map_worker = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_worker.grid(row=1, column=1)
map_worker.set_position(52.23, 21.01)
map_worker.set_zoom(6)

map_user = tkintermapview.TkinterMapView(frame_maps, width=380, height=300)
map_user.grid(row=1, column=2)
map_user.set_position(52.23, 21.01)
map_user.set_zoom(6)

# ============ LOAD START DATA ============

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
