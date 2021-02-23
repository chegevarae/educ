def prefilter_items(data_train):
    # Возьмем топ по популярности
    if take_n_popular is not None:
        popularity = data.groupby('item_id')['quantity'].sum().reset_index()
        popularity.rename(columns={'quantity': 'n_sold'}, inplace=True)
        top = popularity.sort_values('n_sold', ascending=False).head(take_n_popular).item_id.tolist()
        data.loc[~data['item_id'].isin(top), 'item_id'] = 999999
    else:
        # Уберем самые популярные товары (их и так купят)
        popularity = data.groupby('item_id')['user_id'].nunique().reset_index()
        popularity['user_id'] = popularity['user_id'] / data['user_id'].nunique()
        popularity.rename(columns={'user_id': 'share_unique_users'}, inplace=True)
        top_popular = popularity[popularity['share_unique_users'] > 0.2].item_id.tolist()
        data.loc[data['item_id'].isin(top_popular), 'item_id'] = 999999

        # Уберем самые НЕ популярные товары (их и так НЕ купят)
        top_notpopular = popularity[popularity['share_unique_users'] < 0.002].item_id.tolist()
        data.loc[data['item_id'].isin(top_notpopular), 'item_id'] = 999999

        # Уберем товары, которые не продавались за последние 12 месяцев
        actuality = data.groupby('item_id')['week_no'].nunique().reset_index()
        top_actual = actuality[actuality.week_no > 365 / 7].item_id.tolist()
        data.loc[data['item_id'].isin(top_actual), 'item_id'] = 999999

        # Уберем слишком дешевые товары (на них не заработаем). 1 покупка из рассылок стоит 60 руб.
        data['price'] = data['sales_value'] / (np.maximum(data['quantity'], 1))
        low_price = data[data['price'] > 2].item_id.tolist()
        data.loc[data['item_id'].isin(low_price), 'item_id'] = 999999

        # Уберем слишком дорогие товары
        high_price = data[data['price'] > 100].item_id.tolist()
        data.loc[data['item_id'].isin(low_price), 'item_id'] = 999999

    # Уберем department
    if item_features is not None:
        department_size = pd.DataFrame(item_features.groupby('department')['item_id'].nunique().sort_values(ascending=False)).reset_index()
        department_size.columns = ['department', 'n_items']
        rare_departments = department_size[department_size['n_items'] < 150].department.tolist()
        items_in_rare_departments = item_features[item_features['department'].isin(rare_departments)].item_id.unique().tolist()
        data = data[~data['item_id'].isin(items_in_rare_departments)]

    return data
    

def postfilter_items():
    pass


def get_similar_items_recommendation(self, user, N=5):
    """Рекомендуем товары, похожие на топ-N купленных юзером товаров"""

    top_users_purchases = self.top_purchases[self.top_purchases['user_id'] == user].head(N)

    res = top_users_purchases['item_id'].apply(lambda x: self._get_similar_item(x)).tolist()
    res = self._extend_with_top_popular(res, N=N)

    assert len(res) == N, 'Количество рекомендаций != {}'.format(N)
    return res


def get_similar_users_recommendation(self, user, N=5):
    """Рекомендуем топ-N товаров, среди купленных похожими юзерами"""

    res = []
    
    # Находим топ-N похожих пользователей
    similar_users = self.model.similar_users(self.userid_to_id[user], N=N+1)
    similar_users = [rec[0] for rec in similar_users]
    similar_users = similar_users[1:]   # удалим юзера из запроса

    for user in similar_users:
        userid = self.id_to_userid[user] #own recommender works with user_ids
        res.extend(self.get_own_recommendations(userid, N=1))

    res = self._extend_with_top_popular(res, N=N)

    assert len(res) == N, 'Количество рекомендаций != {}'.format(N)
    return res
