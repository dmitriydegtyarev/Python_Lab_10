def create_file():
    try:
        text = ("Студент групи КНдн-35с."
                "\nДігтярьов Дмитро Вікторович."
                "\nУ чому різниця між list і tuple?")

        with open("Lab_10.txt", "w", encoding="utf-8") as file:
            file.write(text)

        # The file will close automatically after exiting the block.

        print("File Lab_10.txt was written")

    except Exception as e:
        print(f"Open file error: {e}")

create_file()