# Python-Base-Practice

> Для понимания описанных здесь вещей желательно знать питон на базовом уровне.

<br>

# Аннотации типов (type hints)

В питоне **типизация** является ***динамической***, что может упрощать многие аспекты разработки, но также это может привести к **непредвиденным ошибкам** и **усложнению понимания кода**. Для улучшения ситуации, в питоне есть такая вещь как ***тайп хинты***. По факту, это просто подсказки для типов переменных, выглядят они так:

```python
x: str = "hello"

def foo(y: int) -> None:
    ...
```

Но это всего лишь **подсказки**, вам ничего не помешает записать в переменную с хинтом str число или объект. При этом, я все равно настоятельно рекомендую вам их прописывать. Во многих ide на их основе, например, создаются интерактивные подсказки.

## Пример без хинта:
<image src="images/1.png">

## Пример с хинтом:
<image src="images/2.png">

***

<br>

Для переменных можно задавать сразу несколько типов с помощью |. Пример:

```python
x: int | str = "123"
y: int | str = 123
z: int | None = None
```

<br>

Для более удобной работы с хинтами в питоне есть встроенная библиотека **typing**:

```python
from typing import Any, Generator, Optional


x: Optional[int]
# то же самое что и:
# x: int | None


# Any - любой тип
def foo() -> Generator[Any]:
    yield 1
    yield "hello"
```

<br>

Вы также можете объявлять свои собственные типы:

```python
from typing import Optional, TypeVar


type Username = Optional[str]
type UserAge = Optional[int]

DataField = TypeVar("UserFields", Username, UserAge)

type UserData = dict[str, DataField]
```

<br>

Подробнее про тайпхинты можете прочитать [тут](https://habr.com/ru/companies/lamoda/articles/432656/)

<br>

# Линтеры и форматеры

Что такое линтер? ***Линтер*** - это всего лишь программа, которая проверяет твой код. Люди, использующие vs code наверняка знакомы с Pylance. Он проверяет синтаксис во время разработки, чтобы сразу указать на все ошибки. Но зачастую, его одного бывает недостаточно. Я выделю три самых главных линтера по-моему мнению.

> Для их использования вам нужно будет установить соответствующий линтер через pip. <br>
> После установить плагин/расширение в вашей ide.

## flake8
Он схож с Pylance, но имеет перед ним огромное преимущество за счет множества плагинов. Вот например самые популярные из них:

- [**bugbear**](https://pypi.org/project/flake8-bugbear/). Помимо проверки синтаксиса добавляются проверки на соответствие стилю написания кода (pep8 и принципы чистого кода).
- [**builtins**](https://pypi.org/project/flake8-builtins/). Добавляет проверки для избежания переопределения встроенных имён.
- [**cognitive-complexity**](https://pypi.org/project/flake8-cognitive-complexity/). Проверяет код на слишком большую вложенность.
- [**eradicate**](https://pypi.org/project/flake8-eradicate/). Проверяет код на отстутсвие закомменченных кусков ненужного кода.

<br>

Сам [flake8](https://pypi.org/project/flake8/)

## mypy
Выше я писал что тайпхинты являются всего линь подсказками, которые никак не проверяются. Так вот, mypy решает эту проблему и начинает подсвечивать несоответствие типов:

<image src="images/3.png">

---

<image src="images/5.png">
<image src="images/4.png">

<br>

К сожалению, на рантайм это никак не влияет и вам все равно могут прилететь другие типы. Внимательно следите за этим и расставляйте тайпхинты, чтобы предотвратить это на этапе разработки.

## isort
Это линтер, который проверяет порядок ваших имортов. В питоне их принято офромлять так:

1. Встроенные библиотеки
2. Установленные библиотеки
3. Свои модули и пакеты

Между каждой категорией должна быть пустая строка, а импорты в каждой категории должны быть расположены в алфавитном порядке.