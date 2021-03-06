import vk
import wget

def get_photos(owner_id):
    photos = vk_api.photos.get(owner_id=owner_id, album_id='281940823', v=5.131, extended=1)
    
    for i in range(len(photos['items'])):
        print(i+1,'из', len(photos['items']), end=', ')
        image_url = photos['items'][i]['sizes'][-1]['url']
        image_filename = wget.download(image_url, bar=None)
        likes = photos['items'][i]['likes']
        user_id = photos['items'][i]['user_id']
        userinfo = vk_api.users.get(user_ids=user_id, v=5.131)
        print(f'автор - {userinfo[0]["first_name"]} {userinfo[0]["last_name"]}, количество лайков - {likes["count"]}')

    print('успешно скачано')


if __name__ == "__main__":
    session = vk.Session(access_token='1e6356e81e6356e81e6356e86b1e1f18b411e631e6356e87c07519017b0923321082549')
    vk_api = vk.API(session)
    owner_id = "-197700721"
    get_photos(owner_id)
