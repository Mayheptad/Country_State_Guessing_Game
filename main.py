
import csv

# import pandas as pd
# with open('weather-data.csv') as wd:
#     data = csv.reader(wd)
#     temp = []
#     for d in data:
#         if d[1] != 'temp':
#             temp.append(int(d[1]))
#     print(temp)

# data = pd.read_csv('weather-data.csv')

# temp_list = data['temp'].to_list()
# sum_list = sum(temp_list)
# calc_average = sum_list / len(temp_list)
# print(calc_average)

# print(data['temp'].max())
# print(data['temp'].mean())

# get data in columns
# data['column_name']
# data.column_name

# get data in row
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# to_fah = monday.temp.apply(lambda self: self * 9/5 + 32)
# print(int(to_fah))

# create dataframe from scratch
# data_dict = {
#     'student': ['bill', 'mayheptad', 'ritchie'],
#     'scores': [76, 56, 65]
# }

# convert dictionary to panda dataframe
# pd_dataframe_data = pd.DataFrame(data_dict)

# convert panda dataframe to csv
# print(pd_dataframe_data.to_csv('new_data.csv'))


# csv_data = pd.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
#
# grey_rows = csv_data[csv_data['Primary Fur Color'] == 'Gray']
# red_rows = csv_data[csv_data['Primary Fur Color'] == 'Cinnamon']
# black_rows = csv_data[csv_data['Primary Fur Color'] == 'Black']
#
# grey_row_count = len(grey_rows)
# red_row_count = len(red_rows)
# black_row_count = len(black_rows)
#
# data_dict = {
#     'For Color': ['Grey', 'Red', 'Black'],
#     'Count': [grey_row_count, red_row_count, black_row_count]
# }
#
# dt_data_from_dict_2_csv = pd.DataFrame.from_dict(data_dict).to_csv('sp_squirrel.csv')
#
# print(dt_data_from_dict_2_csv)

import turtle as tr
import pandas as pd
from tkinter import messagebox

sc = tr.Screen()
sc.title('The_Us_State_Game')

img = 'blank_states_img.gif'

sc.addshape(img)
tr.shape(img)

us_state_data = pd.read_csv('50_states.csv')
us_state_list = us_state_data['state'].to_list()

correct_guess_list = []

while len(correct_guess_list) < 50:

    user_answer = sc.textinput(f'{len(correct_guess_list)}/50 state correct', 'guess another us state name').title()

    if user_answer == 'Exit':

        remaining_states = [state for state in us_state_list if state not in correct_guess_list]

        for state in remaining_states:
            x = us_state_data[us_state_data.state == state].x.item()
            y = us_state_data[us_state_data.state == state].y.item()

            states_to_learn = {
                'states': remaining_states,
                'x': x,
                'y': y
            }

            states_to_learn_csv = pd.DataFrame.from_dict(states_to_learn).to_csv('states_to_learn.csv')
        break

    if user_answer in us_state_list and user_answer not in correct_guess_list:
        correct_guess_list.append(user_answer)
        correct_row = us_state_data[us_state_data.state == user_answer]
        tut = tr.Turtle()
        tut.hideturtle()
        tut.penup()
        tut.goto(int(correct_row.x), int(correct_row.y))
        tut.pendown()
        tut.write(correct_row.state.item())
    else:
        messagebox.showinfo("Something Seems Wrong",
                            "Either the name you guessed is not in the US or you have guessed it before "
                            "try again")

sc.mainloop()
