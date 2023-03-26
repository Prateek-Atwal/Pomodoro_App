from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
after_id = None
reps = 0
timer = "00:00"
check_mark_string = ""


def start_countdown():
    global reps
    global check_mark_string
    reps += 1
    work_sec = 60*WORK_MIN
    short_break_sec = 60*SHORT_BREAK_MIN
    long_break_sec = 60*LONG_BREAK_MIN
    if reps % 8 == 0:
        header.config(width=20, text=f"Long Break - {round(reps/8)}", font=(FONT_NAME, 20, "bold"), fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 1:
        if len(check_mark_string) < 14:
            check_mark_string += CHECK_MARK
        else:
            check_mark_string = f"{round(reps//2 + reps % 2)} {CHECK_MARK}"
        check_mark.config(text=check_mark_string)
        header.config(width=20, text=f"Work Session - {round(reps//2 + reps % 2)}", font=(FONT_NAME, 20, "bold")
                      , fg=GREEN)
        countdown(work_sec)
    elif reps % 2 == 0:
        header.config(width=20, text=f"Short Break - {round(reps/2)}", font=(FONT_NAME, 20, "bold"), fg=PINK)
        countdown(short_break_sec)


def reset_countdown():
    global after_id
    global check_mark_string
    global reps
    window.after_cancel(after_id)
    img.itemconfig(time_label, text=timer, font=(FONT_NAME, 40, "bold"))
    header.config(width=10, text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN)
    check_mark_string = CHECK_MARK
    check_mark.config(text=check_mark_string)
    reps = 0


def countdown(count):
    global after_id
    if count > 0:
        update_time(count)
        after_id = window.after(1000, countdown, count-1)
    else:
        start_countdown()


def update_time(t_left):
    t_left -= 1
    time_minutes = t_left // 60
    time_seconds = t_left % 60
    if time_seconds < 10:
        time_seconds = "0" + str(time_seconds)
    if time_minutes < 10:
        time_minutes = "0" + str(time_minutes)
    cur_timer = str(time_minutes) + ":" + str(time_seconds)
    img.itemconfig(time_label, text=cur_timer)
    print(cur_timer)


window = Tk()
window.title("Pomodoro App")
# window.minsize(width=500, height=400)
window.config(padx=50, pady=50, bg=YELLOW)


img = Canvas(width=210, height=224)
bg_img = PhotoImage(file="tomato.png")
img.create_image(103, 112, image=bg_img)
time_label = img.create_text(103, 130, text=timer, fill="white", font=(FONT_NAME, 40, "bold"))
img.grid(row=1, column=1)
img.config(bg=YELLOW, highlightbackground=YELLOW)


header = Label(text="Timer", width=10, font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
header.grid(row=0, column=1)

start_button = Button(text="Start", bg="white", command=start_countdown, width=7, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg="white", command=reset_countdown, width=7, highlightthickness=0)
reset_button.grid(row=2, column=2)

check_mark = Label(text=check_mark_string, width=25, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_mark.grid(row=4, column=1)

window.mainloop()
