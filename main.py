def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celcius = int(input('enter temperature: '))
    fahrenheit = (1.8*celcius) + 32

    print(f'Fahrenheit: {fahrenheit: .2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
