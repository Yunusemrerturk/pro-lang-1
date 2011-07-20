#!/usr/bin/python
# -*- coding: utf-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import *
import os, sys, warnings

warnings.simplefilter("ignore", DeprecationWarning)
from pyPdf import PdfFileWriter , PdfFileReader

def bilgibas(yol, isim):
        liste = os.listdir(yol)
        liste.sort()
        pdf = canvas.Canvas(isim)
        pdf.setTitle(isim)
        pdf.setAuthor('emineker')
        pdf.setSubject(isim)
        
        bilgi = [       'ONDOKUZ MAYIS ÜNİVERSİTESİ',
                        'MÜHENDİSLİK FAKÜLTESİ',
                        'BİLGİSAYAR MÜHENDİSLİĞİ BÖLÜMÜ',
                        raw_input("dönem ve yıl bilgilerinizi şu şekilde giriniz: '2010-2011 » 2. SINIF 1. DÖNEM'    : "), ' ',
                        raw_input("dersin adını şu şekilde giriniz: 'VERİ YAPILARI'                                  : "),
                        'DERS NOTLARI', ' ',
                        raw_input("not sahibini şu şekilde giriniz: 'AYŞE BEGÜM TOPYILDIZ'                           : "), ' ',
                        'DERS ÖĞRETİCİSİ',
                        raw_input("ders hocasının ismini şu şekilde giriniz: 'NURETTİN ŞENYER'                       : ")        ]
        
        registerFont(TTFont('FreeSansBold', "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"))
        pdf.setFont('FreeSansBold', 18)
        cm = 28.3464566929
        x = 21*cm/2.0
        y = 21.5*cm
        for i in bilgi:
                pdf.drawCentredString(x, y, i)
                y-=0.7*cm
        pdf.showPage()

        for i in liste:
                pdf.drawInlineImage(yol+os.sep+i, 30,40, width=500, height=762)
                pdf.showPage()
        pdf.save()

def jpegbas(yol, isim):
        liste = os.listdir(yol)
        liste.sort()
        pdf = canvas.Canvas(isim)
        pdf.setTitle(isim)
        pdf.setAuthor('emineker')
        pdf.setSubject(isim)
        
        for i in liste:
                pdf.drawInlineImage(yol+os.sep+i, 30,40, width=500, height=762)
                pdf.showPage()
        pdf.save()

def pdf_birlestir(yol, isim):
        """aldığı argümanların pdf olup olmadığına bakarak bunları birleştirir"""
        liste = os.listdir(yol)
        liste.sort()
        islem = PdfFileWriter()
        hedef = open(isim, "wb")
        for dosya in liste:
                if os.path.splitext(dosya)[1]=='.pdf':
                        kaynak = PdfFileReader(open(yol+dosya , "rb"))
                        for i in range(kaynak.getNumPages()):
                                islem.addPage(kaynak.getPage(i))
                else:
                        pass
        islem.write(hedef)
        hedef.close()

def kucult(dosya):
        metin="""#!/bin/sh

for f; do
	[ -f $f ] || continue
	gs	-sOutputFile=$f.new \
		-sDEVICE=pdfwrite \
		-dCompatibilityLevel=1.4 $f </dev/null && mv $f.new $f
done"""
        with open('pdf-sh' , 'w') as sh:
                sh.write(metin)
        os.system('chmod +x pdf-sh')
        os.system('./pdf-sh %s' %dosya)
        os.system('chmod -x pdf-sh')
        os.remove('pdf-sh')


def yardim():
        print """
        programı kullanabilmek için aşağıda belirtilen özelliklere dikkat etmelisiniz.
            -j :  argüman olarak verdiğiniz dizindeki tüm jpeg dosyaları
                     sırası ile pdf dosyasına yazar
            -b :  argüman olarak verdiğiniz dizindeki tüm jpeg dosyaları
                     ilk sayfa bilgileri ile pdf'e dosyasına yazar
            -p :  argüman olarak verdiğiniz dizindeki tüm pdf dosyaları
                     sırası ile yeni bir pdf dosyasında birleştirir
        
        örnek olarak

                $ python notlar.py dosya_adı.pdf -b /home/emin/Masaüstü/elektron_devreler/

        UYARI!  dosya yolunu tam girin (bir üst örnekteki gibi)

        kullanımı bu kadar basit kolay gelsin...
        """

if __name__ == "__main__":
        if len(sys.argv)==1:
                yardim()
                sys.exit()
        yol = sys.argv[3]
        isim = sys.argv[1]
        
        arguman = ['-j','-b','-p']
        if len(sys.argv)>3 and sys.argv[2] in arguman and os.path.exists(yol)==True:
                if sys.argv[2]=='-j':
                        jpegbas(yol, isim)
                elif sys.argv[2]=='-b':
                        bilgibas(yol, isim)
                else:
                        pdf_birlestir(yol, isim)
        else:
                yardim()
                sys.exit()
       
        print '\n\tpdf dosyasının boyutunu küçültelim\n'
        kucult(isim)
        print '\n\n\t»» pdf dosyasının boyutu küçültüldü'
        print '\t»» %s dosyası oluşturuldu\n' %isim


