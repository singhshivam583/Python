import requests

def apiHandler():
    url = 'https://api.freeapi.app/api/v1/public/randomusers'
    res = requests.get(url)
    data = res.json()
    if data["success"] and data["statusCode"] == 200:
        return  data['data']
    else:
        raise Exception("Data not found")

def main():
    try:
        users_list = apiHandler()
        # print(users_list)
        # print('\n')
        # print(users_list["data"])
        # print('\n')
        for index, user in enumerate(users_list["data"], start=1):
            print(f"{index}. {user["name"]["title"]}. {user["name"]["first"]} {user["name"]["last"]}, Country: {user["location"]["country"]}")
    except Exception as e:
        print('Error occurred while fetching the data : ', str(e))

if __name__ == "__main__":
    main()
