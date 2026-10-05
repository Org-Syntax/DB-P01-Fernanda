def sumar(a: int, b: int) -> int:
    return a + b


def main() -> None:
    num1 = 5
    num2 = 10
    resultado = sumar(num1, num2)
    print(f"El primer número es: {num1}")
    print(f"El segundo número es: {num2}")
    print(f"El resultado de la suma automatizada es: {resultado}")


if __name__ == "__main__":
    main()