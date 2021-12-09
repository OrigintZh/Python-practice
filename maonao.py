class Pet:
    
    def __init__ (self,n,h):
        self.nickName = n
        self.health = h
    def show(self):
        print("昵称：%s"%self.nickName)
        print("健康值：%s"%self.health)

class Dog(Pet):
    color = ''
    def __init__(self,n,h,c):
        Pet.__init__(self,n,h)
        self.color = c
    def show(self):
        Pet.show(self)
        print("颜色：%s"%self.color)
    def feed(self):
        self.health += 5

d= Dog('毛毛',5,'黑色')
d.feed()
d.show()
        
            
    
