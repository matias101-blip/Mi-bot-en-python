name=input('Bienbenido al bot de python por thehunter101 \nIngrese su nombre porfavor:')
bot=("waifu bot 1.0")
print("hola "+ name +" Yo soy  "+ bot)
print("Me puedes dar un nombre por favor")
name_bot=input('Porfavor que nombre le daras al bot. \nIngresa el nombre del bot:')
print(bot +":Entonces me llamo "+ name_bot +" me gusta ese nombre ~(^O^~) (~^O^)~")
print(name_bot +": Bueno te preguntare algo mas quieres decirme tu edad o quieres que la calcule. \n presiona 1 para clacular tu edad o 2 para decirmela.")
op=int(input("presione 1 o 2: "))
if op > 1:
    edad=int(input("Porfavor escriba su edad: "))
else:
    fet1=int(input("Porfavor esciba su fecha de nacimiento: "))
    fet2=int(input("Porfavor esciba su fecha actual: "))
    fetr=(fet2 - fet1)
    print(fetr)
    edad=fetr
if edad > 15:
    print(name_bot+": vaya desde ahora te llamare "+ name +"-kun")
else:
    print(name_bot+": vaya que eres joven desde ahora te llamare como un shota xD "+ name +"-nichan")
print("bueno dejemos las preguntas aver realisare una suma tu dame los numero Ok :3")
num1=int(input("-cual sera el primer numero ? :"))
num2=int(input("-que numero sera el ultimo numero ? :"))
res=(num1 + num2)
print(res)
print(name_bot + ": esa es la respuesta :v")
print(name_bot +": jejej soy muy lista no crees xD "+ name)
print("Bueno eso es todo fue un gusto conocerte bye nyan,sayonara Darling")
print("Creditos para:\nThehunter101 \naquien mas son los creditos xD gracias por probar waifu bot 1.0 beta")

