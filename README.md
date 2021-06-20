# GoogleDriveAPITests
## Introduction
This is a Google Drive API Test project written in Python. The script is capable of performing operations such as **List, Upload, Download and Delete Files** to/from the Google Drive. 

## Prerequisites
To start the script execution, following prerequisites needs to be fulfilled.
- Download the script and place it in your local disk
- Refer to [Google Drive Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python#prerequisites) to fulfill the prerequisites mentioned.
- At the step of Creating Credentials, script is made for app type [Create Desktop application credentials](https://developers.google.com/workspace/guides/create-credentials#desktop)
- Place the client secret json file inside the **files** directory of the project and name it as **client_secret.json**.

## Script Overview
Script comprises of 3 directories and 1 main file, contents are as below-
- Directory **files**- This directory contains the files needed for execution. client_secret.json is the credentials file and token.json will be generated at runtime when the script is triggered. It will ask for sign in to Google account and once Authorization Flow is completed, a token.json file will be generated.
- Directory **scripts**- This directory contains the file drive_operation.py. This file is responsible to execute whole operations on Google Drive. It has few functions defined which are called and executed at some point of time.
- Directory **tests**- This directory contains the file related to test cases. It has drive_unittest.py file which have the testcases defined in it. It has a suite file testing_suite.py which needs to be run whenever we needed to run our test cases. One dummy image file named **EiffelTower_TestImage.jpg** is also present which is used to perform operations on Google Drive.
- **main.py** file- Running this file will list all the files available in the Gooogle Drive. The list of files will be presented with Pretty Table with File ID and its Name. Script will take the inputs from user to start the download of the respective file. It will keep on taking user input until user presses n/no as input.

## About Test Cases
Details about few test cases:
1. **test_a_drive_not_empty**- This test case checks if the Google Drive is empty or not. If the Drive is empty, assertTrue will fail.
2. **test_b_upload_test_jpeg_file**- This test case will upload the **EiffelTower_TestImage.jpg** to Google Drive, which will be further used in 4th test case.
3. **test_c_file_exists_in_drive**- This test case will check if the uploaded file is available in Google Drive or not.
4. **test_d_download_image_file**- This test case will download the file uploaded in Test Case 2, new file will be downloaded with name as **Downloaded_EiffelTower_TestImage.jpg**.
5. **test_e_delete_file_from_drive**- This test case will delete file uploaded in Test Case 2.

## Results of Test Cases
1. Initially there are no files present in Google Drive

![image](https://user-images.githubusercontent.com/86096830/122666652-453b9b80-d1cc-11eb-9d63-d9b3490f2cf6.png)

2. I have skipped Test Case 5, to showcase the uploaded file. Running the test suite now

![image](https://user-images.githubusercontent.com/86096830/122666813-2984c500-d1cd-11eb-9009-4bcd141b367a.png)

As part of Test case 4, file is also downloaded

![image](https://user-images.githubusercontent.com/86096830/122667034-54bbe400-d1ce-11eb-9cad-acc5f388e4d9.png)

3. Checking the Google Drive if file is uploaded or not.

![image](https://user-images.githubusercontent.com/86096830/122666852-62bd3500-d1cd-11eb-9e2d-3d3a4bf3ce33.png)

4. Since the file is uploaded, now running only Test Case 5 to delete the file from Drive.

![image](https://user-images.githubusercontent.com/86096830/122667050-74530c80-d1ce-11eb-8588-ada7208913c4.png)

5. The file is deleted from Google Drive as well

![image](https://user-images.githubusercontent.com/86096830/122666913-add74800-d1cd-11eb-8d56-0c48c03b430d.png)

## About main.py file results
I have uploaded 6 files in Google Drive.

![image](https://user-images.githubusercontent.com/86096830/122667095-b67c4e00-d1ce-11eb-95fb-8a7db9e698d8.png)

Now running main.py file.

![image](https://user-images.githubusercontent.com/86096830/122667199-373b4a00-d1cf-11eb-9ffb-bc1bb8381fb1.png)

Files downloaded after execution

![image](https://user-images.githubusercontent.com/86096830/122667226-59cd6300-d1cf-11eb-8feb-ee8fe627e8ec.png)
