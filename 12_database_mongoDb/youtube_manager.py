from pymongo import MongoClient
from bson import ObjectId

db_name = "yt-manager"
db_url = "mongodb+srv://shivamsingh175503:Shivam123@cluster0.gscplb5.mongodb.net"

try:
    client = MongoClient(db_url)
    db = client[db_name]
    video_collection = db["videos"]
except Exception as e:
    print("Database Connection Error:", e)
    exit()

def add_video(name, time):
    try:
        video_collection.insert_one({"name": name, "time": time})
        print("Video added successfully.")
    except Exception as e:
        print("Error:", e)

def list_all_videos():
    try:
        for video in video_collection.find():
            print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")
    except Exception as e:
        print("Error:", e)

def update_video(id, name, time):
    try:
        video_collection.update_one(
            {'_id': ObjectId(id)}, 
            {'$set': {"name": name, 'time': time}}
        )
        print("Video updated successfully.")
    except Exception as e:
        print("Error:", e)

def delete_video(id):
    try:
        video_collection.delete_one({'_id': ObjectId(id)})
        print("Video deleted successfully.")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Remove a video")
        print("5. Exit App")
        choice = input("Enter your option: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter Video Name: ")
            time = input("Enter Video Time: ")
            add_video(name, time)
        elif choice == '3':
            id = input("Enter Video Id to update: ")
            name = input("Enter Updated Video Name: ")
            time = input("Enter Updated Video Time: ")
            update_video(id, name, time)   
        elif choice == '4':
            id = input("Enter Video Id to delete: ")
            delete_video(id)
        elif choice == '5':
            exit()
        else:
            print("Invalid Option!! Please enter again.")

if __name__ == '__main__':
    main()
