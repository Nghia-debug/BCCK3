def nhapcauhoi_tracnghiem():
    cau=["A",'B','C','D','E']
    cauhoi=input("Nhập câu hỏi: ")
    soluong=input('Nhập số lượng câu trả lời(Tối đa 5): ')
    while int(soluong) <=0 or soluong.isnumeric()!= True:
        soluong=input('Vui lòng nhập lại số lượng câu trả lời: ')
    for i in range(1,int(soluong)+1):
        cautraloi=input(f'Nhập câu trả lời cho câu {cau[i-1]}: ')

nhapcauhoi_tracnghiem()
        