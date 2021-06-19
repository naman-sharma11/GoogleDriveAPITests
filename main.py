from scripts import drive_operation


def main():
    print('Listing files from Drive')
    drive = drive_operation.GoogleApiTest()
    files_present, response = drive.list_files()
    download = False
    if files_present:
        download = True
        print('Files Found')
        print(response)
    else:
        if response is None:
            print('No Files Found')
        else:
            print('Exception occurred in listing Files - {}'.format(response))
        print('Exiting')
    while download:
        file_download = drive.download_files(input('Enter File ID:'), input('Enter Downloaded File Name:'))
        if file_download:
            print('Download successful')
        else:
            print('Download Failed')
        if 'y' not in str(input('Enter (Yes/No) or (Y/N) to download more:')).lower():
            print('Exiting')
            download = False


if __name__ == '__main__':
    main()
