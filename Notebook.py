import json

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = {"title": title, "content": content}
    return note

def save_note(note):
    with open("notes.json", "a") as file:
        json.dump(note, file)
        file.write('\n')

def view_notes():
    with open("notes.json", "r") as file:
        notes = file.readlines()
        for note in notes:
            note = json.loads(note)
            print(f"Title: {note['title']}")
            print(f"Content: {note['content']}")
            print("-----------------------------------")

def main():
    while True:
        print("1. Create a new note")
        print("2. View existing notes")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Note saved successfully!")
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print('Thank you for choosing rbyAI Inc.')
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()