#!/usr/bin/ruby
# -*- coding: utf-8 -*-

class Tahmin
  def initialize(ilk = 0, son = 1000)
    @ilk = ilk
    @son = son
    @tahmin = nil
  end
  def sayilari_al
    while true
      print 'başlangıç noktasını giriniz:  '
      ilk = gets
      print 'bitiş noktasını giriniz:  '
      son = gets
      if ilk < son
        @ilk = ilk
        @son = son
        break
      else
        puts 'doğru gir şu sayıları'
      end
    end
  end
  def random
    r = Random.new
    @ilk = r.rand(0...500)
    @son = r.rand(501...1000)
  end
  def tahmin_al
    print '> tahmin edin:  '
    @tahmin = gets
  end
  def dogru_mu
    return Integer(@tahmin).between?(@ilk, @son)
  end
  def basla
    while true
      if dogru_mu
        puts "tamam tamam doğru"
        break
      else
        puts "yanlış girdin hacı"
        tahmin_al
      end
    end
  end
  def to_s
    return "aralık: #{@ilk}-#{@son}"
  end
end

if __FILE__ == $0
  tahmin = Tahmin.new()
  #tahmin.sayilari_al
  tahmin.random
  tahmin.tahmin_al
  tahmin.basla
  puts tahmin
end
