from typing import List
from scrapy import  Selector
import pickle


## used once to save a pickle of response text.
from items import HOUSE_SELECTOR, GummyHouseForSale, \
    HOUSE_SELECTOR_EXTRACT_FIRST



def _clear_string(string_input: str)-> str:
    return  string_input.strip('  \t\n\r ')

def get_field_raw_output( selector :Selector, field_key: str)-> object:
    if field_key in HOUSE_SELECTOR_EXTRACT_FIRST:
        return selector.xpath(
            HOUSE_SELECTOR[field_key]).extract_first()
    else:
        return selector.xpath(HOUSE_SELECTOR[field_key]).extract()


def process_raw_output(field_key: str, raw_output: object)-> object:
    if field_key == "location":
       location_city_county = raw_output[0].split(",")
       return [_clear_string(location_city_county[0]), _clear_string(location_city_county[1])]
    elif field_key == "concealed_phone":
        remove_X_end = raw_output.replace('X', '')
        return _clear_string(remove_X_end)
    else:
        if isinstance( raw_output, List):
            return _clear_string(raw_output[0])
        elif isinstance( raw_output, str):
            return _clear_string(raw_output)

def  save_to_item(item: GummyHouseForSale, field_key: str, clean_string_output: object):
    if field_key == "location":
        item["city"] = clean_string_output[0]
        item["county"] = clean_string_output[1]
    else:
        item[field_key] = clean_string_output


