# v. 0.01
# ENG
# Hello dear friend. This product was created by Vladimir Shalyapin, a post-graduate student of the KubSAU Department of Agrochemistry.
# The authors of the original yield forecasting model are A. I. Trubilin, G. F. Petrik, A. G. Prudnikov.
# References: Forecasting crop yields: textbook / A. I. Trubilin, G. F. Petrik, A. G. Prudnikov - Krasnodar: KubSAU, 2017. - 95 p. ISBN 978-5-00097-382-0
# The principle of the methodology is the sum of the actual yield on average for three years, taken in sequence four years from the forecast year, the increase in yield from the introduction of innovations for 4 years and the stochastic (random) component, the standard deviation.
# The code is written in Python 3.9
# The program code is under development.
# The author expresses special gratitude to my friend and colleague for support in my case, Ali Ali Kadem Ali.

# RUS
# Здравствуй, дорогой друг. Этот продукт создан Владимиром Шаляпиным, аспирантом кафедры агрохимии КубГАУ.
# Авторами оригинальной модели прогнозирования урожайности являются А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников.
# Использованная литература: Прогнозирование урожайности сельскохозяйственных культур: учебное пособие / А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников - Краснодар: КубГАУ, 2017. - 95 с. ISBN 978-5-00097-382-0
# Принцип методики заключается в сумме фактической урожайности в среднем за три года, взятой последовательно за четыре года от года прогноза, прироста урожайности от внедрения инноваций за 4 года и стохастической (случайной) составляющей, среднеквадратичного отклонения.
# Код написан на Python 3.9
# Программный код находится в стадии разработки.
# Особую благодарность автор выражает моему другу и коллеге за поддержку в моем деле Али Али Кадем Али.

import math
print('Данное программное обеспечение расчитывает краткосрочный прогноз урожайности зерновых культур.')
print('Приемлемая длина базисного периода в прогнозировании урожайности является период 11-20 лет и ')
print('четырехлетняя цикличность, формируемая солнечной активностью.')
print('Автор ПО Шаляпин В. В. Авторы оригинальной модели прогнозирования урожайности А. И. Трубилин,')
print('Г. Ф. Петрик, А. Г. Прудников.')

while True:
    year_0 = input('Введите прогнозируемый год: ')
    year_1 = int(year_0) - int(12)
    year_2 = int(year_0) - int(8)
    year_3 = int(year_0) - int(7)
    year_4 = int(year_0) - int(6)
    year_5 = int(year_0) - int(5)
    year_6 = int(year_0) - int(4)
    year_7 = int(year_0) - int(3)
    year_8 = int(year_0) - int(2)
    year_9 = int(year_0) - int(1)
    print('Для расчета потребуются данные об урожайности за следующие года; ' + str(year_1) + ', ' + str(year_2) + ', ' + str(year_3) + ', ' + str(year_4) + ', ' + str(year_5) + ', ' + str(year_6) + ', ' + str(year_7) + ', ' + str(year_8) + ', ' + str(year_9))

    number_1 = input('Урожайность ' + str(year_1) + ' ц/га: ')
    number_2 = input('Урожайность ' + str(year_2) + ' ц/га: ')
    number_3 = input('Урожайность ' + str(year_3) + ' ц/га: ')
    number_4 = input('Урожайность ' + str(year_4) + ' ц/га: ')
    number_5 = input('Урожайность ' + str(year_5) + ' ц/га: ')
    number_6 = input('Урожайность ' + str(year_6) + ' ц/га: ')
    number_7 = input('Урожайность ' + str(year_7) + ' ц/га: ')
    number_8 = input('Урожайность ' + str(year_8) + ' ц/га: ')
    number_9 = input('Урожайность ' + str(year_9) + ' ц/га: ')

    deviation_sum_n2345 = float(number_2) + float(number_3) + float(number_4) + float(number_5)
    middle_square_n2345 = float(deviation_sum_n2345)/4
    r_middle_square_n2345 = round(middle_square_n2345,1)

    deviation_sum_n3456 = float(number_3) + float(number_4) + float(number_5) + float(number_6)
    middle_square_n3456 = float(deviation_sum_n3456)/4
    r_middle_square_n3456 = round(middle_square_n3456,1)

    deviation_sum_n4567 = float(number_4) + float(number_5) + float(number_6) + float(number_7)
    middle_square_n4567 = float(deviation_sum_n4567)/4
    r_middle_square_n4567 = round(middle_square_n4567,1)

    deviation_sum_n5678 = float(number_5) + float(number_6) + float(number_7) + float(number_8)
    middle_square_n5678 = float(deviation_sum_n5678)/4
    r_middle_square_n5678 = round(middle_square_n5678,1)

    deviation_sum_n6789 = float(number_6) + float(number_7) + float(number_8) + float(number_9)
    middle_square_n6789 = float(deviation_sum_n6789)/4
    r_middle_square_n6789 = round(middle_square_n6789,1)

    deviation_n3456_n2345 = float(r_middle_square_n3456) - float(r_middle_square_n2345)
    r_deviation_n3456_n2345 = round(deviation_n3456_n2345,1)
    print('Изменение урожайности по сравнению с предыдущим периодом №1: ' + str(r_deviation_n3456_n2345) + ' ц с га')
    writing_to_file_n3456_n2345 = str('Изменение урожайности по сравнению с предыдущим периодом №1: ') + str(r_deviation_n3456_n2345) + str(' ц с га')

    deviation_n4567_n3456 = float(r_middle_square_n4567) - float(r_middle_square_n3456)
    r_deviation_n4567_n3456 = round(deviation_n4567_n3456,1)
    print('Изменение урожайности по сравнению с предыдущим периодом №2: ' + str(r_deviation_n4567_n3456) + ' ц с га')
    writing_to_file_n4567_n3456 = str('Изменение урожайности по сравнению с предыдущим периодом №2: ') + str(r_deviation_n4567_n3456) + str(' ц с га')

    deviation_n5678_n4567 = float(r_middle_square_n5678) - float(r_middle_square_n4567)
    r_deviation_n5678_n4567 = round(deviation_n5678_n4567,1)
    print('Изменение урожайности по сравнению с предыдущим периодом №3: ' + str(r_deviation_n5678_n4567) + ' ц с га')
    writing_to_file_n5678_n4567 = str('Изменение урожайности по сравнению с предыдущим периодом №3: ') + str(r_deviation_n5678_n4567) + str(' ц с га')

    deviation_n6789_n5678 = float(r_middle_square_n6789) - float(r_middle_square_n5678)
    r_deviation_n6789_n5678 = round(deviation_n6789_n5678,1)
    print('Изменение урожайности по сравнению с предыдущим периодом №4: ' + str(r_deviation_n6789_n5678) + ' ц с га')
    writing_to_file_n6789_n5678 = str('Изменение урожайности по сравнению с предыдущим периодом №4: ') + str(r_deviation_n6789_n5678) + str(' ц с га')

    deviation_sum = float(r_deviation_n3456_n2345) + float(r_deviation_n4567_n3456) + float(r_deviation_n5678_n4567) + float(r_deviation_n6789_n5678)
    r_deviation_sum = round(deviation_sum,1)
    print('Прирост урожайности культуры: ' + str(r_deviation_sum))
    writing_to_file_r_deviation_sum = str('Прирост урожайности культуры: ') + str(r_deviation_sum)

    actual_yield_sum = float(number_1) + float(number_2) + float(number_6)
    actual_yield = float(actual_yield_sum)/3
    r_actual_yield = round(actual_yield,1)
    print('Базисная велинина прогромируемой урожайности: ' + str(r_actual_yield))
    writing_to_file_r_actual_yield = str('Базисная велинина прогромируемой урожайности: ') + str(r_actual_yield)

    deviation_for_a_square_1_r_actual_yield = float(number_1) - float(r_actual_yield)
    deviation_square_1_r_actual_yield = float(deviation_for_a_square_1_r_actual_yield) ** 2
    r_deviation_square_1_r_actual_yield = round(deviation_square_1_r_actual_yield,1)
    dub_deviation_square_1_r_actual_yield = float(r_deviation_square_1_r_actual_yield)/3
    r_dub_deviation_square_1_r_actual_yield = round(dub_deviation_square_1_r_actual_yield,1)
    sq_1_r_actual_yield = math.sqrt(float(r_dub_deviation_square_1_r_actual_yield))
    r_sq_1_r_actual_yield = round(sq_1_r_actual_yield,1)

    deviation_for_a_square_2_r_actual_yield = float(number_2) - float(r_actual_yield)
    deviation_square_2_r_actual_yield = float(deviation_for_a_square_2_r_actual_yield) ** 2
    r_deviation_square_2_r_actual_yield = round(deviation_square_2_r_actual_yield,1)
    dub_deviation_square_2_r_actual_yield = float(r_deviation_square_2_r_actual_yield)/3
    r_dub_deviation_square_2_r_actual_yield = round(dub_deviation_square_2_r_actual_yield,1)
    sq_2_r_actual_yield = math.sqrt(float(r_dub_deviation_square_2_r_actual_yield))
    r_sq_2_r_actual_yield = round(sq_2_r_actual_yield,1)

    deviation_for_a_square_6_r_actual_yield = float(number_6) - float(r_actual_yield)
    deviation_square_6_r_actual_yield = float(deviation_for_a_square_6_r_actual_yield) ** 2
    r_deviation_square_6_r_actual_yield = round(deviation_square_6_r_actual_yield,1)
    dub_deviation_square_6_r_actual_yield = float(r_deviation_square_6_r_actual_yield)/3
    r_dub_deviation_square_6_r_actual_yield = round(dub_deviation_square_6_r_actual_yield,1)
    sq_6_r_actual_yield = math.sqrt(float(r_dub_deviation_square_6_r_actual_yield))
    r_sq_6_r_actual_yield = round(sq_6_r_actual_yield,1)
    s_sq_126 = float(r_sq_1_r_actual_yield) + float(r_sq_2_r_actual_yield) + float(r_sq_6_r_actual_yield)
    r_s_sq_126 = round(s_sq_126)

    sravnenie = float(r_s_sq_126) * float(100.0) / float(r_actual_yield)
    r_sravnenie = round(sravnenie)

    s_deviation_square_126 = float(r_deviation_square_1_r_actual_yield) + float(r_deviation_square_2_r_actual_yield) + float(r_deviation_square_6_r_actual_yield)
    r_s_deviation_square_126 = round(s_deviation_square_126,1)

    if r_sravnenie <= float(12.0):
        ds_deviation_square_126 = float(s_deviation_square_126)
        qt_126 = math.sqrt(float(ds_deviation_square_126))
        qt_126_2 = float(qt_126)/2
        r_qt_126_2 = round(qt_126_2,1)
        otk = round(deviation_for_a_square_1_r_actual_yield,1) + round(deviation_for_a_square_2_r_actual_yield,1) + round(deviation_for_a_square_6_r_actual_yield,1)
        r_otk = round(otk,1)
        print('Отклонение: '+ str(r_otk))
        print('Отклонение сторона: ' + str(r_s_deviation_square_126))
        writing_to_file_otk = str('Отклонение: ') + str(r_otk)
        writing_to_file_r_s_deviation_square_126 = str('Отклонение сторона: ') + str(r_s_deviation_square_126)

    elif r_sravnenie > float(12.0) and float(30.0) > r_sravnenie:
        ds_deviation_square_126 = float(s_deviation_square_126)/2
        qt_126 = math.sqrt(float(ds_deviation_square_126))
        qt_126_2 = float(qt_126)/2
        r_qt_126_2 = round(qt_126_2,1)
        otk = round(deviation_for_a_square_1_r_actual_yield,1) + round(deviation_for_a_square_2_r_actual_yield,1) + round(deviation_for_a_square_6_r_actual_yield,1)
        r_otk = round(otk,1)
        print('Отклонение: '+ str(r_otk))
        print('Отклонение сторона: ' + str(r_s_deviation_square_126))
        writing_to_file_otk = str('Отклонение: ') + str(r_otk)
        writing_to_file_r_s_deviation_square_126 = str('Отклонение сторона: ') + str(r_s_deviation_square_126)

    elif r_sravnenie > float(30.0) and float(45.0) > r_sravnenie:
        ds_deviation_square_126 = float(s_deviation_square_126)/3
        qt_126 = math.sqrt(float(ds_deviation_square_126))
        qt_126_2 = float(qt_126)/2
        r_qt_126_2 = round(qt_126_2,1)
        otk = round(deviation_for_a_square_1_r_actual_yield,1) + round(deviation_for_a_square_2_r_actual_yield,1) + round(deviation_for_a_square_6_r_actual_yield,1)
        r_otk = round(otk,1)
        print('Отклонение: '+ str(r_otk))
        print('Отклонение сторона: ' + str(r_s_deviation_square_126))
        writing_to_file_otk = str('Отклонение: ') + str(r_otk)
        writing_to_file_r_s_deviation_square_126 = str('Отклонение сторона: ') + str(r_s_deviation_square_126)

    elif r_sravnenie > float(45.0):
        ds_deviation_square_126 = float(s_deviation_square_126)/4
        qt_126 = math.sqrt(float(ds_deviation_square_126))
        qt_126_2 = float(qt_126)/2
        r_qt_126_2 = round(qt_126_2,1)
        otk = round(deviation_for_a_square_1_r_actual_yield,1) + round(deviation_for_a_square_2_r_actual_yield,1) + round(deviation_for_a_square_6_r_actual_yield,1)
        r_otk = round(otk,1)
        print('Отклонение: '+ str(r_otk))
        print('Отклонение сторона: ' + str(r_s_deviation_square_126))
        writing_to_file_otk = str('Отклонение: ') + str(r_otk)
        writing_to_file_r_s_deviation_square_126 = str('Отклонение сторона: ') + str(r_s_deviation_square_126)

    if number_9 >= number_8 >= number_7:
            total_yield = float(r_actual_yield) + float(r_deviation_sum) + float(r_qt_126_2) + float(4.0)
            r_total_yield = round(total_yield,1)
            print('Урожайность: ' + str(r_total_yield))
            print('Итоговый показатель урожайности: ' + str(r_total_yield) + ' ± ' + str(r_deviation_sum))
            writing_to_file_r_total_yield = str('Урожайность: ') + str(r_total_yield)
            total_writing_to_file_r_total_yield = str('Итоговый показатель урожайности: ') + str(r_total_yield) + str(' ± ') + str(r_deviation_sum)

    else:
        total_yield = float(r_actual_yield) - float(r_deviation_sum) + float(r_qt_126_2) + float(4.0)
        r_total_yield = round(total_yield,1)
        print('Урожайность: ' + str(r_total_yield))
        print('Итоговый показатель урожайности: ' + str(r_total_yield) + ' ± ' + str(r_deviation_sum))
        writing_to_file_r_total_yield = str('Урожайность: ') + str(r_total_yield)
        total_writing_to_file_r_total_yield = str('Итоговый показатель урожайности: ') + str(r_total_yield) + str(' ± ') + str(r_deviation_sum)


    print('Сохранить в txt файл?')
    button_write = input('Введите + чтобы сохранить расчеты и любую другую кнопку чтобы продолжить: ')

    if button_write == str('+'):
        name_file = input('Введите имя файла: ')
        file_w = open(str(name_file) + '.txt', 'a')
        record_1 = str(writing_to_file_n3456_n2345) + str('\n')
        file_w.write(record_1)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_2 = str(writing_to_file_n4567_n3456) + str('\n')
        file_w.write(record_2)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_3 = str(writing_to_file_n5678_n4567) + str('\n')
        file_w.write(record_3)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_4 = str(writing_to_file_n6789_n5678) + str('\n')
        file_w.write(record_4)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_5 = str(writing_to_file_r_deviation_sum) + str('\n')
        file_w.write(record_5)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_6 = str(writing_to_file_r_actual_yield) + str('\n')
        file_w.write(record_6)
        file_w.closed
        record_7 = str(writing_to_file_otk) + str('\n')
        file_w.write(record_7)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_8 = str(writing_to_file_r_s_deviation_square_126) + str('\n')
        file_w.write(record_8)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_9 = str(writing_to_file_r_total_yield) + str('\n')
        file_w.write(record_9)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_10 = str(total_writing_to_file_r_total_yield) + str('\n')
        file_w.write(record_10)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_11 = str('******************************* ') + str(year_0) + str(' ********************************') + str('\n')
        file_w.write(record_11)
        file_w.closed
        file_w = open(str(name_file) + '.txt', 'a')
        record_12 = str('\n')
        file_w.write(record_12)
        file_w.closed

# MIT License
# Copyright (c) 2022 Vladimir Shalyapin
