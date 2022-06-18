import requests
from auxiliary import Auxiliary
from config import INDIGO_TOKEN
import random


class Indigo:
    """This class allows us get all info which we need from profile in Indigo Browser"""

    def __init__(self, token, port):
        self.token = token
        self.port = port

    def get_profiles(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'token': self.token,
        }
        response = requests.get(
            'https://indigo.multiloginapp.com/clb/rest/v1/t/50a38c97-c687-349b-872c-4eb2945b47ae/'
            'm/7b2ff325-d481-373d-8059-9972a81b5d69/p', headers=headers)

        return response.json()

    def get_profile_info(self, uuid):
        headers = {
            'token': self.token
        }
        json_data = {
            'sid': '00000000-0000-0000-0000-000000000000'
        }

        response = requests.post(f'http://127.0.0.1:{self.port}/clb/p/{uuid}',
                                 headers=headers, json=json_data)
        result = response.json()

        return {
            'name': result['name'],
            'notes': Auxiliary(result).get_notes(),
            'useragent': result['container']['navUserAgent'],
            'proxy': Auxiliary(result).get_proxy(proxy_type=Auxiliary(result).get_proxy_type()),
            'group_name': Auxiliary(result).get_group_name(INDIGO_TOKEN),
            'platform': Auxiliary(result).get_platform(),
            'webgl_vendor': result['container']['webGlVendor'],
            'webgl_renderer': result['container']['webGlRenderer'],
            'webgl2Maximum': Auxiliary(result).get_webgl2maximum(),
            'cpu_cores': result['container']['navigator']['hardwareConcurrency'],
            'screen_resolution': f"{result['container']['scrWidth']}x{result['container']['scrHeight']}",
            'audio_inputs': result['mediaDevicesAudioInputs'],
            'video_inputs': result['mediaDevicesVideoInputs'],
            'audio_outputs': result['mediaDevicesAudioOutputs'],
        }


class Dolphin:
    def __init__(self, token):
        self.token = token

    def create_profile(self, data):
        headers = {
            'Authorization': self.token,
        }

        json_data = {
            'name': data['name'],
            'tags': [
                data['group_name']
            ],
            'platform': data['platform'],
            'browserType': 'anty',
            'mainWebsite': '',
            'useragent': {
                'mode': 'manual',
                'value': data['useragent'],
            },
            'webrtc': {
                'mode': 'altered',
                'ipAddress': None,
            },
            'canvas': {
                'mode': 'real',
            },
            'webgl': {
                'mode': 'real',
            },
            'webglInfo': {
                'mode': 'manual',
                'vendor': data['webgl_vendor'],
                'renderer': data['webgl_renderer'],
                'webgl2Maximum': data['webgl2Maximum'],
            },
            'clientRect': {
                'mode': 'real',
            },
            'notes': {
                'content': data['notes'],
                'color': 'blue',
                'style': 'text',
                'icon': None,
            },
            'timezone': {
                'mode': 'auto',
                'value': None,
            },
            'locale': {
                'mode': 'auto',
                'value': None,
            },
            'proxy': data['proxy'],
            'statusId': 0,
            'geolocation': {
                'mode': 'auto',
                'latitude': None,
                'longitude': None,
                'accuracy': None,
            },
            'cpu': {
                'mode': 'manual',
                'value': data['cpu_cores'],
            },
            'memory': {
                'mode': 'manual',
                'value': random.choice([2, 4, 8]),
            },
            'screen': {
                'mode': 'manual',
                'resolution': data['screen_resolution'],
            },
            'mediaDevices': {
                'mode': 'manual',
                'audioInputs': data['audio_inputs'],
                'videoInputs': data['video_inputs'],
                'audioOutputs': data['audio_outputs'],
            },
            'ports': {
                'mode': 'protect',
                'blacklist': '3389,5900,5800,7070,6568,5938',
            },
            'doNotTrack': False,
            'args': [],
            'platformVersion': '10.13.6',
            'login': '',
            'password': '',
            'appCodeName': 'Mozilla',
            'platformName': 'MacIntel',
            'connectionDownlink': 10,
            'connectionEffectiveType': '4g',
            'connectionRtt': 50,
            'connectionSaveData': 0,
            'cpuArchitecture': '',
            'osVersion': '10.13.6',
            'vendorSub': '',
            'productSub': '20030107',
            'vendor': 'Google Inc.',
            'product': 'Gecko',
        }

        response = requests.post('http://142.132.182.77:81/browser_profiles', headers=headers, json=json_data)

        return response.json()
