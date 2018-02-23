# @author Shubham Agrawal <shubham.agrawal.8025@gmail.com>

from WatermarkSizes import WatermarkSizes
from PIL import Image


class ImageWatermark:
    __image_path = ""
    __watermark_image_path = ""
    __horizontal_offset = 0
    __vertical_offset = 0

    def __init__(self, img_path, wm_img_path):
        self.__image_path = img_path
        self.__watermark_image_path = wm_img_path
        self.original_image = Image.open(self.__image_path, "r")
        self.watermark_image = Image.open(self.__watermark_image_path, "r")

    def get_watermarked_image(self, size_mode):
        self.__set_images_sizes()
        self.convert_images_to_alpha_mode()

        __lower_x = self.__img_rows - self.__vertical_offset
        __lower_y = self.__img_cols - self.__horizontal_offset
        __upper_x = self.__img_rows - (size_mode[0] + self.__vertical_offset)
        __upper_y = self.__img_cols - (size_mode[1] + self.__horizontal_offset)
        __box = (__upper_x, __upper_y, __lower_x, __lower_y)

        self.watermark_image = self.watermark_image.resize(size_mode)
        self.watermark_image.putalpha(150)

        self.original_image.paste(self.watermark_image, __box, self.watermark_image)
        return self.original_image

    def set_offsets(self, h_offset, v_offset):
        if h_offset >= 0:
            self.__horizontal_offset = h_offset
        if v_offset >= 0:
            self.__vertical_offset = v_offset

    def __set_images_sizes(self):
        self.__img_rows, self.__img_cols = self.original_image.size
        self.__wm_rows, self.__wm_cols = self.watermark_image.size

    def convert_images_to_alpha_mode(self):
        self.watermark_image = self.watermark_image.convert("RGBA")
        self.original_image = self.original_image.convert("RGBA")


if __name__ == '__main__':
    img_wm = ImageWatermark("path/to/image", "path/to/watermark")

    # customizable
    img_wm.set_offsets(100, 100)

    # Use Enums like X_SMALL, SMALL, MEDIUM, LARGE, X_LARGE
    # Can also give different size tuple (x, y)
    output = img_wm.get_watermarked_image(WatermarkSizes.X_LARGE.value)

    # show the output
    output.show()
