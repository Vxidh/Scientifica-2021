print("Hello")
t = float(input("enter your temperature(degree F):  "))
if t >= 99:
    print("You have fever. Please get a covid test done as soon as possible.")
    print("Here are a few hospitals and services that provide covid tests nearby:")
    print("Portea (Domlur) - 1800 121 2323 \nManipal Hospital - 1800 102 5555")
else:
    print("Welcome to our healthcare service!")
    choice = 0
    print("We have medicines for the following diseases: ")
    print("1.Common Cold")
    print("2.Diabetes")
    print("3.Tuberclosis")
    print("4.Headache")
    print("5.Acidity")
    print("6. Salmonella")
    choice = input("Enter your diagnosed disease: ")

    def CommonCold():   
       print("The medicines available are: \nStrepsils - 50 Rupees \nParacetamol - 80 Rupees")
       Strepsils = 50
       Paracetamol = 80
       choice_cc = input("If you would like to purchase any of the aforementioned medicines, input the medicine name: ")
       q_cc = int(input("Enter the quantitiy: "))
       if choice_cc == 'Strepsils':
           p_strep = Strepsils * q_cc
           print("The price is: ",p_strep)
       if choice_cc == "Paracetamol":
           p_para = Paracetamol * q_cc
           print("The price is: ",p_para)
            
    if choice == "Common Cold":
        CommonCold()
    
    def Diabetes():
            print("The insulin doses are: \nHuminsulin - 395 Rupees \nLantus - 493 Rupees \nGlaritus - 180")
            Huminsulin = 395
            Lantus = 493
            Glaritus = 180
            choice_di = input("If you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_di = int(input("Enter the quantity(per 10ml): "))
            if choice_di == 'Huminsulin':
                p_hum = Huminsulin * q_di
                print("The price is: ", p_hum)
            if choice_di == 'Lantus':
                p_lant = Lantus * q_di
                print("The price is: ", p_lant)
            if choice_di == "Glaritus":
                p_glar = Glaritus * q_di
                print("the price is :", p_glar)
       
    if choice == "Diabetes":
          Diabetes()
            
    def Tubercolosis():
        # Isoniazid, Rifampin, Pyrazinamide            
            print("The medicines/antibiotics available are: \nIsoniazid - 550 Rupees \nRifampin - 420 Rupees \nPyrazinamide - 470 rupees")
            Isoniazid = 550
            Rifampin = 420
            Pyrazinamide = 470
            choice_tb = input("If you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_tb = int(input("Enter the quantity: "))
            if choice_tb == 'Isoniazid':
                p_iso = Isoniazid * q_tb
                print("The price is: ", p_iso)
            if choice_tb == 'Rifampin':
                p_rif = Rifampin * q_tb
                print("The price is: ", p_rif)
            if choice_tb == 'Pyrazinamide':
                p_pyra = Pyrazinamide * q_tb
                print("the price is :", p_pyra)
        
    if choice == "Tubercolosis":
        Tubercolosis()

        

    if choice == 7:
            stop = input("to stop the program enter (stop/STOP) ")
            if stop == "stop" or stop == "STOP":
                print("Thank you for shopping with us")
                print("Hope you get well soon")
                break