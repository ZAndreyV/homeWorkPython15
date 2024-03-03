import os
import unittest

from get_directory import get_directory_content_info

class TestDirectoryContentInfo(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_directory'
        os.mkdir(self.test_dir)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            pass
        os.mkdir(os.path.join(self.test_dir, 'subdir1'))
        with open(os.path.join(self.test_dir, 'subdir1', 'file2.docx'), 'w') as f:
            pass

    def test_get_directory_content_info(self):
        info = get_directory_content_info(self.test_dir)
        self.assertEqual(len(info), 2)
        self.assertEqual(info[0].name, 'file1')
        self.assertEqual(info[0].extension, 'txt')
        self.assertFalse(info[0].is_directory)
        self.assertEqual(info[0].parent_folder, self.test_dir)
        self.assertEqual(info[1].name, 'subdir1')
        self.assertIsNone(info[1].extension)
        self.assertTrue(info[1].is_directory)
        self.assertEqual(info[1].parent_folder, self.test_dir)

    def tearDown(self):
        os.remove(os.path.join(self.test_dir, 'file1.txt'))
        os.remove(os.path.join(self.test_dir, 'subdir1', 'file2.docx'))
        os.rmdir(os.path.join(self.test_dir, 'subdir1'))
        os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()
