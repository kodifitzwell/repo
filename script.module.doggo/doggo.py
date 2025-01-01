import json, sys
from urllib import parse, request
import xbmcgui, xbmcplugin
import pyxbmct

timeout = 2
QUOTEE, URL = 'Dog API', 'https://dog.ceo/dog-api/'
base_url = 'https://dog.ceo/api/breeds/image/random'
headers = {'User-Agent': 'Mozilla/5.0'}

class Doggo(pyxbmct.AddonDialogWindow):

	def __init__(self, title=''):
		super(Doggo, self).__init__(title)
		self.setGeometry(300, 280, 5, 2)
		self.set_controls()
		self.set_navigation()
		self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
		self.refresh()

	def set_controls(self):
		self.image = pyxbmct.Image('', aspectRatio=2)
		self.placeControl(self.image, 0, 0, rowspan=3, columnspan=2)
		label = pyxbmct.Label(f"- {QUOTEE}  ", alignment=2)
		self.placeControl(label, 3, 0, columnspan=2)
		self.close_button = pyxbmct.Button('Close')
		self.placeControl(self.close_button, 4, 0)
		self.connect(self.close_button, self.close)
		self.refresh_buton = pyxbmct.Button('Refresh')
		self.placeControl(self.refresh_buton, 4, 1)
		self.connect(self.refresh_buton, lambda: self.refresh())

	def set_navigation(self):
		self.close_button.controlRight(self.refresh_buton)
		self.refresh_buton.controlLeft(self.close_button)
		self.setFocus(self.refresh_buton)

	def refresh(self):
		req = request.Request(base_url, headers=headers)
		response = request.urlopen(req, timeout=timeout)
		image = json.loads(response.read())['message']
		self.image.setImage(image)

if __name__ == '__main__':
	handle = int(sys.argv[1])
	try: params = dict(parse.parse_qsl(sys.argv[2][1:]))
	except: params = {}

	if not 'action' in params:
		url = 'plugin://script.module.doggo/?action=doggo'
		listitem = xbmcgui.ListItem('Dog API')
		xbmcplugin.addDirectoryItem(handle, url, listitem, False)
		xbmcplugin.endOfDirectory(handle)
	else:
		doggo = Doggo(URL)
		doggo.doModal()
		del doggo
