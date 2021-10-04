def main():
    #Open a file named numbers.txt
    with open('data.csv', 'r') as data: plaintext = data.read()
    plaintext = plaintext.replace(' ', ',')
    with open('data.csv', 'w') as data: data.write(plaintext)

    #print(plaintext)

#Call the main function
main()