import json

def load_Data():
    try:
        with open('./youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('./youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_Videos(videos):
    print('\n')
    print('*' * 50)
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    print('*' * 50)

def add_Video(videos):
    name = input('Enter Video Name : ')
    time = input('Enter Video Time : ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_Video(videos):
    list_all_Videos(videos)
    id = int(input("Enter the Video Number : " ))

    if 1 <= id <= len(videos):
        name = input("Enter New Video Name : ")
        time = input("Enter New Video Time : ")
        # videos[id - 1]['name'] = name
        # videos[id - 1]['time'] = time
        videos[id - 1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index selected")


def delete_Video(videos):
    list_all_Videos(videos)
    id = int(input("Enter the Video Number : " ))
    if 1 <= id <= len(videos):
        # videos.pop(id - 1)
        del videos[id - 1]
        save_data_helper(videos)
    else:
        print("Invalid Index selected")


def main():
    while True:
        videos = load_Data()
        print('\nYouttube Manager | Choose an Option')
        print('1. List all Videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input('Enter your option : ')
        # print(videos)

        match choice:
            case '1':
                list_all_Videos(videos)

            case '2':
                add_Video(videos)
            
            case '3':
                update_Video(videos)
            
            case '4':
                delete_Video(videos)
                
            case '5':
                exit()
            
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()