count = 0


def flasher():
    global count
    count += 1
    current_color = A.cget("fg")
    next_color = "green" if current_color == "red" else  "red"
    A.config(fg=next_color)
    if count < 10:
        root.after(1000,flasher)
    else:
        count = 0
