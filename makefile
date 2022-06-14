INSTALL_PATH = /usr/local
BIN_PATH=/usr/local/bin

.PHONY: build
build: clean
	test -d venv || python3 -m venv venv
	. venv/bin/activate; python3 -m pip install --upgrade pip; python3 -m pip install -Ur requirements.txt
	mkdir -p $(INSTALL_PATH)/em
	cp -R venv $(INSTALL_PATH)/em
	cp -R src $(INSTALL_PATH)/em
	cp empy $(BIN_PATH)

.PHONY: clean
clean:
	-deactivate
	-rm $(BIN_PATH)/empy
	-rm $(INSTALL_PATH)/em
	-rm -rf venv
	find . -iname "*.pyc" -delete