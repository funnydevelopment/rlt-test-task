from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime


async def get_month_collection(dt_from: str, dt_upto: str) -> dict:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["mydatabase"]
    collection = db["sample_collection"]

    dt_from = datetime.strptime(dt_from, "%Y-%m-%dT%H:%M:%S")
    dt_upto = datetime.strptime(dt_upto, "%Y-%m-%dT%H:%M:%S")

    pipeline = [
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {
            "$group": {
                "_id": {"year": {"$year": "$dt"}, "month": {"$month": "$dt"}},
                "dataset": {"$sum": "$value"},
                "firstDateOfMonth": {"$min": "$dt"},
            }
        },
    ]

    result = await collection.aggregate(pipeline).to_list(None)

    # Сортировка по месяцам
    result.sort(key=lambda x: x["firstDateOfMonth"])

    # Формируем данные в желаемом формате
    formatted_result = {
        "dataset": [doc["dataset"] for doc in result],
        "labels": [
            datetime(
                doc["firstDateOfMonth"].year, doc["firstDateOfMonth"].month, 1
            ).strftime("%Y-%m-%dT%H:%M:%S")
            for doc in result
        ],
    }

    return formatted_result


async def get_day_collection(dt_from: str, dt_upto: str) -> dict:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["mydatabase"]
    collection = db["sample_collection"]

    dt_from = datetime.strptime(dt_from, "%Y-%m-%dT%H:%M:%S")
    dt_upto = datetime.strptime(dt_upto, "%Y-%m-%dT%H:%M:%S")

    pipeline = [
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {
            "$group": {
                "_id": {
                    "year": {"$year": "$dt"},
                    "month": {"$month": "$dt"},
                    "day": {"$dayOfMonth": "$dt"},
                },
                "dataset": {"$sum": "$value"},
                "firstDateOfDay": {"$min": "$dt"},
            }
        },
    ]

    result = await collection.aggregate(pipeline).to_list(None)

    # Сортировка по дням
    result.sort(key=lambda x: x["firstDateOfDay"])

    # Формируем данные в желаемом формате
    formatted_result = {
        "dataset": [doc["dataset"] for doc in result],
        "labels": [
            datetime(
                doc["firstDateOfDay"].year,
                doc["firstDateOfDay"].month,
                doc["firstDateOfDay"].day,
                0,
                0,
                0,
            ).strftime("%Y-%m-%dT%H:%M:%S")
            for doc in result
        ],
    }

    return formatted_result


async def get_hour_collection(dt_from: str, dt_upto: str) -> dict:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["mydatabase"]
    collection = db["sample_collection"]

    dt_from = datetime.strptime(dt_from, "%Y-%m-%dT%H:%M:%S")
    dt_upto = datetime.strptime(dt_upto, "%Y-%m-%dT%H:%M:%S")

    pipeline = [
        {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
        {
            "$group": {
                "_id": {
                    "year": {"$year": "$dt"},
                    "month": {"$month": "$dt"},
                    "day": {"$dayOfMonth": "$dt"},
                    "hour": {"$hour": "$dt"},
                },
                "dataset": {"$sum": "$value"},
                "firstDateOfHour": {"$min": "$dt"},
            }
        },
    ]

    result = await collection.aggregate(pipeline).to_list(None)

    # Сортировка по часам
    result.sort(key=lambda x: x["firstDateOfHour"])

    # Формируем данные в желаемом формате
    formatted_result = {
        "dataset": [doc["dataset"] for doc in result],
        "labels": [
            datetime(
                doc["firstDateOfHour"].year,
                doc["firstDateOfHour"].month,
                doc["firstDateOfHour"].day,
                doc["firstDateOfHour"].hour,
                doc["firstDateOfHour"].minute,
                doc["firstDateOfHour"].second,
            ).strftime("%Y-%m-%dT%H:%M:%S")
            for doc in result
        ],
    }

    return formatted_result
