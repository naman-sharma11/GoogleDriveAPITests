import os
import sys
sys.path.append("../")
import unittest

from scripts.drive_operation import GoogleApiTest


class DriveAPITest(unittest.TestCase):
    def setUp(self):
        self.main_class = GoogleApiTest()

    def test_a_drive_not_empty(self):
        status, result = self.main_class.list_files()
        self.assertTrue(status)

    def test_b_upload_test_jpeg_file(self):
        filename, filepath, mimetype = 'EiffelTower_TestImage.jpg', 'EiffelTower_TestImage.jpg', 'image/jpeg'
        upload = self.main_class.upload_file(filename, filepath, mimetype)
        self.assertTrue(upload)

    def test_c_file_exists_in_drive(self):
        result = self.main_class.search_file("name contains 'EiffelTower_TestImage.jpg'")
        self.assertTrue(result)

    def test_d_download_image_file(self):
        source_file_name = 'EiffelTower_TestImage.jpg'
        destination_file_name = 'Downloaded_EiffelTower_TestImage.jpg'
        file_check = os.path.exists(destination_file_name)
        if file_check:
            os.remove(destination_file_name)
            file_id = self.main_class.search_file('name contains "{}"'.format(source_file_name))
            if file_id is not None:
                result = self.main_class.download_files(file_id, destination_file_name)
                self.assertTrue(result)
            else:
                self.assertIsNotNone(file_id)
        else:
            file_id = self.main_class.search_file('name contains "{}"'.format(source_file_name))
            if file_id is not None:
                result = self.main_class.download_files(file_id, destination_file_name)
                self.assertTrue(result)
            else:
                self.assertIsNotNone(file_id)

    def test_e_delete_file_from_drive(self):
        file_name = 'EiffelTower_TestImage.jpg'
        file_id = self.main_class.search_file('name contains "{}"'.format(file_name))
        if file_id is not None:
            result = self.main_class.delete_file(file_id, file_name)
            self.assertTrue(result)
        else:
            self.assertIsNotNone(file_id)


if __name__ == '__main__':
    unittest.main()
