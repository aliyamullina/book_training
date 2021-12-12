[![Python application](https://github.com/aliyamullina/book_training/actions/workflows/tests_ci.yml/badge.svg?branch=main)](https://github.com/aliyamullina/book_training/actions/workflows/tests_ci.yml)

# Седер, Python. Экспресс курс

### Глава 5. Списки, кортежи и множества
#### СОРТИРОВКА СПИСКОВ
Имеется список, каждый элемент которого также является списком

`[[1, 2, 3], [2, 1, 3], [4, 0, 1]]`.

Допустим, вы хотите отсортировать этот список по второму элементу каждого списка, чтобы получить результат 

`[[4, 0, 1], [2, 1, 3], [1, 2, 3]]`. 

Какую функцию вы бы написали для передачи в параметре key метода sort()?

```
/story/sort_list.py
/tests/test_sort_list.py
```

#### ОПЕРАЦИИ СО СПИСКАМИ
Имеется список x. 

Напишите код безопасного удаления элемента в том случае, 
если значение присутствует в списке.

Измените код так, чтобы элемент удалялся только в том случае, 
если элемент присутствует в списке более чем в одном экземпляре.

```
/story/operations_list.py
/tests/test_operations_list.py
```

#### МОДИФИКАЦИЯ СПИСКОВ
Допустим, список состоит из 10 элементов. 

Как переместить три последних элемента из конца в начало списка без нарушения их исходного порядка?

```
/story/modification_list.py
/tests/test_modification_list.py
```

#### СЕГМЕНТЫ И ИНДЕКСЫ СПИСКОВ
Используя то, что вы знаете о функции len() и сегментах списков, как бы вы получили вторую половину списка неизвестного размера? 

Поэкспериментируйте в сеансе Python и убедитесь в том, что ваше решение работает.

```
/story/segments_indices_list.py
/tests/test_segments_indices_list.py
```

#### КОПИРОВАНИЕ СПИСКОВ
Имеется следующий список: `x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`. 

Какой код вы бы использовали для создания копии y этого списка, в которой элементы можно было бы изменять без побочного эффекта с изменением содержимого x?

```
/story/copy_list.py
/tests/test_copy_list.py
```

### Глава 6. Строки
#### ОПЕРАЦИИ СО СТРОКАМИ
Допустим, имеется список строк, в котором некоторые (но не обязательно все) строки начинаются и 
завершаются символом двойной кавычки:
`x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']`

Какой код вы бы использовали для удаления только двойных кавычек из каждого элемента?

Какой код вы бы использовали для нахождения позиции последней буквы `p` в слове `Mississippi`? 
А после того, как эта позиция будет найдена, какой код вы бы использовали для удаления только этой буквы?

```
/story/operations_string.py
/tests/test_operations_string.py
```

### Глава 7. Словари
#### СОЗДАНИЕ СЛОВАРЯ
Напишите код, который запрашивает у пользователя три имени и три возраста. 

После ввода имен и возрастов запросите у пользователя одно из имен и выведите соответствующий возраст.

```
/story/create_dict.py
/tests/test_create_dict.py
```

### Глава 8. Управляющие конструкции
#### ЦИКЛЫ И КОМАНДЫ IF
Допустим, имеется список `x = [1, 3, 5, 0, -1, 3, -2]`, из которого нужно удалить все отрицательные числа. 
Напишите код для решения этой задачи.

Как бы вы подсчитали общее количество отрицательных чисел в списке `y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]`?

Какой код вы бы использовали для вывода описания: 
- `very low`, если значение `x меньше −5`, 
- `low`, если оно лежит в диапазоне `от −5 до 0`; 
- `neutral`, если оно `равно 0`; 
- `high`, если оно лежит в диапазоне `от 0 до 5`; 
- `very high`, если оно `больше 5`?

```
/story/loops_commands_if.py
/tests/test_loops_commands_if.py
```