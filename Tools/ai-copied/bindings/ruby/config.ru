require 'agoo'

Agoo::Server.init(6464, 'root')

class MyHandler
  def call(req)
    [ 200, { }, [ "hello world" ] ]
  end
end

handler = MyHandler.new
Agoo::Server.handle(:GET, "/hello", handler)
Agoo::Server.start()
