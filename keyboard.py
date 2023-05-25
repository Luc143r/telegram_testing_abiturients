from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


###############
# Кнопка отмены
###############


button_cancel = InlineKeyboardButton('Cancel', callback_data='/cancel')
markup_cancel = InlineKeyboardMarkup()
markup_cancel.row(button_cancel)

button_back_to_menu = InlineKeyboardButton(
    'Вернуться в меню', callback_data='/back_to_menu')
markup_back_to_menu = InlineKeyboardMarkup()
markup_back_to_menu.row(button_back_to_menu)

button_cancel_rebus = InlineKeyboardButton(
    'Cancel', callback_data='/cancel_rebus')
markup_cancel_rebus = InlineKeyboardMarkup()
markup_cancel_rebus.row(button_cancel_rebus)

##############
# Главное меню
##############


button_test_one = InlineKeyboardButton(
    'Какая профессия из мира рекламы тебе подходит', callback_data='/test_one')
button_test_two = InlineKeyboardButton(
    'Какой слоган удачный', callback_data='/test_two')
button_test_three = InlineKeyboardButton(
    'Кто сказал это', callback_data='/test_three')
button_test_four = InlineKeyboardButton(
    'Насколько специальность тебе подходит', callback_data='/test_four')
button_test_five = InlineKeyboardButton(
    'Практико-ориентированные задачи', callback_data='/test_five')
button_rebus = InlineKeyboardButton('Ребусы', callback_data='/rebus')
markup_start_menu = InlineKeyboardMarkup()
markup_start_menu.row(button_test_one)
markup_start_menu.row(button_test_two)
markup_start_menu.row(button_test_three)
markup_start_menu.row(button_test_four)
markup_start_menu.row(button_test_five)
markup_start_menu.row(button_rebus)


#######################
# Выбор ответа (Тест 1)
#######################


button_a_1 = InlineKeyboardButton('A', callback_data='/response_a_1')
button_b_1 = InlineKeyboardButton('B', callback_data='/response_b_1')
button_c_1 = InlineKeyboardButton('C', callback_data='/response_c_1')
button_d_1 = InlineKeyboardButton('D', callback_data='/response_d_1')
markup_keyboard_abcd_1 = InlineKeyboardMarkup()
markup_keyboard_abcd_1.row(button_a_1, button_b_1, button_c_1, button_d_1)
markup_keyboard_abcd_1.row(button_cancel)


button_a_2 = InlineKeyboardButton('A', callback_data='/response_a_2')
button_b_2 = InlineKeyboardButton('B', callback_data='/response_b_2')
button_c_2 = InlineKeyboardButton('C', callback_data='/response_c_2')
button_d_2 = InlineKeyboardButton('D', callback_data='/response_d_2')
markup_keyboard_abcd_2 = InlineKeyboardMarkup()
markup_keyboard_abcd_2.row(button_a_2, button_b_2, button_c_2, button_d_2)
markup_keyboard_abcd_2.row(button_cancel)


button_a_3 = InlineKeyboardButton('A', callback_data='/response_a_3')
button_b_3 = InlineKeyboardButton('B', callback_data='/response_b_3')
button_c_3 = InlineKeyboardButton('C', callback_data='/response_c_3')
button_d_3 = InlineKeyboardButton('D', callback_data='/response_d_3')
markup_keyboard_abcd_3 = InlineKeyboardMarkup()
markup_keyboard_abcd_3.row(button_a_3, button_b_3, button_c_3, button_d_3)
markup_keyboard_abcd_3.row(button_cancel)


button_a_4 = InlineKeyboardButton('A', callback_data='/response_a_4')
button_b_4 = InlineKeyboardButton('B', callback_data='/response_b_4')
button_c_4 = InlineKeyboardButton('C', callback_data='/response_c_4')
button_d_4 = InlineKeyboardButton('D', callback_data='/response_d_4')
markup_keyboard_abcd_4 = InlineKeyboardMarkup()
markup_keyboard_abcd_4.row(button_a_4, button_b_4, button_c_4, button_d_4)
markup_keyboard_abcd_4.row(button_cancel)


button_a_5 = InlineKeyboardButton('A', callback_data='/response_a_5')
button_b_5 = InlineKeyboardButton('B', callback_data='/response_b_5')
button_c_5 = InlineKeyboardButton('C', callback_data='/response_c_5')
button_d_5 = InlineKeyboardButton('D', callback_data='/response_d_5')
markup_keyboard_abcd_5 = InlineKeyboardMarkup()
markup_keyboard_abcd_5.row(button_a_5, button_b_5, button_c_5, button_d_5)
markup_keyboard_abcd_5.row(button_cancel)

button_a_6 = InlineKeyboardButton('A', callback_data='/response_a_6')
button_b_6 = InlineKeyboardButton('B', callback_data='/response_b_6')
button_c_6 = InlineKeyboardButton('C', callback_data='/response_c_6')
button_d_6 = InlineKeyboardButton('D', callback_data='/response_d_6')
markup_keyboard_abcd_6 = InlineKeyboardMarkup()
markup_keyboard_abcd_6.row(button_a_6, button_b_6, button_c_6, button_d_6)
markup_keyboard_abcd_6.row(button_cancel)


button_a_7 = InlineKeyboardButton('A', callback_data='/response_a_7')
button_b_7 = InlineKeyboardButton('B', callback_data='/response_b_7')
button_c_7 = InlineKeyboardButton('C', callback_data='/response_c_7')
button_d_7 = InlineKeyboardButton('D', callback_data='/response_d_7')
markup_keyboard_abcd_7 = InlineKeyboardMarkup()
markup_keyboard_abcd_7.row(button_a_7, button_b_7, button_c_7, button_d_7)
markup_keyboard_abcd_7.row(button_cancel)


button_a_8 = InlineKeyboardButton('A', callback_data='/response_a_8')
button_b_8 = InlineKeyboardButton('B', callback_data='/response_b_8')
button_c_8 = InlineKeyboardButton('C', callback_data='/response_c_8')
button_d_8 = InlineKeyboardButton('D', callback_data='/response_d_8')
markup_keyboard_abcd_8 = InlineKeyboardMarkup()
markup_keyboard_abcd_8.row(button_a_8, button_b_8, button_c_8, button_d_8)
markup_keyboard_abcd_8.row(button_cancel)


button_a_9 = InlineKeyboardButton('A', callback_data='/response_a_9')
button_b_9 = InlineKeyboardButton('B', callback_data='/response_b_9')
button_c_9 = InlineKeyboardButton('C', callback_data='/response_c_9')
button_d_9 = InlineKeyboardButton('D', callback_data='/response_d_9')
markup_keyboard_abcd_9 = InlineKeyboardMarkup()
markup_keyboard_abcd_9.row(button_a_9, button_b_9, button_c_9, button_d_9)
markup_keyboard_abcd_9.row(button_cancel)


button_a_10 = InlineKeyboardButton('A', callback_data='/response_a_10')
button_b_10 = InlineKeyboardButton('B', callback_data='/response_b_10')
button_c_10 = InlineKeyboardButton('C', callback_data='/response_c_10')
button_d_10 = InlineKeyboardButton('D', callback_data='/response_d_10')
markup_keyboard_abcd_10 = InlineKeyboardMarkup()
markup_keyboard_abcd_10.row(button_a_10, button_b_10, button_c_10, button_d_10)
markup_keyboard_abcd_10.row(button_cancel)


#######################
# Выбор ответа (Тест 2)
#######################


button_a_1_2 = InlineKeyboardButton('А', callback_data='/response_a_1_2')
button_b_1_2 = InlineKeyboardButton('Б', callback_data='/response_b_1_2')
button_w_1_2 = InlineKeyboardButton('В', callback_data='/response_w_1_2')
markup_keyboard_abw_1 = InlineKeyboardMarkup()
markup_keyboard_abw_1.row(button_a_1_2, button_b_1_2, button_w_1_2)
markup_keyboard_abw_1.row(button_cancel)


button_a_2_2 = InlineKeyboardButton('А', callback_data='/response_a_2_2')
button_b_2_2 = InlineKeyboardButton('Б', callback_data='/response_b_2_2')
button_w_2_2 = InlineKeyboardButton('В', callback_data='/response_w_2_2')
markup_keyboard_abw_2 = InlineKeyboardMarkup()
markup_keyboard_abw_2.row(button_a_2_2, button_b_2_2, button_w_2_2)
markup_keyboard_abw_2.row(button_cancel)


button_a_3_2 = InlineKeyboardButton('А', callback_data='/response_a_3_2')
button_b_3_2 = InlineKeyboardButton('Б', callback_data='/response_b_3_2')
button_w_3_2 = InlineKeyboardButton('В', callback_data='/response_w_3_2')
markup_keyboard_abw_3 = InlineKeyboardMarkup()
markup_keyboard_abw_3.row(button_a_3_2, button_b_3_2, button_w_3_2)
markup_keyboard_abw_3.row(button_cancel)


button_a_4_2 = InlineKeyboardButton('А', callback_data='/response_a_4_2')
button_b_4_2 = InlineKeyboardButton('Б', callback_data='/response_b_4_2')
button_w_4_2 = InlineKeyboardButton('В', callback_data='/response_w_4_2')
markup_keyboard_abw_4 = InlineKeyboardMarkup()
markup_keyboard_abw_4.row(button_a_4_2, button_b_4_2, button_w_4_2)
markup_keyboard_abw_4.row(button_cancel)


button_a_5_2 = InlineKeyboardButton('А', callback_data='/response_a_5_2')
button_b_5_2 = InlineKeyboardButton('Б', callback_data='/response_b_5_2')
button_w_5_2 = InlineKeyboardButton('В', callback_data='/response_w_5_2')
markup_keyboard_abw_5 = InlineKeyboardMarkup()
markup_keyboard_abw_5.row(button_a_5_2, button_b_5_2, button_w_5_2)
markup_keyboard_abw_5.row(button_cancel)


button_a_6_2 = InlineKeyboardButton('А', callback_data='/response_a_6_2')
button_b_6_2 = InlineKeyboardButton('Б', callback_data='/response_b_6_2')
button_w_6_2 = InlineKeyboardButton('В', callback_data='/response_w_6_2')
markup_keyboard_abw_6 = InlineKeyboardMarkup()
markup_keyboard_abw_6.row(button_a_6_2, button_b_6_2, button_w_6_2)
markup_keyboard_abw_6.row(button_cancel)


button_a_7_2 = InlineKeyboardButton('А', callback_data='/response_a_7_2')
button_b_7_2 = InlineKeyboardButton('Б', callback_data='/response_b_7_2')
button_w_7_2 = InlineKeyboardButton('В', callback_data='/response_w_7_2')
markup_keyboard_abw_7 = InlineKeyboardMarkup()
markup_keyboard_abw_7.row(button_a_7_2, button_b_7_2, button_w_7_2)
markup_keyboard_abw_7.row(button_cancel)


button_a_8_2 = InlineKeyboardButton('А', callback_data='/response_a_8_2')
button_b_8_2 = InlineKeyboardButton('Б', callback_data='/response_b_8_2')
button_w_8_2 = InlineKeyboardButton('В', callback_data='/response_w_8_2')
markup_keyboard_abw_8 = InlineKeyboardMarkup()
markup_keyboard_abw_8.row(button_a_8_2, button_b_8_2, button_w_8_2)
markup_keyboard_abw_8.row(button_cancel)


#######################
# Выбор ответа (Тест 3)
#######################


button_1_1 = InlineKeyboardButton('1', callback_data='/response_1_1')
button_2_1 = InlineKeyboardButton('2', callback_data='/response_2_1')
button_3_1 = InlineKeyboardButton('3', callback_data='/response_3_1')
markup_keyboard_123_1 = InlineKeyboardMarkup()
markup_keyboard_123_1.row(button_1_1, button_2_1, button_3_1)
markup_keyboard_123_1.row(button_cancel)


button_1_2 = InlineKeyboardButton('1', callback_data='/response_1_2')
button_2_2 = InlineKeyboardButton('2', callback_data='/response_2_2')
button_3_2 = InlineKeyboardButton('3', callback_data='/response_3_2')
markup_keyboard_123_2 = InlineKeyboardMarkup()
markup_keyboard_123_2.row(button_1_2, button_2_2, button_3_2)
markup_keyboard_123_2.row(button_cancel)


button_1_3 = InlineKeyboardButton('1', callback_data='/response_1_3')
button_2_3 = InlineKeyboardButton('2', callback_data='/response_2_3')
button_3_3 = InlineKeyboardButton('3', callback_data='/response_3_3')
markup_keyboard_123_3 = InlineKeyboardMarkup()
markup_keyboard_123_3.row(button_1_3, button_2_3, button_3_3)
markup_keyboard_123_3.row(button_cancel)


button_1_4 = InlineKeyboardButton('1', callback_data='/response_1_4')
button_2_4 = InlineKeyboardButton('2', callback_data='/response_2_4')
button_3_4 = InlineKeyboardButton('3', callback_data='/response_3_4')
markup_keyboard_123_4 = InlineKeyboardMarkup()
markup_keyboard_123_4.row(button_1_4, button_2_4, button_3_4)
markup_keyboard_123_4.row(button_cancel)


button_1_5 = InlineKeyboardButton('1', callback_data='/response_1_5')
button_2_5 = InlineKeyboardButton('2', callback_data='/response_2_5')
button_3_5 = InlineKeyboardButton('3', callback_data='/response_3_5')
markup_keyboard_123_5 = InlineKeyboardMarkup()
markup_keyboard_123_5.row(button_1_5, button_2_5, button_3_5)
markup_keyboard_123_5.row(button_cancel)


#######################
# Выбор ответа (Тест 4)
#######################


button_a_1_3 = InlineKeyboardButton('а', callback_data='/response_a_1_3')
button_b_1_3 = InlineKeyboardButton('б', callback_data='/response_b_1_3')
button_w_1_3 = InlineKeyboardButton('в', callback_data='/response_w_1_3')
markup_keyboard_abw_1_2 = InlineKeyboardMarkup()
markup_keyboard_abw_1_2.row(button_a_1_3, button_b_1_3, button_w_1_3)
markup_keyboard_abw_1_2.row(button_cancel)


button_a_2_3 = InlineKeyboardButton('а', callback_data='/response_a_2_3')
button_b_2_3 = InlineKeyboardButton('б', callback_data='/response_b_2_3')
button_w_2_3 = InlineKeyboardButton('в', callback_data='/response_w_2_3')
markup_keyboard_abw_2_2 = InlineKeyboardMarkup()
markup_keyboard_abw_2_2.row(button_a_2_3, button_b_2_3, button_w_2_3)
markup_keyboard_abw_2_2.row(button_cancel)


button_a_3_3 = InlineKeyboardButton('а', callback_data='/response_a_3_3')
button_b_3_3 = InlineKeyboardButton('б', callback_data='/response_b_3_3')
button_w_3_3 = InlineKeyboardButton('в', callback_data='/response_w_3_3')
markup_keyboard_abw_3_2 = InlineKeyboardMarkup()
markup_keyboard_abw_3_2.row(button_a_3_3, button_b_3_3, button_w_3_3)
markup_keyboard_abw_3_2.row(button_cancel)


button_a_4_3 = InlineKeyboardButton('а', callback_data='/response_a_4_3')
button_b_4_3 = InlineKeyboardButton('б', callback_data='/response_b_4_3')
button_w_4_3 = InlineKeyboardButton('в', callback_data='/response_w_4_3')
markup_keyboard_abw_4_2 = InlineKeyboardMarkup()
markup_keyboard_abw_4_2.row(button_a_4_3, button_b_4_3, button_w_4_3)
markup_keyboard_abw_4_2.row(button_cancel)


button_a_5_3 = InlineKeyboardButton('а', callback_data='/response_a_5_3')
button_b_5_3 = InlineKeyboardButton('б', callback_data='/response_b_5_3')
button_w_5_3 = InlineKeyboardButton('в', callback_data='/response_w_5_3')
markup_keyboard_abw_5_2 = InlineKeyboardMarkup()
markup_keyboard_abw_5_2.row(button_a_5_3, button_b_5_3, button_w_5_3)
markup_keyboard_abw_5_2.row(button_cancel)


button_a_6_3 = InlineKeyboardButton('а', callback_data='/response_a_6_3')
button_b_6_3 = InlineKeyboardButton('б', callback_data='/response_b_6_3')
button_w_6_3 = InlineKeyboardButton('в', callback_data='/response_w_6_3')
markup_keyboard_abw_6_2 = InlineKeyboardMarkup()
markup_keyboard_abw_6_2.row(button_a_6_3, button_b_6_3, button_w_6_3)
markup_keyboard_abw_6_2.row(button_cancel)


button_a_7_3 = InlineKeyboardButton('а', callback_data='/response_a_7_3')
button_b_7_3 = InlineKeyboardButton('б', callback_data='/response_b_7_3')
button_w_7_3 = InlineKeyboardButton('в', callback_data='/response_w_7_3')
markup_keyboard_abw_7_2 = InlineKeyboardMarkup()
markup_keyboard_abw_7_2.row(button_a_7_3, button_b_7_3, button_w_7_3)
markup_keyboard_abw_7_2.row(button_cancel)


button_a_8_3 = InlineKeyboardButton('а', callback_data='/response_a_8_3')
button_b_8_3 = InlineKeyboardButton('б', callback_data='/response_b_8_3')
button_w_8_3 = InlineKeyboardButton('в', callback_data='/response_w_8_3')
markup_keyboard_abw_8_2 = InlineKeyboardMarkup()
markup_keyboard_abw_8_2.row(button_a_8_3, button_b_8_3, button_w_8_3)
markup_keyboard_abw_8_2.row(button_cancel)


button_a_9_3 = InlineKeyboardButton('а', callback_data='/response_a_9_3')
button_b_9_3 = InlineKeyboardButton('б', callback_data='/response_b_9_3')
button_w_9_3 = InlineKeyboardButton('в', callback_data='/response_w_9_3')
markup_keyboard_abw_9_2 = InlineKeyboardMarkup()
markup_keyboard_abw_9_2.row(button_a_9_3, button_b_9_3, button_w_9_3)
markup_keyboard_abw_9_2.row(button_cancel)


button_a_10_3 = InlineKeyboardButton('а', callback_data='/response_a_10_3')
button_b_10_3 = InlineKeyboardButton('б', callback_data='/response_b_10_3')
button_w_10_3 = InlineKeyboardButton('в', callback_data='/response_w_10_3')
markup_keyboard_abw_10_2 = InlineKeyboardMarkup()
markup_keyboard_abw_10_2.row(button_a_10_3, button_b_10_3, button_w_10_3)
markup_keyboard_abw_10_2.row(button_cancel)


#######################
# Выбор ответа (Тест 5)
#######################


button_a_1_4 = InlineKeyboardButton('A', callback_data='/response_a_1_4')
button_b_1_4 = InlineKeyboardButton('B', callback_data='/response_b_1_4')
button_c_1_4 = InlineKeyboardButton('C', callback_data='/response_c_1_4')
markup_keyboard_abc_1 = InlineKeyboardMarkup()
markup_keyboard_abc_1.row(button_a_1_4, button_b_1_4, button_c_1_4)
markup_keyboard_abc_1.row(button_cancel)


button_a_2_4 = InlineKeyboardButton('A', callback_data='/response_a_2_4')
button_b_2_4 = InlineKeyboardButton('B', callback_data='/response_b_2_4')
button_c_2_4 = InlineKeyboardButton('C', callback_data='/response_c_2_4')
markup_keyboard_abc_2 = InlineKeyboardMarkup()
markup_keyboard_abc_2.row(button_a_2_4, button_b_2_4, button_c_2_4)
markup_keyboard_abc_2.row(button_cancel)


button_a_3_4 = InlineKeyboardButton('A', callback_data='/response_a_3_4')
button_b_3_4 = InlineKeyboardButton('B', callback_data='/response_b_3_4')
button_c_3_4 = InlineKeyboardButton('C', callback_data='/response_c_3_4')
markup_keyboard_abc_3 = InlineKeyboardMarkup()
markup_keyboard_abc_3.row(button_a_3_4, button_b_3_4, button_c_3_4)
markup_keyboard_abc_3.row(button_cancel)


button_a_4_4 = InlineKeyboardButton('A', callback_data='/response_a_4_4')
button_b_4_4 = InlineKeyboardButton('B', callback_data='/response_b_4_4')
button_c_4_4 = InlineKeyboardButton('C', callback_data='/response_c_4_4')
markup_keyboard_abc_4 = InlineKeyboardMarkup()
markup_keyboard_abc_4.row(button_a_4_4, button_b_4_4, button_c_4_4)
markup_keyboard_abc_4.row(button_cancel)


button_a_5_4 = InlineKeyboardButton('A', callback_data='/response_a_5_4')
button_b_5_4 = InlineKeyboardButton('B', callback_data='/response_b_5_4')
button_c_5_4 = InlineKeyboardButton('C', callback_data='/response_c_5_4')
markup_keyboard_abc_5 = InlineKeyboardMarkup()
markup_keyboard_abc_5.row(button_a_5_4, button_b_5_4, button_c_5_4)
markup_keyboard_abc_5.row(button_cancel)


button_a_6_4 = InlineKeyboardButton('A', callback_data='/response_a_6_4')
button_b_6_4 = InlineKeyboardButton('B', callback_data='/response_b_6_4')
button_c_6_4 = InlineKeyboardButton('C', callback_data='/response_c_6_4')
markup_keyboard_abc_6 = InlineKeyboardMarkup()
markup_keyboard_abc_6.row(button_a_6_4, button_b_6_4, button_c_6_4)
markup_keyboard_abc_6.row(button_cancel)


button_a_7_4 = InlineKeyboardButton('A', callback_data='/response_a_7_4')
button_b_7_4 = InlineKeyboardButton('B', callback_data='/response_b_7_4')
button_c_7_4 = InlineKeyboardButton('C', callback_data='/response_c_7_4')
markup_keyboard_abc_7 = InlineKeyboardMarkup()
markup_keyboard_abc_7.row(button_a_7_4, button_b_7_4, button_c_7_4)
markup_keyboard_abc_7.row(button_cancel)


button_a_8_4 = InlineKeyboardButton('A', callback_data='/response_a_8_4')
button_b_8_4 = InlineKeyboardButton('B', callback_data='/response_b_8_4')
button_c_8_4 = InlineKeyboardButton('C', callback_data='/response_c_8_4')
markup_keyboard_abc_8 = InlineKeyboardMarkup()
markup_keyboard_abc_8.row(button_a_8_4, button_b_8_4, button_c_8_4)
markup_keyboard_abc_8.row(button_cancel)


button_a_9_4 = InlineKeyboardButton('A', callback_data='/response_a_9_4')
button_b_9_4 = InlineKeyboardButton('B', callback_data='/response_b_9_4')
button_c_9_4 = InlineKeyboardButton('C', callback_data='/response_c_9_4')
markup_keyboard_abc_9 = InlineKeyboardMarkup()
markup_keyboard_abc_9.row(button_a_9_4, button_b_9_4, button_c_9_4)
markup_keyboard_abc_9.row(button_cancel)


button_a_10_4 = InlineKeyboardButton('A', callback_data='/response_a_10_4')
button_b_10_4 = InlineKeyboardButton('B', callback_data='/response_b_10_4')
button_c_10_4 = InlineKeyboardButton('C', callback_data='/response_c_10_4')
markup_keyboard_abc_10 = InlineKeyboardMarkup()
markup_keyboard_abc_10.row(button_a_10_4, button_b_10_4, button_c_10_4)
markup_keyboard_abc_10.row(button_cancel)


button_a_11_4 = InlineKeyboardButton('A', callback_data='/response_a_11_4')
button_b_11_4 = InlineKeyboardButton('B', callback_data='/response_b_11_4')
button_c_11_4 = InlineKeyboardButton('C', callback_data='/response_c_11_4')
markup_keyboard_abc_11 = InlineKeyboardMarkup()
markup_keyboard_abc_11.row(button_a_11_4, button_b_11_4, button_c_11_4)
markup_keyboard_abc_11.row(button_cancel)


button_a_12_4 = InlineKeyboardButton('A', callback_data='/response_a_12_4')
button_b_12_4 = InlineKeyboardButton('B', callback_data='/response_b_12_4')
button_c_12_4 = InlineKeyboardButton('C', callback_data='/response_c_12_4')
markup_keyboard_abc_12 = InlineKeyboardMarkup()
markup_keyboard_abc_12.row(button_a_12_4, button_b_12_4, button_c_12_4)
markup_keyboard_abc_12.row(button_cancel)


button_a_13_4 = InlineKeyboardButton('A', callback_data='/response_a_13_4')
button_b_13_4 = InlineKeyboardButton('B', callback_data='/response_b_13_4')
button_c_13_4 = InlineKeyboardButton('C', callback_data='/response_c_13_4')
markup_keyboard_abc_13 = InlineKeyboardMarkup()
markup_keyboard_abc_13.row(button_a_13_4, button_b_13_4, button_c_13_4)
markup_keyboard_abc_13.row(button_cancel)


button_a_14_4 = InlineKeyboardButton('A', callback_data='/response_a_14_4')
button_b_14_4 = InlineKeyboardButton('B', callback_data='/response_b_14_4')
button_c_14_4 = InlineKeyboardButton('C', callback_data='/response_c_14_4')
markup_keyboard_abc_14 = InlineKeyboardMarkup()
markup_keyboard_abc_14.row(button_a_14_4, button_b_14_4, button_c_14_4)
markup_keyboard_abc_14.row(button_cancel)


button_start_rebus = InlineKeyboardButton(
    'Начать', callback_data='/start_rebus')
markup_keyboard_start_rebus = InlineKeyboardMarkup()
markup_keyboard_start_rebus.row(button_start_rebus)
# markup_keyboard_start_rebus.row(button_cancel)


button_rebus_2 = InlineKeyboardButton('Далее', callback_data='/rebus_2')
markup_keyboard_rebus_2 = InlineKeyboardMarkup()
markup_keyboard_rebus_2.row(button_rebus_2)
# markup_keyboard_rebus_2.row(button_cancel)


button_rebus_3 = InlineKeyboardButton('Далее', callback_data='/rebus_3')
markup_keyboard_rebus_3 = InlineKeyboardMarkup()
markup_keyboard_rebus_3.row(button_rebus_3)
# markup_keyboard_rebus_3.row(button_cancel)


button_rebus_4 = InlineKeyboardButton('Далее', callback_data='/rebus_4')
markup_keyboard_rebus_4 = InlineKeyboardMarkup()
markup_keyboard_rebus_4.row(button_rebus_4)
# markup_keyboard_rebus_4.row(button_cancel)


button_rebus_5 = InlineKeyboardButton('Далее', callback_data='/rebus_5')
markup_keyboard_rebus_5 = InlineKeyboardMarkup()
markup_keyboard_rebus_5.row(button_rebus_5)
# markup_keyboard_rebus_5.row(button_cancel)


button_rebus_6 = InlineKeyboardButton('Далее', callback_data='/rebus_6')
markup_keyboard_rebus_6 = InlineKeyboardMarkup()
markup_keyboard_rebus_6.row(button_rebus_6)
# markup_keyboard_rebus_6.row(button_cancel)


button_rebus_7 = InlineKeyboardButton('Далее', callback_data='/rebus_7')
markup_keyboard_rebus_7 = InlineKeyboardMarkup()
markup_keyboard_rebus_7.row(button_rebus_7)
# markup_keyboard_rebus_7.row(button_cancel)


button_rebus_8 = InlineKeyboardButton('Далее', callback_data='/rebus_8')
markup_keyboard_rebus_8 = InlineKeyboardMarkup()
markup_keyboard_rebus_8.row(button_rebus_8)
# markup_keyboard_rebus_8.row(button_cancel)


button_rebus_9 = InlineKeyboardButton('Далее', callback_data='/rebus_9')
markup_keyboard_rebus_9 = InlineKeyboardMarkup()
markup_keyboard_rebus_9.row(button_rebus_9)
# markup_keyboard_rebus_9.row(button_cancel)


button_rebus_10 = InlineKeyboardButton('Далее', callback_data='/rebus_10')
markup_keyboard_rebus_10 = InlineKeyboardMarkup()
markup_keyboard_rebus_10.row(button_rebus_10)
# markup_keyboard_rebus_10.row(button_cancel)
