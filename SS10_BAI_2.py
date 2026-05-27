my_playlist = ["Shape of you" , "Binding lights" , "Perfect", "Stay with ME"]
# my_playlist.clear()
while True:
    choice = input("""\n===========MENU QUAN LY DANH SACH PHAT=============
1. Thêm bài hát vào danh sách phát
2. Xem danh sách phát
3. Xóa bài hát khỏi danh sách
4. Sắp xếp và trích xuất danh sách
5. Thoát chương trình
Nhập lựa chọn của bạn : _ """)
    match choice:
        case "1":
            new_song = input("Nhập tên bài hát mới của bạn : ").strip().lower().capitalize()
            if new_song == "":
                print("Không được để trống bài hát")
                continue
            add_choice_input = input("""
====== THÊM BÀI HÁT ====== 
1. Thêm vào cuối danh sách
2. Thêm vào vị trí cụ thể\n
Nhập lựa chon : _ """)
            match add_choice_input:
                    case "1":
                        print(f"Đã thêm bài hát {new_song} vào cuối danh sách!")
                        my_playlist.append(new_song)
                    case "2":
                        index_add_number = input("Hãy chọn chỗ mà bạn muốn chèn vào")
                        if index_add_number.isalpha():
                             print("Vui lòng chọn số")
                             continue
                        elif index_add_number < "0" or index_add_number > str(len(my_playlist)):
                             print(f"Sai phạm vi playlist từ 1 - {len(my_playlist)} ")
                             continue
                        else:
                            index_add_number = int(index_add_number)
                            my_playlist.insert(index_add_number,new_song)
                    case _ :
                      print("Không đúng chức năng ")
        case "2":
            if len(my_playlist) == 0:
                print("Danh sách hiện đang trống")
            else:
                print("---- DANH SÁCH BÀI HÁT ----")
                for index , music in enumerate(my_playlist , start=1):
                    print(f"{index}. {music}")
        case "3":
            delete_choice = input("""
----XÓA BÀI HÁT----
1.Xóa theo tên bài
2.Xóa theo số TT\n""")
            match delete_choice:
                case "1":
                    delete_name_input = input("Nhập tên bài bạn muốn xóa").strip().lower().capitalize()
                    if not delete_name_input in my_playlist:
                        print(f"Bài hát {delete_name_input} không có trong playlist!")
                    else:
                        print(f"Đã xóa bài hát {delete_name_input} !")
                        my_playlist.remove(delete_name_input)
                case "2":
                    delete_index_input = input("Nhập vị trí bài hát bạn muốn xóa")
                    if delete_index_input < "0" or delete_index_input > str(len(my_playlist)):
                        print("Không hợp lệ")
                        continue
                    else:
                        delete_index_input = int(delete_index_input)
                        my_playlist.pop(delete_index_input)
                        print(f"Đã xóa bài hát {delete_index_input + 1} - {my_playlist.pop(delete_index_input)}")
                case _ :
                    print("Vui lòng chọn đúng chức năng")
        case "4":
            list_interaction_input = input("""
-- SẮP XẾP VÀ TRÍCH XUẤT --
1. Sắp xếp danh sách theo bảng chữ cái từ A - Z
2. Hiển thị 3 bài hát đầu tiên """)
            match list_interaction_input:
                case "1":
                    if len(my_playlist) == 0:
                        print("Giờ hiện chưa có bài hát nào")
                    else:
                        print("==== DANH SÁCH ĐÃ ĐƯỢC XẾP ====")
                        sorted_playist = sorted(my_playlist)
                        for index , song_name in enumerate(sorted_playist , start= 1):
                            print(f"{index} - {song_name}")

                case "2":
                    if len(my_playlist) == 0:
                        print("Hiện giờ chưa có bài hát nào")
                    else:
                        print("----- 3 BÀI ĐẦU -----")
                        first_threesongs = my_playlist[:3]
                        for index,song_name in enumerate(first_threesongs, start=1):
                            print(f"{index} - {song_name}")
                case _:
                    print("Vui lòng nhập đúng chức năng")
                    continue
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Chọn đúng chức năng 1- 5")