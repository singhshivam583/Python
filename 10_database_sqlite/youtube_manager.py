import sqlite3

try:
    connection = sqlite3.connect('youtube_video.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            duration TEXT
        )
    ''')

except Exception as e:
    print("Error:", e)
    exit()


def list_videos():
    try:
        print('\n')
        print('*' * 50)
        videos = cursor.execute("SELECT * FROM videos")
        for row in videos.fetchall():
            print(row)
        print('*' * 50)
        print('\n')
    except Exception as e:
        print("Error:", e)


def add_video(name, duration):
    try:
        cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
        connection.commit()
        print("Video added successfully.")
    except Exception as e:
        print("Error:", e)


def update_video(id, name, duration):
    try:
        cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, id))
        connection.commit()
        print("Video updated successfully.")
    except Exception as e:
        print("Error:", e)


def delete_video(id):
    try:
        cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
        connection.commit()
        print("Video deleted successfully.")
    except Exception as e:
        print("Error:", e)


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
            break

        else:
            print("Invalid choice")
            continue

    # closing connection after exit
    connection.close()


if __name__ == "__main__":
    main()
