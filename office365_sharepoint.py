import os
import environ
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

# env = environ.Env()
# environ.Env.read_env()
#
# SHAREPOINT_CLIENT_ID = env('sharepoint_client_id')
# SHAREPOINT_SECRET_ID = env('sharepoint_secret_id')
# SHAREPOINT_SITE = env('sharepoint_url_site')
# SHAREPOINT_SITE_NAME = env('sharepoint_site_name')
# SHAREPOINT_DOC = env('sharepoint_doc_library')

class Sharepoint:

    def __int__(self):
        self.env = environ.Env()
        self.environ.Env.read_env()

        self.SHAREPOINT_CLIENT_ID = self.env('sharepoint_client_id')
        self.SHAREPOINT_SECRET_ID = self.env('sharepoint_secret_id')
        self.SHAREPOINT_SITE = self.env('sharepoint_url_site')
        self.SHAREPOINT_SITE_NAME = self.env('sharepoint_site_name')
        self.SHAREPOINT_DOC = self.env('sharepoint_doc_library')

    def _auth(self):
        client_credentials = ClientCredential(self.SHAREPOINT_CLIENT_ID, self.SHAREPOINT_SECRET_ID)
        conn = ClientContext(self.SHAREPOINT_SITE).with_client_certificate(
            client_credentials)
        return conn

    def _get_files_list(self, folder_name):
        conn = self._auth()
        target_folder_url = f'{self.SHAREPOINT_DOC}/{folder_name}'
        root_folder = conn.web.get_folder_by_server_relative_url(target_folder_url)
        root_folder.expand(["Files", "Folders"]).get().execute_query()
        return root_folder.files

    def download_file(self, file_name, folder_name):
        conn = self._auth()
        file_url = f'/sites/{self.SHAREPOINT_SITE_NAME}/{self.SHAREPOINT_DOC}/{folder_name}/{file_name}'
        file = File.open_binary(conn, file_url)
        return file.content

    def download_files(self, folder_name):
        _files_list = self._get_files_list(folder_name)
        return _files_list;




