# Лабораторные работы по предмету "Модели данных и системы управления базами данных"
# ЛР 1. 
Создать скрипты для создания, удаления, наполнения таблиц
## ЛР 2. 
Объявить переменную Perem1 для хранения информации о денежной величине, а 
переменную Perem2  – для хранения чисел с целой частью,равной 8, и дробной 
частью, равной 2. 

Определить  переменную  Date1  типа  ДАТА.  Присвоить  ей  значение даты 
07.01.2012 в формате dd.mm.yyyy. 

Определить  переменную  Date1  типа  ДАТА.  Присвоить  ей  значение даты 
23.02.2014 в формате yyyy.mm.dd. 

Создать запись с названием TEMP и полями типа дата, длинное целое, строка. 
Присвоить полям записи данные и вывести результат на экран. 

Объявить  переменные  типа  NUMERIC,  VARCHAR2,  DATE.  Присвоить  значения, 
соответствующие типам. Выполнить преобразование переменных типа NUMERIC, 
VARCHAR2, DATE в FLOAT, CHAR,NUMERIC соответственно и вывести результат 
на экран. 

Подсчитать  среднюю  цену  (стоимость,  оплату,  оценку,  сумму,  размер 
комиссионных,  стаж  работы,  стоимость  тарифа  или  любого  другого  значения 
согласно  варианту)в  одной  из  таблиц  на  выбор.Если  полученноезначение 
находится  в  заданном  диапазоне,  например  от  3000  до  5000,  то  ничего  не
сообщать, в противном случае вывести сообщение вида "Среднеезначение = …" 
(вместо многоточия поставить точную среднюю стоимость). 

Объявить  курсор  по  данным  нескольких  полей  из  нескольких  таблиц  на  выбор. 
Вывести данные 5-й записи курсора. 

По правилам оформления машинописных текстов перед знаками.,!?:; пробелы не 
ставятся, но обязательно ставятся после этих знаков. Удалите лишние пробелы. 
Подсчитать количество исправлений. 

Удалить из базового текста 2-е, 4-е, 6-е, 8-е слова. 

Вставить в базовый текст вместо букв «е» и «о» – «ББ». 
## ЛР 3. 
1. Вывести сделку, у которой размер комиссионных превышает заданное число. 
2. Вывести список соискателей, которые имеют предполагаемый размер заданной 
платы меньше, чем размер комиссионных, предлагаемых со стороны 
работодателя.
3. Вывести список работодателей по заданному виду деятельности и отсортировать 
список по возрастанию комиссионных.
## ЛР 4. 
1. Создать  строковый  триггер,  который  будет  фиксировать  любое  текстовое  поле  в 
отдельно организованной таблице при добавлении нового объекта в одну из таблиц. 
2. Создать  операторный  триггер,  который  будет  фиксировать  в  отдельно 
организованной  таблице  дату  операции,  вид  операции,  имя  пользователя  при 
удалении, добавлении или изменении данных в одной из таблиц. 
3. Создать  системный  триггер  на  уровне  схемы,  который  будет  фиксировать  в 
отдельно  организованной  таблице  информацию  о  пользователях  и  объектах, 
структуру которых создают.
## ЛР 5. 
Оказалось,  что  база  данных  не  совсем  точно  описывает  работу  бюро.  В  базе 
фиксируется только сделка, а информация по открытым вакансиям не хранится. 
Кроме того, для автоматического поиска вариантов необходимо вести справочник 
«Виды деятельности». 
Предусмотреть  обработку  пользовательского  исключения,  когда  при  добавлении 
нового  соискателя  выводилось  бы  пользовательское  сообщение  об  ошибке,  если 
фамилия, имя и отчество полностью совпадают.