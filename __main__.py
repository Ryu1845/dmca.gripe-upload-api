import requests
from sys import argv


class UploadAPI:
    def __init__(self, api_url: str):
        """
        :param api_url:
        """
        self.api_url = api_url

    def __repr__(self):
        return f'<Upload API for {self.api_url}>'

    def get_data(self, file_path: str) -> dict:
        byte_file = open(file_path, "rb")
        return_data = {'files[]': byte_file}
        return return_data

    def get_header(self) -> dict:
        headers = {}
        if argv.count("-auth") == 1:
            headers['token'] = ''
        return headers

    def upload(self, file_path: str) -> str:
        response = requests.post(
            self.api_url,
            files=self.get_data(file_path),
            headers=self.get_header()
        )
        return response.text


if __name__ == '__main__':
    file_path = argv[argv.index("-file") + 1]
    upload = UploadAPI("https://dmca.gripe/api/upload")
    print(upload.upload(file_path))
