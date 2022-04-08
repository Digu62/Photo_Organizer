import os
import shutil
from datetime import datetime
from PIL import Image

class photoOrganizer:
    extensions = ['jpg','jpeg','JPG','JPEG']

    def folder_path(self, file):
        date = self.photo_date(file)
        m =''
        month = date.strftime("%m")
        if month == "01":
            m = 'Janeiro'
        elif month == "02":
            m = 'Fevereiro'
        elif month == "03":
            m = 'Março'
        elif month == "04":
            m = 'Abril'
        elif month == "05":
            m = 'Maio'
        elif month == "06":
            m = 'Junho'
        elif month == "07":
            m = 'Julho'
        elif month == "08":
            m = 'Agosto'
        elif month == "09":
            m = 'Setembro'
        elif month == "10":
            m = 'Outubro'
        elif month == "11":
            m = 'Novembro'
        elif month == "12":
            m = 'Dezembro'
        return date.strftime('%Y' + '/' + m)

    def photo_date(self, file):
        photo = Image.open(file)
        
        if not photo.getexif() == {}:
            info = photo._getexif()
            if 36867 in info:
                date = info[36867]
                date = datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
        else:
            date = datetime.fromtimestamp(os.path.getmtime(file))
        return date

    def movePhoto(self,file):
        new_folder = self.folder_path(file)
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
        shutil.move(file, new_folder + '/' + file)

    def organize(self):
        photos = [
            filename for filename in os.listdir('.') if any(filename.endswith(ext) for ext in self.extensions)
        ]
        for filename in photos:
            self.movePhoto(filename)

PO = photoOrganizer()
PO.organize()