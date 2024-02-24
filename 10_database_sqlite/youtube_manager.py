import sqlite3

connection = sqlite3.connect('youtube_video.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        duration TEXT
    )
''')


def list_videos():
    print('\n')
    print('*' * 50)
    videos = cursor.execute("SELECT * FROM videos")
    # print(videos)
    # for row in cursor.fetchall():
    for row in videos.fetchall():
        print(row)
    print('*' * 50)
    print('\n')

def add_video(name, duration):
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    connection.commit()

def update_video(id, name, duration):
    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, id))
    connection.commit()
    

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    connection.commit()

def main():
    while True:
        print("Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your Choice : ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name : ")
            duration = input("Enter the video duration : ")
            add_video(name, duration)
            print('\n')

        elif choice == '3':
            list_videos()
            id = input("Enter video id : ")
            name = input("Enter the video name : ")
            duration = input("Enter the video duration : ")
            update_video(id, name, duration)
            print('\n')

        elif choice == '4':
            list_videos()
            id = input("Enter video id to delete : ")
            delete_video(id)

        elif choice == '5':
            # exit()
            break

        else:
            print("Invalid choice")
            continue
     # closing connection after exit   
    connection.close()

if __name__ == "__main__":
    main()
