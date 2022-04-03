# v. 4.0
# Python 3.9.7

import math

# Deviation calculation function and its sum
# Функция расчета отклонений и ее сумма
def deviation_sum(a, b, c, d):
    deviation_sum_n = a + b + c + d
    middle_square_n = float(deviation_sum_n) / 4
    r_middle_square_n = round(middle_square_n,1)
    # return возвращает значение
    return r_middle_square_n

# Yield change
# Изменение урожайности
def yield_change(a, b):
    yield_change_difference = a - b
    r_yield_change_difference = round(yield_change_difference, 1)
    return r_yield_change_difference

# Calculation of yield growth for a short-term forecast
# Расчет прироста урожайности для краткосрочного прогноза
def yield_increase(a, b, c, d):
    # abs нужно чтобы было только абсолютные (положительные) числа
    # abs needs to be only absolute (positive) numbers
    yield_increase_s = abs(a) + abs(b) + abs(c) + abs(d)
    r_yield_increase_s = round(yield_increase_s, 1)
    return r_yield_increase_s

# Calculation of the basic programmable yield
# Расчет базисной программируемой урожайности
def mean_actual_yield(a, b, c):
    actual_yield_sum = a + b + c
    mean_actual_yield_sum = float(actual_yield_sum)/3
    r_mean_actual_yield_sum = round(mean_actual_yield_sum, 1)
    return r_mean_actual_yield_sum

# Squared deviation
# Квадрат отклонения
def calculate_the_random_component(a, b):
    deviation_from_the_mean = float(a) - float(b)
    squared_deviation = float(deviation_from_the_mean) ** 2
    r_squared_deviation = round(squared_deviation, 1)
    return r_squared_deviation  

# We consider the divisor of the standard deviation
# Считаем делитель среднеквадратичного отклонения
def divisor(a, b):
    divisor_t = float(a) - float(b)
    a_divisor_t = abs(divisor_t) / abs(b) * abs(100)
    r_a_divisor_t = round(a_divisor_t, 1)
    if float(r_a_divisor_t) <= float(15.0):
        cons_divisor = float(1.0)
    elif float(r_a_divisor_t) >= float(30.0):
        cons_divisor = float(4.0)
    elif float(r_a_divisor_t) >= float(15.0) and float(r_a_divisor_t) <= float(30.0):
        cons_divisor = float(2.0)
    return cons_divisor

# Wheat calculation logic (Russia, Krasnodar Territory), it is necessary to compare yield time series for a specific region
# Логика расчета пшеницы (Россия, Краснодарский край), необходимо сравнить временные ряды урожайности для конкретного региона

def wheat(a, b, c, d, e, f, g, h):
    if float(a) > float(b):
            if float(b) < float(c):
                if float(c) > float(d):
                    if float(d) < float(e):
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                    else:
                        condition = float(h) - float(g)
                        if float(condition) < float(5.0):
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        else:
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                else:    
                    result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
            elif float(b) > float(c):
                if float(c) > float(d):
                    result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)                        
                else:
                    condition_2 = float(d) - float(c)
                    if float(condition_2) >= float(10.0) and float(condition_2) <= float(10.4):
                        result = float(d_mean_actual_yield) - float(yield_increase_sum)
                    else:
                        condition_3 = float(e) - float(f)
                        if float(condition_3) >= float(2.5) and float(condition_3) <= float(8.0):
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        elif float(condition_3) >= float(0.0) and float(condition_3) <= float(2.4):
                            result = float(d_mean_actual_yield) - float(root_meaning)
                        else:
                            result = float(d_mean_actual_yield) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) - float(yield_increase_sum)
    elif float(c) > float(b) > float(a):
        if float(a) < float(g):
            condition_4 = float(g) - float(h)
            if float(condition_4) >= float(0.0) and float(condition_4) <= float(5.0):
                result = float(d_mean_actual_yield) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum)
        else:
            result = float(d_mean_actual_yield) - float(yield_increase_sum) + float(root_meaning)
    elif float(a) < float(b) > float(c):
        result = float(d_mean_actual_yield) + float(yield_increase_sum)
    else:
        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
    return result
            
# Barley calculation logic (Russia, Krasnodar Territory), it is necessary to compare yield time series for a specific region
# Логика расчета ячменя (Россия, Краснодарский край), необходимо сравнить временные ряды урожайности для конкретного региона

def barley(a, b, c, d, e, f, g, h):
    if float(a) > float(b):
            if float(b) < float(c):
                if float(c) > float(d):
                    if float(d) < float(e):
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                    else:
                        condition = float(h) - float(g)
                        if float(condition) < float(5.0):
                            n_condition = float(a) - float(g)
                            if float(n_condition) < float(10.0):
                                result = float(d_mean_actual_yield) + float(root_meaning)
                            else:                    
                                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        else:
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                else:    
                    result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
            elif float(b) > float(c):
                if float(c) > float(d):
                    condition_2 = float(g) - float(h)
                    if float(condition_2) <= float(0.0):
                        result = float(d_mean_actual_yield) + float(root_meaning)
                    else:
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)                        
                else:
                    condition_3 = float(d) - float(c)
                    if float(condition_3) >= float(10.0) and float(condition_3) <= float(10.4):
                        result = float(d_mean_actual_yield) - float(yield_increase_sum)
                    else:
                        condition_4 = float(e) - float(f)
                        if float(condition_4) >= float(2.5) and float(condition_4) <= float(8.0):
                            condition_4_2 = float(g) - float(h)
                            if float(condition_4_2) <= float(2.4):
                                result = float(d_mean_actual_yield) - float(yield_increase_sum)
                            else:
                                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        elif float(condition_4) >= float(0.0) and float(condition_4) <= float(2.4):
                            result = float(d_mean_actual_yield) - float(root_meaning)
                        else:                   
                            result = float(d_mean_actual_yield) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) - float(yield_increase_sum)
    elif float(c) > float(b) > float(a):
        if float(a) < float(g):
            condition_5 = float(g) - float(h)
            if float(condition_5) >= float(0.0) and float(condition_5) <= float(5.0):
                result = float(d_mean_actual_yield) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum)
        else:
            result = float(d_mean_actual_yield) - float(yield_increase_sum) + float(root_meaning)
    elif float(a) < float(b) > float(c):
        condition_6 = float(g) - float(h)
        if float(condition_6) >= float(10.0):
            result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
        else:
            result = float(d_mean_actual_yield) + float(yield_increase_sum)
    else:
        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
    return result

# Maize calculation logic (Russia, Krasnodar Territory), it is necessary to compare yield time series for a specific region
# Логика расчета кукурузы (Россия, Краснодарский край), необходимо сравнить временные ряды урожайности для конкретного региона

def maize(a, b, c, d, e, f, g, h):
    if float(a) > float(b):
        if float(b) < float(c):
            if float(c) > float(d):
                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
            else:
                if float(e) > float(f):
                    result = float(d_mean_actual_yield) + float(root_meaning)
                else:
                    result = float(d_mean_actual_yield)
        elif float(b) > float(c):
            if float(c) < float(d):
                result = float(d_mean_actual_yield) + float(yield_increase_sum)   
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
        else:
            result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
    elif float(a) < float(b):
        if float(b) > float(c):
            if float(c) > float(d):
                result = float(d_mean_actual_yield) - float(yield_increase_sum)
            elif float(c) == float(d):
                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) + float(root_meaning)
        elif float(b) < float(c):
            if float(c) < float(d): 
                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum)
    else:
        result = float(d_mean_actual_yield) + float(yield_increase_sum)*2 + float(root_meaning)*2
    return result

# РУС
print('\n')
print('Данное ПО рассчитывает краткосрочный прогноз урожайности зерновых культур.')
print('Авторы оригинальной модели краткосрочного прогнозирования урожайности А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников.')
print('Автор данного ПО В. В. Шаляпин.')
print('Принцип методики краткосрочного прогнозирования заключается в сумме фактической урожайности в среднем за три года, взятой последовательно за четыре года от года прогноза, прироста урожайности от внедрения инноваций за 4 года и стохастической(случайной) составляющей, среднеквадратичного отклонения.')
print('ВНИМАНИЕ! Данный алгоритм разработан конкретно для России, Краснодарского края. Для другого региона следует смотреть временные ряды')
print('урожайности зерновых культур для выбранного региона и изменять логику в коде.')
print('Литература:')
print('Прогнозирование урожайности сельскохозяйственных культур: учебное пособие / А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников - Краснодар: КубГАУ, 2017. - 95 с. ISBN 978-5-00097-382-0')
print(' Автор хотел бы выразить особую благодарность другу и коллеге Али Али Кадем Али за его поддержку в моем деле.')
print('*MIT License*')
print('*Copyright (c) 2022 Vladimir Shalyapin*')

# ENG
print('\n')
print('This software calculates a short-term forecast of crop yields.')
print('The authors of the original model of short-term yield forecasting A. I. Trubilin, G. F. Petrik, A. G. Prudnikov.')
print('The author of this software is V. V. Shalyapin.')
print('The principle of the short-term forecasting technique is the sum of the actual yields on average over three years, taken sequentially for four years from the year of the forecast, the increase in productivity from the introduction of innovations for 4 years and the stochastic (random) component, standard deviation.')
print('ATTENTION! This algorithm was developed specifically for Russia, the Krasnodar Territory.')
print('For another region, you should look at the time series of crop yields for the selected region and change the logic in the code.')
print('References:')
print('Forecasting crop yields: textbook / A. I. Trubilin, G. F. Petrik, A. G. Prudnikov - Krasnodar: KubSAU, 2017. - 95 p. ISBN 978-5-00097-382-0')
print(' The author would like to express special thanks to Ali Ali\'s friend and colleague Kadem Ali for his support in my cause.')
print('*MIT License*')
print('*Copyright (c) 2022 Vladimir Shalyapin \n*')

# Language selection
# Выбор языка
print('Выберите язык. Введите RUS, чтобы работать на русском языке.')
print('Choose a language. Enter ENG to work in English. \n')

language = input('Ввод сюда\Input here: ')

while True:

    if language == str('RUS') or language == str('rus'):

        year_0 = input('Введите прогнозируемый год: ')
        culture = input('Напишите 1 если сельскохозяйственная культура пшеница, 2 если ячмень, 3 если кукуруза: ')
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

        # h
        number_1 = input('Урожайность ' + str(year_1) + ' ц/га: ')
        # g
        number_2 = input('Урожайность ' + str(year_2) + ' ц/га: ')
        number_3 = input('Урожайность ' + str(year_3) + ' ц/га: ')
        # f
        number_4 = input('Урожайность ' + str(year_4) + ' ц/га: ')
        # e
        number_5 = input('Урожайность ' + str(year_5) + ' ц/га: ')
        # d
        number_6 = input('Урожайность ' + str(year_6) + ' ц/га: ')
        # c
        number_7 = input('Урожайность ' + str(year_7) + ' ц/га: ')
        # b
        number_8 = input('Урожайность ' + str(year_8) + ' ц/га: ')
        # a
        number_9 = input('Урожайность ' + str(year_9) + ' ц/га: ')

        deviation_sum_n2345 = deviation_sum(float(number_2), float(number_3), float(number_4), float(number_5))
        deviation_sum_n3456 = deviation_sum(float(number_3), float(number_4), float(number_5), float(number_6))
        deviation_sum_n4567 = deviation_sum(float(number_4), float(number_5), float(number_6), float(number_7))
        deviation_sum_n5678 = deviation_sum(float(number_5), float(number_6), float(number_7), float(number_8))
        deviation_sum_n6789 = deviation_sum(float(number_6), float(number_7), float(number_8), float(number_9))

        deviation_n3456_n2345 = yield_change(float(deviation_sum_n3456), float(deviation_sum_n2345))
        deviation_n4567_n3456 = yield_change(float(deviation_sum_n4567), float(deviation_sum_n3456))
        deviation_n5678_n4567 = yield_change(float(deviation_sum_n5678), float(deviation_sum_n4567))
        deviation_n6789_n5678 = yield_change(float(deviation_sum_n6789), float(deviation_sum_n5678))

        print('Изменение урожайности по сравнению с предыдущим периодом № 1: ' + str(deviation_n3456_n2345) + ' ц с га')
        print('Изменение урожайности по сравнению с предыдущим периодом № 2: ' + str(deviation_n4567_n3456) + ' ц с га')
        print('Изменение урожайности по сравнению с предыдущим периодом № 3: ' + str(deviation_n5678_n4567) + ' ц с га')
        print('Изменение урожайности по сравнению с предыдущим периодом № 4: ' + str(deviation_n6789_n5678) + ' ц с га')

        # Для сохранения в txt файл
        writing_to_file_n3456_n2345 = str('Изменение урожайности по сравнению с предыдущим периодом № 1: ') + str(deviation_n3456_n2345) + str(' ц с га')
        writing_to_file_n4567_n3456 = str('Изменение урожайности по сравнению с предыдущим периодом № 2: ') + str(deviation_n4567_n3456) + str(' ц с га')
        writing_to_file_n5678_n4567 = str('Изменение урожайности по сравнению с предыдущим периодом № 3: ') + str(deviation_n5678_n4567) + str(' ц с га')
        writing_to_file_n6789_n5678 = str('Изменение урожайности по сравнению с предыдущим периодом № 4: ') + str(deviation_n6789_n5678) + str(' ц с га')
            
        yield_increase_sum = yield_increase(float(deviation_n3456_n2345), float(deviation_n4567_n3456), float(deviation_n5678_n4567), float(deviation_n6789_n5678))
        d_mean_actual_yield = mean_actual_yield(float(number_1), float(number_2), float(number_6))

        print('Прирост урожайности культуры: ' + str(yield_increase_sum))
        print('Базисная велинина программируемой урожайности: ' + str(d_mean_actual_yield))

        # Для сохранения в txt файл
        writing_to_file_r_deviation_sum = str('Прирост урожайности культуры: ') + str(yield_increase_sum)
        writing_to_file_r_actual_yield = str('Базисная велинина программируемой урожайности: ') + str(d_mean_actual_yield)

        t1_calculate_the_random_component = calculate_the_random_component(number_1, d_mean_actual_yield)
        t2_calculate_the_random_component = calculate_the_random_component(number_2, d_mean_actual_yield)
        t3_calculate_the_random_component = calculate_the_random_component(number_6, d_mean_actual_yield)
        s_123_calculate_the_random_component = float(t1_calculate_the_random_component) + float(t2_calculate_the_random_component) + float(t3_calculate_the_random_component)
        f_s_123_calculate_the_random_component = float(s_123_calculate_the_random_component) / 2
        sq_f_s_123_calculate_the_random_component = math.sqrt(float(f_s_123_calculate_the_random_component))
        r_sq_f_s_123_calculate_the_random_component = round(sq_f_s_123_calculate_the_random_component, 1)
                     
        t1_divisor = divisor(number_1, d_mean_actual_yield)
        t2_divisor = divisor(number_2, d_mean_actual_yield)
        t3_divisor = divisor(number_6, d_mean_actual_yield)

        if float(t1_divisor) == float(2.0) and float(t2_divisor) == float(2.0) and float(t3_divisor) == float(2.0) or float(t1_divisor) == float(2.0) or float(t2_divisor) == float(2.0) or float(t3_divisor) == float(2.0):
            ts_divisor = float(2.0)
        elif float(t1_divisor) == float(4.0) and float(t2_divisor) == float(4.0) and float(t3_divisor) == float(4.0) or float(t1_divisor) == float(4.0) or float(t2_divisor) == float(4.0) or float(t3_divisor) == float(4.0):
            ts_divisor = float(4.0)
        elif float(t1_divisor) == float(1.0) and float(t2_divisor) == float(1.0) and float(t3_divisor) == float(1.0) or float(t1_divisor) == float(1.0) or float(t2_divisor) == float(1.0) or float(t3_divisor) == float(1.0):
            ts_divisor = float(1.0)
            
        root_meaning = float(r_sq_f_s_123_calculate_the_random_component) / float(ts_divisor)

        if str(culture) == str(1):
            t_result = wheat(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        elif str(culture) == str(2):
            t_result = barley(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        elif str(culture) == str(3):
            t_result = maize(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        else:
            culture = input('Напишите 1 если сельскохозяйственная культура пшеница, 2 если ячмень, 3 если кукуруза: ')

        r_result = round(t_result, 1)
        print(str('Прогнозируемая урожайность: ') + str(r_result))
        writing_r_result = str('Прогнозируемая урожайность: ') + str(r_result)

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
            record_7 = str(writing_r_result) + str('\n')
            file_w.write(record_7)
            file_w.closed
            file_w = open(str(name_file) + '.txt', 'a')
            record_8 = str('********************************* ') + str(year_0) + str(' **********************************') + str('\n')
            file_w.write(record_8)
            file_w.closed
            file_w = open(str(name_file) + '.txt', 'a')
            record_9 = str('\n')
            file_w.write(record_9)
            file_w.closed
            
    elif language == str('ENG') or language == str('eng'):

        year_0 = input('Enter forecast year: ')
        culture = input('Write 1 if the crop is wheat, 2 if barley, 3 if corn: ')
        year_1 = int(year_0) - int(12)
        year_2 = int(year_0) - int(8)
        year_3 = int(year_0) - int(7)
        year_4 = int(year_0) - int(6)
        year_5 = int(year_0) - int(5)
        year_6 = int(year_0) - int(4)
        year_7 = int(year_0) - int(3)
        year_8 = int(year_0) - int(2)
        year_9 = int(year_0) - int(1)
        print('The calculation will require yield data for the following years; ' + str(year_1) + ', ' + str(year_2) + ', ' + str(year_3) + ', ' + str(year_4) + ', ' + str(year_5) + ', ' + str(year_6) + ', ' + str(year_7) + ', ' + str(year_8) + ', ' + str(year_9))

        # h
        number_1 = input('Yield ' + str(year_1) + ' c/ha: ')
        # g
        number_2 = input('Yield ' + str(year_2) + ' c/ha: ')
        number_3 = input('Yield ' + str(year_3) + ' c/ha: ')
        # f
        number_4 = input('Yield ' + str(year_4) + ' c/ha: ')
        # e
        number_5 = input('Yield ' + str(year_5) + ' c/ha: ')
        # d
        number_6 = input('Yield ' + str(year_6) + ' c/ha: ')
        # c
        number_7 = input('Yield ' + str(year_7) + ' c/ha: ')
        # b
        number_8 = input('Yield ' + str(year_8) + ' c/ha: ')
        # a
        number_9 = input('Yield ' + str(year_9) + ' c/ha: ')

        deviation_sum_n2345 = deviation_sum(float(number_2), float(number_3), float(number_4), float(number_5))
        deviation_sum_n3456 = deviation_sum(float(number_3), float(number_4), float(number_5), float(number_6))
        deviation_sum_n4567 = deviation_sum(float(number_4), float(number_5), float(number_6), float(number_7))
        deviation_sum_n5678 = deviation_sum(float(number_5), float(number_6), float(number_7), float(number_8))
        deviation_sum_n6789 = deviation_sum(float(number_6), float(number_7), float(number_8), float(number_9))

        deviation_n3456_n2345 = yield_change(float(deviation_sum_n3456), float(deviation_sum_n2345))
        deviation_n4567_n3456 = yield_change(float(deviation_sum_n4567), float(deviation_sum_n3456))
        deviation_n5678_n4567 = yield_change(float(deviation_sum_n5678), float(deviation_sum_n4567))
        deviation_n6789_n5678 = yield_change(float(deviation_sum_n6789), float(deviation_sum_n5678))

        print('Change in yield compared to the previous period № 1: ' + str(deviation_n3456_n2345) + ' c/ha')
        print('Change in yield compared to the previous period № 2: ' + str(deviation_n4567_n3456) + ' c/ha')
        print('Change in yield compared to the previous period № 3: ' + str(deviation_n5678_n4567) + ' c/ha')
        print('Change in yield compared to the previous period № 4: ' + str(deviation_n6789_n5678) + ' c/ha')

        # To save to txt file
        writing_to_file_n3456_n2345 = str('Change in yield compared to the previous period № 1: ') + str(deviation_n3456_n2345) + str(' c/ha')
        writing_to_file_n4567_n3456 = str('Change in yield compared to the previous period № 2: ') + str(deviation_n4567_n3456) + str(' c/ha')
        writing_to_file_n5678_n4567 = str('Change in yield compared to the previous period № 3: ') + str(deviation_n5678_n4567) + str(' c/ha')
        writing_to_file_n6789_n5678 = str('Change in yield compared to the previous period № 4: ') + str(deviation_n6789_n5678) + str(' c/ha')

        yield_increase_sum = yield_increase(float(deviation_n3456_n2345), float(deviation_n4567_n3456), float(deviation_n5678_n4567), float(deviation_n6789_n5678))
        d_mean_actual_yield = mean_actual_yield(float(number_1), float(number_2), float(number_6))

        print('Increase in crop yield: ' + str(yield_increase_sum))
        print('Basic value of programmable yield: ' + str(d_mean_actual_yield))

        # To save to txt file
        writing_to_file_r_deviation_sum = str('Increase in crop yield: ') + str(yield_increase_sum)
        writing_to_file_r_actual_yield = str('Basic value of programmable yield: ') + str(d_mean_actual_yield)

        t1_calculate_the_random_component = calculate_the_random_component(number_1, d_mean_actual_yield)
        t2_calculate_the_random_component = calculate_the_random_component(number_2, d_mean_actual_yield)
        t3_calculate_the_random_component = calculate_the_random_component(number_6, d_mean_actual_yield)
        s_123_calculate_the_random_component = float(t1_calculate_the_random_component) + float(t2_calculate_the_random_component) + float(t3_calculate_the_random_component)
        f_s_123_calculate_the_random_component = float(s_123_calculate_the_random_component) / 2
        sq_f_s_123_calculate_the_random_component = math.sqrt(float(f_s_123_calculate_the_random_component))
        r_sq_f_s_123_calculate_the_random_component = round(sq_f_s_123_calculate_the_random_component, 1)
                     
        t1_divisor = divisor(number_1, d_mean_actual_yield)
        t2_divisor = divisor(number_2, d_mean_actual_yield)
        t3_divisor = divisor(number_6, d_mean_actual_yield)

        if float(t1_divisor) == float(2.0) and float(t2_divisor) == float(2.0) and float(t3_divisor) == float(2.0) or float(t1_divisor) == float(2.0) or float(t2_divisor) == float(2.0) or float(t3_divisor) == float(2.0):
            ts_divisor = float(2.0)
        elif float(t1_divisor) == float(4.0) and float(t2_divisor) == float(4.0) and float(t3_divisor) == float(4.0) or float(t1_divisor) == float(4.0) or float(t2_divisor) == float(4.0) or float(t3_divisor) == float(4.0):
            ts_divisor = float(4.0)
        elif float(t1_divisor) == float(1.0) and float(t2_divisor) == float(1.0) and float(t3_divisor) == float(1.0) or float(t1_divisor) == float(1.0) or float(t2_divisor) == float(1.0) or float(t3_divisor) == float(1.0):
            ts_divisor = float(1.0)

        root_meaning = float(r_sq_f_s_123_calculate_the_random_component) / float(ts_divisor)

        if str(culture) == str(1):
            t_result = wheat(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        elif str(culture) == str(2):
            t_result = barley(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        elif str(culture) == str(3):
            t_result = maize(number_9, number_8, number_7, number_6, number_5, number_4, number_2, number_1)
        else:
            culture = input('Write 1 if the crop is wheat, 2 if barley, 3 if corn: ')

        r_result = round(t_result, 1)
        print(str('Projected yield: ') + str(r_result))

        # To save to txt file
        writing_r_result = str('Projected yield: ') + str(r_result)

        print('Save to txt file?')
        button_write = input('Enter + to save calculations and any other button to continue: ')

        if button_write == str('+'):
            name_file = input('Enter filename: ')
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
            record_7 = str(writing_r_result) + str('\n')
            file_w.write(record_7)
            file_w.closed
            file_w = open(str(name_file) + '.txt', 'a')
            record_8 = str('********************************* ') + str(year_0) + str(' **********************************') + str('\n')
            file_w.write(record_8)
            file_w.closed
            file_w = open(str(name_file) + '.txt', 'a')
            record_9 = str('\n')
            file_w.write(record_9)
            file_w.closed
        
    elif language != str('RUS') or language != str('ENG') or language != str('rus') or language != str('eng'):
        print('Я тебя не понимаю, повтори!\I don\'t understand you, repeat!')
        language = input('Ввод сюда\Input here: ')
