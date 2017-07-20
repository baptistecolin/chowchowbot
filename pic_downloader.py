import flickr_api
import json

credentials_file = open("flickr_credentials")
credentials_file_data = credentials_file.read()
credentials_data = json.loads(credentials_file_data)

flickr_api.set_keys(credentials_data["key"],
                    credentials_data["secret"])

photos = flickr_api.Walker(flickr_api.Photo.search,
                           tags='chow chow', 
                           sort='relevance')

i = 0

for photo in photos:
    try:
        photo.save("pics/" + str(i) + ".jpg", size_label='Medium 640')
    except flickr_api.flickrerrors.FlickrError:
        photo.save("pics/" + str(i) + ".jpg")
    finally:
        print("photo #" + str(i) + " downloaded")
        i = i+1

    if(i==1500):
        break
