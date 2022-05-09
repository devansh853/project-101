import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'sl.BHRZlh3CxIzq_NnUv1FEOZmw622pyFbxpN6S42BwrqmFGhySR18bGYk8RmrqnF48ABAbkmX15VBVm7o2I44u68SHzepp3sruTz0bb_1_zLbA5EvvAIxLDggZb62XZqZvwPrco7lB4_pL'
    transferData = TransferData(access_token)
    file_from =input("enter the file path to transfer:-")
    file_to = input('enter the full path to upload to dropbox:-')
    transferData.upload_file(file_from,file_to)
    print('file has been moved')

main()