import pickle


class CountryState:

    def __init__(self, country_dict=None):
        if country_dict is None:
            country_dict = {}
        self.country_dict = country_dict

    def add_country(self, country, capital):
        self.country_dict[country] = capital
        return f'Добавлена страна {country} столица {self.country_dict[country]}.'

    def remove_country(self, country):
        return f'Удалена страна {country} столица {self.country_dict.pop(country)}.'

    def search_country(self, country):
        for key in self.country_dict.keys():
            if key == country:
                return f'Есть такая страна: {key}. Ее столица {self.country_dict[key]}.'
            else:
                return 'Такой страны нет.'

    def search_capital(self, capital):
        for key, value in self.country_dict.items():
            if value == capital:
                return f'Есть такая столица: {value}. Это столица страны {key}.'
            else:
                return 'Такой столицы нет.'

    def replace_capital(self, country, new_capital):
        if country in self.country_dict.keys():
            replace_capital = self.country_dict[country]
            self.country_dict[country] = new_capital
            return f'Заменили столицу {replace_capital} страны {country} на новую столицу {self.country_dict[country]}.'
        else:
            return 'Такой страны нет.'

    def pickle_file(self, filename, protocol):
        with open(filename, 'wb') as file:
            pickle.dump(self.country_dict, file, protocol)
        return 'Произведен пиклинг в файл'

    def unpickle_file(self, pickled_file):
        with open(pickled_file, 'rb') as file:
            unpickle_data = pickle.load(file)
            return unpickle_data


my_country_state = CountryState()
print(my_country_state.add_country('Russia', 'Moscow'))
print(my_country_state.add_country('England', 'London'))
print(my_country_state.add_country('USA', 'Washington'))
print(my_country_state.remove_country('USA'))
print(my_country_state.country_dict)
print(my_country_state.search_country('USA'))
print(my_country_state.search_capital('Moscow'))
print(my_country_state.replace_capital('USA', 'Saint-Petersburg'))
print(my_country_state.country_dict)
print(my_country_state.pickle_file('CountryState_pickle.txt', 5))
print(my_country_state.unpickle_file('CountryState_pickle.txt'))
