.PHONY: build-linux build-macos build-windows rebuild clean

build-macos:
	pyinstaller --onefile --windowed --icon=icon.icns --name "Offer_Prompt_Generator" --add-data "profile.json:." gui_interface.py

build-linux:
	pyinstaller --onefile --windowed --icon=icon.ico --name "Offer_Prompt_Generator" --add-data "profile.json:." gui_interface.py

build-windows:
	pyinstaller --onefile --windowed --icon=icon.ico --name "Offer_Prompt_Generator" --add-data "profile.json;." gui_interface.py

rebuild:
	pyinstaller Offer_Prompt_Generator.spec

clean:
	rm -rf build dist MonApp.spec
