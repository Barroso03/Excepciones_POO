class web():
    def __init__(self,correo,entrar):
        self.correo = correo
        self.entar = entrar
    def set_correo(self,nombre,final,medio,todo):
        self.nombre = nombre
        self.final = final
        self.medio = medio
        self.todo = todo
        todo = (nombre,final,medio)
        if todo == str :
            print("{}".format(nombre), "@","{}".format(medio),"{}".format(final))
        else:
            print("Puede ser un ciber ataque")
    def get_correo(self,correo):
        self.correo = correo
    def set_entrar(self,entrar):
        self.entrar = entrar
        if web.set_correo() == True:
            print("Has entrado en la web")
    def get_entrar(self,entrar):
        self.entrar = entrar
        
