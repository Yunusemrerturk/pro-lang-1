using System;
using System.IO;

/*
 * ilginç bir nesne yönelimli ödevi
 * verilen kaynak dosyaların öncesinde ölçülmüş değerleri için
 * istenilen taglar ile kontrol edilip oluşturulmuş ölçüye
 * uyup uymama probleminin çözümüdür
 */

namespace uzay {
	public class Stack {
		public int k = 0; 	// dizinin kaç elemanı olduğunu tutan değişken
		public string[] liste;  // liste'mizin türünü ve erişimini tanımlayalım

		public Stack(int a) {
			liste = new string[a];
		}
		public bool IsEmpty() {
			if (k == 0)
				return true;
			return false;
		}
		public int Push(string b) {
			if (liste[liste.Length-1] == null) {
				liste[k] = b;
				return k++;
			}
			return -1;
		}
		public string Peek() {
			if (k == 0)
				return null;
			return liste[k-1];
		}
		public string Pop() {
			if (k == 0)
				return null;
			string don = liste[k-1];
			liste[--k] = "";
			return don;
		}
	}

	public class kontrol {
		public string okunan;
		public int uzunluk;
		public kontrol(string dosya) {
			StreamReader sr = new StreamReader(dosya);
			okunan = sr.ReadToEnd();
			sr.Close();
			uzunluk = okunan.Length;
		}
		public bool checker() {
			Stack s = new Stack(uzunluk/3);
			bool balanced = true;
			int i = 0;
			while (i < uzunluk && balanced) {
				if ((okunan[i] == '<') && (okunan[i+1] != '/')) {
					s.Push(okunan[i+1].ToString());
					i+=3;
				}

				else if ((okunan[i] == '<') && (okunan[i+1] == '/')) {
					if (s.IsEmpty())
						balanced = false;
					else {
						if (s.Pop() != okunan[i+2].ToString())
							balanced = false;
					}
					i+=4;
				}
				else
					i++;
			}
			if (balanced && s.IsEmpty())
				return true;
			return false;
		}
		public string yaz() {
			string son = "";
			int x = 0, y = 0, i = 0, u = 0, b = 0;
			// burada <h> tagından kurtulalım nasıl olsa ekrana yazdırmayacaz
			while (true) {
				x = okunan.IndexOf("<h>");
				y = okunan.IndexOf("</h>");
				if (x < 0)
					break;
				okunan = okunan.Substring(0, x-1) + okunan.Substring(y+4);
			}

			while (i < okunan.Length)			{
				if ((okunan[i] == '<') && (okunan[i+1] != '/')) {
					if (okunan[i+1] == 'b')
						b = 1;
					else if (okunan[i+1] == 'u')
						u = 1;
					else if (okunan[i+1] == 'p')
						if (b == 1)
							son += "[[";
						else
							son += "[";
					i = i + 3;
				}
				else if ((okunan[i] == '<') && (okunan[i+1] == '/')) {
					if (okunan[i + 2] == 'b')
						b = 0;
					else if (okunan[i+2] == 'u')
						u = 0;
					else if (okunan[i+2] == 'p')
						if (b == 1){
							son += "]]";
						}
						else
							son += "]";
					i = i + 4;
				}
				else {
					if (b == 1){
						if (u == 1)
							son += okunan[i].ToString().ToUpper() + okunan[i].ToString().ToUpper();
						else
							son += okunan[i].ToString() + okunan[i].ToString();
					}
					else if (u == 1)
						son += okunan[i].ToString().ToUpper();
					else
						son += okunan[i];
					i++;
				}
			}
			return son;
		}
	}

	class Program {
		static void Main() {
			kontrol sonuc = new kontrol("kaynak.txt");
			if (sonuc.checker() == true)
				Console.WriteLine(sonuc.yaz());
			else
				Console.WriteLine("Kaynak dosyanin bicimleme etiketleri hatalidir, kontrol ediniz.");
			Console.ReadLine(); // bu sizin için hocam...
		}
	}
}

