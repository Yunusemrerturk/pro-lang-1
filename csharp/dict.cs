using System;

/*
 * Nesne yönelimli programlamanın inceliklerini kullanarak
 * ascii karakterler üzerinden oluşturulan bir sözlük yapısı
 */

namespace uzay {
        public class Node {
                public string val = null;
                public Node[] list;
        }
        public class KelimeAgaci {
                public Node root;
                public string[] dizi;
                Node[] takas;
                int i = 0;
                public KelimeAgaci() {
                        root = new Node();
                        root.list = new Node[26];
                }

                public int find(char x) {
                        return Convert.ToInt16(x)-97;
                }

                public void KelimeEkle(string key, string val) {
                        takas = root.list;
                        foreach (char x in key) {
                                i = find(x);
                                if (takas[i] == null) {
                                        takas[i] = new Node();
                                        takas[i].list = new Node[26];
                                        takas = takas[i].list;
                                }
                                else
                                        takas = takas[i].list;
                        }
                        try {
                                takas[i].val = takas[i].val + ";" + val;
                        }
                        catch {
                                takas[i] = new Node();
                                takas[i].list = new Node[26];
                                takas[i].val = val;
                        }
                }
                public string AnlamBul(string key) {
                        takas = root.list;
                        foreach (char x in key) {
                                i = find(x);
                                if ((takas[i] != null))
                                        takas = takas[i].list;
                                else
                                        return "[kelime bulunamadi]";
                        }
                        if (takas[i].val == "$")
                                return "[bu kelime daha once silinmis]";
                        else
                                return takas[i].val;
                }
                public void KelimeSil(string key) {
                        takas = root.list;
                        foreach (char x in key) {
                                i = find(x);
                                if ((takas[i] != null))
                                        takas = takas[i].list;
                        }
                        takas[i].val = "$";
                }
        }

        class Program {
                static void Main() {
                        KelimeAgaci sozluk = new KelimeAgaci();
                        sozluk.KelimeEkle("legal", "yasal");
                        sozluk.KelimeEkle("leg", "bacak");
                        sozluk.KelimeEkle("a", "bir");
                        sozluk.KelimeEkle("legend", "efsane");
                        sozluk.KelimeEkle("leg", "dik kenar");
                        Console.WriteLine("leg : {0}", sozluk.AnlamBul("leg"));
                        Console.WriteLine("bell : {0}", sozluk.AnlamBul("bell"));
                        Console.WriteLine("a : {0}", sozluk.AnlamBul("a"));
                        Console.WriteLine("legend : {0}", sozluk.AnlamBul("legend"));
                        Console.WriteLine("legal : {0}", sozluk.AnlamBul("legal"));
                        Console.WriteLine("paper : {0}", sozluk.AnlamBul("paper"));
                        sozluk.KelimeSil("legal");
                        Console.WriteLine("legal : {0}", sozluk.AnlamBul("legal"));
                        Console.ReadLine();
                }
        }
}

