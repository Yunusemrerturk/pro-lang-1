#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# konsoldan alınan ergümanları listeler
sys.argv

# programın o noktada sonlanmasını sağlar
sys.exit()

# betiğin dil kodlaması
sys.getdefaultencoding()

# python'a ait path bilgileri
sys.path

#path'de istediğin noktaya yol ekle
sys.path.append("/herhangi/bir/dizin")
sys.path.insert(0, "/herhangi/bir/dizin")

# kullandığınız işletim sistemi bilgisi
sys.platform

# işletim sisteminin mimarisi
import platform
platform.architecture()

# python sürümü hakkında bilgi verir
sys.version_info

# satır atlamadan arka arkaya ekrana yazı yazdırır
for i in 'emineker':
    sys.stdout.write(str(i))
    sys.stdout.flush()

# print fonksiyonunu yönlendirme
dosya = open("log.txt", "w")
sys.stdout = dosya
print "Yeni bir mesajınız var!"
dosya.close()

# print komutunu orjinaline döndürelim
sys.stdout = sys.__stdout__





