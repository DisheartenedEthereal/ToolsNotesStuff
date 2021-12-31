keyem = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
p keyem.join("")


puts "-"*50


def sveditabales()

  return (1..32).step(2).to_a
end
puts sveditabales().count()
def cleditabales()
  return (0..32).step(2).to_a
end
puts "-"*50
puts cleditabales().count()


for i in sveditabales()
  keyem[i] = 1
end
for i in cleditabales
  keyem[i] = 1
end

puts keyem
