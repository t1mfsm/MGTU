package main

import (
	"fmt"
	"strings"
	"unicode"
)

func caesarEncrypt(text string, shift int) string {
	encryptedText := ""
	for _, char := range text {
		if unicode.IsLetter(char) {
			isUpper := unicode.IsUpper(char)
			char = unicode.ToLower(char)
			shifted := int(char) + shift
			if shifted > int('z') {
				shifted -= 26
			}
			encryptedChar := string(rune(shifted))
			if isUpper {
				encryptedChar = strings.ToUpper(encryptedChar)
			}
			encryptedText += encryptedChar
		} else {
			encryptedText += string(char)
		}
	}
	return encryptedText
}

func caesarDecrypt(encryptedText string, shift int) string {
	return caesarEncrypt(encryptedText, -shift)
}

func vigenereEncrypt(text string, key string) string {
	encryptedText := ""
	keyLength := len(key)
	for i, char := range text {
		if unicode.IsLetter(char) {
			isUpper := unicode.IsUpper(char)
			char = unicode.ToLower(char)
			shift := int(key[i%keyLength]) - int('a')
			shifted := int(char) + shift
			if shifted > int('z') {
				shifted -= 26
			}
			encryptedChar := string(rune(shifted))
			if isUpper {
				encryptedChar = strings.ToUpper(encryptedChar)
			}
			encryptedText += encryptedChar
		} else {
			encryptedText += string(char)
		}
	}
	return encryptedText
}

func vigenereDecrypt(encryptedText string, key string) string {
	decryptedText := ""
	keyLength := len(key)
	for i, char := range encryptedText {
		if unicode.IsLetter(char) {
			isUpper := unicode.IsUpper(char)
			char = unicode.ToLower(char)
			shift := int(key[i%keyLength]) - int('a')
			shifted := int(char) - shift
			if shifted < int('a') {
				shifted += 26
			}
			decryptedChar := string(rune(shifted))
			if isUpper {
				decryptedChar = strings.ToUpper(decryptedChar)
			}
			decryptedText += decryptedChar
		} else {
			decryptedText += string(char)
		}
	}
	return decryptedText
}

func main() {
	fmt.Println("Программа для шифрования и дешифрования текста.")
	var choice string
	fmt.Print("Выберите шифр (1 - Цезарь, 2 - Виженер): ")
	fmt.Scan(&choice)

	switch choice {
	case "1":
		var text string
		fmt.Print("Введите текст: ")
		fmt.Scan(&text)
		var shift int
		fmt.Print("Введите сдвиг: ")
		fmt.Scan(&shift)

		encryptedText := caesarEncrypt(text, shift)
		fmt.Printf("Зашифрованный текст: %s\n", encryptedText)

		decryptedText := caesarDecrypt(encryptedText, shift)
		fmt.Printf("Расшифрованный текст: %s\n", decryptedText)
	case "2":
		var text, key string
		fmt.Print("Введите текст: ")
		fmt.Scan(&text)
		fmt.Print("Введите ключ: ")
		fmt.Scan(&key)

		encryptedText := vigenereEncrypt(text, key)
		fmt.Printf("Зашифрованный текст: %s\n", encryptedText)

		decryptedText := vigenereDecrypt(encryptedText, key)
		fmt.Printf("Расшифрованный текст: %s\n", decryptedText)
	default:
		fmt.Println("Неверный выбор. Выберите 1 или 2.")
	}
}
