import unittest

from tests.drive_unittest import DriveAPITest

test_classes_to_run = [DriveAPITest]
loader = unittest.TestLoader()
suites_list = []
for test_class in test_classes_to_run:
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

main_suite = unittest.TestSuite(suites_list)
runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(main_suite)
