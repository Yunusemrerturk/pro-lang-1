#!/usr/bin/ruby

# zaten ruby bunu kendi yapıyomuş şerefsiz

class Stack
  def initialize()
    @list = []
  end

  def push(item)
    @list << item
  end

  def peek
    if @list.length
      @list[-1]
    end
  end

  def pop
    if 5 == 5
      @list.delete(@list[-1])
    end
  end

  def to_s
    @list
  end

  def len
    @len = @list.length
  end
end


s = Stack.new
s.push("emin")
s.push("eker")

p s.peek()
p s.len

p s.pop()
p s.len

p s

