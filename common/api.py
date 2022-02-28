class API:

    @staticmethod
    def api_headers(db_access_code='9902403'): #  9905474
        return {
        'content-type': "application/json",
        #'olridentity': db_access_code,
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }
