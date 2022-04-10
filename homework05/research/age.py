import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    """
    Наивный прогноз возраста пользователя по возрасту его друзей.

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: Идентификатор пользователя.
    :return: Медианный возраст пользователя.
    """
    friends = get_friends(user_id, fields=["bdate"])
    friend_ages = []
    for f in friends.items:
        try:
            age = dt.datetime.today().year - int(f["bdate"].split(".")[2])  # type: ignore
            friend_ages.append(age)
        except:
            pass
    if friend_ages:
        return statistics.median(friend_ages)
    return None
