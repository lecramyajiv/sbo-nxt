FPACKAGE = sudo-trinity
VERSION = 1.0

build:

clean:

install:
	mkdir -p /etc
	cp -Rp etc/*  $(DESTDIR)/etc/
	chmod -R 644 $(DESTDIR)/etc
	chmod -R 0440 $(DESTDIR)/etc/sudoers.d/tde-secure-path
