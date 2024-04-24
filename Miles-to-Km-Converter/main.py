from tkinter import *


def calculate_conversion_button():
    user_miles = miles_input.get()
    user_km = round(float(user_miles) * 1.609, 2)
    output_km_label.config(text=str(user_km))

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=10)


#User input
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Text Labels
miles_label = Label(text=" Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

km_label = Label(text=" Km")
km_label.grid(column=2, row=1)

output_km_label = Label(text="0")
output_km_label.grid(column=1, row=1)

#Calculate button
calc_button = Button(text="Calculate", command=calculate_conversion_button)
calc_button.grid(column=1, row=2)







window.mainloop()