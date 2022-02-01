from typing import Dict, List


def check_values(dataset: Dict) -> Dict:
    for key in dataset:
        if dataset[key] % 2 != 0:
            dataset[key] -= 1
    return dataset


def give_median(values: List) -> int:
    len_value = len(values)
    if len_value % 2 == 0:
        index1 = len_value // 2 - 1
        index2 = index1 + 1
        median = (values[index1] + values[index2]) // 2
    else:
        median = values[(len_value - 1) // 2]
    return median


def give_name(value: int, dataset: Dict) -> str:
    for k, v in dataset.items():
        if v == value:
            return k


if __name__ == '__main__':
    dataset = {'admin$': 2, 'daemon_': 6, 'Kovalev': 16, 'Anderson': 21, 'Corvin': 3, 'Borat': 23, 'aBrams': 14,
               '13': 20,
               'Gerhaгd': 19, 'Zidane': 12, 'Messi': 10, 'Rupert': 10}

    # Шаг 1
    footballers = ['Messi', 'Zidane']
    dataset = {key: val for key, val in dataset.items() if key.isalpha()}
    dataset = {key: val for key, val in dataset.items() if key not in footballers}
    dataset = check_values(dataset)

    # Шаг 2
    values = [i for i in dataset.values()]
    values.sort(reverse=True)
    median = give_median(values)
    high_median_values = [i for i in values if i > median]
    result = []
    for i in high_median_values:
        result.append(give_name(i, dataset))

    """
    ЗАДАЧА:
    ШАГ 1
    Очистить датасет по совокупности условий:
    1) Нам нужны только люди (фамилия состоит из букв)
    2) Нам не нужны футболисты
    3) Показатель может быть только чётным, остальное – искажения. Искажения исправить: привести к ближайшему меньшему чётному.
    Вернуть очищенный словарь в переменной cleared_dataset.
    ШАГ 2
    Теперь небольшая аналитика на очищенном словаре. 
    Надо вернуть список фамилий тех, у кого значение показателя выше медианного, в порядке убывания показателя.
    Список поместить в переменной result.
    """