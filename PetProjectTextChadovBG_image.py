import cv2
import numpy as np

# Создание чистого изображения
image = np.zeros((300, 800, 3), dtype="uint8")

# Задаем текст и его позицию
text = "Hello, World!"
text_position = (50, 150)

# Загружаем шрифт и указываем параметры текста
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 2

# Наносим текст на изображение
cv2.putText(image, text, text_position, font, font_scale, (255, 255, 255), font_thickness)

# Применяем эффект размытия к тексту
blurred_image = cv2.GaussianBlur(image, (55, 55), 0)

# Создаем эффект свечения (увеличиваем яркость)
brightened_image = cv2.addWeighted(blurred_image, 1.5, np.zeros(image.shape, image.dtype), 0, 0)

# Добавляем еще один слой текста на размытое изображение
additional_text = "Hello, World!"
additional_text_position = (50, 150)
cv2.putText(brightened_image, additional_text, additional_text_position, font, font_scale, (255, 255, 255), font_thickness)

# Отображаем изображение с добавленным текстом
cv2.imshow("Final Image", brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
