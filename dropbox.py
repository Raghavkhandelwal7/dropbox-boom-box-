import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root,filename)
            
                relativepath=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relativepath)

                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'Wi9zUronYwkAAAAAAAAAAcfqys7KUMOmGwQ00m5mG3ybXKZtN-Z0nKgMVWi5wQ8W'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the file path to transfer: "))
    file_to = input("Enter the file path to be uploaded to the dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved!!!")

main()
