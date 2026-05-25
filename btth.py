
raw_input = "   nGuyen vaN aN  ;  2004   "
while True:
    print("===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa Họ tên và tính Tuổi")
    print("3. Tạo Mã ID và Email tự động")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn: ")
    match choice:

        case "1":

            print("\nDữ liệu gốc:")
            print(raw_input)

        case "2":
            info = raw_input.split(";")
            full_name = info[0].strip().title()
            birth_year = info[1].strip()
            age = 2026 - int(birth_year)

            print("\n===== THÔNG TIN THÀNH VIÊN =====")
            print("Họ tên:", full_name)
            print("Tuổi:", age)
        case "3":
            info = raw_input.split(";")
            full_name = info[0].strip().title()
            birth_year = info[1].strip()
            name_parts = full_name.split()
            last_name = name_parts[0]
            middle_name = name_parts[1]
            first_name = name_parts[2]
            email = (
                last_name[0]
                + middle_name[0]
                + first_name
            ).lower() + "@company.com"
            member_id = first_name.upper() + birth_year[-2:]
            print("===== THẺ THÀNH VIÊN =====")

            print("Họ tên :", full_name)
            print("Email  :", email)
            print("Mã ID  :", member_id)
        case "4":
            print("Tạm biệt")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")