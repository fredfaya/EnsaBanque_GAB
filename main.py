from images.backend_functions import DataManager

api_url = 'https://gmail.googleapis.com/$discovery/rest?version=v1'

dataManager = DataManager(api_url)
dataManager.getData()