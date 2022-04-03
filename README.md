# crop_yield_forecasting_-on_the_example_of_cereals-
# ENG
# Hello dear friend. This product was created by Vladimir Shalyapin, a post-graduate student of the Department of Agrochemistry of Kuban State Agrarian University.
# This software calculates a short-term forecast of crop yields.
# The authors of the original yield forecasting model are A. I. Trubilin, G. F. Petrik, A. G. Prudnikov.
# References: Forecasting crop yields: textbook / A. I. Trubilin, G. F. Petrik, A. G. Prudnikov - Krasnodar: KubSAU, 2017. - 95 p. ISBN 978-5-00097-382-0
# The principle of the methodology is the sum of the actual yield on average for three years, taken in sequence four years from the forecast year, the increase in yield from the introduction of innovations for 4 years and the stochastic (random) component, the standard deviation.
# ATTENTION! This algorithm was developed specifically for Russia, the Krasnodar Territory. For another region, you should look at the time series of crop yields for the selected region and change the logic in the code.
# The code is written in Python 3.9
# The author would like to express special thanks to Ali Ali\'s friend and colleague Kadem Ali for his support in my cause.

# RUS
# Здравствуй, дорогой друг. Этот продукт создан Владимиром Шаляпиным, аспирантом кафедры агрохимии КубГАУ.
# Данное ПО рассчитывает краткосрочный прогноз урожайности зерновых культур.
# Авторами оригинальной модели прогнозирования урожайности являются А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников.
# Использованная литература: Прогнозирование урожайности сельскохозяйственных культур: учебное пособие / А. И. Трубилин, Г. Ф. Петрик, А. Г. Прудников - Краснодар: КубГАУ, 2017. - 95 с. ISBN 978-5-00097-382-0
# Принцип методики заключается в сумме фактической урожайности в среднем за три года, взятой последовательно за четыре года от года прогноза, прироста урожайности от внедрения инноваций за 4 года и стохастической (случайной) составляющей, среднеквадратичного отклонения.
# ВНИМАНИЕ! Данный алгоритм разработан конкретно для России, Краснодарского края. Для другого региона следует смотреть временные ряды урожайности зерновых культур для выбранного региона и изменять логику в коде.
# Код написан на Python 3.9
# Автор хотел бы выразить особую благодарность другу и коллеге Али Али Кадем Али за его поддержку в моем деле.

# MIT License
# Copyright (c) 2022 Vladimir Shalyapin
