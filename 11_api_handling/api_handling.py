import requests as request 

def fetch_random_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    response = request.get(url)
    data = response.json()
    # print(data)
    if data["success"] and "data" in data:
        userData = data["data"]
        userName = userData["login"]["username"]
        userCountry = userData["location"]["country"]
        return userName, userCountry
    else:
        raise  Exception("Failed to get random user")


def main():
    try:
        userName , userCountry = fetch_random_user()
        print(f"User Name : {userName}, \nUser Country : {userCountry}")

    except Exception as e :
        print(str(e))


if  __name__ == "__main__":
    main()
     
    