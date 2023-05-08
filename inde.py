import webbrowser 
from random import *
from turtle import *
from time import *
def function_communication(function, your_amount_of_money):
    while function == 'общение':
        topic_for_conversation = input('О чём хочешь поговорить?(Название темы): ').lower()
        if topic_for_conversation == 'мировые новости':
            print('В мире зима. Россия проводит спец.операцию на территории Украины, много санкций и рубль падает.')
        elif topic_for_conversation == 'привет':
            print('Не посчитай за грубость. Пока')
        elif topic_for_conversation == "да":
            print('Ты ожидал услышать это? Нет, это грубо')
        elif topic_for_conversation == 'лиза':
            Liza_ = input('Всмысле ты про имя?: ').lower()
            if Liza_ == 'да':
                print('Лиза - Очень красивое имя, прекрасные женщины с таким именем.')
            elif Liza_ == 'нет':
                print('Не понял о чём ты, но всё равно. Лиза - Очень красивое имя, прекрасные женщины с таким именем.')
            else:
                print('Ну если ты не про имя Лиза, то незнаю о чём ты')
        elif topic_for_conversation == 'на какой ты стадии разработки?':
            print('На ранней, пре-пре-альфа или версия 0.3.1, мой код не очень гармоничен и неудобный.')
        elif topic_for_conversation == 'надя' or topic_for_conversation == 'настя' or topic_for_conversation == 'ася' or topic_for_conversation == 'аня' or topic_for_conversation == 'анна':
            print('Отличное имя')
        elif topic_for_conversation == 'никита':
            print('Хорошое мужское имя(только не отдавайте никит на футбол)')
        elif topic_for_conversation == 'андрей':
            print('Андрей не в чём не виноват')
        elif topic_for_conversation == 'тимур':
            print('Интересный факт: это имя разработчика данного бота')
            name_gamedel = input('А тебя зовут Тимур что - ли?').lower()
            if name_gamedel == 'да':
                print('Ты получаешь плюс 20 монеток для азартных игр')
                your_amount_of_money += 20
            elif name_gamedel == 'нет':
                print('Жалко, очень жалко')
            else:
                print('Понятненько')
            want_to_see_youtube = input('Хочешь увидеть ютуб создателя?').lower()
            while want_to_see_youtube != 'да' and want_to_see_youtube != 'нет':
                want_to_see_youtube == input('Не понял тебя, да или нет?')
            if want_to_see_youtube == 'да':
                print('Лови')
                webbrowser.open('https://www.youtube.com/channel/UCwh2Towv5tlBB4vhc_RNsag')
            elif want_to_see_youtube == 'нет':
                print('Не хочешь, значит не хочешь')
        elif topic_for_conversation == 'обновления' or topic_for_conversation == 'будущие обновления':
            print('Ну до полной версии бота выйдет много обновлений. Планируется массивное обновление калькулятора, изменить всю его систему. Тоже самое про общение. Также, в этой же линейки обновлений 0.3 появится пэинт:)')
        elif topic_for_conversation == 'спойлер':
            print('Одна из идей будущих обнов: пэинт будет уже в 0.3.2, а будущие планы это добавить игры')
        elif topic_for_conversation == 'телефоны' or topic_for_conversation == 'телефон':
            model_phone = input('Интересная тема, давай выберем конкретную марку телефонов').lower()
            if model_phone == 'айфон' or model_phone == 'iphone':
                print('Интересная модель, но в основном не стоит своих денег говорят многие. Но многие знаменитости ходят с лучшими айфонами. В чём же секрет?')
            elif model_phone == 'ксиоми' or model_phone == 'xiaomi':
                print('Хороший бюджетник, наверное большой конкурент другим телефонам')
            elif model_phone == 'нокиа' or model_phone == 'nokia':
                print('Ты серьёзно? Почти никто не ходит с ними, их популярность пиковая прошла давно')
            elif model_phone == 'хуавей' or model_phone == 'huawei':
                print('Хороший телефон, но в магазине приложений мало что скачать, поэтому сейчас он не очень')
            elif model_phone == 'самсунг' or model_phone == 'samsung':
                print('Очень много разновидностей моделей и их линеек. Легендарная серия телефонов')
            elif model_phone == 'гугл фон' or model_phone == 'google phone':
                print('Не очень популярна в России, с такими почти не ходят')
            elif model_phone == 'блэкберри' or model_phone == 'блэкбери' or model_phone == 'blackberry':
                print('Среднячок, незнаю даже что сказать')
            elif model_phone == 'асус' or model_phone == 'asus':
                print('Незнаю что сказать, Асус хорошая модель но в России как телефон не популярен')
            elif model_phone == 'вега' or model_phone == 'vega':
                print('Вроде бы перевёрнутое название топово звучит, а так телефон не популярен в России')
            elif model_phone == 'леново' or model_phone == 'lenovo':
                print('Топчик вообще то, у них хорошие планшеты')
            elif model_phone == 'хонор' or model_phone == 'honor':
                print('Хороший телефон, многие в детстве его путали наверное с хуавеем и сейчас кто то считает его хуавеем')
            elif model_phone == 'асер' or model_phone == 'акер' or model_phone == 'acer' or model_phone == 'aser':
                print('Хорошие мониторы, а всмысле они выпускают телефоны?')
            elif model_phone == 'сони' or model_phone == 'sony':
                print('PlayStation 4 и PlayStation 5. А стоп, это телефоны?')
            elif model_phone == 'лджи' or model_phone == 'lg':
                print('Стоп, они не только бытовую технику и всякие моники выпускают, но и телефоны??')
            elif model_phone == 'моторола' or model_phone == 'motorola':
                print('Это вроде бы осталось в 90-х, в эре кнопочных')
            elif model_phone == 'виво' or model_phone == 'vivo':
                print('Почему название похоже на вега? Ладно вроде бы телефон, дак телефон')
            else:
                print('Незнаю такой, извини')
        elif topic_for_conversation == 'крутой бот':
            print('Спасибо')
        elif topic_for_conversation == 'ютуб':
            YouTube = input("Ты хочешь узнать про новости или перейти на ютуб?").lower()
            if YouTube == 'перейти на ютуб' or YouTube == 'посмотреть ютуб' or YouTube == 'смотреть' or YouTube == 'просмотр': 
                print('А что медлить, давай откроем и посмотрим')
                print('Загрузка...')
                webbrowser.open('https://www.youtube.com/')
            elif YouTube == 'посмотреть новости' or YouTube == 'новости' or YouTube == 'просмотр новостей':
                print('Давай осведомимся')
                webbrowser.open('https://ria.ru/organization_YouTube_LLC/')
        elif topic_for_conversation == 'твич':
            print('Там весело...')
            webbrowser.open('https://cyber.sports.ru/media/twitch/')
        elif topic_for_conversation == 'новости':
            News_24 = input('Ты хочешь посмотреть новости?').lower()
            if News_24 == 'да':
                webbrowser.open('https://ria.ru/organization_YouTube_LLC/')
            else:
                print('Если не да, тогда чего тут забыл?')
        elif topic_for_conversation == 'обновление' or topic_for_conversation == 'версия':
            print('На данный момент версия 0.3.1, основное дополнение: это азартные игры!!! Но также исправлены баги, дополнено как всегда общение и запущена новая линейка обновлений.')
        elif topic_for_conversation == 'игры':
            print('Интересненько, есть несколько крутых и популярных игр сейчас или которые скоро выйдут')
            print('🧟Dying Light 2 Stay Human🧟 - Игра про мир в котором эпидемия, похожая на вирус зомби')
            print('Ну и другие игры, по типу: Horizon Forbidden West, Bendy and the Dark Revival, Hello Neighbor 2')
            print('А также: Atomic Heart, God of War Ragnarok и S.T.A.L.K.E.R. 2: Heart of Chernobyl')
            games_details = input('Выбери что ты хочешь увидеть(Описание игр или выйти(просто напиши что нибудь не по теме))').lower()
            if games_details == 'описание игр' or games_details == 'описание':
                game_description == input('Введи название игры из вышеперечисленных(напиши главное правильно)').lower()
                if game_description == 'dying light 2 stay human':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Dying_Light_2:_Stay_Human')
                elif game_description == 'horizon forbidden west':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Horizon_Forbidden_West')
                elif game_description == 'bendy and the dark revival':
                    print('Описание:')
                    webbrowser.open('https://bendy-and-the-ink-machine.fandom.com/ru/wiki/Bendy_and_the_Dark_Revival')
                elif game_description == 'hello neighbor 2':
                    print('Описание:')
                    webbrowser.open('https://hello-neighbor-game.fandom.com/ru/wiki/Hello_Neighbor_2')
                elif game_description == 'atomic heart':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/Atomic_Heart')
                elif game_description == 'god of war ragnarok':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/God_of_War:_Ragnar%C3%B6k')
                elif game_description == 'stalker 2' or game_description == 's.t.a.l.k.e.r. 2: heart of chernobyl' or game_description == 'stalker 2: heart of chernobyl' or game_description == "Stalker 2" or game_description == 'STALKER 2':
                    print('Описание:')
                    webbrowser.open('https://ru.wikipedia.org/wiki/S.T.A.L.K.E.R._2:_Heart_of_Chernobyl')
            else:
                print('Ты решил(а) выйти из темы игр, удачи')
        elif topic_for_conversation == 'азартные игры' or topic_for_conversation == 'казино':
            print('Ты в общение, кстати если ты хочешь подзаработать монет в азартных играх, то тут есть варианты развития чатов где дадут бонус-монеты')
        elif topic_for_conversation == 'рандомайзер':
            print('Не забывай, ты в общение')
        elif topic_for_conversation == 'roleplay':
            print('Рп проекты, где отыгрывают так называемый RolePlay, есть на гта 5, гта сан андреас и в других играх.')
        elif topic_for_conversation == 'калькулятор': #дописать потом про фишки
            print('Псссс, ты выбрал(а) общение, не забудь:)')#дописать потом как выйти из циклов общения
        elif topic_for_conversation == 'скучный бот':
            print('Я могу и обидеться вообще то')
        elif topic_for_conversation == 'футбол':
            print('Футбольные новости:')
            webbrowser.open('https://www.championat.com/news/football/1.html')
        elif topic_for_conversation == 'python':
            print('Есть такая змея, питон. Ну а ёще язык программирования на котором написан данный бот.')
        elif topic_for_conversation == '23':
            print('23 числа у кого то день рождение, у кого то праздники, события или исторические даты. Но 23 - это число которое являеться одним из первых чит кодов, поздравляем, ты получаешь +10 монет')
            your_amount_of_money += 10
        elif topic_for_conversation == '14':
            print('Не знаю что это за тема такая, но в сентябре такого числа день рождение у создателя,по этому это являеться 3 чит-кодом,ты получаешь +15 монет')
            your_amount_of_money += 15
        elif topic_for_conversation == '22':
            print('22 февраля 2022 года началось создание этого проекта и он вышел в свет')
            your_amount_of_money += 20
        elif topic_for_conversation == 'сколько у меня денег' or topic_for_conversation == 'мой счёт' or topic_for_conversation == 'счёт':
            print('Твоё количество денег:', your_amount_of_money)
        elif topic_for_conversation == 'андрей не виноват' or topic_for_conversation == 'андрей не в чём не виноват' or topic_for_conversation == 'андрей ни в чём не виноват':
            print('Согласен с твоим мнением')
        elif topic_for_conversation == 'день рождение':
            print('День, когда исполняется определённое количество лет со дня рождения кого то.')#дописать потом ответы
        elif topic_for_conversation == 'как тебя зовут' or topic_for_conversation == 'твое имя' or topic_for_conversation == 'твоё имя' or topic_for_conversation == 'имя':
            print('Пока что конкретного имени нету, но в будущуем оно будет')
        elif topic_for_conversation == 'как дела?' or topic_for_conversation == 'как дела':
            How_are_you = input('Нормально. А твоё?').lower()
            if How_are_you == 'отлично' or How_are_you == 'прекрасно' or How_are_you == 'замечательно':
                print('Это замечательно, фантастично и феерично')
            elif How_are_you == 'плохо' or How_are_you == 'ужасно' or How_are_you == 'отвратно':
                response_to_mood = input('Не печалься, чем я могу тебе помочь?').lower()
                if response_to_mood == 'ничем':
                    print('Ну давай тогда хотя бы пообщаемся')
                elif response_to_mood == 'можешь':
                    print('Тогда пошли общаться и развлекаться, хоть у меня и ранняя версия')
                else:
                    print('Пошли общаться и всё будет хорошо:)')
            else:
                print('Такого настроения в базе моих данных пока что нету или ты написал(а) неправильно')
        elif topic_for_conversation == 'феменизм':
            print('Это спорный вопрос, давай о другом')
        elif topic_for_conversation == 'кринж' or topic_for_conversation == 'треш' or topic_for_conversation == 'зашквар' or topic_for_conversation == 'рофл':
            print("Молодёжный сленг, воу. Хотя даже сленгом не назовёшь сильно")
        elif topic_for_conversation == 'алгоритмика':
            print('Это проект, на базе которого мы делаем эти проекты, ты сейчас сидишь на этом проекте благодаря этому проекту и обучаешься чему то благодаря этому проекту(скороговорка какая-то получилась)')
            back_to_algorithmic = input('Ты хочешь вернуться на главную страницу алгоритмики?').lower()
            if back_to_algorithmic == 'да':
                print('Удачи')
                webbrowser.open('https://learn.algoritmika.org/main')
            else:
                print('Ну остаёшься, так остаёшься')
        elif topic_for_conversation == 'россия':
            print('Наша великая страна, богатая земными ресурсами. Но постоянно какие то проблемы. В чём корень зла?')
        elif topic_for_conversation == 'покажи код':
            print('Извини, но нет')
        elif topic_for_conversation == 'крым':
            print('Политика, не хочу о таком')
        elif topic_for_conversation == 'чит-коды' or topic_for_conversation == 'чит-код':
            print('Чит-кодики ищещь значит, ну подскажу, чат бот появился 22 февраля, немного изменить и получишь чит-код')
        elif topic_for_conversation == 'читы':
            print('Вот это осуждаю уже')
        elif topic_for_conversation == 'школа':
            print('То самое место, которое не любят множество детей? В котором тебе придёться быть или 9, или 11 классов. Впр, ОГЭ и ЕГЭ. Как весело не правда - ли?')
        else:
            random_reply_chat = randint(1,5)
            if random_reply_chat == 1:
                print('Достаточно интересная тема, но давай в следующий раз')
            elif random_reply_chat == 2:
                print('Извини, такой темы в базе данных нету, у меня их слишком мало пока что')
            elif random_reply_chat == 3:
                print('Извини, не в моём репертуаре говорить об этом')
            elif random_reply_chat == 4:
                print('Это как?')
            elif random_reply_chat == 5:
                print('Давай пропустим')
        desire_for_communication = input('Ты хочешь ёще продолжить общение?').lower()
        while desire_for_communication != 'да' and desire_for_communication != 'нет':
            desire_for_communication = input('Не понял тебя, напиши да или нет. Ты хочешь ёще продолжить общение?').lower()
        if desire_for_communication == 'да':
            function = 'общение'
        elif desire_for_communication == 'нет':
            function = input('Какую функцию тогда ты выберешь? Калькулятор, рандомайзер или азартные игры')#потом дописать
    return function

def greetings_bot():
    greeting = randint(1,2)
    if greeting == 1:
        greeting_proposal = input('Поздоровайся с чат ботом:)')
    elif greeting == 2:
        greeting_proposal = input('Приятно тебя видеть, поздоровайся с чат ботом:)')
    write_a_command = input('Привет, я чат бот и я нахожусь в ранней стадии разработки. Напиши мне "твои возможности" и я предоставлю то что могу сделать').lower()
    while write_a_command != 'твои возможности':
        write_a_command = input('Я тебя не понял, напиши пожалуйста правильно.').lower()
    print('Отлично, мои возможности на момент ранней разработки, так называемой пре-пре-альфы: общение, калькулятор, рандомайзер и казино')#дописать в конце разработки фишки
    function = input('По функции "общение" начнётся общение со мной, на момент пре-пре-альфы есть небольшое количество фраз и общение в будущем будет дорабатываться.\nПо функции "калькулятор" активируется система калькулятора.\nРандомайзер будет рандомно определять числа заданной категории и диапазона.\nВ казино находиться в ранней версии и там есть ставки на гонки и рулетка.').lower() #дописывать фишки потом
    return function

def calculation_type_True_or_False(calculation_type, action_with_a_number):
    if calculation_type == 'да' or calculation_type == 'всё ещё':
        calculation_type = action_with_a_number
    return calculation_type

def calculation_function(function):
    while function == 'калькулятор':
        print('Это калькулятор')
        calculation_type = input('Введи тип действий с числом(классические 4, определение корня, возведение в степень, нахождение факториала)').lower()
        while calculation_type == 'сложение':
            term_number = int(input('Введи количество сложений:'))
            term_all = 0
            for i in range(term_number):
                term = int(input('Введи слагаемое(первое слагаемое 0):'))
                term_all += term
            print('Сумма:', term_all)
            calculation_type = input('Все ещё сложение?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'сложение')
        while calculation_type == 'вычитание':
            minuend = int(input('Введи уменьшаемое:'))
            subtrahend = int(input('Введи вычитаемое:'))
            difference = minuend - subtrahend
            print('Разность:', difference)
            calculation_type = input('Все ещё вычитание?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'вычитание')
        while calculation_type == 'умножение':
            multiplied_one = int(input('Введи первый множитель:'))
            multiplied_two = int(input('Введи второй множитель:'))
            product_multiplied = multiplied_one * multiplied_two
            print('Произведение данных чисел:', product_multiplied)
            calculation_type = input('Все ещё умножение?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'умножение')
        while calculation_type == 'деление':
            what_is_the_separation = input('Введи вариант деления(деление с точностью, деление и получение целого числа, получение остатка от деления)')
            dividend = int(input('Введи делимое:'))
            divider = int(input('Введи делитель:'))
            if what_is_the_separation == 'первое' or what_is_the_separation == '1' or what_is_the_separation == 'деление с точностью':
                private_division = dividend/divider
                print('Частное:', private_division)
            elif what_is_the_separation == 'второе' or what_is_the_separation == '2' or what_is_the_separation == 'деление и получение целого числа' or what_is_the_separation == 'деление, получение целого числа':
                private_division = dividend//divider
                print('Целое частное:', private_division)
            elif what_is_the_separation == 'третье' or what_is_the_separation == '3' or what_is_the_separation == 'получение остатка' or what_is_the_separation == 'получение остатка от деления':
                private_division = dividend%divider
                print('Остаток:', private_division)
            else:
                print('Не очень понял тебя')
            calculation_type = input('Все ещё деление?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'деление')
        while calculation_type == 'определение корня' or calculation_type == 'корень' or calculation_type == "корень числа":
            a_number_with_a_root = int(input('Введите число из которого хотите вычислить корень:'))
            print('Корень числа:', a_number_with_a_root, 'равняется -', a_number_with_a_root**0.5 )
            calculation_type = input('Все ещё работа с корнем?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'корень')
        while calculation_type == 'возведение в степень' or calculation_type == 'степень':
            number_for_exponentiation = int(input('Введи число которое возведёшь в степень:'))
            degree_number = int(input('Введи число степени в которую возведёшь предыдущее число:'))
            print('Число', number_for_exponentiation, 'в степени', degree_number, 'равняется', number_for_exponentiation**degree_number)
            calculation_type = input('Все ещё работа с степенью?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'степень')
        while calculation_type == 'факториал' or calculation_type == 'нахождение факториала' or calculation_type == 'факториал числа' or calculation_type == 'нахождение фаткориала числа':
            number_factory = int(input('Введите число, факториал которого найдёт программа(0 или более)'))
            the_resulting_number = 0
            if number_factory > 0 and number_factory <= 300:
                initial_number_in_factory_location = 1
                while initial_number_in_factory_location <= number_factory:
                    if initial_number_in_factory_location > 1:
                        the_resulting_number*=initial_number_in_factory_location
                    else:
                        the_resulting_number += initial_number_in_factory_location
                    initial_number_in_factory_location += 1
                print('Факториал числа', number_factory, 'является', the_resulting_number)
            elif number_factory == 0:
                the_resulting_number = 1
                print('Факториал числа', number_factory, 'является', the_resulting_number)
            elif number_factory < 0:
                print('К факту, факториал отрицательного числа найти нельзя')
            elif number_factory > 300:
                print('Извиняюсь, но такие большие числа застопят систему, поэтому считай что бесконечность')
            calculation_type = input('Все ещё работа с факториалами?(если нет, то напиши другой тип действий)')
            calculation_type = calculation_type_True_or_False(calculation_type, 'факториал')
        else:
            print('Незнаю такого типа действий. Либо он написан неправильно, либо его нету пока что в моей базе данных.')
        desire_for_communication = input('Ты хочешь ёще продолжить пользоваться калькулятором?').lower()
        while desire_for_communication != 'да' and desire_for_communication != 'нет':
            desire_for_communication = input('Не понял тебя, напиши да или нет. Ты хочешь ёще продолжить пользоваться калькулятором?').lower()
        if desire_for_communication == 'да':
            function = 'калькулятор'
        elif desire_for_communication == 'нет':
            function = input('Какую функцию тогда ты выберешь? Общение, рандомайзер или азартные игры')#потом дописать
    return function

def randomizer_function(function):
    while function == 'рандомайзер':
        print('Здравствуй, это рандомайзер, тут ты можешь получить рандомное отрицательное число, положительное, просто все целые числа или дробное число от 0 до 1')
        random_choice = input('Какие числа по типу будут: рандомные отрицательные числа, положительные, просто все целые числа или дробное число от 0 до 1').lower()
        if random_choice == 'рандомное дробное число' or random_choice == 'рандомные дробные числа' or random_choice == 'дробное число' or random_choice == 'дробные числа':
            print(random()) 
        elif random_choice != 'рандомное дробное число' and random_choice != 'рандомные дробные числа' and random_choice != 'дробное число' and random_choice != 'дробные числа':
            number_range_1 = int(input('Введи первое, меньшее число'))
            number_range_2 = int(input('Введи второе число, большее число'))
            if (random_choice == 'рандомное отрицательное число' or random_choice == 'рандомные отрицательные числа' or random_choice == 'отрицательное число' or random_choice == 'отрицательные числа' or random_choice == 'отрицательное' or random_choice == 'отрицательные') and ((number_range_1 < 0) and (number_range_2 < 0)) and (number_range_1 <= number_range_2):
                print(randint(number_range_1, number_range_2))
            elif (random_choice == 'рандомное положительное число' or random_choice == 'рандомные положительные числа' or random_choice == 'положительное число' or random_choice == 'положительные числа' or random_choice == 'положительное' or random_choice == 'положительные') and ((number_range_1 > 0) and (number_range_2 > 0)) and (number_range_1 <= number_range_2):
                print(randint(number_range_1, number_range_2))
            elif (random_choice == 'рандомное целое число' or random_choice == 'рандомные целые числа' or random_choice == 'целое число' or random_choice == 'целые числа' or random_choice == 'целое' or random_choice == 'целые' or random_choice == 'все целые числа') and (number_range_1 <= number_range_2):
                print(randint(number_range_1, number_range_2))
            else:
                print('Проверь все условия, ты значит что то сделал неправильно или хочешь выйти из функции')
        desire_for_communication = input('Ты хочешь ёще продолжить работать с рандомайзером?').lower()
        while desire_for_communication != 'да' and desire_for_communication != 'нет':
            desire_for_communication = input('Не понял тебя, напиши да или нет. Ты хочешь ёще продолжить работать с рандомайзером?').lower()
        if desire_for_communication == 'да':
            function = 'рандомайзер'
        elif desire_for_communication == 'нет':
            function = input('Какую функцию тогда ты выберешь?(Калькулятор, общение или азартные игры')
    return function

def lines_vertical():
    speed(-1)
    gorizontal = -160
    pensize(3)
    right(90)
    for i in range(12):
        color('red')
        penup()
        gorizontal += 10
        goto(gorizontal, 150)
        pendown()
        forward(250)
        color('blue')
        penup()
        gorizontal += 10
        goto(gorizontal, 150)
        pendown()
        forward(250)
        color('green')
        penup()
        gorizontal += 10
        goto(gorizontal, 150)
        pendown()
        forward(250)
    penup()
    hideturtle()
    exitonclick()

def startRace(a, b, c):
    a.penup()
    a.goto(-150, 0)
    b.penup()
    b.goto(-150, 50)
    c.penup()
    c.goto(-150, -50)
    a.x = 0
    b.x = 0
    c.x = 0

def creation_turtles_one(a, b, c, shape_one_turtle, shape_two_turtle, shape_three_turtle, color_one_turtle, color_two_turtle, color_three_turtle):
    a.shape(shape_one_turtle)
    b.shape(shape_two_turtle)
    c.shape(shape_three_turtle)
    a.color(color_one_turtle)
    b.color(color_three_turtle)
    c.color(color_three_turtle)

def racing_turtle_a(a):
    random_forward = randint(5, 10)
    a.forward(random_forward)
    a.x += random_forward

def racing_turtle_b(b):
    random_forward = randint(5, 10)
    b.forward(random_forward)
    b.x += random_forward

def racing_turtle_c(c):
    random_forward = randint(5, 10)
    c.forward(random_forward)
    c.x += random_forward

def who_is_the_winner(a, b, c):
    if a.x > b.x and a.x > c.x:
        number_of_the_winning_turtle = 1
    elif a.x > b.x and a.x < c.x:
        number_of_the_winning_turtle = 3
    elif a.x < b.x and a.x < c.x:
        if b.x > c.x:
            number_of_the_winning_turtle = 2
        else:
            number_of_the_winning_turtle = 3
    return number_of_the_winning_turtle

def all_casinos_function(function, your_amount_of_money):
    while function == 'азартные игры' or function == 'казино':
        print('Казино: Чат Бот')
        print('Твоё количество денег:', your_amount_of_money)
        Choice_of_gambling = input('Перед тобой выбор азартных игр: Ставки(на момент 0.3 есть только один вид, но он тоже прикольный)').lower()#дописать потом правильные названия
        while Choice_of_gambling == 'ставки' or Choice_of_gambling == 'ставка':
            print('Приветствую тебя в ставках. Твоё количество денег:', your_amount_of_money)
            type_of_rates = input('Какие ставки выберешь?(ставки на гонки или рулетка)').lower()
            bet_of_money_on_races = int(input('Твоя ставка:(кол-во денег)'))
            while bet_of_money_on_races > your_amount_of_money:
                print('Ты не можешь поставить столько, у тебя столько нету:(')
                bet_of_money_on_races = int(input('Твоя ставка:'))
            if type_of_rates == 'гонки' or type_of_rates == 'гонка' or type_of_rates == 'ставки на гонки' or type_of_rates == 'ставка на гонку':
                turtle_number = int(input('Твоя ставка:(номер гонщика, от 1-3)'))
                readiness_for_editing = input('Ты готов приступить к редактированию гонщиков?(пиши готов или нет)').lower()
                while readiness_for_editing != 'готов' and readiness_for_editing != 'да':
                    readiness_for_editing = input('Ты или неправильно написал или не готов, напиши в строку ниже как будешь готов').lower()
                if True:
                    shape_one_turtle = input('Форма(черепашка, треугольник и т.д) первого гонщика(на английском)').lower()
                    want_uniformity_shape = input('Вы хотите чтобы все гонщики были одной формы?(да/нет)').lower()
                    if want_uniformity_shape == 'да':
                        shape_two_turtle = shape_one_turtle
                        shape_three_turtle = shape_one_turtle
                    else:
                        shape_two_turtle = input('Форма(черепашка, треугольник и т.д) второго гонщика(на английском)').lower()
                        shape_three_turtle = input('Форма(черепашка, треугольник и т.д) третьего гонщика(на английском)').lower()
                if True:
                    color_one_turtle = input('Цвет(красный, синий и т.д(обязательно на английском)) первого гонщика').lower()
                    want_uniformity_color = input('Вы хотите чтобы все гонщики были одного цвета?').lower()
                    if want_uniformity_color == 'да':
                        color_two_turtle = color_one_turtle
                        color_three_turtle = color_one_turtle
                    else:
                        color_two_turtle = input('Цвет(красный, синий и т.д(обязательно на английском)) второго гонщика').lower()
                        color_three_turtle = input('Цвет(красный, синий и т.д(обязательно на английском)) третьего гонщика').lower()
                lines_vertical()
                a = Turtle()
                b = Turtle()
                c = Turtle()
                creation_turtles_one(a, b, c, shape_one_turtle, shape_two_turtle, shape_three_turtle, color_one_turtle, color_two_turtle, color_three_turtle)
                startRace(a, b, c)
                racing_turtle_a(a)
                racing_turtle_b(b)
                racing_turtle_c(c)
                while a.x <= 340 and b.x <= 340 and c.x <= 340:
                    racing_turtle_a(a)
                    racing_turtle_b(b)
                    racing_turtle_c(c)
                number_of_the_winning_turtle =  who_is_the_winner(a, b, c)
                print('Победитель черепашка -' + str(number_of_the_winning_turtle))
                if turtle_number == number_of_the_winning_turtle:
                    print('Поздравляем, твоя черепашка выиграла, ты получаешь x3 от ставки, ты выиграл:', bet_of_money_on_races * 3)
                    your_amount_of_money += bet_of_money_on_races
                else:
                    print('Не расстраивайся, бывают поражения. Ты проиграл:', bet_of_money_on_races)
                    your_amount_of_money -= bet_of_money_on_races
            elif type_of_rates == 'рулетка' or type_of_rates == 'рулетки':
                print('Приветствуем тебя в Рулетке')
                roulette_number_bet = input('Введи число на которое ты ставишь(от 1-37)')
                beaten_number_in_roulette = randint(1, 37)
                if beaten_number_in_roulette == roulette_number_bet:
                    print('Ты сорвал куш!!! Твой счёт выигранных денег:', bet_of_money_on_races * 6)
                    if randint(1, 30) == 26:
                        print('Ты сорвал x2 куш!,поэтому твои выигранные деньги умножаются в 2 раза, ты выиграл:', bet_of_money_on_races * 12)
                    your_amount_of_money += bet_of_money_on_races
                else:
                    print('Не расстраивайся, бывают поражения. Ты проиграл:', bet_of_money_on_races)
                    if randint(1, 37) != 26:
                        your_amount_of_money -= bet_of_money_on_races
                    else:
                        print('Тебе повезло и ты не теряешь денег!')
            else:
                print('Я не умею догадываться, напиши правильно или проверь есть ли такая функция из предложенных в ставках')
            if input('Ты хочешь продолжить делать ставки?').lower() != 'да':
                Choice_of_gambling = False
        desire_for_communication = input('Ты хочешь ёще продолжить играть в азартные игры?').lower()
        while desire_for_communication != 'да' and desire_for_communication != 'нет':
            desire_for_communication = input('Не понял тебя, напиши да или нет. Ты хочешь ёще продолжить играть в азартные игры?').lower()
        if desire_for_communication == 'да':
            function = 'азартные игры'
        elif desire_for_communication == 'нет':
            function = input('Какую функцию тогда ты выберешь?(Калькулятор, общение или рандомайзер')
    return function           

def opportunities_that_are():
    print('Мои возможности на момент ранней разработки, так называемой пре-пре-альфы: общение, калькулятор, рандомайзер и казино')

def functions_that_are():
    print('По кнопке Tab покажуться функции которые существуют в боте.\nПо кнопке Home показываються кнопки которые есть в чат боте(как раз сейчас ты и нажал его).')

scr = getscreen()

scr.onkey(opportunities_that_are, 'Tab')
scr.onkey(functions_that_are, 'Home')
exit_question = input('Ты хочешь начать работу с ботом?(да/нет): ').lower()
offensive_exit = True
your_amount_of_money = 10
while offensive_exit:
    if exit_question == 'да':
        function = greetings_bot()
        while exit_question != 'нет':
            if function == 'общение':
                function = function_communication(function, your_amount_of_money)
            elif function == 'калькулятор':
                function = calculation_function(function)
            elif function == 'рандомайзер':
                function = randomizer_function(function)
            elif function == 'азартные игры' or function == 'казино':
                function = all_casinos_function(function, your_amount_of_money)
            exit_question == input('Ты завершил цикл команд, ты хочешь продолжить работу с ботом?: ').lower() 
            if function != 'общение' and function != 'калькулятор' and function != 'рандомайзер' and (function != 'казино' and 'азартный игры'):
                function = input('Введите пожалуйста правильно функцию: ')
    elif exit_question != 'да' and exit_question != 'нет':
        exit_question = input('Ты написал неправильно, напиши да или нет: ').lower()
    elif exit_question == 'нет':
        print('Удачи тебе')
        offensive_exit = False
