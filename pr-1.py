print("Hello")
t = float(input("Enter your temperature(degree F):  "))
if t >= 99:
    print("You have fever. Please get a covid test done as soon as possible.")
    print("Here are a few hospitals and services that provide covid tests nearby:")
    print("Portea (Domlur) - 1800 121 2323 \nManipal Hospital - 1800 102 5555")
else:
    print("Welcome to our healthcare service!")
    while True:
        choice = 0
        print("\n\nWe have medicines for the following diseases: ")
        print("1.Common Cold")
        print("2.Diabetes")
        print("3.Tuberclosis")
        print("4.Headache")
        print("5.Conjunctivitis")
        print("6.Salmonella")
        print("7.Exit")
        choice = input("\nEnter your diagnosed disease: ")

        def CommonCold():
            print("\nThe medicines available are: \nStrepsils - 50 Rupees \nParacetamol - 80 Rupees")
            Strepsils = 50
            Paracetamol = 80
            choice_cc = input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_cc = int(input("Enter the quantity: "))
            if choice_cc == 'Strepsils':
                p_strep = Strepsils * q_cc
                print("The price is: ",p_strep)
            if choice_cc == "Paracetamol":
                p_para = Paracetamol * q_cc
                print("The price is: ",p_para)
            
        if choice == "Common Cold":
            CommonCold()
    
        def Diabetes():
        # Huminsulin, Lantus, Glaritus
            print("\nThe insulin doses are: \nHuminsulin - 395 Rupees \nLantus - 493 Rupees \nGlaritus - 180")
            Huminsulin = 395
            Lantus = 493
            Glaritus = 180
            choice_di = input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_di = int(input("Enter the quantity(per 10ml): "))
            if choice_di == 'Huminsulin':
                p_hum = Huminsulin * q_di
                print("The price is: ", p_hum)
            if choice_di == 'Lantus':
                p_lant = Lantus * q_di
                print("The price is: ", p_lant)
            if choice_di == "Glaritus":
                p_glar = Glaritus * q_di
                print("The price is :", p_glar)
       
        if choice == "Diabetes":
            Diabetes()
            
        def Tubercolosis():
        # Isoniazid, Rifampin, Pyrazinamide            
            print("\nThe medicines/antibiotics available are: \nIsoniazid - 550 Rupees \nRifampin - 420 Rupees \nPyrazinamide - 470 rupees")
            Isoniazid = 550
            Rifampin = 420
            Pyrazinamide = 470
            choice_tb = input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_tb = int(input("Enter the quantity: "))
            if choice_tb == 'Isoniazid':
                p_iso = Isoniazid * q_tb
                print("The price is: ", p_iso)
            if choice_tb == 'Rifampin':
                p_rif = Rifampin * q_tb
                print("The price is: ", p_rif)
            if choice_tb == 'Pyrazinamide':
                p_pyra = Pyrazinamide * q_tb
                print("The price is :", p_pyra)
        
        if choice == "Tubercolosis":
            Tubercolosis()

        def Headache():
            # Aspirin, Ibuprofen, Ketorolac
            print("\nThe medicines/antibiotics available are: \nAspirin  - 100 Rupees \nIbuprofen - 60 Rupees \nKetorolac - 50 rupees")
            Aspirin = 100
            Ibuprofen = 60
            Ketorolac = 50
            choice_h = input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_h = int(input("Enter the quantity: "))
            if choice_h == 'Aspirin':
                p_as = Aspirin * q_h
                print("The price is: ", p_as)
            if choice_h == 'Ibuprofen':
                p_ib = Ibuprofen * q_h
                print("The price is: ", p_ib)
            if choice_h == 'Ketorolac':
                p_ke = Ketorolac * q_h
                print("The price is :", p_ke)
         
        if choice == "Headache":
            Headache()

        def Conjunctivitis():
            #FML-1,Itone,Ciplox
            print("\nThe medicines/antibiotics available are: \nFML-1  - 200 Rupees \nItone - 250 Rupees \nCiplox - 230 rupees")
            FML1 = 200
            Itone = 250
            Ciplox = 230
            choice_conj= input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_C = int(input("Enter the quantity: "))
            if choice_conj == 'FML-1':
                p_fm = FML1 * q_C
                print("The price is: ", p_fm)
            if choice_conj == 'Itone':
                p_it = Itone * q_C
                print("The price is: ", p_it)
            if choice_conj == 'Ciplox':
                p_ci = Ciplox * q_C
                print("The price is :", p_ci)
                
        if choice == "Conjunctivitis":
            Conjunctivitis()
            
    
        def Salmonella():
            #Ciprofloxacin, Ofloxacin, Azithromycin
            print("\nThe medicines/antibiotics available are: \nCiprofloxacin  - 680 Rupees \nOfloxacin - 320 Rupees \nAzithromycin - 100 rupees")
            Ciprofloxacin = 680
            Ofloxacin = 320
            Azithromycin = 100
            choice_sal= input("\nIf you would like to purchase any of the aforementioned medicines, input the medicine name: ")
            q_S = int(input("Enter the quantity: "))
            if choice_sal == 'Ciprofloxacin':
                p_cip = Ciprofloxacin * q_S
                print("The price is: ", p_cip)
            if choice_sal == 'Ofloxacin':
                p_of = Ofloxacin * q_S
                print("The price is: ", p_of)
            if choice_sal== 'azithromycin':
                p_az = Azithromycin * q_S
                print("The price is :", p_az)
                
        if choice == "Salmonella":
            Salmonella()


        if choice == 7:
            stop = input("\n\nTo stop the program enter (stop/STOP) ")
            if stop == "stop" or stop == "STOP":
                print("Thank you for shopping with us. Hope you get well soon! :D")
            break
   
    

