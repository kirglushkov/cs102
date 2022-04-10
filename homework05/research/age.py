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
    user_age = []
    friends = get_friends(user_id, fields=["bdate"])
    for friend in friends.items:
        age = dt.datetime.today().year - int(friend["bdate"].split(".")[2])  # type: ignore
        user_age.append(age)
    return statistics.median(user_age) if user_age else None


if __name__ == "__main__":
    print(age_predict(162318084))
