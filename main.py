from Drivers.ImageModelDriver import *
from Drivers.ImageDisplayDriver import *
from Models.SPDImage import *

# Загружаем фото
loaded_image = SPDImage('photo/', 'photo', '.jpg')

# Обрабатываем
ImageModelDriver.add_shift(loaded_image, 30)
ImageDisplayDriver.save(loaded_image)

ImageModelDriver.multi_shift(loaded_image, 1.3)
ImageDisplayDriver.save(loaded_image)

# Вывод результата
ImageModelDriver.anti_shift(loaded_image)
ImageDisplayDriver.save(loaded_image)