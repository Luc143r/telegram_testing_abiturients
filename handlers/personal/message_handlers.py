from aiogram import types
from main import dp, bot, counter_response, list_users
from fsm import *
from keyboard import *
import re


########################################
# Callback handlers / Обрабочтики кнопок
########################################

# №№№№№№№№№№№№
# ПЕРВЫЙ ТЕСТ
# №№№№№№№№№№№№


@dp.callback_query_handler(lambda call: call.data == '/test_one')
async def start_test_one(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Привет! Этот тест направлен на опредление профессии из мира рекламы, которая тебе подойдет.\n'
                                                          'Выбери один вариант ответа из четырех, который наиболее точно отражает твоё мнение.\n'
                                                          'Не спеши, внимательно читай каждый вопрос. Удачи!\n\n\n'
                                                          '1. Какая из этих задач кажется тебе наиболее интересной?\n\n'
                                                          'A. Создание уникального дизайна\n'
                                                          'B. Анализ уникального дизайна\n'
                                                          'C. Работа с текстом и контентом\n'
                                                          'D. Взаимодействие с клиентами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_1)
    await Test_one().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/response_a_1', state=Test_one.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=2)
    owner_message_bot = await owner_message_bot.edit_text('2. Какой из этих социальных медиа ты используешь чаще всего?\n\n'
                                                          'A. Вконтакте\n'
                                                          'B. Tik-Tok\n'
                                                          'C. Ок.ру\n'
                                                          'D. Pinterest')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_1', state=Test_one.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=1)
    owner_message_bot = await owner_message_bot.edit_text('2. Какой из этих социальных медиа ты используешь чаще всего?\n\n'
                                                          'A. Вконтакте\n'
                                                          'B. Tik-Tok\n'
                                                          'C. Ок.ру\n'
                                                          'D. Pinterest')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_1', state=Test_one.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=3)
    owner_message_bot = await owner_message_bot.edit_text('2. Какой из этих социальных медиа ты используешь чаще всего?\n\n'
                                                          'A. Вконтакте\n'
                                                          'B. Tik-Tok\n'
                                                          'C. Ок.ру\n'
                                                          'D. Pinterest')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_1', state=Test_one.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=4)
    owner_message_bot = await owner_message_bot.edit_text('2. Какой из этих социальных медиа ты используешь чаще всего?\n\n'
                                                          'A. Вконтакте\n'
                                                          'B. Tik-Tok\n'
                                                          'C. Ок.ру\n'
                                                          'D. Pinterest')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_2', state=Test_one.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=3)
    owner_message_bot = await owner_message_bot.edit_text('3. Какое из этих слов наиболее точно описывает твой стиль?\n\n'
                                                          'A. Креативный\n'
                                                          'B. Логический\n'
                                                          'C. Аналитический\n'
                                                          'D. Коммуникабельный')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_2', state=Test_one.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=1)
    owner_message_bot = await owner_message_bot.edit_text('3. Какое из этих слов наиболее точно описывает твой стиль?\n\n'
                                                          'A. Креативный\n'
                                                          'B. Логический\n'
                                                          'C. Аналитический\n'
                                                          'D. Коммуникабельный')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_2', state=Test_one.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=2)
    owner_message_bot = await owner_message_bot.edit_text('3. Какое из этих слов наиболее точно описывает твой стиль?\n\n'
                                                          'A. Креативный\n'
                                                          'B. Логический\n'
                                                          'C. Аналитический\n'
                                                          'D. Коммуникабельный')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_2', state=Test_one.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=4)
    owner_message_bot = await owner_message_bot.edit_text('3. Какое из этих слов наиболее точно описывает твой стиль?\n\n'
                                                          'A. Креативный\n'
                                                          'B. Логический\n'
                                                          'C. Аналитический\n'
                                                          'D. Коммуникабельный')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_3', state=Test_one.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=4)
    owner_message_bot = await owner_message_bot.edit_text('4. Что тебе нравится делать больше всего в свободное время?\n\n'
                                                          'A. Читать книги и журналы\n'
                                                          'B. Играть в видеоигры\n'
                                                          'C. Рисовать или создавать что-то своими руками\n'
                                                          'D. Общаться с друзьями и знакомыми')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_3', state=Test_one.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=2)
    owner_message_bot = await owner_message_bot.edit_text('4. Что тебе нравится делать больше всего в свободное время?\n\n'
                                                          'A. Читать книги и журналы\n'
                                                          'B. Играть в видеоигры\n'
                                                          'C. Рисовать или создавать что-то своими руками\n'
                                                          'D. Общаться с друзьями и знакомыми')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_3', state=Test_one.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=1)
    owner_message_bot = await owner_message_bot.edit_text('4. Что тебе нравится делать больше всего в свободное время?\n\n'
                                                          'A. Читать книги и журналы\n'
                                                          'B. Играть в видеоигры\n'
                                                          'C. Рисовать или создавать что-то своими руками\n'
                                                          'D. Общаться с друзьями и знакомыми')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_3', state=Test_one.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=3)
    owner_message_bot = await owner_message_bot.edit_text('4. Что тебе нравится делать больше всего в свободное время?\n\n'
                                                          'A. Читать книги и журналы\n'
                                                          'B. Играть в видеоигры\n'
                                                          'C. Рисовать или создавать что-то своими руками\n'
                                                          'D. Общаться с друзьями и знакомыми')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_4', state=Test_one.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=2)
    owner_message_bot = await owner_message_bot.edit_text('5. Какое из этих качеств наиболее важное для работы в рекламе?\n\n'
                                                          'A. Креативность\n'
                                                          'B. Умение работать с данными и статистикой\n'
                                                          'C. Лидерские качества\n'
                                                          'D. Навыки продаж')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_4', state=Test_one.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=1)
    owner_message_bot = await owner_message_bot.edit_text('5. Какое из этих качеств наиболее важное для работы в рекламе?\n\n'
                                                          'A. Креативность\n'
                                                          'B. Умение работать с данными и статистикой\n'
                                                          'C. Лидерские качества\n'
                                                          'D. Навыки продаж')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_4', state=Test_one.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=3)
    owner_message_bot = await owner_message_bot.edit_text('5. Какое из этих качеств наиболее важное для работы в рекламе?\n\n'
                                                          'A. Креативность\n'
                                                          'B. Умение работать с данными и статистикой\n'
                                                          'C. Лидерские качества\n'
                                                          'D. Навыки продаж')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_4', state=Test_one.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=4)
    owner_message_bot = await owner_message_bot.edit_text('5. Какое из этих качеств наиболее важное для работы в рекламе?\n\n'
                                                          'A. Креативность\n'
                                                          'B. Умение работать с данными и статистикой\n'
                                                          'C. Лидерские качества\n'
                                                          'D. Навыки продаж')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_5', state=Test_one.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=4)
    owner_message_bot = await owner_message_bot.edit_text('6. Какой вид рекламы тебе кажется наиболее интересным?\n\n'
                                                          'A. Телевизионная реклама\n'
                                                          'B. Реклама в социальных сетях\n'
                                                          'C. Радиореклама\n'
                                                          'D. Реклама на улицах')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_5', state=Test_one.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=2)
    owner_message_bot = await owner_message_bot.edit_text('6. Какой вид рекламы тебе кажется наиболее интересным?\n\n'
                                                          'A. Телевизионная реклама\n'
                                                          'B. Реклама в социальных сетях\n'
                                                          'C. Радиореклама\n'
                                                          'D. Реклама на улицах')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_5', state=Test_one.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=3)
    owner_message_bot = await owner_message_bot.edit_text('6. Какой вид рекламы тебе кажется наиболее интересным?\n\n'
                                                          'A. Телевизионная реклама\n'
                                                          'B. Реклама в социальных сетях\n'
                                                          'C. Радиореклама\n'
                                                          'D. Реклама на улицах')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_5', state=Test_one.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=1)
    owner_message_bot = await owner_message_bot.edit_text('6. Какой вид рекламы тебе кажется наиболее интересным?\n\n'
                                                          'A. Телевизионная реклама\n'
                                                          'B. Реклама в социальных сетях\n'
                                                          'C. Радиореклама\n'
                                                          'D. Реклама на улицах')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_6', state=Test_one.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=2)
    owner_message_bot = await owner_message_bot.edit_text('7. Какой из этих навыков ты бы хотел развивать в работе?\n\n'
                                                          'A. Умение работать с графическими редакторами\n'
                                                          'B. Аналитические навыки и умение работать с Excel\n'
                                                          'C. Навыки управления проектами\n'
                                                          'D. Коммуникационные навыки')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_6', state=Test_one.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=4)
    owner_message_bot = await owner_message_bot.edit_text('7. Какой из этих навыков ты бы хотел развивать в работе?\n\n'
                                                          'A. Умение работать с графическими редакторами\n'
                                                          'B. Аналитические навыки и умение работать с Excel\n'
                                                          'C. Навыки управления проектами\n'
                                                          'D. Коммуникационные навыки')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_6', state=Test_one.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=1)
    owner_message_bot = await owner_message_bot.edit_text('7. Какой из этих навыков ты бы хотел развивать в работе?\n\n'
                                                          'A. Умение работать с графическими редакторами\n'
                                                          'B. Аналитические навыки и умение работать с Excel\n'
                                                          'C. Навыки управления проектами\n'
                                                          'D. Коммуникационные навыки')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_6', state=Test_one.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=3)
    owner_message_bot = await owner_message_bot.edit_text('7. Какой из этих навыков ты бы хотел развивать в работе?\n\n'
                                                          'A. Умение работать с графическими редакторами\n'
                                                          'B. Аналитические навыки и умение работать с Excel\n'
                                                          'C. Навыки управления проектами\n'
                                                          'D. Коммуникационные навыки')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_7', state=Test_one.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=4)
    owner_message_bot = await owner_message_bot.edit_text('8. Какой из этих ролей ты бы предпочел играть в команде?\n\n'
                                                          'A. Идеолог и творческий директор\n'
                                                          'B. Аналитик и стратег\n'
                                                          'C. Проектный менеджер\n'
                                                          'D. Менеджер по продажам')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_7', state=Test_one.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=3)
    owner_message_bot = await owner_message_bot.edit_text('8. Какой из этих ролей ты бы предпочел играть в команде?\n\n'
                                                          'A. Идеолог и творческий директор\n'
                                                          'B. Аналитик и стратег\n'
                                                          'C. Проектный менеджер\n'
                                                          'D. Менеджер по продажам')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_7', state=Test_one.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=2)
    owner_message_bot = await owner_message_bot.edit_text('8. Какой из этих ролей ты бы предпочел играть в команде?\n\n'
                                                          'A. Идеолог и творческий директор\n'
                                                          'B. Аналитик и стратег\n'
                                                          'C. Проектный менеджер\n'
                                                          'D. Менеджер по продажам')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_7', state=Test_one.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=1)
    owner_message_bot = await owner_message_bot.edit_text('8. Какой из этих ролей ты бы предпочел играть в команде?\n\n'
                                                          'A. Идеолог и творческий директор\n'
                                                          'B. Аналитик и стратег\n'
                                                          'C. Проектный менеджер\n'
                                                          'D. Менеджер по продажам')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_8', state=Test_one.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=4)
    owner_message_bot = await owner_message_bot.edit_text('9. Какой из этих сценариев работы тебе кажется наиболее привлекательным?\n\n'
                                                          'A. Работа в креативном агентстве\n'
                                                          'B. Работа в маркетинговом агентстве\n'
                                                          'C. Работа в digital-агентстве\n'
                                                          'D. Работа в медиа-агентстве')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_8', state=Test_one.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=2)
    owner_message_bot = await owner_message_bot.edit_text('9. Какой из этих сценариев работы тебе кажется наиболее привлекательным?\n\n'
                                                          'A. Работа в креативном агентстве\n'
                                                          'B. Работа в маркетинговом агентстве\n'
                                                          'C. Работа в digital-агентстве\n'
                                                          'D. Работа в медиа-агентстве')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_8', state=Test_one.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=3)
    owner_message_bot = await owner_message_bot.edit_text('9. Какой из этих сценариев работы тебе кажется наиболее привлекательным?\n\n'
                                                          'A. Работа в креативном агентстве\n'
                                                          'B. Работа в маркетинговом агентстве\n'
                                                          'C. Работа в digital-агентстве\n'
                                                          'D. Работа в медиа-агентстве')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_8', state=Test_one.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=1)
    owner_message_bot = await owner_message_bot.edit_text('9. Какой из этих сценариев работы тебе кажется наиболее привлекательным?\n\n'
                                                          'A. Работа в креативном агентстве\n'
                                                          'B. Работа в маркетинговом агентстве\n'
                                                          'C. Работа в digital-агентстве\n'
                                                          'D. Работа в медиа-агентстве')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_9', state=Test_one.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=4)
    owner_message_bot = await owner_message_bot.edit_text('10. Какой из этих аспектов рекламной кампании тебе кажется наиболее важным?\n\n'
                                                          'A. Визуальный дизайн\n'
                                                          'B. Уникальный контент\n'
                                                          'C. Таргетированная реклама\n'
                                                          'D. Сильный брендинг')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_9', state=Test_one.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=1)
    owner_message_bot = await owner_message_bot.edit_text('10. Какой из этих аспектов рекламной кампании тебе кажется наиболее важным?\n\n'
                                                          'A. Визуальный дизайн\n'
                                                          'B. Уникальный контент\n'
                                                          'C. Таргетированная реклама\n'
                                                          'D. Сильный брендинг')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_9', state=Test_one.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=3)
    owner_message_bot = await owner_message_bot.edit_text('10. Какой из этих аспектов рекламной кампании тебе кажется наиболее важным?\n\n'
                                                          'A. Визуальный дизайн\n'
                                                          'B. Уникальный контент\n'
                                                          'C. Таргетированная реклама\n'
                                                          'D. Сильный брендинг')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_d_9', state=Test_one.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=2)
    owner_message_bot = await owner_message_bot.edit_text('10. Какой из этих аспектов рекламной кампании тебе кажется наиболее важным?\n\n'
                                                          'A. Визуальный дизайн\n'
                                                          'B. Уникальный контент\n'
                                                          'C. Таргетированная реклама\n'
                                                          'D. Сильный брендинг')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abcd_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_one.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_10', state=Test_one.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=3)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия графического дизайнера')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 24:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 25 and result_test <= 31:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия digital-маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 32 and resultt_test <= 40:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия менеджера по работе с клиентами в рекламном агенстве')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_b_10', state=Test_one.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=2)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия графического дизайнера')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 24:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 25 and result_test <= 31:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия digital-маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 32 and resultt_test <= 40:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия менеджера по работе с клиентами в рекламном агенстве')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_c_10', state=Test_one.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=4)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия графического дизайнера')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 24:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 25 and result_test <= 31:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия digital-маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 32 and result_test <= 40:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия менеджера по работе с клиентами в рекламном агенстве')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_d_10', state=Test_one.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=1)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия графического дизайнера')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 24:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 25 and result_test <= 31:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия digital-маркетолога')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 32 and resultt_test <= 40:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Вам подойдет профессия менеджера по работе с клиентами в рекламном агенстве')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


#############
# ВТОРОЙ ТЕСТ
#############


@dp.callback_query_handler(lambda call: call.data == '/test_two')
async def start_test_two(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Слоган - важная составляющая любого бренда или компании.\n'
                                                          'Сможешь ли ты выбрать наиболее удачный? Действуй!\n\n'
                                                          'Выберите верный ответ из трех вариантов и проверьте свои знания и кругозор в этой области.\n'
                                                          'Если у тебя появятся вопросы по слогану, то свяжись с нами: pr_sapiens@inbox.ru\n\n\n'
                                                          '1. Компания, занимающаяся спортивными товарами, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n'
                                                          'А. Спорт - это жизнь\n'
                                                          'Б. Мы делаем спорт доступным\n'
                                                          'В. Покоряй вершины вместе с нами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_1)
    await Test_two().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/response_a_1_2', state=Test_two.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Зоомагазин хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Любите своих питомцев\n'
                                                          'Б. У нас все для ваших любимцев\n'
                                                          'В. Ухаживайте за своим питомцем, как за собой')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_1_2', state=Test_two.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Зоомагазин хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Любите своих питомцев\n'
                                                          'Б. У нас все для ваших любимцев\n'
                                                          'В. Ухаживайте за своим питомцем, как за собой')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_1_2', state=Test_two.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=1)
    owner_message_bot = await owner_message_bot.edit_text('2. Зоомагазин хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Любите своих питомцев\n'
                                                          'Б. У нас все для ваших любимцев\n'
                                                          'В. Ухаживайте за своим питомцем, как за собой')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_2_2', state=Test_two.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Строительная компания хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Строим крепкие дома\n'
                                                          'Б. Дом, который вы заслуживаете\n'
                                                          'В. Качественное строительство - наша гарантия')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_2_2', state=Test_two.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=1)
    owner_message_bot = await owner_message_bot.edit_text('3. Строительная компания хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Строим крепкие дома\n'
                                                          'Б. Дом, который вы заслуживаете\n'
                                                          'В. Качественное строительство - наша гарантия')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_2_2', state=Test_two.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Строительная компания хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Строим крепкие дома\n'
                                                          'Б. Дом, который вы заслуживаете\n'
                                                          'В. Качественное строительство - наша гарантия')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_3_2', state=Test_two.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Компания, занимающаяся косметикой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Красота в каждой баночке\n'
                                                          'Б. Натуральная косметика для идеальной кожи\n'
                                                          'В. Дарите себе роскошь каждый день')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_3_2', state=Test_two.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=1)
    owner_message_bot = await owner_message_bot.edit_text('4. Компания, занимающаяся косметикой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Красота в каждой баночке\n'
                                                          'Б. Натуральная косметика для идеальной кожи\n'
                                                          'В. Дарите себе роскошь каждый день')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_3_2', state=Test_two.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Компания, занимающаяся косметикой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Красота в каждой баночке\n'
                                                          'Б. Натуральная косметика для идеальной кожи\n'
                                                          'В. Дарите себе роскошь каждый день')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_4_2', state=Test_two.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Компания, занимающаяся массажными услугами, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Отдохните и расслабьтесь в наших опытных руках\n'
                                                          'Б. Дарите своему телу заслуженный отдых\n'
                                                          'В. Освободите напряжение и чувствуйте себя прекрассно с нашими массажными услугами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_4_2', state=Test_two.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Компания, занимающаяся массажными услугами, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Отдохните и расслабьтесь в наших опытных руках\n'
                                                          'Б. Дарите своему телу заслуженный отдых\n'
                                                          'В. Освободите напряжение и чувствуйте себя прекрассно с нашими массажными услугами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_4_2', state=Test_two.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=1)
    owner_message_bot = await owner_message_bot.edit_text('5. Компания, занимающаяся массажными услугами, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Отдохните и расслабьтесь в наших опытных руках\n'
                                                          'Б. Дарите своему телу заслуженный отдых\n'
                                                          'В. Освободите напряжение и чувствуйте себя прекрассно с нашими массажными услугами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_5_2', state=Test_two.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    owner_message_bot = await owner_message_bot.edit_text('6. Компания, занимающаяся компьютерной техникой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Надежность и качество - наша фирменная марка!\n'
                                                          'Б. У нас есть техника для каждой задачи\n'
                                                          'В. Делайте больше, тратя меньше с нашими продуктами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_5_2', state=Test_two.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=1)
    owner_message_bot = await owner_message_bot.edit_text('6. Компания, занимающаяся компьютерной техникой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Надежность и качество - наша фирменная марка!\n'
                                                          'Б. У нас есть техника для каждой задачи\n'
                                                          'В. Делайте больше, тратя меньше с нашими продуктами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_5_2', state=Test_two.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    owner_message_bot = await owner_message_bot.edit_text('6. Компания, занимающаяся компьютерной техникой, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Надежность и качество - наша фирменная марка!\n'
                                                          'Б. У нас есть техника для каждой задачи\n'
                                                          'В. Делайте больше, тратя меньше с нашими продуктами')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_6_2', state=Test_two.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=0)
    owner_message_bot = await owner_message_bot.edit_text('7. Компания, занимающаяся продажей одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Найдите свой стиль вместе с нами\n'
                                                          'Б. Стиль начинается с одежды - начните с нас\n'
                                                          'В. Одежда, которая делает вас уверенными в себе.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_6_2', state=Test_two.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=1)
    owner_message_bot = await owner_message_bot.edit_text('7. Компания, занимающаяся продажей одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Найдите свой стиль вместе с нами\n'
                                                          'Б. Стиль начинается с одежды - начните с нас\n'
                                                          'В. Одежда, которая делает вас уверенными в себе.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_6_2', state=Test_two.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=0)
    owner_message_bot = await owner_message_bot.edit_text('7. Компания, занимающаяся продажей одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Найдите свой стиль вместе с нами\n'
                                                          'Б. Стиль начинается с одежды - начните с нас\n'
                                                          'В. Одежда, которая делает вас уверенными в себе.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_7_2', state=Test_two.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=0)
    owner_message_bot = await owner_message_bot.edit_text('8. Компания, занимающаяся пошивом одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Каждое изделие - это уникальное произведение искусства!\n'
                                                          'Б. Мы воплощаем ваши мечты в реальность.\n'
                                                          'В. Сделайте ваши вещи по-настоящему уникальными с помощью наших мастеров.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_7_2', state=Test_two.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=0)
    owner_message_bot = await owner_message_bot.edit_text('8. Компания, занимающаяся пошивом одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Каждое изделие - это уникальное произведение искусства!\n'
                                                          'Б. Мы воплощаем ваши мечты в реальность.\n'
                                                          'В. Сделайте ваши вещи по-настоящему уникальными с помощью наших мастеров.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_7_2', state=Test_two.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=1)
    owner_message_bot = await owner_message_bot.edit_text('8. Компания, занимающаяся пошивом одежды, хочет придумать новый слоган. Какой из следующих вариантов является удачным?\n\n'
                                                          'А. Каждое изделие - это уникальное произведение искусства!\n'
                                                          'Б. Мы воплощаем ваши мечты в реальность.\n'
                                                          'В. Сделайте ваши вещи по-настоящему уникальными с помощью наших мастеров.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_two.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_8_2', state=Test_two.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=1)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 3 and result_test <= 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь много о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 6 and result_test <= 8:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text(f'Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_b_8_2', state=Test_two.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=0)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 3 and result_test <= 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь много о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 6 and result_test <= 8:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_w_8_2', state=Test_two.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=0)
    data_question = await state.get_data()
    print(data_question)
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 3 and result_test <= 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь много о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 6 and result_test <= 8:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text(f'Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await state.finish()


#############
# ТРЕТИЙ ТЕСТ
#############


@dp.callback_query_handler(lambda call: call.data == '/test_three')
async def start_test_three(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Тест на знание известных фраз из мира рекламы.\n'
                                                          'Выберите верный ответ из трех вариантов и проверьте свои знания и кругозор в этой области.\n\n\n'
                                                          '1. Кому принадлежит цитата: \n'
                                                          '"Многие мелочи стали важными благодаря правильной рекламе"?\n\n'
                                                          '1. Марк Твен\n'
                                                          '2. Стивен Фридман\n'
                                                          '3. Эдвард Бернейс')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_1)
    await Test_three().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/response_1_1', state=Test_three.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=1)
    owner_message_bot = await owner_message_bot.edit_text('2. Кому принадлежит цитата: \n'
                                                          '"Если говорят о рекламе, это плохая реклама. Если говорят о товаре, это хорошая реклама"?\n\n'
                                                          '1. Тим Белл\n'
                                                          '2. Дэвид Огилви\n'
                                                          '3. Ричард Эдельман')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_2_1', state=Test_three.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Кому принадлежит цитата: \n'
                                                          '"Если говорят о рекламе, это плохая реклама. Если говорят о товаре, это хорошая реклама"?\n\n'
                                                          '1. Тим Белл\n'
                                                          '2. Дэвид Огилви\n'
                                                          '3. Ричард Эдельман')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_3_1', state=Test_three.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Кому принадлежит цитата: \n'
                                                          '"Если говорят о рекламе, это плохая реклама. Если говорят о товаре, это хорошая реклама"?\n\n'
                                                          '1. Тим Белл\n'
                                                          '2. Дэвид Огилви\n'
                                                          '3. Ричард Эдельман')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_1_2', state=Test_three.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Кому принадлежит цитата: \n'
                                                          '"Если вас не заметили, вы остаетесь ни с чем. Вам нужно чтобы вас заметили, но без криков и обмана"?\n\n'
                                                          '1. Ли Клондайкер\n'
                                                          '2. Ричард Киршенбаум\n'
                                                          '3. Лео Барнетт')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_2_2', state=Test_three.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=1)
    owner_message_bot = await owner_message_bot.edit_text('3. Кому принадлежит цитата: \n'
                                                          '"Если вас не заметили, вы остаетесь ни с чем. Вам нужно чтобы вас заметили, но без криков и обмана"?\n\n'
                                                          '1. Ли Клондайкер\n'
                                                          '2. Ричард Киршенбаум\n'
                                                          '3. Лео Барнетт')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_3_2', state=Test_three.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Кому принадлежит цитата: \n'
                                                          '"Если вас не заметили, вы остаетесь ни с чем. Вам нужно чтобы вас заметили, но без криков и обмана"?\n\n'
                                                          '1. Ли Клондайкер\n'
                                                          '2. Ричард Киршенбаум\n'
                                                          '3. Лео Барнетт')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_1_3', state=Test_three.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Кому принадлежит цитата: \n'
                                                          '"Нет такой рекламы, которая не нашла бы своего читателя"?\n\n'
                                                          '1. Илья Ильф\n'
                                                          '2. Андреас Вилигер\n'
                                                          '3. Герри Джуджикли')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_2_3', state=Test_three.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Кому принадлежит цитата: \n'
                                                          '"Нет такой рекламы, которая не нашла бы своего читателя"?\n\n'
                                                          '1. Илья Ильф\n'
                                                          '2. Андреас Вилигер\n'
                                                          '3. Герри Джуджикли')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_3_3', state=Test_three.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=1)
    owner_message_bot = await owner_message_bot.edit_text('4. Кому принадлежит цитата: \n'
                                                          '"Нет такой рекламы, которая не нашла бы своего читателя"?\n\n'
                                                          '1. Илья Ильф\n'
                                                          '2. Андреас Вилигер\n'
                                                          '3. Герри Джуджикли')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_1_4', state=Test_three.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=1)
    owner_message_bot = await owner_message_bot.edit_text('5. Кому принадлежит цитата: \n'
                                                          '"Рекламные объявления - это наскальные рисунки ХХ века"?\n\n'
                                                          '1. Джордж Льюис\n'
                                                          '2. Маршалл Маклюэн\n'
                                                          '3. Клод Хопкинс')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_2_4', state=Test_three.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Кому принадлежит цитата: \n'
                                                          '"Рекламные объявления - это наскальные рисунки ХХ века"?\n\n'
                                                          '1. Джордж Льюис\n'
                                                          '2. Маршалл Маклюэн\n'
                                                          '3. Клод Хопкинс')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_3_4', state=Test_three.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Кому принадлежит цитата: \n'
                                                          '"Рекламные объявления - это наскальные рисунки ХХ века"?\n\n'
                                                          '1. Джордж Льюис\n'
                                                          '2. Маршалл Маклюэн\n'
                                                          '3. Клод Хопкинс')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_123_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_three.next()


@dp.callback_query_handler(lambda call: call.data == '/response_1_5', state=Test_three.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test == 0:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Начинающий. Впереди столько времени, чтобы изучить мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 1:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 3:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Гуру. Ты знаешь все о рекламе и пиаре, и можешь считать себя настоящим гуру в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_2_5', state=Test_three.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=1)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test == 0:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Начинающий. Впереди столько времени, чтобы изучить мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 1:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 3:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Гуру. Ты знаешь все о рекламе и пиаре, и можешь считать себя настоящим гуру в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_3_5', state=Test_three.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test == 0:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Начинающий. Впереди столько времени, чтобы изучить мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 1:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 2:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 3:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test == 5:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Гуру. Ты знаешь все о рекламе и пиаре, и можешь считать себя настоящим гуру в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


################
# ЧЕТВЕРТЫЙ ТЕСТ
################


@dp.callback_query_handler(lambda call: call.data == '/test_four')
async def start_test_four(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Добро пожаловать на тест "Насколько специальность реклама и связи с общественностью тебе подходит".\n\n'
                                                          'Этот тест поможет тебе определить, насколько ты подходишь для этой увлекательной профессии.\n\n'
                                                          'В тесте всего 10 вопросов, и время на выполнение не ограничено, поэтому ты можешь сделать его в своем собственном темпе.\n\n'
                                                          'Для каждого вопроса выбери ответ, который точно отражает твои мысли и предпочтения.\n'
                                                          'Помни, что нет правильных или неправильных ответов - ответы будут использоваться только для того, чтобы определить твой потенциал в области рекламы и связей с общественностью.\n'
                                                          'Читай внимательно каждый вопрос и ответ.\n\n'
                                                          'Удачи!\n\n'
                                                          '1. Какую роль играют креативные идеи в твоей жизни?\n'
                                                          'а) Они являются основой моего творчества и выражения личности.\n'
                                                          'б) Они иногда приходят мне в голову, но не всегда.\n'
                                                          'в) Я предпочитаю быть более аналитичным(-ой) и рациональным(-ой).')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_1_2)
    await Test_four().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/response_a_1_3', state=Test_four.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=3)
    owner_message_bot = await owner_message_bot.edit_text('2. Как ты относишься к общению с людьми?\n'
                                                          'а) Я обожаю общаться с людьми и налаживать новые контакты.\n'
                                                          'б) Я коммуникабельный(-ая), но иногда предпочитаю уединение.\n'
                                                          'в) Я предпочитаю работать в одиночку и избегать больших групп людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_1_3', state=Test_four.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=2)
    owner_message_bot = await owner_message_bot.edit_text('2. Как ты относишься к общению с людьми?\n'
                                                          'а) Я обожаю общаться с людьми и налаживать новые контакты.\n'
                                                          'б) Я коммуникабельный(-ая), но иногда предпочитаю уединение.\n'
                                                          'в) Я предпочитаю работать в одиночку и избегать больших групп людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_1_3', state=Test_four.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=1)
    owner_message_bot = await owner_message_bot.edit_text('2. Как ты относишься к общению с людьми?\n'
                                                          'а) Я обожаю общаться с людьми и налаживать новые контакты.\n'
                                                          'б) Я коммуникабельный(-ая), но иногда предпочитаю уединение.\n'
                                                          'в) Я предпочитаю работать в одиночку и избегать больших групп людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_2_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_2_3', state=Test_four.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=3)
    owner_message_bot = await owner_message_bot.edit_text('3. Как ты оцениваешь свои навыки письменного выражения?\n'
                                                          'а) Я уверен(-на) в своей способности писать убедительно и лаконично.\n'
                                                          'б) Я считаю, что у меня неплохие навыки письма, но есть место для улучшений.\n'
                                                          'в) Я предпочитаю выражать свои мысли устно, а не письменно.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_2_3', state=Test_four.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=2)
    owner_message_bot = await owner_message_bot.edit_text('3. Как ты оцениваешь свои навыки письменного выражения?\n'
                                                          'а) Я уверен(-на) в своей способности писать убедительно и лаконично.\n'
                                                          'б) Я считаю, что у меня неплохие навыки письма, но есть место для улучшений.\n'
                                                          'в) Я предпочитаю выражать свои мысли устно, а не письменно.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_2_3', state=Test_four.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=1)
    owner_message_bot = await owner_message_bot.edit_text('3. Как ты оцениваешь свои навыки письменного выражения?\n'
                                                          'а) Я уверен(-на) в своей способности писать убедительно и лаконично.\n'
                                                          'б) Я считаю, что у меня неплохие навыки письма, но есть место для улучшений.\n'
                                                          'в) Я предпочитаю выражать свои мысли устно, а не письменно.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_3_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_3_3', state=Test_four.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=3)
    owner_message_bot = await owner_message_bot.edit_text('4. Как ты относишься к исследовательской работе и анализу данных?\n'
                                                          'а) Я наслаждаюсь исследовательской работой и люблю анализировать данные.\n'
                                                          'б) Я справляюсь с исследованиями и анализом, но не считаю это своей страстью.\n'
                                                          'в) Я предпочитаю практическую деятельность и не очень люблю работу с данными.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_3_3', state=Test_four.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=2)
    owner_message_bot = await owner_message_bot.edit_text('4. Как ты относишься к исследовательской работе и анализу данных?\n'
                                                          'а) Я наслаждаюсь исследовательской работой и люблю анализировать данные.\n'
                                                          'б) Я справляюсь с исследованиями и анализом, но не считаю это своей страстью.\n'
                                                          'в) Я предпочитаю практическую деятельность и не очень люблю работу с данными.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_3_3', state=Test_four.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=1)
    owner_message_bot = await owner_message_bot.edit_text('4. Как ты относишься к исследовательской работе и анализу данных?\n'
                                                          'а) Я наслаждаюсь исследовательской работой и люблю анализировать данные.\n'
                                                          'б) Я справляюсь с исследованиями и анализом, но не считаю это своей страстью.\n'
                                                          'в) Я предпочитаю практическую деятельность и не очень люблю работу с данными.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_4_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_4_3', state=Test_four.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=3)
    owner_message_bot = await owner_message_bot.edit_text('5. Какую роль играют социальные медиа в твоей жизни?\n'
                                                          'а) Я активно использую социальные медиа и интересуюсь их влиянием на общество.\n'
                                                          'б) Я вполне знаком(-а) с социальным медиа, но не увлекаюсь ими особенню\n'
                                                          'в) Я предпочитаю ограниченное использование социальных медиа или совсем ими не пользуюсь.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_4_3', state=Test_four.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=2)
    owner_message_bot = await owner_message_bot.edit_text('5. Какую роль играют социальные медиа в твоей жизни?\n'
                                                          'а) Я активно использую социальные медиа и интересуюсь их влиянием на общество.\n'
                                                          'б) Я вполне знаком(-а) с социальным медиа, но не увлекаюсь ими особенню\n'
                                                          'в) Я предпочитаю ограниченное использование социальных медиа или совсем ими не пользуюсь.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_4_3', state=Test_four.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=1)
    owner_message_bot = await owner_message_bot.edit_text('5. Какую роль играют социальные медиа в твоей жизни?\n'
                                                          'а) Я активно использую социальные медиа и интересуюсь их влиянием на общество.\n'
                                                          'б) Я вполне знаком(-а) с социальным медиа, но не увлекаюсь ими особенню.\n'
                                                          'в) Я предпочитаю ограниченное использование социальных медиа или совсем ими не пользуюсь.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_5_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_5_3', state=Test_four.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=3)
    owner_message_bot = await owner_message_bot.edit_text('6. Как ты реагируешь на изменения и неожиданности?\n'
                                                          'а) Я легко адаптируюсь к изменениям и вижу в них две новые возможности.\n'
                                                          'б) Я могу приспособиться к изменениям, но иногда нужно время для адаптации.\n'
                                                          'в) Я предпочитаю стабильность и планомерность и не очень хорошо переношу неожиданности.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_5_3', state=Test_four.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=2)
    owner_message_bot = await owner_message_bot.edit_text('6. Как ты реагируешь на изменения и неожиданности?\n'
                                                          'а) Я легко адаптируюсь к изменениям и вижу в них две новые возможности.\n'
                                                          'б) Я могу приспособиться к изменениям, но иногда нужно время для адаптации.\n'
                                                          'в) Я предпочитаю стабильность и планомерность и не очень хорошо переношу неожиданности.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_5_3', state=Test_four.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=1)
    owner_message_bot = await owner_message_bot.edit_text('6. Как ты реагируешь на изменения и неожиданности?\n'
                                                          'а) Я легко адаптируюсь к изменениям и вижу в них две новые возможности.\n'
                                                          'б) Я могу приспособиться к изменениям, но иногда нужно время для адаптации.\n'
                                                          'в) Я предпочитаю стабильность и планомерность и не очень хорошо переношу неожиданности.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_6_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_6_3', state=Test_four.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=3)
    owner_message_bot = await owner_message_bot.edit_text('7. Какую роль играют эмоции в твоей жизни?\n'
                                                          'а) Я очень эмоциональный(-ая) человек и эмоции важны для моего самовыражения.\n'
                                                          'б) Эмоции играют определенную роль в моей жизни, но не всегда определяют мои решения.\n'
                                                          'в) Я склонен(-а) к рациональному мышлению и стараюсь оставаться объективным(-ой).')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_6_3', state=Test_four.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=2)
    owner_message_bot = await owner_message_bot.edit_text('7. Какую роль играют эмоции в твоей жизни?\n'
                                                          'а) Я очень эмоциональный(-ая) человек и эмоции важны для моего самовыражения.\n'
                                                          'б) Эмоции играют определенную роль в моей жизни, но не всегда определяют мои решения.\n'
                                                          'в) Я склонен(-а) к рациональному мышлению и стараюсь оставаться объективным(-ой).')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_6_3', state=Test_four.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=1)
    owner_message_bot = await owner_message_bot.edit_text('7. Какую роль играют эмоции в твоей жизни?\n'
                                                          'а) Я очень эмоциональный(-ая) человек и эмоции важны для моего самовыражения.\n'
                                                          'б) Эмоции играют определенную роль в моей жизни, но не всегда определяют мои решения.\n'
                                                          'в) Я склонен(-а) к рациональному мышлению и стараюсь оставаться объективным(-ой).')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_7_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_7_3', state=Test_four.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=3)
    owner_message_bot = await owner_message_bot.edit_text('8. Как ты относишься к работе в команде?\n'
                                                          'а) Я нахожусь в своей тарелке, работая в коллективе, и ценю сотрудничество.\n'
                                                          'б) Я могу хорошо сотрудничать с другими, но иногда предпочитаю работать самостоятельно.\n'
                                                          'в) Я предпочитаю работать в одиночку и самостоятельно принимать решения.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_7_3', state=Test_four.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=2)
    owner_message_bot = await owner_message_bot.edit_text('8. Как ты относишься к работе в команде?\n'
                                                          'а) Я нахожусь в своей тарелке, работая в коллективе, и ценю сотрудничество.\n'
                                                          'б) Я могу хорошо сотрудничать с другими, но иногда предпочитаю работать самостоятельно.\n'
                                                          'в) Я предпочитаю работать в одиночку и самостоятельно принимать решения.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_7_3', state=Test_four.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=1)
    owner_message_bot = await owner_message_bot.edit_text('8. Как ты относишься к работе в команде?\n'
                                                          'а) Я нахожусь в своей тарелке, работая в коллективе, и ценю сотрудничество.\n'
                                                          'б) Я могу хорошо сотрудничать с другими, но иногда предпочитаю работать самостоятельно.\n'
                                                          'в) Я предпочитаю работать в одиночку и самостоятельно принимать решения.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_8_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_8_3', state=Test_four.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=3)
    owner_message_bot = await owner_message_bot.edit_text('9. Как важно для тебя иметь творческую свободу и выражение личности в работе?\n'
                                                          'а) Это крайне важно для меня, и я стремлюсь к работе, где могу полностью проявить себя.\n'
                                                          'б) Творческая свобода и выражение личности имеют значение для меня, но не являются главными приоритетами.\n'
                                                          'в) Я предпочитаю работу, где у меня есть определенные рамки, и я могу работать в предоставленных рамках.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_9_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_8_3', state=Test_four.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=2)
    owner_message_bot = await owner_message_bot.edit_text('9. Как важно для тебя иметь творческую свободу и выражение личности в работе?\n'
                                                          'а) Это крайне важно для меня, и я стремлюсь к работе, где могу полностью проявить себя.\n'
                                                          'б) Творческая свобода и выражение личности имеют значение для меня, но не являются главными приоритетами.\n'
                                                          'в) Я предпочитаю работу, где у меня есть определенные рамки, и я могу работать в предоставленных рамках.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_9_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_8_3', state=Test_four.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=1)
    owner_message_bot = await owner_message_bot.edit_text('9. Как важно для тебя иметь творческую свободу и выражение личности в работе?\n'
                                                          'а) Это крайне важно для меня, и я стремлюсь к работе, где могу полностью проявить себя.\n'
                                                          'б) Творческая свобода и выражение личности имеют значение для меня, но не являются главными приоритетами.\n'
                                                          'в) Я предпочитаю работу, где у меня есть определенные рамки, и я могу работать в предоставленных рамках.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_9_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_9_3', state=Test_four.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=3)
    owner_message_bot = await owner_message_bot.edit_text('10. Как ты относишься к идеи влиять на мнение и поведение людей через коммуникацию?\n'
                                                          'а) Я увлечен(-а) идеей влиять на мнение и поведение людей и видеть результаты своей коммуникации.\n'
                                                          'б) Мне интересно иметь некоторое влияние на людей, но не является это моей главной мотивацией.\n'
                                                          'в) Я предпочитаю не заниматься манипуляцией или влиянием на мнение людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_10_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_9_3', state=Test_four.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=2)
    owner_message_bot = await owner_message_bot.edit_text('10. Как ты относишься к идеи влиять на мнение и поведение людей через коммуникацию?\n'
                                                          'а) Я увлечен(-а) идеей влиять на мнение и поведение людей и видеть результаты своей коммуникации.\n'
                                                          'б) Мне интересно иметь некоторое влияние на людей, но не является это моей главной мотивацией.\n'
                                                          'в) Я предпочитаю не заниматься манипуляцией или влиянием на мнение людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_10_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_w_9_3', state=Test_four.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=1)
    owner_message_bot = await owner_message_bot.edit_text('10. Как ты относишься к идеи влиять на мнение и поведение людей через коммуникацию?\n'
                                                          'а) Я увлечен(-а) идеей влиять на мнение и поведение людей и видеть результаты своей коммуникации.\n'
                                                          'б) Мне интересно иметь некоторое влияние на людей, но не является это моей главной мотивацией.\n'
                                                          'в) Я предпочитаю не заниматься манипуляцией или влиянием на мнение людей.')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abw_10_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_four.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_10_3', state=Test_four.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=3)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Специальность в области рекламы и связей с общественностью не является вашим идеальным выбором.\n'
                                                              'Вам могут больше подойти другие профессии, учитывающие ваши предпочтения и интересы.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 25:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Ваш интерес к рекламе и связям с общественностью заметен, но вам может потребоваться некоторое время для определения, насколько эта область соответствует вашим навыкам и целям.\n'
                                                              'Рекомендуется дополнительное изучение и разведка данной области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 26 and result_test <= 30:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, У вас сильный интерес и потенциал для занятий в области рекламы и связей с общественностью.\n'
                                                              'Вам следует серьезно рассмотреть возможность развития в этой сфере и продолжить изучение ее аспектов.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_b_10_3', state=Test_four.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=2)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Специальность в области рекламы и связей с общественностью не является вашим идеальным выбором.\n'
                                                              'Вам могут больше подойти другие профессии, учитывающие ваши предпочтения и интересы.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 25:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Ваш интерес к рекламе и связям с общественностью заметен, но вам может потребоваться некоторое время для определения, насколько эта область соответствует вашим навыкам и целям.\n'
                                                              'Рекомендуется дополнительное изучение и разведка данной области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 26 and result_test <= 30:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, У вас сильный интерес и потенциал для занятий в области рекламы и связей с общественностью.\n'
                                                              'Вам следует серьезно рассмотреть возможность развития в этой сфере и продолжить изучение ее аспектов.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_w_10_3', state=Test_four.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_10=1)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test >= 10 and result_test <= 17:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Специальность в области рекламы и связей с общественностью не является вашим идеальным выбором.\n'
                                                              'Вам могут больше подойти другие профессии, учитывающие ваши предпочтения и интересы.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 18 and result_test <= 25:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, Ваш интерес к рекламе и связям с общественностью заметен, но вам может потребоваться некоторое время для определения, насколько эта область соответствует вашим навыкам и целям.\n'
                                                              'Рекомендуется дополнительное изучение и разведка данной области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 26 and result_test <= 30:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, У вас сильный интерес и потенциал для занятий в области рекламы и связей с общественностью.\n'
                                                              'Вам следует серьезно рассмотреть возможность развития в этой сфере и продолжить изучение ее аспектов.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


################
# ПЯТЫЙ ТЕСТ
################


@dp.callback_query_handler(lambda call: call.data == '/test_five')
async def start_test_five(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('Привет! Этот тест составлен из реальных кейсов компаний, который сталкивались с подобными ситуациями.\n'
                                                          'В нем представлены различные ситуации, из которых необходимо найти верное решение.\n'
                                                          'Попробуешь себя в роли специалиста по рекламе и PR? Приступим!\n'
                                                          'Выберите верный ответ из трех вариантов и проверьте свои знания и кругозор в этой области.\n'
                                                          'Если у тебя появятся вопросы, то свяжись с нами: pr_sapiens@inbox.ru\n\n'
                                                          '1. Ваша компания запускает новую рекламную кампанию на телевидении, главным элементом которой является логотип компании.\n'
                                                          'В каком случае изменение логотипа может быть негативным для бренда?\n'
                                                          'A) Если новый логотип хуже, чем старый\n'
                                                          'B) Если новый логотип не отражает ценности и миссию компании\n'
                                                          'C) Если новый логотип имеет яркий дизайн')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_1)
    await Test_five().question_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/response_a_1_4', state=Test_five.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Ваша компания запускает новый продукт на рынке.\n'
                                                          'Какой фактор может оказать наибольшее влияние на успех продукта?\n'
                                                          'A) Уникальность продукта\n'
                                                          'B) Большой бюджет рекламной кампании\n'
                                                          'C) Наличие конкурентов на рынке')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_1_4', state=Test_five.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=1)
    owner_message_bot = await owner_message_bot.edit_text('2. Ваша компания запускает новый продукт на рынке.\n'
                                                          'Какой фактор может оказать наибольшее влияние на успех продукта?\n'
                                                          'A) Уникальность продукта\n'
                                                          'B) Большой бюджет рекламной кампании\n'
                                                          'C) Наличие конкурентов на рынке')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_1_4', state=Test_five.question_1)
async def response_question_1(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_1=0)
    owner_message_bot = await owner_message_bot.edit_text('2. Ваша компания запускает новый продукт на рынке.\n'
                                                          'Какой фактор может оказать наибольшее влияние на успех продукта?\n'
                                                          'A) Уникальность продукта\n'
                                                          'B) Большой бюджет рекламной кампании\n'
                                                          'C) Наличие конкурентов на рынке')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_2)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_2_4', state=Test_five.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=1)
    owner_message_bot = await owner_message_bot.edit_text('3. Ваша компания по производству спортивных товаров планирует организовать благотворительное мероприятие.\n'
                                                          'Какая форма мероприятия может быть наиболее эффективной для продвижения бренда?\n'
                                                          'A) Концерт известных музыкантов\n'
                                                          'B) Турнир по гольфу для представителей бизнес-сообщества\n'
                                                          'C) Аукцион редких предметов искусства')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_2_4', state=Test_five.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Ваша компания по производству спортивных товаров планирует организовать благотворительное мероприятие.\n'
                                                          'Какая форма мероприятия может быть наиболее эффективной для продвижения бренда?\n'
                                                          'A) Концерт известных музыкантов\n'
                                                          'B) Турнир по гольфу для представителей бизнес-сообщества\n'
                                                          'C) Аукцион редких предметов искусства')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_2_4', state=Test_five.question_2)
async def response_question_2(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_2=0)
    owner_message_bot = await owner_message_bot.edit_text('3. Ваша компания по производству спортивных товаров планирует организовать благотворительное мероприятие.\n'
                                                          'Какая форма мероприятия может быть наиболее эффективной для продвижения бренда?\n'
                                                          'A) Концерт известных музыкантов\n'
                                                          'B) Турнир по гольфу для представителей бизнес-сообщества\n'
                                                          'C) Аукцион редких предметов искусства')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_3)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_3_4', state=Test_five.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Ваша компания готовится к выходу на новый рынок.\n'
                                                          'Какая стратегия может быть наиболее эффективной для привлечения внимания потенциальных клиентов?\n'
                                                          'A) Большой бюджет рекламной кампании в социальных сетях\n'
                                                          'B) Подключение партнеров по продаже в целевой стране\n'
                                                          'C) Организация публичной конференции')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_3_4', state=Test_five.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=1)
    owner_message_bot = await owner_message_bot.edit_text('4. Ваша компания готовится к выходу на новый рынок.\n'
                                                          'Какая стратегия может быть наиболее эффективной для привлечения внимания потенциальных клиентов?\n'
                                                          'A) Большой бюджет рекламной кампании в социальных сетях\n'
                                                          'B) Подключение партнеров по продаже в целевой стране\n'
                                                          'C) Организация публичной конференции')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_3_4', state=Test_five.question_3)
async def response_question_3(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_3=0)
    owner_message_bot = await owner_message_bot.edit_text('4. Ваша компания готовится к выходу на новый рынок.\n'
                                                          'Какая стратегия может быть наиболее эффективной для привлечения внимания потенциальных клиентов?\n'
                                                          'A) Большой бюджет рекламной кампании в социальных сетях\n'
                                                          'B) Подключение партнеров по продаже в целевой стране\n'
                                                          'C) Организация публичной конференции')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_4)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_4_4', state=Test_five.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Вы работаете в PR-отделе компании, которая планирует запустить новую рекламную кампанию в социальных сетях.\n'
                                                          'Какие из этих элементов необходимо учитывать при разработке контента для кампании\n'
                                                          'A) Возраст и пол вашей целевой аудитории\n'
                                                          'B) Интересы и поведение вашей целевой аудитории\n'
                                                          'C) Цветовые предпочтения рекламных агенств')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_4_4', state=Test_five.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=1)
    owner_message_bot = await owner_message_bot.edit_text('5. Вы работаете в PR-отделе компании, которая планирует запустить новую рекламную кампанию в социальных сетях.\n'
                                                          'Какие из этих элементов необходимо учитывать при разработке контента для кампании\n'
                                                          'A) Возраст и пол вашей целевой аудитории\n'
                                                          'B) Интересы и поведение вашей целевой аудитории\n'
                                                          'C) Цветовые предпочтения рекламных агенств')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_4_4', state=Test_five.question_4)
async def response_question_4(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_4=0)
    owner_message_bot = await owner_message_bot.edit_text('5. Вы работаете в PR-отделе компании, которая планирует запустить новую рекламную кампанию в социальных сетях.\n'
                                                          'Какие из этих элементов необходимо учитывать при разработке контента для кампании\n'
                                                          'A) Возраст и пол вашей целевой аудитории\n'
                                                          'B) Интересы и поведение вашей целевой аудитории\n'
                                                          'C) Цветовые предпочтения рекламных агенств')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_5)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_5_4', state=Test_five.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=1)
    owner_message_bot = await owner_message_bot.edit_text('6. Ваша компания планирует провести мероприятие в поддержку благотворительной организации.\n'
                                                          'Какая из этих стратегий может увеличить интерес и участие публики в мероприятии?\n'
                                                          'A) Размещение информации о мероприятии только на сайте компании\n'
                                                          'B) Организация конкурсов и розыгрышей на страницах социальных сетей\n'
                                                          'C) Ограничение доступа к мероприятию только для важных гостей')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_5_4', state=Test_five.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    owner_message_bot = await owner_message_bot.edit_text('6. Ваша компания планирует провести мероприятие в поддержку благотворительной организации.\n'
                                                          'Какая из этих стратегий может увеличить интерес и участие публики в мероприятии?\n'
                                                          'A) Размещение информации о мероприятии только на сайте компании\n'
                                                          'B) Организация конкурсов и розыгрышей на страницах социальных сетей\n'
                                                          'C) Ограничение доступа к мероприятию только для важных гостей')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_5_4', state=Test_five.question_5)
async def response_question_5(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_5=0)
    owner_message_bot = await owner_message_bot.edit_text('6. Ваша компания планирует провести мероприятие в поддержку благотворительной организации.\n'
                                                          'Какая из этих стратегий может увеличить интерес и участие публики в мероприятии?\n'
                                                          'A) Размещение информации о мероприятии только на сайте компании\n'
                                                          'B) Организация конкурсов и розыгрышей на страницах социальных сетей\n'
                                                          'C) Ограничение доступа к мероприятию только для важных гостей')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_6)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_6_4', state=Test_five.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=0)
    owner_message_bot = await owner_message_bot.edit_text('7. Ваша компания получила отрицательный обзор от одного из влиятельных блогеров в вашей отрасли.\n'
                                                          'Какие действия можно предпринять, чтобы изменить отношение блогера к вашей компании\n'
                                                          'A) Опубликовать негативный обзор в ответ на блоге этого блогера\n'
                                                          'B) Связаться с блогером и попросить его удалить отрицательный обзор\n'
                                                          'C) Предложить блогеру бесплатную продукцию для тестирования')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_6_4', state=Test_five.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=1)
    owner_message_bot = await owner_message_bot.edit_text('7. Ваша компания получила отрицательный обзор от одного из влиятельных блогеров в вашей отрасли.\n'
                                                          'Какие действия можно предпринять, чтобы изменить отношение блогера к вашей компании\n'
                                                          'A) Опубликовать негативный обзор в ответ на блоге этого блогера\n'
                                                          'B) Связаться с блогером и попросить его удалить отрицательный обзор\n'
                                                          'C) Предложить блогеру бесплатную продукцию для тестирования')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_6_4', state=Test_five.question_6)
async def response_question_6(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_6=0)
    owner_message_bot = await owner_message_bot.edit_text('7. Ваша компания получила отрицательный обзор от одного из влиятельных блогеров в вашей отрасли.\n'
                                                          'Какие действия можно предпринять, чтобы изменить отношение блогера к вашей компании\n'
                                                          'A) Опубликовать негативный обзор в ответ на блоге этого блогера\n'
                                                          'B) Связаться с блогером и попросить его удалить отрицательный обзор\n'
                                                          'C) Предложить блогеру бесплатную продукцию для тестирования')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_7)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_7_4', state=Test_five.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=0)
    owner_message_bot = await owner_message_bot.edit_text('8. Ваша компания запустила новый продукт, который не получает достаточного количества продаж.\n'
                                                          'Какие действия можно предпринять, чтобы увеличить количество продаж?\n'
                                                          'A) Увеличить цену продукта\n'
                                                          'B) Организовать бесплатный промо-материал для клиентов\n'
                                                          'C) Создать рекламную кампанию в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_7_4', state=Test_five.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=0)
    owner_message_bot = await owner_message_bot.edit_text('8. Ваша компания запустила новый продукт, который не получает достаточного количества продаж.\n'
                                                          'Какие действия можно предпринять, чтобы увеличить количество продаж?\n'
                                                          'A) Увеличить цену продукта\n'
                                                          'B) Организовать бесплатный промо-материал для клиентов\n'
                                                          'C) Создать рекламную кампанию в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_7_4', state=Test_five.question_7)
async def response_question_7(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_7=1)
    owner_message_bot = await owner_message_bot.edit_text('8. Ваша компания запустила новый продукт, который не получает достаточного количества продаж.\n'
                                                          'Какие действия можно предпринять, чтобы увеличить количество продаж?\n'
                                                          'A) Увеличить цену продукта\n'
                                                          'B) Организовать бесплатный промо-материал для клиентов\n'
                                                          'C) Создать рекламную кампанию в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_8)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_8_4', state=Test_five.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=0)
    owner_message_bot = await owner_message_bot.edit_text('9. Ваша компания планирует организовать пресс-конференцию для представления нового продукта.\n'
                                                          'Какие действия могут помочь привлечь больше внимания к мероприятию?\n'
                                                          'A) Отправить приглашения только локальным журналистам\n'
                                                          'B) Попросить участников мероприятия написать отзывы на сайте компании\n'
                                                          'C) Разместить рекламу о мероприятии в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_8_4', state=Test_five.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=0)
    owner_message_bot = await owner_message_bot.edit_text('9. Ваша компания планирует организовать пресс-конференцию для представления нового продукта.\n'
                                                          'Какие действия могут помочь привлечь больше внимания к мероприятию?\n'
                                                          'A) Отправить приглашения только локальным журналистам\n'
                                                          'B) Попросить участников мероприятия написать отзывы на сайте компании\n'
                                                          'C) Разместить рекламу о мероприятии в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_8_4', state=Test_five.question_8)
async def response_question_8(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_8=1)
    owner_message_bot = await owner_message_bot.edit_text('9. Ваша компания планирует организовать пресс-конференцию для представления нового продукта.\n'
                                                          'Какие действия могут помочь привлечь больше внимания к мероприятию?\n'
                                                          'A) Отправить приглашения только локальным журналистам\n'
                                                          'B) Попросить участников мероприятия написать отзывы на сайте компании\n'
                                                          'C) Разместить рекламу о мероприятии в социальных сетях')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_9)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_9_4', state=Test_five.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=0)
    owner_message_bot = await owner_message_bot.edit_text('10. Ваша компания запустила рекламную кампанию, но результаты не соответствуют ожиданиям.\n'
                                                          'Какие действия можно предпринять, чтобы улучшить эффективность кампании?\n'
                                                          'A) Увеличить стоимость продукта\n'
                                                          'B) Изменить изображение в рекламной кампании\n'
                                                          'C) Изменить цвета логотипа компании')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_9_4', state=Test_five.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=0)
    owner_message_bot = await owner_message_bot.edit_text('10. Ваша компания запустила рекламную кампанию, но результаты не соответствуют ожиданиям.\n'
                                                          'Какие действия можно предпринять, чтобы улучшить эффективность кампании?\n'
                                                          'A) Увеличить стоимость продукта\n'
                                                          'B) Изменить изображение в рекламной кампании\n'
                                                          'C) Изменить цвета логотипа компании')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_9_4', state=Test_five.question_9)
async def response_question_9(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question_9=1)
    owner_message_bot = await owner_message_bot.edit_text('10. Ваша компания запустила рекламную кампанию, но результаты не соответствуют ожиданиям.\n'
                                                          'Какие действия можно предпринять, чтобы улучшить эффективность кампании?\n'
                                                          'A) Увеличить стоимость продукта\n'
                                                          'B) Изменить изображение в рекламной кампании\n'
                                                          'C) Изменить цвета логотипа компании')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_10)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_10_4', state=Test_five.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question10=0)
    owner_message_bot = await owner_message_bot.edit_text('11. Ваша компания получила негативные отзывы на сайтах отзывов.\n'
                                                          'Какие действия можно предпринять, чтобы снизить количество негативных отзывов?\n'
                                                          'A) Удалить негативные отзывы\n'
                                                          'B) Написать поддельные положительные отзывы\n'
                                                          'C) Связаться с клиентами, чтобы понять их проблемы и решить их')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_11)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_10_4', state=Test_five.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question10=1)
    owner_message_bot = await owner_message_bot.edit_text('11. Ваша компания получила негативные отзывы на сайтах отзывов.\n'
                                                          'Какие действия можно предпринять, чтобы снизить количество негативных отзывов?\n'
                                                          'A) Удалить негативные отзывы\n'
                                                          'B) Написать поддельные положительные отзывы\n'
                                                          'C) Связаться с клиентами, чтобы понять их проблемы и решить их')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_11)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_10_4', state=Test_five.question_10)
async def response_question_10(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question10=0)
    owner_message_bot = await owner_message_bot.edit_text('11. Ваша компания получила негативные отзывы на сайтах отзывов.\n'
                                                          'Какие действия можно предпринять, чтобы снизить количество негативных отзывов?\n'
                                                          'A) Удалить негативные отзывы\n'
                                                          'B) Написать поддельные положительные отзывы\n'
                                                          'C) Связаться с клиентами, чтобы понять их проблемы и решить их')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_11)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_11_4', state=Test_five.question_11)
async def response_question_11(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question11=0)
    owner_message_bot = await owner_message_bot.edit_text('12. Ваша компания запускает новый продукт, и вы хотите привлечь внимание СМИ.\n'
                                                          'Какие действия можно предпринять, чтобы получить максимальное количество публикаций?\n'
                                                          'A) Купить рекламу на всех доступных СМИ\n'
                                                          'B) Связаться с журналистами и рассказать им о продукте\n'
                                                          'C) Создать ложные новости о продукте')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_12)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_11_4', state=Test_five.question_11)
async def response_question_11(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question11=0)
    owner_message_bot = await owner_message_bot.edit_text('12. Ваша компания запускает новый продукт, и вы хотите привлечь внимание СМИ.\n'
                                                          'Какие действия можно предпринять, чтобы получить максимальное количество публикаций?\n'
                                                          'A) Купить рекламу на всех доступных СМИ\n'
                                                          'B) Связаться с журналистами и рассказать им о продукте\n'
                                                          'C) Создать ложные новости о продукте')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_12)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_11_4', state=Test_five.question_11)
async def response_question_11(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question11=1)
    owner_message_bot = await owner_message_bot.edit_text('12. Ваша компания запускает новый продукт, и вы хотите привлечь внимание СМИ.\n'
                                                          'Какие действия можно предпринять, чтобы получить максимальное количество публикаций?\n'
                                                          'A) Купить рекламу на всех доступных СМИ\n'
                                                          'B) Связаться с журналистами и рассказать им о продукте\n'
                                                          'C) Создать ложные новости о продукте')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_12)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_12_4', state=Test_five.question_12)
async def response_question_12(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question12=0)
    owner_message_bot = await owner_message_bot.edit_text('13. Вы хотите увеличить число подписчиков на странице вашей компании в социальных сетях.\n'
                                                          'Какие действия можно предпринять, чтобы достичь этой цели?\n'
                                                          'A) Купить подписчиков\n'
                                                          'B) Создать интересный контент, который будет популярен в социальных сетях\n'
                                                          'C) Принудительно подписывать пользователей на вашу страницу')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_13)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_12_4', state=Test_five.question_12)
async def response_question_12(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question12=1)
    owner_message_bot = await owner_message_bot.edit_text('13. Вы хотите увеличить число подписчиков на странице вашей компании в социальных сетях.\n'
                                                          'Какие действия можно предпринять, чтобы достичь этой цели?\n'
                                                          'A) Купить подписчиков\n'
                                                          'B) Создать интересный контент, который будет популярен в социальных сетях\n'
                                                          'C) Принудительно подписывать пользователей на вашу страницу')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_13)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_12_4', state=Test_five.question_12)
async def response_question_12(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question12=0)
    owner_message_bot = await owner_message_bot.edit_text('13. Вы хотите увеличить число подписчиков на странице вашей компании в социальных сетях.\n'
                                                          'Какие действия можно предпринять, чтобы достичь этой цели?\n'
                                                          'A) Купить подписчиков\n'
                                                          'B) Создать интересный контент, который будет популярен в социальных сетях\n'
                                                          'C) Принудительно подписывать пользователей на вашу страницу')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_13)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_13_4', state=Test_five.question_13)
async def response_question_13(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question13=0)
    owner_message_bot = await owner_message_bot.edit_text('14. Вы узнали, что конкурентная компания запускает агрессивную рекламную кампанию, направленную на отрицание вашего продукта.\n'
                                                          'Какие действия можно предпринять, чтобы справиться с этим вызовом?\n'
                                                          'A) Изменить свой продукт, чтобы сделать его более конкурентноспособным\n'
                                                          'B) Запустить еще более агрессивную рекламную кампанию\n'
                                                          'C) Сделать акцент на качественных характеристиках продукта в своей рекламе')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_14)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_b_13_4', state=Test_five.question_13)
async def response_question_13(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question13=1)
    owner_message_bot = await owner_message_bot.edit_text('14. Вы узнали, что конкурентная компания запускает агрессивную рекламную кампанию, направленную на отрицание вашего продукта.\n'
                                                          'Какие действия можно предпринять, чтобы справиться с этим вызовом?\n'
                                                          'A) Изменить свой продукт, чтобы сделать его более конкурентноспособным\n'
                                                          'B) Запустить еще более агрессивную рекламную кампанию\n'
                                                          'C) Сделать акцент на качественных характеристиках продукта в своей рекламе')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_14)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_c_13_4', state=Test_five.question_13)
async def response_question_13(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question13=0)
    owner_message_bot = await owner_message_bot.edit_text('14. Вы узнали, что конкурентная компания запускает агрессивную рекламную кампанию, направленную на отрицание вашего продукта.\n'
                                                          'Какие действия можно предпринять, чтобы справиться с этим вызовом?\n'
                                                          'A) Изменить свой продукт, чтобы сделать его более конкурентноспособным\n'
                                                          'B) Запустить еще более агрессивную рекламную кампанию\n'
                                                          'C) Сделать акцент на качественных характеристиках продукта в своей рекламе')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_abc_14)
    data_question = await state.get_data()
    print(data_question)
    await Test_five.next()


@dp.callback_query_handler(lambda call: call.data == '/response_a_14_4', state=Test_five.question_14)
async def response_question_14(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question14=0)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 5 and result_test <= 9:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 10 and result_test <= 12:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 13 and result_test <= 14:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_a_14_4', state=Test_five.question_14)
async def response_question_14(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question14=0)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 5 and result_test <= 9:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 10 and result_test <= 12:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 13 and result_test <= 14:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_b_14_4', state=Test_five.question_14)
async def response_question_14(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question14=0)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 5 and result_test <= 9:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 10 and result_test <= 12:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 13 and result_test <= 14:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/response_c_14_4', state=Test_five.question_14)
async def response_question_14(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await state.update_data(question14=1)
    data_question = await state.get_data()
    result_test = 0
    for i in data_question:
        result_test = result_test + data_question[i]
    if result_test <= 4:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Новичок. Тебе еще предстоит много учиться и изучать мир рекламы:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 5 and result_test <= 9:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Опытный. Ты знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 10 and result_test <= 12:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Профессионал. Ты отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    elif result_test >= 13 and result_test <= 14:
        owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username} - Эксперт. Ты имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    else:
        owner_message_bot = await owner_message_bot.edit_text('Что-то пошло не так с подсчетом результатов, попрробуем еще разок?😢')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    print(data_question)
    await state.finish()


@dp.callback_query_handler(lambda call: call.data == '/cancel', state='*')
async def cancel(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, привет!\nПройдем несколько тестов?😉')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_start_menu)
    await state.reset_data()
    await state.reset_state()
    await state.finish()
    await callback_query.answer()


###############
# СТАРТ РЕБУСОВ
###############


@dp.callback_query_handler(lambda call: call.data == '/cancel_rebus', state='*')
async def cancel(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    await owner_message_bot.delete()
    owner_message_bot = await bot.send_message(callback_query.message.chat.id, f'@{callback_query.from_user.username}, привет!\nПройдем несколько тестов?😉', reply_markup=markup_start_menu)
    await state.reset_data()
    await state.reset_state()
    await state.finish()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/rebus')
async def start_test_one(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text('В этом тесте необходимо написать ответ в чат. Умеешь ли ты решать ребусы? Провеерим!')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_keyboard_start_rebus)
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/start_rebus')
async def start_rebus(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    with open('pictures/rebus/1.png', 'rb') as rebus:
        await owner_message_bot.delete()
        owner_message_bot = await bot.send_photo(callback_query.message.chat.id, rebus, caption='Пришли ответ в чат:)')
        owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
    await Rebus().rebus_1.set()
    await callback_query.answer()


@dp.callback_query_handler(lambda call: call.data == '/back_to_menu')
async def back_to_menu(callback_query: types.CallbackQuery, state: FSMContext):
    global owner_message_bot
    owner_message_bot = await owner_message_bot.edit_text(f'@{callback_query.from_user.username}, привет!\nПройдем несколько тестов?😉')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_start_menu)
    await callback_query.answer()


##########################################
# Message handlers / Обрабочтики сообщений
##########################################


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    global owner_message_bot
    global list_users
    owner_message_bot = await bot.send_message(message.chat.id, f'@{message.from_user.username}, привет!\nПройдем несколько тестов?😉', reply_markup=markup_start_menu)
    username = message.from_user.username
    if username in list_users:
        pass
    else:
        list_users.append(f'@{username}')
    print(list_users)
    print(message.chat.id)
    await message.delete()


@dp.message_handler(commands='users')
async def command_users(message: types.Message):
    global owner_message_bot
    global list_users
    owner_message_bot = await owner_message_bot.edit_text(f'Список пользователей которые сюда писали:\n\n{list_users}')
    owner_message_bot = await owner_message_bot.edit_reply_markup(markup_back_to_menu)
    await message.delete()


#######################
# Ответ на первый ребус
#######################


@dp.message_handler(state=Rebus.rebus_1)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'билборд' and counter_response == 0:
        await state.update_data(rebus_1=0)
        await message.delete()
        with open('pictures/rebus/1.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'билборд' and counter_response == 1:
        await state.update_data(rebus_1=0)
        await message.delete()
        with open('pictures/rebus/1.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'билборд' and counter_response == 2:
        await state.update_data(rebus_1=0)
        await message.delete()
        with open('pictures/rebus/2.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Билборд".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'билборд' and counter_response < 3:
        await state.update_data(rebus_1=1)
        await message.delete()
        with open('pictures/rebus/2.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Верный ответ: Билборд. Рекламные щиты, установленные, как правило на самых оживленных трассах и магистралях\n'
                                                     'Популярные размеры рекламного поля серийных щитов - 3х6 м и 3х12 м.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_2)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'баннер' and counter_response == 0:
        await state.update_data(rebus_2=0)
        await message.delete()
        with open('pictures/rebus/2.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'баннер' and counter_response == 1:
        await state.update_data(rebus_2=0)
        await message.delete()
        with open('pictures/rebus/2.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'баннер' and counter_response == 2:
        await state.update_data(rebus_2=0)
        await message.delete()
        with open('pictures/rebus/3.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Баннер".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'баннер' and counter_response < 3:
        await state.update_data(rebus_2=1)
        await message.delete()
        with open('pictures/rebus/3.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Баннер (от англ. banner - флаг, транспарант, растяжка) - 1) прямоугольник из винилового полотна (ткани) с рекламным текстом, используемый для транспаранта-перетяжки;\n'
                                                     '2) напечатанное на виниловой ткани изображение для магистральных щитов (билбордов);\n'
                                                     '3) рекламный плакат, выполненный в виде флага с напечатанным на нем рекламным объявлением;\n'
                                                     '4) изображение или текстовый блок на web-сайте, являющиеся гиперссылкой на сайт рекламодателя, где находится подробное описание продукта или услуги.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_3)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'брендбук' and counter_response == 0:
        await state.update_data(rebus_3=0)
        await message.delete()
        with open('pictures/rebus/3.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'брендбук' and counter_response == 1:
        await state.update_data(rebus_3=0)
        await message.delete()
        with open('pictures/rebus/3.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'брендбук' and counter_response == 2:
        await state.update_data(rebus_3=0)
        await message.delete()
        with open('pictures/rebus/4.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Брендбук".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'брендбук' and counter_response < 3:
        await state.update_data(rebus_3=1)
        await message.delete()
        with open('pictures/rebus/4.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Брендбук (брэндбук) - руководсттво по фирменному стилю.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_4)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'имидж' and counter_response == 0:
        await state.update_data(rebus_4=0)
        await message.delete()
        with open('pictures/rebus/4.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'имидж' and counter_response == 1:
        await state.update_data(rebus_4=0)
        await message.delete()
        with open('pictures/rebus/4.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'имидж' and counter_response == 2:
        await state.update_data(rebus_4=0)
        await message.delete()
        with open('pictures/rebus/5.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Имидж".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'имидж' and counter_response < 3:
        await state.update_data(rebus_4=1)
        await message.delete()
        with open('pictures/rebus/5.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Имидж - (от англ. image - мысленный образ, преедставление, мнение) - \n'
                                                     '1. Образ товара, услуги или компании, как совокупность асссоциаций и впечатлений о них, который складывается в сознании потребителей и формирует их определенное отношение к этому товару, услуге или компании.\n'
                                                     '2. Специально проектируемый в интересах фирмы, основанный на особенностях деятельности, достоинствах, качествах образ, который целенаправленно внедряется в сознаниеи подсознание целевой аудитории, соответствует их ожиданиям, стереотипам и служит отличию фирмы, товаров, услуг, бренда от аналогичных.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_5)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'контент' and counter_response == 0:
        await state.update_data(rebus_5=0)
        await message.delete()
        with open('pictures/rebus/5.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'контент' and counter_response == 1:
        await state.update_data(rebus_5=0)
        await message.delete()
        with open('pictures/rebus/5.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'контент' and counter_response == 2:
        await state.update_data(rebus_5=0)
        await message.delete()
        with open('pictures/rebus/6.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Контент".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'контент' and counter_response < 3:
        await state.update_data(rebus_5=1)
        await message.delete()
        with open('pictures/rebus/6.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Контент (от англ. content - содержкание) - в широком смысле это наполнение сайта.\n'
                                                     'Контент сайта соотносится с дизайном, как содержание с формой.\n'
                                                     'В более узком смысле слова контент сайта - это материалы, размещенные на нем: в основном тексты, а также картинки и музыка.\n'
                                                     'В этом смысле веб-сервисы и разного рода движки контентов не ялвяются.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_6)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'медиапланирование' and counter_response == 0:
        await state.update_data(rebus_6=0)
        await message.delete()
        with open('pictures/rebus/6.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'медиапланирование' and counter_response == 1:
        await state.update_data(rebus_6=0)
        await message.delete()
        with open('pictures/rebus/6.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'медиапланирование' and counter_response == 2:
        await state.update_data(rebus_6=0)
        await message.delete()
        with open('pictures/rebus/7.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Медиапланирование".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'медиапланирование' and counter_response < 3:
        await state.update_data(rebus_6=1)
        await message.delete()
        with open('pictures/rebus/7.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Медиапланирование - план проведения рекламной кампании, учитывающий бюджет, сроки и конкретные СМИ, в которых будут размещаться рекламные обращения.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_7)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'мерчандайзинг' and counter_response == 0:
        await state.update_data(rebus_7=0)
        await message.delete()
        with open('pictures/rebus/7.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'мерчандайзинг' and counter_response == 1:
        await state.update_data(rebus_7=0)
        await message.delete()
        with open('pictures/rebus/7.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'мерчандайзинг' and counter_response == 2:
        await state.update_data(rebus_7=0)
        await message.delete()
        with open('pictures/rebus/8.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Мерчандайзинг".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'мерчандайзинг' and counter_response < 3:
        await state.update_data(rebus_7=1)
        await message.delete()
        with open('pictures/rebus/8.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Мерчандайзинг - комплекс маркетинговых коммуникаций в розничной торговле.\n'
                                                     'Мерчандайзинг использует в основном приемы рекламы на местах продаж и sales promotion.\n'
                                                     'Основная задача - стимулирование продавцов к активным продажам рекламируемых товаров и воздействию на покупателей с целью обеспечения ими покупки.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_8)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'позиционирование' and counter_response == 0:
        await state.update_data(rebus_8=0)
        await message.delete()
        with open('pictures/rebus/8.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'позиционирование' and counter_response == 1:
        await state.update_data(rebus_8=0)
        await message.delete()
        with open('pictures/rebus/8.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'позиционирование' and counter_response == 2:
        await state.update_data(rebus_8=0)
        await message.delete()
        with open('pictures/rebus/9.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Позиционирование".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'позиционирование' and counter_response < 3:
        await state.update_data(rebus_8=1)
        await message.delete()
        with open('pictures/rebus/9.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Поцизионирование - формирование в сознании потребителей четкого образа компании или продукта, отличного от конкурентов.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_9)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'таргетинг' and counter_response == 0:
        await state.update_data(rebus_9=0)
        await message.delete()
        with open('pictures/rebus/10.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'таргетинг' and counter_response == 1:
        await state.update_data(rebus_9=0)
        await message.delete()
        with open('pictures/rebus/9.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'таргетинг' and counter_response == 2:
        await state.update_data(rebus_9=0)
        await message.delete()
        with open('pictures/rebus/10.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Правильный ответ - "Таргетинг".\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()
    elif message.text.lower() == 'таргетинг' and counter_response < 3:
        await state.update_data(rebus_9=1)
        await message.delete()
        with open('pictures/rebus/10.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Таргетинг (от англ. target - цель, употребляется также форма "таргетирование") - \n'
                                                     'это механизм, позволяющий выделить из всей имеющейся аудитории только ту часть, которая удовлетворяет заданным критериям (целевую аудиторию), и показать рекламу именно ей.\n\n'
                                                     'А теперь давай дальше: ')
        counter_response = 0
        print(counter_response)
        await Rebus.next()


@dp.message_handler(state=Rebus.rebus_10)
async def write_response_rebus_1(message: types.Message, state: FSMContext):
    global owner_message_bot
    global counter_response
    if message.text.lower() != 'маркетинг' and counter_response == 0:
        await state.update_data(rebus_10=0)
        await message.delete()
        with open('pictures/rebus/10.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 2 попытки')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'маркетинг' and counter_response == 1:
        await state.update_data(rebus_10=0)
        await message.delete()
        with open('pictures/rebus/10.png', 'rb') as rebus:
            await owner_message_bot.delete()
            owner_message_bot = await bot.send_photo(message.chat.id, rebus, caption='Ответ неправильный, у тебя еще 1 попытка')
            owner_message_bot = await owner_message_bot.edit_reply_markup(markup_cancel_rebus)
        counter_response += 1
        print(counter_response)
    elif message.text.lower() != 'маркетинг' and counter_response == 2:
        await state.update_data(rebus_10=0)
        await message.delete()
        await owner_message_bot.delete()
        counter_response = 0
        print(counter_response)
        data_rebus = await state.get_data()
        result_rebus = 0
        for i in data_rebus:
            result_rebus = result_rebus + data_rebus[i]
        print(result_rebus)
        if result_rebus <= 2:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Новичок.\nТебе еще предстоит много учиться и изучать мир рекламы:)\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 3 and result_rebus <= 5:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Опытный.\nТы знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 6 and result_rebus <= 8:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Профессионал.\nТы отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 9 and result_rebus <= 10:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Эксперт.\nТы имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        await state.finish()
    elif message.text.lower() == 'маркетинг' and counter_response < 3:
        await state.update_data(rebus_10=1)
        await message.delete()
        await owner_message_bot.delete()
        counter_response = 0
        print(counter_response)
        data_rebus = await state.get_data()
        result_rebus = 0
        for i in data_rebus:
            result_rebus = result_rebus + data_rebus[i]
        print(result_rebus)
        if result_rebus <= 2:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Новичок.\nТебе еще предстоит много учиться и изучать мир рекламы:)\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 3 and result_rebus <= 5:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Опытный.\nТы знаешь многое о рекламе и пиаре, но еще есть некоторые пробелы в знаниях\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 6 and result_rebus <= 8:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Профессионал.\nТы отлично разбираешься в этой области и можешь считать себя настоящим профессионалом.\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        elif result_rebus >= 9 and result_rebus <= 10:
            owner_message_bot = await bot.send_message(message.chat.id, 'Правильный ответ - "Маркетинг".\nТы - Эксперт.\nТы имеешь глубокие знания и понимание мира рекламы, и можешь считать себя экспертом в этой области.\n\nНадеюсь ты уже прошел остальные тесты?:)', reply_markup=markup_back_to_menu)
        await state.finish()
