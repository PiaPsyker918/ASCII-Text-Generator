import pyfiglet

def main():
    text = input("Enter the text: ")
    ufonts = int(input("Count of showed fonts (500+): "))
    
    fonts = pyfiglet.FigletFont.getFonts()
    
    print("\nFonts:")
    for i, font in enumerate(fonts[:ufonts]):
        print(f"{i+1}. {font}")
    print("... and more (all: {})".format(len(fonts)))
    
    choice = input("\nChoice font (Enter for standart): ")
    
    try:
        font_name = fonts[int(choice)-1] if choice.strip() else "standard"
    except:
        font_name = "standard"
    
    result = pyfiglet.figlet_format(text, font=font_name)
    print("\nYour ASCII Text:")
    print(result)
    input("Enter to exit...")

if __name__ == "__main__":
    main()