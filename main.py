import os
import smtplib


letter_shablon = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
site_name = 'https://dvmn.org/referrals/I5OAcDxqLdPjrO6Wv5GMwmsSRVatAYUsQvwGDse3/'
friend_name = 'Dmitry'
sender_name = 'Dmitry.Sha'
email_senter = 'demid58000@yandex.ru'
email_recipient = 'kuriatov.dima@yandex.ru'
letter_shablon = letter_shablon.replace('%my_name%', 'Dmitry.Sha')
letter_shablon = letter_shablon.replace('%friend_name%', 'Dmitry')
letter_shablon = letter_shablon.replace('%website%', 'https://dvmn.org/referrals/I5OAcDxqLdPjrO6Wv5GMwmsSRVatAYUsQvwGDse3/')

letter = """From: {es}
To: {er}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {fn}! {sname} приглашает тебя на сайт {sn}!

{sn} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {sn}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {sn}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
""".format(sn = site_name, fn = friend_name, sname = sender_name, es = email_senter, er = email_recipient)
letter = letter.encode("UTF-8")

my_secret = os.environ['YA_PASSWORD']

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(email_senter, my_secret)
server.sendmail(email_senter, email_recipient, letter)
server.quit()
