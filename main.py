import conversor_temperatura
import conversor_medidas

class Principal:
    def _init_(self) -> None:
        self.menu_principal()

    def menu_principal(self):
        while True:
            print("\nEscolha a conversão desejada:")
            print("1. Fahrenheit para Celsius")
            print("2. Celsius para Fahrenheit")
            print("3. Centímetros para Metros")
            print("4. Metros para Centímetros")
            print("5. Sair")
            escolha = input("Digite o número da sua escolha: ")

            if escolha == '1':
                self.converter_fahrenheit_para_celsius()
            elif escolha == '2':
                self.converter_celsius_para_fahrenheit()
            elif escolha == '3':
                self.converter_cm_para_metros()
            elif escolha == '4':
                self.converter_metros_para_cm()
            elif escolha == '5':
                print("Saindo do programa.")
                break
            else:
                print("Escolha inválida. Tente novamente.")

    def converter_fahrenheit_para_celsius(self):
        f = float(input("Digite a temperatura em Fahrenheit: "))
        c = conversor_temperatura.fahrenheit_para_celsius(f)
        print(f"{f}°F é igual a {c:.2f}°C.")

    def converter_celsius_para_fahrenheit(self):
        c = float(input("Digite a temperatura em Celsius: "))
        f = conversor_temperatura.celsius_para_fahrenheit(c)
        print(f"{c}°C é igual a {f:.2f}°F.")

    def converter_cm_para_metros(self):
        cm = float(input("Digite o comprimento em centímetros: "))
        m = conversor_medidas.cm_para_metros(cm)
        print(f"{cm} cm é igual a {m} metros.")

    def converter_metros_para_cm(self):
        m = float(input("Digite o comprimento em metros: "))
        cm = conversor_medidas.metros_para_cm(m)
        print(f"{m} metros é igual a {cm} centímetros.")

if _name_ == "_main_":
    Principal()