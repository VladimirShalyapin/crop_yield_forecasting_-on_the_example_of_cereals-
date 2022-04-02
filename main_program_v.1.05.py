# v. 1.05
# Python 3.9.7
# Второй метод еще разрабатывается.
# The second method is still being developed.

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


# Calculation of yield increase
# Расчет прироста урожайности
def yield_increase(a, b, c, d):
    # abs нужно чтобы было только абсолютные (положительные) числа
    # abs needs to be only absolute (positive) numbers
    yield_increase_s = abs(a) + abs(b) + abs(c) + abs(d)
    r_yield_increase_s = round(yield_increase_s, 1)
    return r_yield_increase_s

# Calculation of the basic program of productivity
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

# РУС
print('\n')
print('Данное ПО рассчитывает краткосрочный и долгосрочный прогноз урожайности зерновых культур.')
print('Авторы оригинальной модели краткосрочного прогнозирования урожайности А. И. Трубилин,')
print('Г. Ф. Петрик, А. Г. Прудников.')
print('Автор данного ПО и модели долгосрочного прогноза урожайности зерновых культур В. В. Шаляпин.')
print('I. Принцип методики краткосрочного прогнозирования заключается в сумме фактической урожайности в среднем за три года,')
print('   взятой последовательно за четыре года от года прогноза, прироста урожайности от внедрения инноваций за 4 года и стохастической')
print('   (случайной) составляющей, среднеквадратичного отклонения.')
print('II. Методика долгосрочного прогнозирования подразумевает сумму средних значений урожайности зерновых культур, годы которых деляться нацело на 10,')
print('   взятые последовательно за четыредесятилетия от года прогноза, прироста урожайности от внедрения инноваций за 40 лет и стохастической')
print('   (случайной) составляющей, среднеквадратичного отклонения.')
print('Литература:')
print('1. Прогнозирование урожайности сельскохозяйственных культур: учебное пособие / А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников - Краснодар: КубГАУ, 2017. - 95 с. ISBN 978-5-00097-382-0')
print(' Автор хотел бы выразить особую благодарность другу и коллеге Али Али Кадем Али за его поддержку в моем деле.')
print('*MIT License*')
print('*Copyright (c) 2022 Vladimir Shalyapin*')

# ENG
print('\n')
print('This software calculates short-term and long-term forecast of crop yields.')
print('The authors of the original model of short-term yield forecasting A. I. Trubilin,')
print('G. F. Petrik, A. G. Prudnikov.')
print('The author of this software and the model of long-term forecast of crop yields is V. V. Shalyapin.')
print('I. The principle of the short-term forecasting technique is the sum of the actual yields on average over three years,')
print('   taken sequentially for four years from the year of the forecast, the increase in productivity from the introduction of innovations for 4 years and the stochastic')
print('   (random) component, standard deviation.')
print('II. A method of predictive forecasting of a decrease in the growth of crop yields, which years are divided by target designation by 10,')
print('   taken sequentially over four decades from the year of the forecast, the increase in productivity from the introduction of innovations over 40 years and the')
print('   stochastic (random) component, standard deviation.')
print('References:')
print('1. Forecasting crop yields: textbook / A. I. Trubilin, G. F. Petrik, A. G. Prudnikov - Krasnodar: KubSAU, 2017. - 95 p. ISBN 978-5-00097-382-0')
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

        # Выбор метода
        print('Выбери метод: ')
        print('              нажми 1 чтобы спрогнозировать урожайность по методике краткосрочного прогноза')
        print('              нажми 2 чтобы спрогнозировать урожайность по методике долгосрочного прогноза')
        metod_selection = input(str())

        # Метод 1
        if metod_selection == str(1):
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
            writing_to_file_n3456_n2345 = str('Изменение урожайности по сравнению с предыдущим периодом № 2: ') + str(deviation_n4567_n3456) + str(' ц с га')
            writing_to_file_n3456_n2345 = str('Изменение урожайности по сравнению с предыдущим периодом № 3: ') + str(deviation_n5678_n4567) + str(' ц с га')
            writing_to_file_n3456_n2345 = str('Изменение урожайности по сравнению с предыдущим периодом № 4: ') + str(deviation_n6789_n5678) + str(' ц с га')
            
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

            if float(number_9) > float(number_8):
                if float(number_8) < float(number_7):
                    if float(number_7) > float(number_6):
                        if float(number_6) < float(number_5):
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        else:
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                    else:    
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                elif float(number_8) > float(number_7):
                    if float(number_7) > float(number_6):
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)                        
                    else:
                        condition = float(number_6) - float(number_7)
                        if float(condition) >= float(10.0) and float(condition) <= float(10.4):
                            result = float(d_mean_actual_yield) - float(yield_increase_sum)
                        else:
                            condition_2 = float(number_5) - float(number_4)
                            if float(condition_2) <= float(8.0):
                                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                            else:
                                result = float(d_mean_actual_yield) + float(root_meaning)
                else:
                    result = float(d_mean_actual_yield) - float(yield_increase_sum)
            elif float(number_9) < float(number_8) < float(number_7):
                if float(number_9) < float(number_2):
                    result = float(d_mean_actual_yield) + float(yield_increase_sum)
                else:
                    result = float(d_mean_actual_yield) - float(yield_increase_sum) + float(root_meaning)
            elif float(number_9) < float(number_8) > float(number_7):
                result = float(d_mean_actual_yield) + float(yield_increase_sum)
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)

            r_result = round(result, 1)
            print(str('Прогнозируемая урожайность: ') + str(r_result))
            writing_r_result = str('Прогнозируемая урожайность: ') + str(r_result)
            
        # Метод 2
        elif metod_selection == str(2):
            print('Метод еще в разработке!')

        elif metod_selection != str(1) or metod_selection == str(2):
            print('Повтори цифру')
            metod_selection = input(str())

    elif language == str('ENG') or language == str('eng'):
        # Method selection
        print('Choose method: ')
        print('              press 1 to predict the yield using the short-term forecast method')
        print('              press 2 to predict the yield using the long-term forecast method')
        metod_selection = input(str())

        # Method 1
        if metod_selection == str(1):
            year_0 = input('Enter forecast year: ')
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

            number_1 = input('Yield ' + str(year_1) + ' c/ha: ')
            number_2 = input('Yield ' + str(year_2) + ' c/ha: ')
            number_3 = input('Yield ' + str(year_3) + ' c/ha: ')
            number_4 = input('Yield ' + str(year_4) + ' c/ha: ')
            number_5 = input('Yield ' + str(year_5) + ' c/ha: ')
            number_6 = input('Yield ' + str(year_6) + ' c/ha: ')
            number_7 = input('Yield ' + str(year_7) + ' c/ha: ')
            number_8 = input('Yield ' + str(year_8) + ' c/ha: ')
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
            writing_to_file_n3456_n2345 = str('Change in yield compared to the previous period № 2: ') + str(deviation_n4567_n3456) + str(' c/ha')
            writing_to_file_n3456_n2345 = str('Change in yield compared to the previous period № 3: ') + str(deviation_n5678_n4567) + str(' c/ha')
            writing_to_file_n3456_n2345 = str('Change in yield compared to the previous period № 4: ') + str(deviation_n6789_n5678) + str(' c/ha')

            yield_increase_sum = yield_increase(float(deviation_n3456_n2345), float(deviation_n4567_n3456), float(deviation_n5678_n4567), float(deviation_n6789_n5678))
            d_mean_actual_yield = mean_actual_yield(float(number_1), float(number_2), float(number_6))

            print('Increase in crop yield: ' + str(yield_increase_sum))
            print('Basic value of programmable yield: ' + str(d_mean_actual_yield))

            # Для сохранения в txt файл
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

            if float(number_9) > float(number_8):
                if float(number_8) < float(number_7):
                    if float(number_7) > float(number_6):
                        if float(number_6) < float(number_5):
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                        else:
                            result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                    else:    
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) - float(root_meaning)
                elif float(number_8) > float(number_7):
                    if float(number_7) > float(number_6):
                        result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)                        
                    else:
                        condition = float(number_6) - float(number_7)
                        if float(condition) >= float(10.0) and float(condition) <= float(10.4):
                            result = float(d_mean_actual_yield) - float(yield_increase_sum)
                        else:
                            condition_2 = float(number_5) - float(number_4)
                            if float(condition_2) <= float(8.0):
                                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)
                            else:
                                result = float(d_mean_actual_yield) + float(root_meaning)
                else:
                    result = float(d_mean_actual_yield) - float(yield_increase_sum)
            elif float(number_9) < float(number_8) < float(number_7):
                if float(number_9) < float(number_2):
                    result = float(d_mean_actual_yield) + float(yield_increase_sum)
                else:
                    result = float(d_mean_actual_yield) - float(yield_increase_sum) + float(root_meaning)
            elif float(number_9) < float(number_8) > float(number_7):
                result = float(d_mean_actual_yield) + float(yield_increase_sum)
            else:
                result = float(d_mean_actual_yield) + float(yield_increase_sum) + float(root_meaning)

            r_result = round(result, 1)
            print(str('Projected yield: ') + str(r_result))
            writing_r_result = str('Projected yield: ') + str(r_result)


        # Method 2
        elif metod_selection == str(2):
            print('The method is still under development!')
        elif metod_selection != str(1) or metod_selection == str(2):
            print('The method is still under development!')
            metod_selection = input(str())

    elif language != str('RUS') or language != str('ENG') or language != str('rus') or language != str('eng'):
        print('Я тебя не понимаю, повтори!\I don\'t understand you, repeat!')
        language = input('Ввод сюда\Input here: ')
