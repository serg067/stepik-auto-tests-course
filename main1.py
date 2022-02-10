import requests
import re

all_times_in_min = (5 * 8 * 60)
remainder = 0
summary_report_time = 0

#token = "d3H1q2ziYvi5Yykl"    #отчет за 01-5 ноября
#token = "VtHlLsAqjj9oX7RF"    #отчет за 08-12 ноября
#token = "UYvyoZB5r8BbroRg"    #отчет за 15-19 ноября
#token = "z6r5nbdAThfQXfpf"    #отчет за 22-26 ноября
#token = "VSR1eOFqAuAZO42p"    #отчет за 29.11-03.12
#token = "RXRnH50lQXTuC038"    #отчет за 06.12-10.12
#token = "CAnCGzbmrSkEdMJ2"    #отчет за 13.12-17.12
#token = "d1NX1ozjxKgV5xRa"    #отчет за 20.12-24.12
#token = "jbZEtFQ5RU6qaKiD"    #отчет за 27.12-30.12
#token = "25dqh2VFCJwVsQoL"    #отчет за 10.01.22-14.01.22
#token = "qaxGOV3kjHvyJiHa"    #отчет за 17.01-21.01
#token = "MkYbntkSBhLaSJYT"    #отчет за 24.01-28.01    с начала ноября переработка 7 часов 53 минуты
tokens = ("d3H1q2ziYvi5Yykl") #это список всех нужных токенов
for token in tokens:
    url = "https://reportbot.olegb.ru/api/report_token?token=" + token
    r = requests.get(url)

    date_list_json = r.json()

    print("\nСписок дат и ссылок в отчете за неделю:")
    for date in date_list_json['dates']:
        print(date + " | Ссылка на отчет: " + "https://reportbot.olegb.ru/api/report?token=" + token + "&date=" + date)

    print()
    weekday = 0
    report_time = 0
    for i in range(0, len(date_list_json['dates'])):

        weekday += 1

        if weekday == 1:
            print("Отчет за Понедельник:")
        elif weekday == 2:
            print("\nОтчет за Вторник:")
        elif weekday == 3:
            print("\nОтчет за Среду:")
        elif weekday == 4:
            print("\nОтчет за Четверг:")
        elif weekday == 5:
            print("\nОтчет за Пятницу:")
        elif weekday == 6:
            print("\nОтчет за Субботу:")
        elif weekday == 7:
            print("\nОтчет за Воскресенье:")

        day = date_list_json['dates'][i]
        link_to_daily_report = requests.get("https://reportbot.olegb.ru/api/report?token=" + token + "&date=" + day
                                        + "&project_id=23")
        daily_report_json = link_to_daily_report.json()
        
        res = daily_report_json['report']
        
        row_number = 0
        time_per_day = 0
        for string in res.split("\n\n"):
            if len(string) > 1:
                row_number += 1
                print(row_number, string)
                searching_for_time_in_a_string = re.search(r'\[(\d{1,2})[dhm](.*)\]', string)
                remove_the_brackets = searching_for_time_in_a_string[0][1:-1]
                
                time_per_task = 0
                for i in range(len(remove_the_brackets.split())):
                    type_time = remove_the_brackets.split()[i][-1]
                    value_time = remove_the_brackets.split()[i][:-1]
                   
                    value_time_int = int(value_time)
                    if type_time == "d":
                        value_time_in_min = value_time_int * 8 * 60
                        time_per_task += value_time_in_min

                    elif type_time == "h":
                        value_time_in_min = value_time_int * 60
                        time_per_task += value_time_in_min

                    elif type_time == "m":
                        time_per_task += value_time_int

                    else:
                        print("Error")

                time_per_day += time_per_task

            else:
                print(" — Отчет отсутствует")

        if time_per_day > 0:
            report_time += time_per_day
            print(" — Минут за день:", time_per_day, "/", 8*60, "| Осталось = ", 8*60-time_per_day)

    summary_report_time += report_time
    print("\n\nВремя за неделю: ", report_time, "из", all_times_in_min)
    remainder = all_times_in_min - report_time
    hours = remainder // 60
    minutes = remainder - hours * 60
    if remainder == 0:
        print("Отдыхай")
    elif report_time > all_times_in_min:
        print("Переработка за неделю:", report_time - all_times_in_min)
    else:
        print("Осталось: ", remainder, "мин = ", hours, "ч", minutes, "мин")

    result = 0
    result += remainder

print("\n\nИтого за все время: ", summary_report_time, "из", all_times_in_min * len(tokens))
if result == 0:
    print("Отдыхай")
elif summary_report_time > all_times_in_min * len(tokens):
    result = summary_report_time - all_times_in_min * len(tokens)
    hours = result // 60
    minutes = result - hours * 60
    print("Переработка за все время:", result, "мин = ", hours, "ч", minutes, "мин")
else:
    result = all_times_in_min * len(tokens) - summary_report_time
    hours = result // 60
    minutes = result - hours * 60
    print("Осталось: ", result, "мин = ", hours, "ч", minutes, "мин")   