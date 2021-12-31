require 'socket'        # Sockets are in standard library

#hostname = 'localhost'
#port = 2000

#s = TCPSocket.open(hostname, port)

#while line = s.gets     # Read lines from the socket
#   puts line.chop       # And print with platform line terminator
#end
#s.close                 # Close the socket when done
lsc = []
class Term
  attr_accessor :width, :height, :datatypes
  
  def initialize(width,height,exist=false)
    @width = width
    @height = height
    @exist = exist
  end

  def clear()
    system("clear")
  end
end
class Screen < Term
  attr_accessor :pixelsused
  def initialize(width,height,datatypes=false,pixelsused)
    @pixelsused = pixelsused
    super(width,height,datatypes)
  end
  def balancepixels(pix)
    lsc << pix 
  end
  def countpix()
    return lsc.inject(0, :+)
  end
end
terminal = Screen.new(55,88,true,55)

p terminal.countpix()
