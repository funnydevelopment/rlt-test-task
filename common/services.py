from datetime import datetime
import json

from .enums import GroupType, RequestType


async def has_json_format(data: str) -> bool:
    """
    Имеет ли входящие данные json формат
    :param data: {
                    "dt_from":"2022-09-01T00:00:00",
                    "dt_upto":"2022-12-31T23:59:00",
                    "group_type":"month"
                }
    :return: True | False
    """
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False


async def has_correct_length(data: str) -> bool:
    """
    Имеет ли входящие данные необходимую длину
    :param data: {
                    "dt_from":"2022-09-01T00:00:00",
                    "dt_upto":"2022-12-31T23:59:00",
                    "group_type":"month"
                }
    :return: True | False
    """
    try:
        json_data = json.loads(data)

        if isinstance(json_data, dict) and len(json_data) == 3:
            return True
    except json.JSONDecodeError:
        pass

    return False


async def are_items_valid(data: str) -> bool:
    """

    :param data: {
                    "dt_from":"2022-09-01T00:00:00",
                    "dt_upto":"2022-12-31T23:59:00",
                    "group_type":"month"
                }
    :return: True | False
    """
    try:
        json_data = json.loads(data)

        # Проверка наличия требуемых ключей
        required_keys = [item.value for item in RequestType]
        if all(key in json_data for key in required_keys):
            dt_from = json_data[RequestType.DT_FROM.value]
            dt_upto = json_data[RequestType.DT_UPTO.value]
            try:
                datetime.fromisoformat(dt_from)
                datetime.fromisoformat(dt_upto)
            except ValueError:
                return False
            group_type = json_data[RequestType.GROUP_TYPE.value]
            if group_type not in [e.value for e in GroupType]:
                return False
            return True

    except json.JSONDecodeError:
        pass

    return False


async def are_dates_valid(data: str) -> bool:
    try:
        json_data = json.loads(data)
        dt_from_str = json_data.get("dt_from")
        dt_upto_str = json_data.get("dt_upto")

        if not dt_from_str or not dt_upto_str:
            return False

        dt_from = datetime.strptime(dt_from_str, "%Y-%m-%dT%H:%M:%S")
        dt_upto = datetime.strptime(dt_upto_str, "%Y-%m-%dT%H:%M:%S")

        return dt_from < dt_upto

    except json.JSONDecodeError:
        return False


async def get_dict_data(data: str) -> dict:
    dict_data = json.loads(data)
    return dict_data
