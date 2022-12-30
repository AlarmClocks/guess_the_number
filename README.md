# Проект 0. Угадай число (guess the number)

## Оглавление  
[1. Описание проекта](README.md#Описание-проекта)
[2. Какой кейс решаем?](README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](README.md#Этапы-работы-над-проектом)  
[5. Результат](README.md#Результат)    
[6. Выводы](README.md#Выводы) 

### Описание проекта    
Игра 'Угадай число'.
Угадать загаданное компьютером число за минимальное число попыток.

 [к оглавлению](README.md#Оглавление)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия задания:**  
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше или меньше случайное число нужного нам числа.
- Представлен шаблон baseline из скринкаста.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток (не более 20).

**Что практикуем**     
- Учимся писать хороший код на Python.
- Учимся работать с IDE.
- Учимся работать с GitHub.

:arrow_up:[к оглавлению](README.md#Оглавление)

### Краткая информация о данных
Посредством рандомайзера numpy, генерируется случайное целое число от 1 до 100.
Программа работает с переменными типа int.

  
[к оглавлению](README.md#Оглавление)


### Этапы работы над проектом  
1 написание кода:
    - Написана функция автоматического загадывания;
    - Написана функция и угадывания числа за минимальное количество попыток < 20;
    - Написана функция для подсчёта среднего количества попыток при 1000 повторений.
2 код решения загружен на GitHub;
3 GitHub оформлен соответствующим образом;
4 код соответствует стандарту PEP8;
5 код воспроизводим.
???!!! Оформлен Jupyter Notebook для демонстрации работы функций и подведения итога работы.

[к оглавлению](README.md#Оглавление)


### Результаты:  
- программа угадывает число за 5 попыток;
- код решения загружен на GitHub;
- GitHub оформлен соответствующим образом;
- код соответствует стандарту PEP8;
- код воспроизводим.

[к оглавлению](README.md#Оглавление)


### Выводы:  
Использование простого метода поиска числа посредством рандомайзера не является оптимальным.
Использование метода цикличного нахождения среднего значения между max и min, и сравнения его с загаданным числом является оптимальным вариантом. 
- Выполнены все 5 критериев задания

[к оглавлению](README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень благодарен Вам, если отметите репозиторий и профиль ⭐️