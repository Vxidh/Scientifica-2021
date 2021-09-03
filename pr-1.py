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
        print("The insulin doses available are: ")
        print("The medicines available are: \nHuminsulin R 100 - 395 Rupees \nLantus 100 IU Injection - 493 Rupees \nGlaritus 100iu Injection - 1580")
        Huminsulin R 100 = 395
        Lantus 100 IU Injection = 493 
        
        choice_cc = input("If you would like to purchase any of the aforementioned medicines, input the medicine name: ")