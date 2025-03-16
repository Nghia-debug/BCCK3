khoi_verify=[range(6,11)]
lop_monhoc_verify=[["10A7","Giang","Hóa"]]
class lop:
    def __init__(self,khoi,lophoc,mon):
        self.khoi=khoi
        self.lophoc=lophoc
        self.mon=mon

    def lopcheck(self):
        for i in lop_monhoc_verify:
            if self.khoi:
                if self.mon in i:
                    return f"Chào mừng ... dạy môn {self.mon}"
                




                