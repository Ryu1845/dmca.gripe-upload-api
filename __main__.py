import requests
from sys import argv


class UploadAPI:
    def __init__(self, api_url: str, file_path: str):
        """
        :param api_url:
        """
        self.api_url = api_url
        self.file_path = file_path

    def __call__(self, file_path):
        self.file_path = file_path

    def __repr__(self):
        return f'<Upload API for {self.api_url}>'

    def get_data(self) -> dict:
        byte_file = open(self.file_path, "rb")
        return_data = {'files[]': byte_file}
        return return_data

    def get_header(self) -> dict:
        headers = {}
        if argv.count("-auth") == 1:
            headers['token'] = ''
        return headers

    def upload(self) -> str:
        response = requests.post(
            self.api_url,
            files=self.get_data(),
            headers=self.get_header()
        )
        return response.text


if __name__ == '__main__':
    file_path = argv[argv.index("-file") + 1]
    upload = UploadAPI("https://dmca.gripe/api/upload", file_path)
    print(upload.upload())
    file_path2 = 'placeholder'
    # upload(file_path2)
    # print(upload.upload())
