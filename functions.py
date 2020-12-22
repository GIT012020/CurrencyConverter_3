import json
import requests


def connecting_nbp_api():
    """connecting to NBP API if cant connected returns an error"""
    try:
        nbp_data = requests.get(
            "http://api.nbp.pl/api/exchangerates/tables/a/")
    except requests.exceptions.ConnectionError:
        return "ERROR1"

    """extracting data in json"""
    nbp_list = nbp_data.json()[0]  # change list to a dict

    """add polish zloty to the data"""
    modification = list(nbp_list['rates'])
    modification.insert(
        0, {'currency': 'Polish Zloty', 'code': 'PLN', 'mid': 1.0})
    nbp_list["rates"] = modification
    return nbp_list


def extracting_data_nbp_reply(nbp_list, inquiry):

    try:
        if inquiry == 'effectiveDate':
            date = nbp_list[inquiry]
            return date
        else:
            exchange_rates_dict = (nbp_list["rates"])
            try:
                exchange_rate = next(
                    item for item in exchange_rates_dict if item["code"] == f"{inquiry}")
                return exchange_rate['mid']
            except StopIteration:
                return "ERROR2"
    # TypeError appears for example, when list does not contain dict.
    except (KeyError, TypeError):
        return "ERROR2.2"


def calculate_result(ex_rate_1, ex_rate_2, value):

    try:
        currency_ratio = float(ex_rate_1)/float(ex_rate_2)
        final_result = currency_ratio * float(value)
        return round(final_result, 2), currency_ratio
    except ValueError:
        return "ERROR3"
    except ZeroDivisionError:
        return "ERROR4"


if __name__ == '__main__':
    connecting_nbp_api()
