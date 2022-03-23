#created on fr [ junior 11 21:11:53 2020]
dia_actual =20;
mes_actual =6;
años_actual =2021;


dia_nacimiento = int(input("ingrese el dia nacimiento"));
mes_nacimiento = int(input("ingrese el mes nacimiento"));
años_nacimiento = int(input("ingrese el años de nacimiento"));

if(dia_actual>=mes_nacimiento):
     if(mes_actual>mes_nacimiento):
         edad = años_actual-años_nacimiento -1
     else:
             edad = años_actual-años_nacimiento
             
             
else:
      edad = años_actual-años_nacimiento 





print("la edad es:",edad)






    
     