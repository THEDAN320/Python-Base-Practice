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

# Докстринги (docstrings)

**Докстринги** - это специальные комментарии в коде, по которым ide создает подсказки. Прописываются они в начале функций, классов, методов и модулей.

Выглядят они так:

<image src="images/7.png">

Вот так выглядят подсказки в vs code:

<image src="images/8.png">

Вот [хорошая статья](https://realpython.com/documenting-python-code/#docstring-formats) по докстрингам и разным стилям их написания.

# Автодокументирование (Sphinx)

В экосистеме питона есть инструмент для автоматического создания документации (как gcov_report для C), называется он sphinx.

Базовый вариант документация выглядит примерно так:

<image src="images/9.jpg">

Есть и второй вариант внешнего вида:

<image src="images/10.jpg">

<br>

[Документация sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html).

[Статья](https://habr.com/ru/companies/netologyru/articles/815563/) с понятным объяснением по настройке.

# Линтеры

Что такое линтер? **Линтер** - это всего лишь программа, которая проверяет твой код. Люди, использующие vs code наверняка знакомы с Pylance. Он проверяет синтаксис во время разработки, чтобы сразу указать на все ошибки. Но зачастую, его одного бывает недостаточно. Я выделю три самых главных линтера по-моему мнению.

> Для их использования вам нужно будет установить соответствующий линтер через pip. <br>
> После установить плагин/расширение в вашей ide.

## flake8
Он схож с Pylance, но имеет перед ним огромное преимущество за счет множества плагинов. Вот например самые популярные из них:

- [**bugbear**](https://pypi.org/project/flake8-bugbear/). Помимо проверки синтаксиса добавляются проверки на соответствие стилю написания кода (pep8 и pycodestyle).
- [**builtins**](https://pypi.org/project/flake8-builtins/). Добавляет проверки для избежания переопределения встроенных имён.
- [**cognitive-complexity**](https://pypi.org/project/flake8-cognitive-complexity/). Проверяет код на слишком большую вложенность.
- [**eradicate**](https://pypi.org/project/flake8-eradicate/). Проверяет код на отстутсвие закомменченных кусков ненужного кода.

## mypy
Выше я писал что тайпхинты являются всего линь подсказками, которые никак не проверяются. Так вот, mypy решает эту проблему и начинает подсвечивать несоответствие типов:

<image src="images/3.png">

---

<image src="images/5.png">
<image src="images/4.png">

К сожалению, на рантайм это никак не влияет и вам все равно могут прилететь другие типы. Внимательно следите за этим и расставляйте тайпхинты, чтобы предотвратить это на этапе разработки.

## isort
Это линтер, который проверяет порядок ваших имортов. В питоне их принято офромлять так:

1. Встроенные библиотеки
2. Установленные библиотеки
3. Свои модули и пакеты

Между каждой категорией должна быть пустая строка, а импорты в каждой категории должны быть расположены в алфавитном порядке.

---

В каких-то местах некоторые линтеры могут конфликтовать. Но это не проблема, потому-что каждый из них можно настроить. Сделать это можно в файлах setup.cfg или pyproject.toml. Все правила можно кастомизировать под себя, конкретные настройки можно найти в документации линтеров. Пример файла setup.cfg лежит в репозитории.

Страницы на pypi:

* [flake8](https://pypi.org/project/flake8/)
* [mypy](https://pypi.org/project/mypy/)
* [isort](https://pypi.org/project/isort/)

<br>

# форматтеры
Форматтер - это программа, которая сама редактирует код для соответствия стилям. Самый популярный форматтер сейчас это [black](https://pypi.org/project/black/)

Для его настройки можно использовать те же файлы, что и для настройки линтеров.

Командой `black .` можно сразу же отформатировать все файлы проекта.

# pre-commit

[pre-commit](https://pypi.org/project/pre-commit/) - это программа, которая позволяет работать с гит хуками. С помощью нее мы можем запускать выполнение каких-то своих утилит когда делаем `git commit`

Например, через https://github.com/pre-commit/pre-commit-hooks можно настроить:
* Удаление лишних пробелов в коде
* Добавления символа переноса на новую строку в конце всех файлов
* Проверку корректности yaml, json файлов
* Проверка на отсутствие конфиденциальных данных в коде

И еще множество всего.

Также, хуки для пре-коммита имеют и линтеры с black:
* [flake8](https://github.com/PyCQA/flake8)
* [isort](https://github.com/PyCQA/isort)
* [mypy](https://github.com/pre-commit/mirrors-mypy)
* [black](https://github.com/psf/black)

С помощью них мы можем сделать форматирование кода и затем проверить через все линтеры перед отправкой на удаленный репозиторий. Выглядит это примерно так:
<image src="images/6.png">

# Pydantic

Представьте, у вас есть класс для данных пользователя:

```python
class User:
    """User class."""

    def __init__(self, tg_id: int) -> None:
        """User init.

        :param tg_id: user id from telegram.
        """
        self.tg_id = tg_id
```

И во избежания ошибок вы хотите уже на этом моменте убедиться что tg_id это числовой тип. Для этого можно воспользоваться встроенной функцией isinstance:

```python
class User:
    """User class."""

    def __init__(self, tg_id: int) -> None:
        """User init.

        :param tg_id: user id from telegram.
        """
        if isinstance(tg_id, int):
            self.tg_id = tg_id
        else:
            raise ValueError(
                "type for tg_id is incorrect! Excpected int."
            )

```

И это нормальное решение. Однако, в реальном классе может передаваться гораздо больше параметров, под которые придеться писать свои проверки. Тут нам поможет библиотека [Pydantic](https://pypi.org/project/pydantic/). Она позволяет создавать классы с автоматической валидацией типов. Работает она при помощи тайп хинтов. Вот как с ней выглядел бы наш класс:

```python
from pydantic import BaseModel


class User(BaseModel):
    """User class.

    :param tg_id: user id from telegram."""

    tg_id: int


user = User(123)
```
Это выглядит гораздо менее громоздко. При этом конструктор для класса Pydantic cоздаст сам, на основе наших параметров.

Докстринги для конструктора в таком случае прописываем в докстринге класса.

Если мы попытаемся создать объект с неккоректным типом, например `User(tg_id=1.23)`, то получим ошибку:

```bash
pydantic_core._pydantic_core.ValidationError: 1 validation error for User
tg_id
  Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=1.23, input_type=float]
    For further information visit https://errors.pydantic.dev/2.7/v/int_from_float
```

И тут есть важный момент. Pydantic всегда сначала пытается привести тип к нужному и только потом если у него это не получилось выбрасывает ошибку. Например, если мы попытаемся создать юзера так:

```python
user = User("123")
```

То никакой ошибки не будет, наша строка преобразуется в число. Для того чтобы строго проверять типы, в pydantic есть специальные типы:

```python
from pydantic import BaseModel, StrictInt


class User(BaseModel):
    """User class.

    :param tg_id: user id from telegram."""

    tg_id: StrictInt
```

p.s. И вот мы пришли к (псевдо-)статической типизации, от которой пытались уйти...

Также, в pydantic имеется возможность добавлять проверки на сами значения. Для этого этого есть специальная сущность `Field`:

```python
from typing import Annotated

from pydantic import BaseModel, Field, StrictInt


class User(BaseModel):
    """User class.

    :param tg_id: user id from telegram."""

    tg_id: Annotated[StrictInt, Field(gt=10)]
```

**Annotated** - это тип, который содержит другой тип вместе с метаданными. Здесь у нас в качестве типа `StrictInt`, в качестве метаданных `Field`.

Параметр gt (greater than) позволяет нам указать минимальное значение для нашего числа. Если мы передадим 9, получим следующую ошибку:

```bash
self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for User
tg_id
  Input should be greater than 10 [type=greater_than, input_value=9, input_type=int]
    For further information visit https://errors.pydantic.dev/2.7/v/greater_than
```

Такие проверки можно настроить для любых типов данных. вот список всех параметров что можно настроить:

<image src="images/11.png">

<br>

Полная [документация Pydantic](https://docs.pydantic.dev/latest/)

# Конфиги и приватные данные